"""
Mac OS X .app build command for distutils

Originally (loosely) based on code from py2exe's build_exe.py by Thomas Heller.
"""
import sys
import os
import zipfile
import plistlib
import shlex
from cStringIO import StringIO

from distutils.core import Command
from distutils.spawn import spawn
from distutils.util import convert_path, change_root
from distutils.errors import *

from altgraph.compat import *

from modulegraph.find_modules import find_modules, parse_mf_results
from modulegraph.modulegraph import SourceModule
from modulegraph import modulegraph

import macholib.dyld
import macholib.MachOGraph

from py2app.create_appbundle import create_appbundle
from py2app.util import fancy_split, byte_compile, make_loader, imp_find_module, copy_tree, move, fsencoding, strip_path, writablefile
from py2app import recipes

def iterRecipes(module=recipes):
    for name in dir(module):
        if name.startswith('_'):
            continue
        check = getattr(getattr(module, name), 'check', None)
        if check is not None:
            yield (name, check)
 
# A very loosely defined "target".  We assume either a "script" or "modules"
# attribute.  Some attributes will be target specific.
class Target(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # If modules is a simple string, assume they meant list
        m = self.__dict__.get("modules")
        if m and isinstance(m, basestring):
            self.modules = [m]

    def get_dest_base(self):
        dest_base = getattr(self, "dest_base", None)
        if dest_base: return dest_base
        script = getattr(self, "script", None)
        if script:
            return os.path.basename(os.path.splitext(script)[0])
        modules = getattr(self, "modules", None)
        assert modules, "no script, modules or dest_base specified"
        return modules[0].split(".")[-1]

    def validate(self):
        resources = getattr(self, "resources", [])
        for r_filename in resources:
            if not os.path.isfile(r_filename):
                raise DistutilsOptionError, "Resource filename '%s' does not exist" % (r_filename,)

def FixupTargets(targets, default_attribute):
    if not targets:
        return targets
    ret = []
    for target_def in targets:
        if isinstance(target_def, basestring):
            # Create a default target object, with the string as the attribute
            target = Target(**{default_attribute: target_def})
        else:
            d = getattr(target_def, "__dict__", target_def)
            if default_attribute not in d:
                raise DistutilsOptionError, "This target class requires an attribute '%s'" % (default_attribute,)
            target = Target(**d)
        target.validate()
        ret.append(target)
    return ret

def normalize_data_file(fn):
    if isinstance(fn, basestring):
        fn = convert_path(fn)
        return ('', [fn])
    return fn

def stdlib_filter(module):
    # this should work but isn't ideal
    rp = os.path.realpath(module.filename)
    prefix = os.path.join(os.path.realpath(sys.prefix), '')
    return ((not rp.startswith(prefix)) or ('/site-packages/' in rp))

def not_system_filter(n):
    fn = n.filename
    return (
        (not fn.startswith('/System/'))
        and (fn.startswith('/usr/local/') or not fn.startswith('/usr/'))
    )

def has_filename_filter(n):
    return getattr(n, 'filename', None) is not None

def bundle_or_dylib_filter(n):
    return getattr(n, 'filetype', None) in ('bundle', 'dylib')

def is_system():
    return os.path.realpath(sys.executable).startswith('/System/')

def installation_info():
    if is_system():
        return sys.version[:3] + " (FORCED: Using vendor Python)"
    else:
        return sys.version[:3]

class py2app(Command):
    description = "create a Mac OS X application from Python scripts"
    # List of option tuples: long name, short name (None if no short
    # name), and help string.
    
    
    user_options = [
        ('optimize=', 'O',
         "optimization level: -O1 for \"python -O\", "
         "-O2 for \"python -OO\", and -O0 to disable [default: -O0]"),
        ("includes=", 'i',
         "comma-separated list of modules to include"),
        ("packages=", 'p',
         "comma-separated list of packages to include"),
        ("iconfile=", None,
         "Icon file to use"),
        ("excludes=", 'e',
         "comma-separated list of modules to exclude"),
        ("dylib-excludes=", 'E',
         "comma-separated list of frameworks or dylibs to exclude (XXX)"),
        ("resources=", 'r',
         "comma-separated list of additional data files and folders to include (not for code!)"),
        ("frameworks=", 'f',
         "comma-separated list of additional frameworks and dylibs to include"),
        ("plist=", 'P',
         "Info.plist template file, dict, or plistlib.Plist"),
        ("graph", 'g',
         "output module dependency graph"),
        ("strip", 'S',
         "strip debug and local symbols from output"),
        #("compressed", 'c',
        # "create a compressed zipfile"),
        ("no-chdir", 'C',
         "do not change to the data directory (Contents/Resources)"),
        #("no-zip", 'Z',
        # "do not use a zip file (XXX)"),
        ("semi-standalone", 's',
         "depend on an existing installation of Python " + installation_info()),
        ("alias", 'A',
         "Use an alias to current source file (for development only!)"),
        ("argv-emulation", 'a',
         "Use argv emulation"),
        ("argv-inject=", None,
         "Inject some commands into the argv"),
        ('bdist-base=', 'b',
         'base directory for build library (default is build)'),
        ('dist-dir=', 'd',
         "directory to put final built distributions in (default is dist)"),
        ('site-packages', None,
         "include the system and user site-packages into sys.path"),
        ('debug-modulegraph', None,
         'Drop to pdb console after the module finding phase is complete'),
        ]

    boolean_options = [
        #"compressed",
        "strip",
        "site-packages",
        "semi-standalone",
        "alias",
        "argv-emulation",
        #"no-zip",
        "no-chdir",
        "debug-modulegraph",
        "graph",
    ]
    
    def initialize_options (self):
        self.bdist_base = None
        self.graph = False
        self.no_zip = 0
        self.optimize = 0
        self.strip = False
        self.iconfile = None
        self.alias = 0
        self.argv_emulation = 0
        self.argv_inject = None
        self.no_chdir = 0
        self.site_packages = False
        self.includes = None
        self.packages = None
        self.excludes = None
        self.dylib_excludes = None
        self.frameworks = None
        self.resources = None
        self.plist = None
        self.compressed = True
        self.semi_standalone = is_system()
        self.dist_dir = None
        self.debug_modulegraph = False
        self.filters = []

    def finalize_options (self):
        self.optimize = int(self.optimize)
        if self.argv_inject and isinstance(self.argv_inject, basestring):
            self.argv_inject = shlex.split(self.argv_inject)
        self.includes = set(fancy_split(self.includes))
        self.includes.add('encodings.*')
        self.packages = set(fancy_split(self.packages))
        self.excludes = set(fancy_split(self.excludes))
        self.excludes.add('readline')
        # included by apptemplate
        self.excludes.add('site')
        self.dylib_excludes = set(fancy_split(self.dylib_excludes))
        self.resources = fancy_split(self.resources)
        self.frameworks = map(macholib.dyld.framework_find, fancy_split(self.frameworks))
        if not self.plist:
            self.plist = {}
        if isinstance(self.plist, basestring):
            self.plist = plistlib.Plist.fromFile(self.plist)
        if isinstance(self.plist, plistlib.Dict):
            self.plist = dict(self.plist.__dict__)
        else:
            self.plist = dict(self.plist)
            
        self.set_undefined_options('bdist',
                                   ('dist_dir', 'dist_dir'),
                                   ('bdist_base', 'bdist_base'))

        if self.semi_standalone:
            self.filters.append(stdlib_filter)

        self.runtime_preferences = list(self.get_runtime_preferences())


    def get_runtime_preferences(self, prefix=None, version=None):
        # XXX - this is a bit of a hack!
        #       ideally we'd use dylib functions to figure this out
        if prefix is None:
            prefix = sys.prefix
        if version is None:
            version = sys.version
        version = version[:3]
        info = None
        try:
            fmwk = macholib.dyld.framework_find(prefix)
        except ValueError:
            info = None
        else:
            info = macholib.dyld.framework_info(fmwk)
        if info is not None:
            dylib = info['name']
            runtime = os.path.join(info['location'], info['name'])
        else:
            dylib = 'libpython%s.dylib' % (sys.version[:3],)
            runtime = os.path.join(prefix, 'lib', dylib)
        yield os.path.join('@executable_path', '..', 'Frameworks', dylib)
        if self.semi_standalone or self.alias:
            yield runtime
    
    def run(self):
        build = self.reinitialize_command('build')
        build.build_base = self.bdist_base
        build.run()
        sys_old_path = sys.path[:]
        self.additional_paths = [os.path.abspath(p) for p in [build.build_platlib, build.build_lib] if p is not None]
        sys.path[:0] = self.additional_paths
        try:
            self._run()
        finally:
            sys.path = sys_old_path

    
    def iter_data_files(self):
        dist = self.distribution
        for (path, files) in imap(normalize_data_file, chain(getattr(dist, 'data_files', ()) or (), self.resources)):
            for fn in files:
                yield fn, os.path.join(path, os.path.basename(fn))
    
    def _run(self):
        self.create_directories()
        self.fixup_distribution()
        dist = self.distribution
        plist = {}
        for target in dist.app:
            plist.update(getattr(target, 'plist', {}))
        plist.update(self.plist)
        self.plist = plist
        if self.alias:
            self.app_files = []
            for target in dist.app:
                dst = self.build_alias_executable(target, target.script)
                self.app_files.append(dst)
            return

        # and these contains file names
        required_files = set()
        rdict = dict(iterRecipes())

        for target in dist.app:
            required_files.add(target.script)
            required_files.update([k for k in target.prescripts if isinstance(k, basestring)])

        if self.debug_modulegraph:
            debug = 4
        else:
            debug = 0
        mf = find_modules(
            scripts=required_files,
            includes=self.includes,
            packages=self.packages,
            excludes=self.excludes,
            debug=debug,
        )

        filters = [has_filename_filter] + list(self.filters)
        flatpackages = {}
        while True:
            for name, check in rdict.iteritems():
                rval = check(self, mf)
                if rval is None:
                    continue
                # we can pull this off so long as we stop the iter
                del rdict[name]
                print '*** using recipe: %s ***' % (name,)
                self.packages.update(rval.get('packages', ()))
                for pkg in rval.get('flatpackages', ()):
                    if isinstance(pkg, basestring):
                        pkg = (os.path.basename(pkg), pkg)
                    flatpackages[pkg[0]] = pkg[1]
                filters.extend(rval.get('filters', ()))
                newbootstraps = map(self.get_bootstrap,
                    rval.get('prescripts', ()))
                for fn in newbootstraps:
                    if isinstance(fn, basestring):
                        mf.run_script(fn)
                for target in dist.app:
                    target.prescripts.extend(newbootstraps)
                break
            else:
                break
        
        if self.debug_modulegraph:
            import pdb
            pdb.Pdb().set_trace()



        print "*** filtering dependencies ***"
        nodes_seen, nodes_removed, nodes_orphaned = mf.filterStack(filters)
        print '%d total' % (nodes_seen,)
        print '%d filtered' % (nodes_removed,)
        print '%d orphaned' % (nodes_orphaned,)
        print '%d remaining' % (nodes_seen - nodes_removed,)

        if self.graph:
            for target in dist.app:
                base = target.get_dest_base()
                appdir = os.path.join(self.dist_dir, os.path.dirname(base))
                appname = self.plist.get('CFBundleName', os.path.basename(base))
                dgraph = os.path.join(appdir, appname+'.dot')
                print "*** creating dependency graph: %s ***" % (os.path.basename(dgraph),)
                mf.graphreport(file(dgraph, 'w'), flatpackages=flatpackages)
        
        py_files, extensions = parse_mf_results(mf)
        py_files = list(py_files)
        extensions = list(extensions)

        print "*** finding dylibs needed ***"
        mm = self.find_dylibs(extensions)

        print "*** filtering dylib dependencies ***"
        dylib_filters = [has_filename_filter, not_system_filter, bundle_or_dylib_filter]
        nodes_seen, nodes_removed, nodes_orphaned = mm.filterStack(dylib_filters)
        print '%d total' % (nodes_seen,)
        print '%d filtered' % (nodes_removed,)
        print '%d orphaned' % (nodes_orphaned,)
        print '%d remaining' % (nodes_seen - nodes_removed,)

        print "*** create binaries ***"
        pkgdirs = filter(os.path.exists, [
            os.path.join(os.path.realpath(self.get_bootstrap(pkg)), '')
            for pkg in self.packages
        ])
        self.create_binaries(py_files, pkgdirs, extensions, mm)


    def find_dylibs(self, extensions):
        mm = macholib.MachOGraph.MachOGraph()
        for fn in extensions:
            mm.run_file(fn.filename)
        if not self.semi_standalone and os.path.exists(sys.executable):
            #  assume that Python has no dependencies
            #  when using semi-standalone .. this is
            #  pretty reasonable
            mm.run_file(sys.executable)
        for fn in self.frameworks:
            mm.run_file(fn)
        return mm

    def create_directories(self):
        bdist_base = self.bdist_base
        if self.semi_standalone:
            self.bdist_dir = os.path.join(bdist_base, 'python%s-semi_standalone' % (sys.version[:3],), 'app')
        else:
            self.bdist_dir = os.path.join(bdist_base, 'python%s-standalone' % (sys.version[:3],), 'app')

        self.collect_dir = os.path.abspath(os.path.join(self.bdist_dir, "collect"))
        self.mkpath(self.collect_dir)

        self.temp_dir = os.path.abspath(os.path.join(self.bdist_dir, "temp"))
        self.mkpath(self.temp_dir)

        self.dist_dir = os.path.abspath(self.dist_dir)
        self.mkpath(self.dist_dir)

        self.lib_dir = os.path.join(self.bdist_dir,
                                    os.path.dirname(self.distribution.zipfile))
        self.mkpath(self.lib_dir)

        self.ext_dir = os.path.join(self.lib_dir, 'lib-dynload')
        self.mkpath(self.ext_dir)

        self.framework_dir = os.path.join(self.bdist_dir, 'Frameworks')
        self.mkpath(self.framework_dir)

    def create_binaries(self, py_files, pkgdirs, extensions, mm):
        dist = self.distribution
        pkgexts = []
        extmap = {}
        def packagefilter(mod, pkgdirs=pkgdirs):
            fn = os.path.realpath(getattr(mod, 'filename', None))
            if fn is None:
                return None
            for pkgdir in pkgdirs:
                if fn.startswith(pkgdir):
                    return None
            return fn
        if pkgdirs:
            py_files = filter(packagefilter, py_files)
        for ext in extensions:
            fn = packagefilter(ext)
            if fn is None:
                fn = os.path.realpath(getattr(ext, 'filename', None))
                pkgexts.append(ext)
            else:
                py_files.append(self.create_loader(ext))
            extmap[fn] = ext

        # byte compile the python modules into the target directory
        print "*** byte compile python files ***"
        byte_compile(py_files,
                     target_dir=self.collect_dir,
                     optimize=self.optimize,
                     force=0,
                     verbose=self.verbose,
                     dry_run=self.dry_run)

        self.lib_files = []
        self.app_files = []

        # create the shared zipfile containing all Python modules
        archive_name = os.path.join(self.lib_dir,
                                    os.path.basename(dist.zipfile))
        arcname = self.make_lib_archive(archive_name, base_dir=self.collect_dir,
                                   verbose=self.verbose, dry_run=self.dry_run)
        self.lib_files.append(arcname)

        print "*** filtering extensions and dylibs ***"
        
        changemap = {}
        machfiles = []
        for fobj in mm.flatten():
            fn = fobj.filename
            ext = extmap.get(fn)
            rdst = '@executable_path/../Frameworks'
            if ext is not None:
                # this is an extension
                base = os.path.dirname(ext.identifier.replace('.', os.sep))
                dst = os.path.join(self.ext_dir, base)
                rdst = os.path.join(rdst, base)
                self.mkpath(dst)
            else:
                # framework or dylib
                dst = self.framework_dir
                self.mkpath(dst)
            info = macholib.dyld.framework_info(fn)
            if info is not None:
                outfile = os.path.join(dst, info['name'])
                changemap[fn] = os.path.join(rdst, info['name'])
                # XXX - hack hack hack
                if info['shortname'] == 'Python':
                    self.copy_python_framework(info, dst)
                else:
                    self.copy_versioned_framework(info, dst)
            else:
                outfile = os.path.join(dst, os.path.basename(fn))
                changemap[fn] = os.path.join(rdst, os.path.basename(fn))
                self.copy_file(fobj.filename, outfile)
            machfiles.append((outfile, fobj))
        for outfile, fobj in machfiles:
            if fobj.rewriteLoadCommands(changemap):
                f = writablefile(outfile, 'rb+')
                fobj.write(f)
                f.seek(0, 2)
                f.flush()
                f.close()

        # build the executables
        for target in dist.app:
            dst = self.build_executable(target, arcname, pkgexts, target.script)
            if self.strip:
                strip_path(dst)
            self.app_files.append(dst)

    def copy_versioned_framework(self, info, dst):
        # XXX - Boy is this ugly, but it makes sense because the developer
        #       could have both Python 2.3 and 2.4, or Tk 8.4 and 8.5, etc.
        #       Saves a good deal of space, and I'm pretty sure this ugly
        #       hack is correct in the general case.
        version = info['version']
        if version is None:
            return self.copy_framework(info, dst)
        short = info['shortname'] + '.framework'
        infile = os.path.join(info['location'], short)
        outfile = os.path.join(dst, short)
        vsplit = os.path.join(infile, 'Versions').split(os.sep)
        def condition(src, vsplit=vsplit, version=version):
            srcsplit = src.split(os.sep)
            if (
                    len(srcsplit) > len(vsplit) and
                    srcsplit[:len(vsplit)] == vsplit and
                    srcsplit[len(vsplit)] != version
                ):
                return False
            return True

        return self.copy_tree(infile, outfile, preserve_symlinks=True, condition=condition)
    
    def copy_framework(self, info, dst):
        short = info['shortname'] + '.framework'
        infile = os.path.join(info['location'], short)
        outfile = os.path.join(dst, short)
        return self.copy_tree(infile, outfile, preserve_symlinks=True)
    
    def copy_python_framework(self, info, dst):
        # XXX - In this particular case we know exactly what we can
        #       get away with.. should this be extended to the general
        #       case?  Per-framework recipes?
        indir = os.path.dirname(os.path.join(info['location'], info['name']))
        outdir = os.path.dirname(os.path.join(dst, info['name']))
        self.mkpath(os.path.join(outdir, 'Resources'))
        self.copy_tree(
            os.path.join(indir, 'Resources', 'English.lproj'),
            os.path.join(outdir, 'Resources', 'English.lproj'))
        for fn in [os.path.basename(info['name']), 'Resources/Info.plist', 'Resources/version.plist']:
            self.copy_file(
                os.path.join(indir, fn),
                os.path.join(outdir, fn))
    
    def fixup_distribution(self):
        dist = self.distribution
        
        # Convert our args into target objects.
        dist.app = FixupTargets(dist.app, "script")

        # make sure all targets use the same directory, this is
        # also the directory where the pythonXX.dylib must reside
        paths = set()
        for target in dist.app:
            paths.add(os.path.dirname(target.get_dest_base()))

        if len(paths) > 1:
            raise DistutilsOptionError, \
                  "all targets must use the same directory: %s" % \
                  [p for p in paths]
        if paths:
            app_dir = paths.pop() # the only element
            if os.path.isabs(app_dir):
                raise DistutilsOptionError, \
                      "app directory must be relative: %s" % app_dir
            self.app_dir = os.path.join(self.dist_dir, app_dir)
            self.mkpath(self.app_dir)
        else:
            # Do we allow to specify no targets?
            # We can at least build a zipfile...
            self.app_dir = self.lib_dir

        prescripts = []
        if self.site_packages or self.alias:
            prescripts.append('site_packages')
        if self.iconfile:
            iconfile = self.iconfile
            if not os.path.exists(iconfile):
                iconfile = iconfile+'.icns'
            if not os.path.exists(iconfile):
                raise DistutilsOptionError, "icon file must exist: %r" % (self.icon,)
            self.resources.append(iconfile)
            self.plist[u'CFBundleIconFile'] = os.path.basename(iconfile)
            
        if self.argv_emulation:
            prescripts.append('argv_emulation')
            if u'CFBundleDocumentTypes' not in self.plist:
                self.plist[u'CFBundleDocumentTypes'] = [
                    {
                        u'CFBundleTypeOSTypes' : [
                            u'****',
                            u'fold',
                            u'disk',
                        ],
                        u'CFBundleTypeRole': u'Viewer'
                    },
                ]

        if self.argv_inject is not None:
            prescripts.append('argv_inject')
            prescripts.append(
                StringIO('_argv_inject(%r)\n' % (self.argv_inject,)))

        if not self.no_chdir:
            prescripts.append('chdir_resource')
        if not self.alias:
            prescripts.append('disable_linecache')
            prescripts.append('boot_app')
        else:
            if self.additional_paths:
                prescripts.append('path_inject')
                prescripts.append(
                    StringIO('_path_inject(%r)\n' % (self.additional_paths,)))
            prescripts.append('boot_aliasapp')
        newprescripts = []
        for s in prescripts:
            if isinstance(s, basestring):
                newprescripts.append(self.get_bootstrap('py2app.bootstrap.'+s))
            else:
                newprescripts.append(s)

        for target in dist.app:
            target.prescripts = newprescripts
            

    def get_bootstrap(self, bootstrap):
        if isinstance(bootstrap, basestring):
            if not os.path.exists(bootstrap):
                bootstrap = imp_find_module(bootstrap)[1]
        return bootstrap

    def get_bootstrap_data(self, bootstrap):
        bootstrap = self.get_bootstrap(bootstrap)
        if not isinstance(bootstrap, basestring):
            return bootstrap.getvalue()
        else:
            return file(bootstrap, 'rU').read()
        
    def create_appbundle(self, target, script, use_runtime_preference=True):
        base = target.get_dest_base()
        appdir = os.path.join(self.dist_dir, os.path.dirname(base))
        appname = os.path.basename(base)
        print "*** creating application bundle: %s ***" % (appname,)
        if self.runtime_preferences and use_runtime_preference:
            self.plist.setdefault(
                'PyRuntimeLocations', self.runtime_preferences)
        appdir, plist = create_appbundle(appdir, appname, plist=self.plist)
        appdir = fsencoding(appdir)
        resdir = os.path.join(appdir, 'Contents', 'Resources')
        return appdir, resdir, plist
        
    def build_alias_executable(self, target, script):
        # Build an alias executable for the target
        appdir, resdir, plist = self.create_appbundle(target, script)

        # symlink data files
        for src, dest in self.iter_data_files():
            dest = os.path.join(resdir, dest)
            try:
                os.remove(dest)
            except:
                pass
            os.symlink(os.path.abspath(src), dest)
        
        from Carbon.File import FSRef
        aliasdata = FSRef(script).FSNewAliasMinimal().data

        bootfile = file(os.path.join(resdir, '__boot__.py'), 'w')
        for fn in target.prescripts:
            bootfile.write(self.get_bootstrap_data(fn))
            bootfile.write('\n\n')
        bootfile.write('_run(%r)\n' % (aliasdata,))
        bootfile.close()
        
        target.appdir = appdir
        return appdir

    def build_executable(self, target, arcname, pkgexts, script):
        # Build an executable for the target
        appdir, resdir, plist = self.create_appbundle(target, script)

        for src, dest in self.iter_data_files():
            dest = os.path.join(resdir, dest)
            self.mkpath(os.path.dirname(dest))
            if os.path.isdir(src):
                self.copy_tree(src, dest, preserve_symlinks=True)
            else:
                self.copy_file(src, dest)
        
        bootfile = file(os.path.join(resdir, '__boot__.py'), 'w')
        for fn in target.prescripts:
            bootfile.write(self.get_bootstrap_data(fn))
            bootfile.write('\n\n')
        bootfile.write('_run(%r)\n' % (os.path.basename(script),))
        bootfile.close()
        
        pydir = os.path.join(resdir, 'Python')
        self.mkpath(pydir)
        self.copy_file(arcname, pydir)
        self.copy_file(script, pydir)
        ext_dir = os.path.join(pydir, os.path.basename(self.ext_dir))
        self.copy_tree(self.ext_dir, ext_dir, preserve_symlinks=True)
        self.copy_tree(self.framework_dir,
            os.path.join(appdir, 'Contents', 'Frameworks'),
            preserve_symlinks=True)
        sitepkg = os.path.join(
            pydir,
            os.path.splitext(os.path.basename(arcname))[0],
        )
        for pkg in self.packages:
            pkg = self.get_bootstrap(pkg)
            dst = os.path.join(sitepkg, os.path.basename(pkg))
            self.mkpath(dst)
            self.copy_tree(pkg, dst)
        for pkgext in pkgexts:
            fn = (
                pkgext.identifier.replace('.', os.sep) +
                os.path.splitext(pkgext.filename)[1]
            )
            self.mkpath(os.path.join(sitepkg, os.path.dirname(fn)))
            move(os.path.join(ext_dir, fn), os.path.join(sitepkg, fn))

        target.appdir = appdir
        return appdir

    def create_loader(self, item):
        # Hm, how to avoid needless recreation of this file?
        slashname = item.identifier.replace('.', os.sep)
        pathname = os.path.join(self.temp_dir, "%s.py" % slashname)
        if os.path.exists(pathname):
            if self.verbose:
                print "skipping python loader for extension %r" % (item.identifier,)
        else:
            self.mkpath(os.path.dirname(pathname))
            # and what about dry_run?
            if self.verbose:
                print "creating python loader for extension %r" % (item.identifier,)

            fname = slashname + os.path.splitext(item.filename)[1]
            source = make_loader(fname)
            if not self.dry_run:
                open(pathname, "w").write(source)
            else:
                return
        return SourceModule(item.identifier, pathname)

    def make_lib_archive(self, zip_filename, base_dir, verbose=0,
                         dry_run=0):
        # Like distutils "make_archive", except we can specify the
        # compression to use - default is ZIP_STORED to keep the
        # runtime performance up.
        # Also, we don't append '.zip' to the filename.
        from distutils.dir_util import mkpath
        mkpath(os.path.dirname(zip_filename), dry_run=dry_run)

        if self.compressed:
            compression = zipfile.ZIP_DEFLATED
        else:
            compression = zipfile.ZIP_STORED
        if not dry_run:
            z = zipfile.ZipFile(zip_filename, "w",
                                compression=compression)
            save_cwd = os.getcwd()
            os.chdir(base_dir)
            for dirpath, dirnames, filenames in os.walk('.'):
                for fn in filenames:
                    path = os.path.normpath(os.path.join(dirpath, fn))
                    if os.path.isfile(path):
                        z.write(path, path)
            os.chdir(save_cwd)
            z.close()

        return zip_filename

    def copy_tree(self, infile, outfile,
                   preserve_mode=1, preserve_times=1, preserve_symlinks=0,
                   level=1, condition=None):
        """Copy an entire directory tree respecting verbose, dry-run,
        and force flags.

        This version doesn't bork on existing symlinks
        """
        return copy_tree(
            infile, outfile,
            preserve_mode,preserve_times,preserve_symlinks,
            not self.force,
            dry_run=self.dry_run,
            condition=condition)
