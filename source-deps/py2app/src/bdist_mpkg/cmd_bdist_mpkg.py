"""bdist_mpkg.cmd_bdist_mpkg

Implements the Distutils 'bdist_mpkg' command (create an OS X "mpkg"
binary distribution)."""

import os
import sys
from distutils.core import Command
from distutils.util import get_platform
from distutils.dir_util import remove_tree, mkpath
from distutils.version import LooseVersion
from distutils.errors import *
from distutils import log

from altgraph.compat import *

import pkg
import tools
import plists

class bdist_mpkg (Command):

    description = "create a Mac OS X mpkg distribution for Installer.app"

    user_options = [
        ('pkg-base=', None,
         "base directory for creating pkg (defaults to \"mpkg\" "
         "under --bdist-base"),
        ('bdist-base=', None,
         "bdist base directory"),
        ('component-directory=', None,
         "component directory for packages relative to the mpkg "
         "(defaults to ./Contents/Packages)"),
        ('keep-temp', 'k',
         "keep the pseudo-installation tree around after creating "
         "the distribution archive"),
        ('open', None,
         'Open with Installer.app after building'),
        ('readme', None,
         'readme text file to be used in pkg (defaults to ReadMe)'),
        ('license', None,
         'license text file to be used in pkg (defaults to License or COPYING)'),
        ('welcome', None,
         'welcome text file to be used in pkg (defaults to Welcome)'),
        ('background', None,
         'background image to be used in pkg (defaults to Background)'),
        ('dist-dir=', 'd',
         "directory to put final built pkg distributions in"),
        ('skip-build', None,
         "skip rebuilding everything (for testing/debugging)"),
    ]

    boolean_options = ['skip-build', 'keep-temp', 'open']

    def initialize_options (self):
        self.skip_build = False
        self.keep_temp = False
        self.open = False
        self.template = None
        self.readme = None
        self.license = None
        self.welcome = None
        self.background = None
        self.bdist_base = None
        self.pkg_base = None
        self.dist_dir = None
        self.plat_name = None
        self.component_directory = './Contents/Packages'
        self.install_schemes = set(['purelib', 'platlib', 'headers', 'scripts', 'data'])
        self.scheme_map = {}
        self.packages = []
        self.scheme_descriptions = {}
        self.packagesdir = None
        self.metapackagename = None

    def finalize_options (self):
        self.set_undefined_options('bdist', ('bdist_base', 'bdist_base'))
        if self.pkg_base is None:
            self.pkg_base = os.path.join(self.bdist_base, 'mpkg')

        install = self.reinitialize_command('install', reinit_subcommands=1)
        install.ensure_finalized()
        for key in self.install_schemes:
            self.scheme_map[key] = os.path.realpath(getattr(install, 'install_'+key))
        descriptions = dict(
            purelib = u'(Required) Pure Python modules and packages',
            platlib = u'(Required) Python modules, extensions, and packages',
            headers = u'(Optional) Header files for development',
            scripts = u'(Optional) Scripts to use from the Unix shell',
            data    = u'(Optional) Additional data files (sometimes documentation)',
        )
        is_framework = os.path.dirname(os.path.dirname(sys.prefix)).endswith('.framework')
        if is_framework and self.scheme_map['scripts'].startswith(sys.prefix):
            self.scheme_map['scripts'] = '/usr/local/bin'

        for k,v in descriptions.iteritems():
            path = self.scheme_map.get(k)
            if path:
                self.scheme_descriptions.setdefault(
                    k,
                    u'%s\nInstalled to: %s' % (v, tools.unicode_path(path)),
                )

        self.set_undefined_options('bdist',
            ('dist_dir', 'dist_dir'),
            ('plat_name', 'plat_name'),
        )
        self.finalize_package_data()

    def finalize_package_data(self):
        if self.license is None:
            for attempt in ('License', 'COPYING'):
                self.license = pkg.try_exts(attempt, exts=pkg.TEXT_EXTS)
                if self.license is not None:
                    break

        if self.readme is None:
            self.readme = pkg.try_exts('ReadMe', exts=pkg.TEXT_EXTS)

        if self.welcome is None:
            self.welcome = pkg.try_exts('Welcome', exts=pkg.TEXT_EXTS)

        if self.background is None:
            self.background = pkg.try_exts('Background', exts=pkg.IMAGE_EXTS)

        if self.template is None:
            vers = os.popen('/usr/bin/sw_vers -productVersion').read().strip()
            if LooseVersion(vers) < LooseVersion('10.3'):
                self.template = 'prepanther'
            else:
                self.template = 'postjaguar'

        self.metapackagename = self.distribution.get_fullname() + '.mpkg'
        self.packagesdir = os.path.join(self.dist_dir, self.metapackagename, self.component_directory)


    def run_extra(self):
        """
        Subclass and add stuff here to add entries to scheme_map
        """
        pass
    
    def scheme_hook(self, scheme, pkgname, version, files, common, prefix, pkgdir):
        """
        Subclass and do stuff with the scheme post-packaging
        """
        pass
    
    def run (self):
        dist = self.distribution
        if not self.skip_build:
            self.run_command('build')

        install = self.reinitialize_command('install', reinit_subcommands=1)
        for key in self.install_schemes:
            setattr(install, 'install_' + key, key)
        install.root = self.pkg_base
        install.skip_build = self.skip_build
        install.warn_dir = 0

        log.info("installing to %s" % self.pkg_base)
        self.run_command('install')
        self.run_extra()
        tools.adminperms(self.pkg_base, verbose=self.verbose, dry_run=self.dry_run)

        # And make an archive relative to the root of the
        # pseudo-installation tree.
        pseudoinstall_root = os.path.join(self.dist_dir, self.metapackagename)
        packagesdir = self.packagesdir
        mkpath(packagesdir, dry_run=self.dry_run, verbose=self.verbose)

        name, version = dist.get_name(), dist.get_version()
        #if version:
        #    name = ' '.join([name, version])

        packages = self.packages
        for scheme, prefix in self.scheme_map.iteritems():
            schemedir = os.path.join(self.pkg_base, scheme)
            if not os.path.exists(schemedir):
                continue
            files, common, prefix = tools.find_root(schemedir, base=prefix)
            pkgname = '-'.join([name, scheme])
            pkgfile = '-'.join([name, scheme, version])+ '.pkg'
            packages.append((pkgfile, 'selected'))
            pkgdir = os.path.join(packagesdir, pkgfile)
            mkpath(pkgdir, dry_run=self.dry_run, verbose=self.verbose)
            info = ()
            desc = self.scheme_descriptions.get(scheme)
            pkg.make_package(self, pkgname, version, files, common, prefix, pkgdir, info, desc)
            self.scheme_hook(scheme, pkgname, version, files, common, prefix, pkgdir)
            
        info = dict(
            IFRequirementDicts=[plists.python_requirement(name)],
            IFPkgFlagComponentDirectory=tools.unicode_path(self.component_directory),
        )
        pkg.make_metapackage(self, name, version, packages, pseudoinstall_root, info)
        
        if not self.keep_temp:
            remove_tree(self.pkg_base, dry_run=self.dry_run)
        if self.open:
            TOOL = '/usr/bin/open'
            os.spawnv(os.P_NOWAIT, TOOL, [TOOL, pseudoinstall_root])

    # run()

# class bdist_dumb
