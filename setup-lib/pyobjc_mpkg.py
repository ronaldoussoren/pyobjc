import os
import sys
from distutils.version import LooseVersion
from distutils import log
from bdist_mpkg.command import bdist_mpkg as _bdist_mpkg
from py2app.util import copy_tree, skipscm
try:
    set
except NameError:
    from sets import Set as set

JUNK = set(['.DS_Store', '.gdb_history', 'build', 'dist', 'NonFunctional'])
JUNK_EXTS = set(['.pbxuser', '.pyc', '.pyo'])
def skipjunk(fn, junk=JUNK, junk_exts=JUNK_EXTS):
    if not skipscm(fn):
        return False
    elif os.path.basename(fn) in junk:
        return False
    elif os.path.splitext(fn)[1] in junk_exts:
        return False
    return True

PREFLIGHT_RM = """#!/usr/bin/env python
import shutil, os
for fn in %(files)r:
    if os.path.isdir(fn):
        shutil.rmtree(fn, ignore_errors=True)
    elif os.path.exists(fn):
        os.unlink(fn)
"""
def run_setup(*args, **kwargs):
    import distutils.core
    d = {
        '_setup_stop_after':None,
        '_setup_distribution':None,
    }
    for k in d:
        d[k] = getattr(distutils.core, k, None)
    try:
        return distutils.core.run_setup(*args, **kwargs)
    finally:
        for k,v in d.iteritems():
            setattr(distutils.core, k, v)
    
    
def write_preflight_rm(path, files):
    fobj = file(path, 'w')
    fobj.write(PREFLIGHT_RM % dict(files=map(os.path.normpath, files)))
    fobj.close()
    os.chmod(path, 0775)

OSX_VERSION = LooseVersion(os.popen('/usr/bin/sw_vers -productVersion').read().strip())
class bdist_mpkg(_bdist_mpkg):
    def initialize_options(self):
        _bdist_mpkg.initialize_options(self)
        self.readme = 'Installer Package/%s/Resources/ReadMe.txt' % ('.'.join(map(str, OSX_VERSION.version[:2])),)
        self.preflight_rm = {}
        self.scheme_descriptions.update(dict(
            pbx   = u'(Optional) Project Builder File and Project templates for PyObjC\nInstalled to: /Developer/ProjectBuilder Extras',
            xcode = u'(Optional) Xcode File and Project templates for PyObjC\nInstalled to: /Library/Application Support/Apple/Developer Tools',
            docs  = u'(Optional) PyObjC Documentation\nInstalled to: /Developer/Python/PyObjC/Documentation',
            examples = u'(Optional) PyObjC Example Code\nInstalled to: /Developer/Python/PyObjC/Examples',
        ))


    def run_extra(self):
        _bdist_mpkg.run_extra(self)
        prepanther = OSX_VERSION < LooseVersion('10.3')
        if prepanther:
            self.pyobjc_pb_template()
        else:
            self.pyobjc_xcode_template()
        self.pyobjc_documentation()
        self.pyobjc_examples()
        self.pyobjc_platlib()
        self.pyobjc_py2app()

    def scheme_hook(self, scheme, pkgname, version, files, common, prefix, pkgdir):
        _bdist_mpkg.scheme_hook(self, scheme, pkgname, version, files, common, prefix, pkgdir)
        rmfiles = self.preflight_rm.get(scheme)
        if rmfiles is None:
            return
        rmfiles = [os.path.normpath(os.path.join(prefix, fn)) for fn in rmfiles]
        preflight = os.path.join(pkgdir, 'Contents', 'Resources', 'preflight')
        write_preflight_rm(preflight, rmfiles)

    def pyobjc_py2app(self):
        bdist_base = os.path.abspath(os.path.join(self.bdist_base, 'py2app'))
        dist_dir = os.path.abspath(self.packagesdir)
        cwd = os.getcwd()
        srcdir = os.path.abspath('source-deps/py2app')
        os.chdir(srcdir)
        old_path = list(sys.path)
        sys.path.insert(0, srcdir)
        args = ['bdist_mpkg', '--bdist-base=' + bdist_base, '--dist-dir=' + dist_dir]
        try:
            sub = run_setup('setup.py', args)
            pkg = sub.get_command_obj('bdist_mpkg').metapackagename
        finally:
            sys.path = old_path
            os.chdir(cwd)
        if pkg is not None:
            self.packages.append((pkg, 'selected'))

    def pyobjc_platlib(self):
        scheme = 'platlib'
        schemedir = os.path.join(self.pkg_base, scheme)
        self.preflight_rm[scheme] = os.listdir(schemedir)
        
    def pyobjc_pb_template(self):
        scheme = 'pbx'
        schemedir = os.path.join(self.pkg_base, scheme)
        self.scheme_map[scheme] = '/Developer/ProjectBuilder Extras'
        copy_tree('ProjectBuilder Extras', schemedir,
            condition=skipjunk, dry_run=self.dry_run, verbose=self.verbose)
        # skip clean.py
        cleanpath = os.path.join(schemedir, 'ProjectBuilder Extras', 'Project Templates', 'clean.py')
        if os.path.exists(cleanpath):
            os.unlink(cleanpath)
        files = []
        files.extend([
            os.path.join('Project Templates', fn)
            for fn in os.listdir(os.path.join(schemedir, 'Project Templates'))])
        files.extend([
            os.path.join('Specifications', fn)
            for fn in os.listdir(os.path.join(schemedir, 'Specifications'))])
        self.preflight_rm[scheme] = files

    def pyobjc_xcode_template(self):
        scheme = 'xcode'
        schemedir = os.path.join(self.pkg_base, scheme)
        self.scheme_map[scheme] = '/Library/Application Support/Apple/Developer Tools'
        files = []
        for path in [
                    'Project Templates',
                    'File Templates/Cocoa',
                    'File Templates/Pure Python',
                ]:
            copy_tree(
                os.path.join('Xcode', path),
                os.path.join(schemedir, path),
                condition=skipjunk, dry_run=self.dry_run, verbose=self.verbose)
            files.extend([
                os.path.join(path, fn)
                for fn in os.listdir(os.path.join(schemedir, path))])
        self.preflight_rm[scheme] = files

    def pyobjc_documentation(self):
        try:
            import build_html
            build_html.build_html()
        except ImportError:
            log.info("*** Can't update HTML, DocArticle missing")
        scheme = 'docs'
        schemedir = os.path.join(self.pkg_base, scheme)
        self.scheme_map[scheme] = '/Developer/Python/PyObjC/Documentation'
        copy_tree('Doc', schemedir,
            condition=skipjunk, dry_run=self.dry_run, verbose=self.verbose)
        self.preflight_rm[scheme] = ['.']

    def pyobjc_examples(self):
        scheme = 'examples'
        schemedir = os.path.join(self.pkg_base, scheme)
        self.scheme_map[scheme] = '/Developer/Python/PyObjC/Examples'
        copy_tree('Examples', schemedir,
            condition=skipjunk, dry_run=self.dry_run, verbose=self.verbose)
        self.preflight_rm[scheme] = ['.']

cmdclass = {'bdist_mpkg': bdist_mpkg}
