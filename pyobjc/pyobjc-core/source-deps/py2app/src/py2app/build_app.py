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
try:
    set
except NameError:
    from sets import Set as set

from distutils.core import Command
from distutils.util import convert_path
from distutils import log
from distutils.errors import *

from altgraph.compat import *

from modulegraph.find_modules import find_modules, parse_mf_results
from modulegraph.modulegraph import SourceModule

import macholib.dyld
import macholib.MachOStandalone

from py2app.create_appbundle import create_appbundle
from py2app.create_pluginbundle import create_pluginbundle
from py2app.util import fancy_split, byte_compile, make_loader, imp_find_module, copy_tree, fsencoding, strip_files, in_system_path, makedirs, iter_platform_files, find_version, skipscm, momc
from py2app.filters import not_stdlib_filter, not_system_filter, has_filename_filter
from py2app import recipes

def framework_copy_condition(src):
    # Skip Headers, .svn, and CVS dirs
    return skipscm(src) and os.path.basename(src) != 'Headers'

class PythonStandalone(macholib.MachOStandalone.MachOStandalone):
    def __init__(self, appbuilder, *args, **kwargs):
        super(PythonStandalone, self).__init__(*args, **kwargs)
        self.appbuilder = appbuilder

    def copy_dylib(self, src):
        dest = os.path.join(self.dest, os.path.basename(src))
        return self.appbuilder.copy_dylib(src, dest)

    def copy_framework(self, info):
        destfn = self.appbuilder.copy_framework(info, self.dest)
        dest = os.path.join(self.dest, info['shortname'] + '.framework')
        self.pending.append((destfn, iter_platform_files(dest)))
        return destfn

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

def is_system(executable=None):
    if executable is None:
        executable = sys.executable
    return in_system_path(executable)

def installation_info(executable=None, version=None):
    if version is None:
        version = sys.version
    if is_system(executable):
        return version[:3] + " (FORCED: Using vendor Python)"
    else:
        return version[:3]

class py2app(Command):
    description = "create a Mac OS X application or plugin from Python scripts"
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
        ("datamodels=", None,
         "xcdatamodels to be compiled and copied into Resources"),
        ("resources=", 'r',
         "comma-separated list of additional data files and folders to include (not for code!)"),
        ("frameworks=", 'f',
         "comma-separated list of additional frameworks and dylibs to include"),
        ("plist=", 'P',
         "Info.plist template file, dict, or plistlib.Plist"),
        ("extension=", None,
         "Bundle extension [default:.app for app, .plugin for plugin]"),
        ("graph", 'g',
         "output module dependency graph"),
        # XXX
        #("xref", 'x',
        # "output module cross-reference as html"),
        ("no-strip", None,
         "do not strip debug and local symbols from output"),
        #("compressed", 'c',
        # "create a compressed zipfile"),
        ("no-chdir", 'C',
         "do not change to the data directory (Contents/Resources) [forced for plugins]"),
        #("no-zip", 'Z',
        # "do not use a zip file (XXX)"),
        ("semi-standalone", 's',
         "depend on an existing installation of Python " + installation_info()),
        ("alias", 'A',
         "Use an alias to current source file (for development only!)"),
        ("argv-emulation", 'a',
         "Use argv emulation [disabled for plugins]"),
        ("argv-inject=", None,
         "Inject some commands into the argv"),
        ("use-pythonpath", None,
         "Allow PYTHONPATH to effect the interpreter's environment"),
        ('bdist-base=', 'b',
         'base directory for build library (default is build)'),
        ('dist-dir=', 'd',
         "directory to put final built distributions in (default is dist)"),
        ('site-packages', None,
         "include the system and user site-packages into sys.path"),
        ('debug-modulegraph', None,
         'Drop to pdb console after the module finding phase is complete'),
        ("strip", 'S',
         "strip debug and local symbols from output (on by default, for compatibility)"),
        ("archs", None,
         "Comma-separated list of architectures to build"),
        ]

    boolean_options = [
        #"compressed",
        "strip",
        "no-strip",
        "site-packages",
        "semi-standalone",
        "alias",
        "argv-emulation",
        #"no-zip",
        "use-pythonpath",
        "no-chdir",
        "debug-modulegraph",
        "graph",
    ]

    def initialize_options (self):
        self.bdist_base = None
        self.graph = False
        self.no_zip = 0
        self.optimize = 0
        self.strip = True
        self.no_strip = False
        self.iconfile = None
        self.extension = None
        self.alias = 0
        self.argv_emulation = 0
        self.argv_inject = None
        self.no_chdir = 0
        self.site_packages = False
        self.use_pythonpath = False
        self.includes = None
        self.packages = None
        self.excludes = None
        self.dylib_excludes = None
        self.frameworks = None
        self.resources = None
        self.datamodels = None
        self.plist = None
        self.compressed = True
        self.semi_standalone = is_system()
        self.dist_dir = None
        self.debug_modulegraph = False
        self.filters = []
        self.archs = None

    def finalize_options (self):
        if self.archs is None:
            from os import environ
            self.archs = set(environ.get("ARCHS", "ppc i386").split())
        else:
            self.archs = set(self.archs.split(","))
        if not self.strip:
            self.no_strip = True
        elif self.no_strip:
            self.strip = False
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
        dylib_excludes = fancy_split(self.dylib_excludes)
        self.dylib_excludes = []
        for fn in dylib_excludes:
            try:
                res = macholib.dyld.framework_find(fn)
            except ValueError:
                try:
                    res = macholib.dyld.dyld_find(fn)
                except ValueError:
                    res = fn
            self.dylib_excludes.append(res)
        self.resources = fancy_split(self.resources)
        frameworks = fancy_split(self.frameworks)
        self.frameworks = []
        for fn in frameworks:
            try:
                res = macholib.dyld.framework_find(fn)
            except ValueError:
                res = macholib.dyld.dyld_find(fn)
            while res in self.dylib_excludes:
                self.dylib_excludes.remove(res)
            self.frameworks.append(res)
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
            self.filters.append(not_stdlib_filter)

        self.runtime_preferences = list(self.get_runtime_preferences())


    def get_default_plist(self):
        # XXX - this is all single target stuff
        plist = {}
        target = self.targets[0]

        version = self.distribution.get_version()
        if version == '0.0.0':
            try:
                version = find_version(target.script)
            except ValueError:
                pass
        plist['CFBundleVersion'] = version

        name = self.distribution.get_name()
        if name == 'UNKNOWN':
            base = target.get_dest_base()
            name = os.path.basename(base)
        plist['CFBundleName'] = name

        return plist

    def get_runtime(self, prefix=None, version=None):
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
        return dylib, runtime

    def get_runtime_preferences(self, prefix=None, version=None):
        dylib, runtime = self.get_runtime(prefix=prefix, version=version)
        yield os.path.join('@executable_path', '..', 'Frameworks', dylib)
        if self.semi_standalone or self.alias:
            yield runtime

    def run(self):
        build = self.reinitialize_command('build')
        build.build_base = self.bdist_base
        build.run()
        self.create_directories()
        self.fixup_distribution()
        self.initialize_plist()

        sys_old_path = sys.path[:]
        extra_paths = [
            os.path.dirname(target.script)
            for target in self.targets
        ]
        extra_paths.extend([build.build_platlib, build.build_lib])
        self.additional_paths = [
            os.path.abspath(p)
            for p in extra_paths
            if p is not None
        ]
        sys.path[:0] = self.additional_paths

        # this needs additional_paths
        self.initialize_prescripts()

        try:
            self._run()
        finally:
            sys.path = sys_old_path


    def iter_datamodels(self, resdir):
        for (path, files) in imap(normalize_data_file, self.datamodels or ()):
            path = fsencoding(path)
            for fn in files:
                fn = fsencoding(fn)
                basefn, ext = os.path.splitext(fn)
                if ext != '.xcdatamodel':
                    basefn = fn
                    fn += '.xcdatamodel'
                destfn = os.path.basename(basefn) + '.mom'
                yield fn, os.path.join(resdir, path, destfn)

    def compile_datamodels(self, resdir):
        for src, dest in self.iter_datamodels(resdir):
            self.mkpath(os.path.dirname(dest))
            momc(src, dest)
        
    def iter_data_files(self):
        dist = self.distribution
        for (path, files) in imap(normalize_data_file, chain(getattr(dist, 'data_files', ()) or (), self.resources)):
            path = fsencoding(path)
            for fn in files:
                fn = fsencoding(fn)
                yield fn, os.path.join(path, os.path.basename(fn))

    def collect_scripts(self):
        # these contains file names
        scripts = set()

        for target in self.targets:
            scripts.add(target.script)
            scripts.update([k for k in target.prescripts if isinstance(k, basestring)])

        return scripts

    def get_plist_options(self):
        return dict(
            PyOptions=dict(
                use_pythonpath=bool(self.use_pythonpath),
                site_packages=bool(self.site_packages),
                alias=bool(self.alias),
                argv_emulation=bool(self.argv_emulation),
                no_chdir=bool(self.no_chdir),
                optimize=self.optimize,
            ),
        )

    
    def initialize_plist(self):
        plist = self.get_default_plist()
        for target in self.targets:
            plist.update(getattr(target, 'plist', {}))
        plist.update(self.plist)
        plist.update(self.get_plist_options())
        self.plist = plist
        return plist

    def run_alias(self):
        self.app_files = []
        for target in self.targets:
            dst = self.build_alias_executable(target, target.script)
            self.app_files.append(dst)

    def collect_recipedict(self):
        return dict(iterRecipes())

    def get_modulefinder(self):
        if self.debug_modulegraph:
            debug = 4
        else:
            debug = 0
        return find_modules(
            scripts=self.collect_scripts(),
            includes=self.includes,
            packages=self.packages,
            excludes=self.excludes,
            debug=debug,
        )

    def collect_filters(self):
        return [has_filename_filter] + list(self.filters)

    def process_recipes(self, mf, filters, flatpackages, loader_files):
        rdict = self.collect_recipedict()
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
                loader_files.extend(rval.get('loader_files', ()))
                newbootstraps = map(self.get_bootstrap,
                    rval.get('prescripts', ()))

                for fn in newbootstraps:
                    if isinstance(fn, basestring):
                        mf.run_script(fn)
                for target in self.targets:
                    target.prescripts.extend(newbootstraps)
                break
            else:
                break

    def _run(self):
        try:
            if self.alias:
                self.run_alias()
            else:
                self.run_normal()
        except:
            # XXX - remove when not debugging
            #       distutils sucks
            if 0:
                import pdb, sys, traceback
                traceback.print_exc()
                pdb.post_mortem(sys.exc_info()[2])
            raise

    def filter_dependencies(self, mf, filters):
        print "*** filtering dependencies ***"
        nodes_seen, nodes_removed, nodes_orphaned = mf.filterStack(filters)
        print '%d total' % (nodes_seen,)
        print '%d filtered' % (nodes_removed,)
        print '%d orphaned' % (nodes_orphaned,)
        print '%d remaining' % (nodes_seen - nodes_removed,)

    def get_appname(self):
        return self.plist['CFBundleName']

    def build_graph(self, mf, flatpackages):
        for target in self.targets:
            base = target.get_dest_base()
            appdir = os.path.join(self.dist_dir, os.path.dirname(base))
            appname = self.get_appname()
            dgraph = os.path.join(appdir, appname + '.dot')
            print "*** creating dependency graph: %s ***" % (os.path.basename(dgraph),)
            mf.graphreport(file(dgraph, 'w'), flatpackages=flatpackages)

    def finalize_modulefinder(self, mf):
        py_files, extensions = parse_mf_results(mf)
        py_files = list(py_files)
        extensions = list(extensions)
        return py_files, extensions

    def collect_packagedirs(self):
        return filter(os.path.exists, [
            os.path.join(os.path.realpath(self.get_bootstrap(pkg)), '')
            for pkg in self.packages
        ])

    def run_normal(self):
        mf = self.get_modulefinder()
        filters = self.collect_filters()
        flatpackages = {}
        loader_files = []
        self.process_recipes(mf, filters, flatpackages, loader_files)

        if self.debug_modulegraph:
            import pdb
            pdb.Pdb().set_trace()

        self.filter_dependencies(mf, filters)

        if self.graph:
            self.build_graph(mf, flatpackages)

        py_files, extensions = self.finalize_modulefinder(mf)
        pkgdirs = self.collect_packagedirs()
        self.create_binaries(py_files, pkgdirs, extensions, loader_files)

    def create_directories(self):
        bdist_base = self.bdist_base
        if self.semi_standalone:
            self.bdist_dir = os.path.join(bdist_base,
                'python%s-semi_standalone' % (sys.version[:3],), 'app')
        else:
            self.bdist_dir = os.path.join(bdist_base,
                'python%s-standalone' % (sys.version[:3],), 'app')

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

    def create_binaries(self, py_files, pkgdirs, extensions, loader_files):
        print "*** create binaries ***"
        dist = self.distribution
        pkgexts = []
        copyexts = []
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
                copyexts.append(ext)
            extmap[fn] = ext

        # byte compile the python modules into the target directory
        print "*** byte compile python files ***"
        byte_compile(py_files,
                     target_dir=self.collect_dir,
                     optimize=self.optimize,
                     force=self.force,
                     verbose=self.verbose,
                     dry_run=self.dry_run)

        self.lib_files = []
        self.app_files = []

        # create the shared zipfile containing all Python modules
        archive_name = os.path.join(self.lib_dir,
                                    os.path.basename(dist.zipfile))

        for (path, files) in loader_files:
            dest = os.path.join(self.collect_dir, path)
            for fn in files:
                self.copy_file(fn, os.path.join(dest, os.path.basename(fn)))

        arcname = self.make_lib_archive(archive_name, base_dir=self.collect_dir,
                                   verbose=self.verbose, dry_run=self.dry_run)
        self.lib_files.append(arcname)

        # build the executables
        for target in self.targets:
            dst = self.build_executable(target, arcname, pkgexts, copyexts, target.script)
            exp = os.path.join(dst, 'Contents', 'MacOS')
            mm = PythonStandalone(self, dst, executable_path=exp, archs=self.archs)
            dylib, runtime = self.get_runtime()
            if self.semi_standalone:
                mm.excludes.append(runtime)
            else:
                mm.run_file(runtime)
            for exclude in self.dylib_excludes:
                info = macholib.dyld.framework_info(exclude)
                if info is not None:
                    exclude = os.path.join(info['location'], info['shortname'] + '.framework')
                mm.excludes.append(exclude)
            for fmwk in self.frameworks:
                mm.run_file(fmwk)
            platfiles = mm.run()
            if self.strip:
                self.strip_files(platfiles)
            self.app_files.append(dst)

    def strip_files(self, files):
        unstripped = 0L
        stripfiles = []
        for fn in files:
            unstripped += os.stat(fn).st_size
            stripfiles.append(fn)
            log.info('stripping %s', os.path.basename(fn))
        strip_files(stripfiles, dry_run=self.dry_run, verbose=self.verbose)
        stripped = 0L
        for fn in stripfiles:
            stripped += os.stat(fn).st_size
        log.info('stripping saved %d bytes (%d / %d)',
            unstripped - stripped, stripped, unstripped)

    def copy_dylib(self, src, dst):
        # will be copied from the framework?
        if src != sys.executable:
            force, self.force = self.force, True
            self.copy_file(src, dst)
            self.force = force
        return dst

    def copy_versioned_framework(self, info, dst):
        # XXX - Boy is this ugly, but it makes sense because the developer
        #       could have both Python 2.3 and 2.4, or Tk 8.4 and 8.5, etc.
        #       Saves a good deal of space, and I'm pretty sure this ugly
        #       hack is correct in the general case.
        version = info['version']
        if version is None:
            return self.raw_copy_framework(info, dst)
        short = info['shortname'] + '.framework'
        infile = os.path.join(info['location'], short)
        outfile = os.path.join(dst, short)
        vsplit = os.path.join(infile, 'Versions').split(os.sep)
        def condition(src, vsplit=vsplit, version=version):
            srcsplit = src.split(os.sep)
            if (
                    len(srcsplit) > len(vsplit) and
                    srcsplit[:len(vsplit)] == vsplit and
                    srcsplit[len(vsplit)] != version and
                    not os.path.islink(src)
                ):
                return False
            # Skip Headers, .svn, and CVS dirs
            return framework_copy_condition(src)

        return self.copy_tree(infile, outfile, preserve_symlinks=True, condition=condition)

    def copy_framework(self, info, dst):
        force, self.force = self.force, True
        if info['shortname'] == 'Python':
            self.copy_python_framework(info, dst)
        else:
            self.copy_versioned_framework(info, dst)
        self.force = force
        return os.path.join(dst, info['name'])

    def raw_copy_framework(self, info, dst):
        short = info['shortname'] + '.framework'
        infile = os.path.join(info['location'], short)
        outfile = os.path.join(dst, short)
        return self.copy_tree(infile, outfile, preserve_symlinks=True, condition=framework_copy_condition)

    def copy_python_framework(self, info, dst):
        # XXX - In this particular case we know exactly what we can
        #       get away with.. should this be extended to the general
        #       case?  Per-framework recipes?
        indir = os.path.dirname(os.path.join(info['location'], info['name']))
        outdir = os.path.dirname(os.path.join(dst, info['name']))
        self.mkpath(os.path.join(outdir, 'Resources'))
        self.mkpath(os.path.join(outdir, 'bin'))
        if 0:
            self.copy_tree(
                os.path.join(indir, 'Resources', 'English.lproj'),
                os.path.join(outdir, 'Resources', 'English.lproj'))
        for fn in [os.path.basename(info['name']), 'Resources/Info.plist', 'Resources/version.plist', 'bin/python']:
            self.copy_file(
                os.path.join(indir, fn),
                os.path.join(outdir, fn))
        sym = '/'.join(['..'] * (len(info['name'].split('/')) - 1))
        outf = os.path.join(outdir, 'Frameworks')
        try:
            os.unlink(outf)
        except OSError:
            pass
        os.symlink(sym, outf)

    def fixup_distribution(self):
        dist = self.distribution

        # Convert our args into target objects.
        dist.app = FixupTargets(dist.app, "script")
        dist.plugin = FixupTargets(dist.plugin, "script")
        if dist.app and dist.plugin:
            # XXX - support apps and plugins?
            raise DistutilsOptionError(
                "You must specify either app or plugin, not both")
        elif dist.app:
            self.style = 'app'
            self.targets = dist.app
        elif dist.plugin:
            self.style = 'plugin'
            self.targets = dist.plugin
        else:
            raise DistutilsOptionError(
                "You must specify either app or plugin")
        if len(self.targets) != 1:
            # XXX - support multiple targets?
            raise DistutilsOptionError(
                "Multiple targets not currently supported")
        if not self.extension:
            self.extension = '.' + self.style

        # make sure all targets use the same directory, this is
        # also the directory where the pythonXX.dylib must reside
        paths = set()
        for target in self.targets:
            paths.add(os.path.dirname(target.get_dest_base()))

        if len(paths) > 1:
            raise DistutilsOptionError(
                  "all targets must use the same directory: %s" %
                  ([p for p in paths],))
        if paths:
            app_dir = paths.pop() # the only element
            if os.path.isabs(app_dir):
                raise DistutilsOptionError(
                      "app directory must be relative: %s" % (app_dir,))
            self.app_dir = os.path.join(self.dist_dir, app_dir)
            self.mkpath(self.app_dir)
        else:
            # Do we allow to specify no targets?
            # We can at least build a zipfile...
            self.app_dir = self.lib_dir

    def initialize_prescripts(self):
        prescripts = []
        if self.site_packages or self.alias:
            prescripts.append('site_packages')
        if self.iconfile:
            iconfile = self.iconfile
            if not os.path.exists(iconfile):
                iconfile = iconfile + '.icns'
            if not os.path.exists(iconfile):
                raise DistutilsOptionError, "icon file must exist: %r" % (self.icon,)
            self.resources.append(iconfile)
            self.plist[u'CFBundleIconFile'] = os.path.basename(iconfile)

        if self.argv_emulation and self.style == 'app':
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

        if self.style == 'app' and not self.no_chdir:
            prescripts.append('chdir_resource')
        if not self.alias:
            prescripts.append('disable_linecache')
            prescripts.append('boot_' + self.style)
        else:
            if self.additional_paths:
                prescripts.append('path_inject')
                prescripts.append(
                    StringIO('_path_inject(%r)\n' % (self.additional_paths,)))
            prescripts.append('boot_alias' + self.style)
        newprescripts = []
        for s in prescripts:
            if isinstance(s, basestring):
                newprescripts.append(self.get_bootstrap('py2app.bootstrap.'+s))
            else:
                newprescripts.append(s)

        for target in self.targets:
            prescripts = getattr(target, 'prescripts', [])
            target.prescripts = newprescripts + prescripts


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

    def create_pluginbundle(self, target, script, use_runtime_preference=True):
        base = target.get_dest_base()
        appdir = os.path.join(self.dist_dir, os.path.dirname(base))
        appname = self.get_appname()
        print "*** creating plugin bundle: %s ***" % (appname,)
        if self.runtime_preferences and use_runtime_preference:
            self.plist.setdefault(
                'PyRuntimeLocations', self.runtime_preferences)
        appdir, plist = create_pluginbundle(
            appdir,
            appname,
            plist=self.plist,
            extension=self.extension,
        )
        appdir = fsencoding(appdir)
        resdir = os.path.join(appdir, 'Contents', 'Resources')
        return appdir, resdir, plist

    def create_appbundle(self, target, script, use_runtime_preference=True):
        base = target.get_dest_base()
        appdir = os.path.join(self.dist_dir, os.path.dirname(base))
        appname = self.get_appname()
        print "*** creating application bundle: %s ***" % (appname,)
        if self.runtime_preferences and use_runtime_preference:
            self.plist.setdefault(
                'PyRuntimeLocations', self.runtime_preferences)
        pythonInfo = self.plist.setdefault(u'PythonInfoDict', {})
        py2appInfo = pythonInfo.setdefault(u'py2app', {}).update(dict(
            alias=bool(self.alias),
        ))
        appdir, plist = create_appbundle(
            appdir,
            appname,
            plist=self.plist,
            extension=self.extension,
        )
        appdir = fsencoding(appdir)
        resdir = os.path.join(appdir, 'Contents', 'Resources')
        return appdir, resdir, plist

    def create_bundle(self, target, script, use_runtime_preference=True):
        fn = getattr(self, 'create_%sbundle' % (self.style,))
        return fn(
            target,
            script,
            use_runtime_preference=use_runtime_preference
        )

    def iter_frameworks(self):
        for fn in self.frameworks:
            fmwk = macholib.dyld.framework_info(fn)
            if fmwk is None:
                yield fn
            else:
                basename = fmwk['name'] + '.framework'
                yield os.path.join(fmwk['location'], basename)
    
    def build_alias_executable(self, target, script):
        # Build an alias executable for the target
        appdir, resdir, plist = self.create_bundle(target, script)

        # symlink data files
        for src, dest in self.iter_data_files():
            dest = os.path.join(resdir, dest)
            if src == dest:
                continue
            makedirs(os.path.dirname(dest))
            try:
                os.remove(dest)
            except:
                pass
            os.symlink(os.path.abspath(src), dest)

        # symlink frameworks
        for src in self.iter_frameworks():
            dest = os.path.join(appdir, 'Contents', 'Frameworks', os.path.basename(src))
            if src == dest:
                continue
            makedirs(os.path.dirname(dest))
            try:
                os.remove(dest)
            except:
                pass
            os.symlink(os.path.abspath(src), dest)

        self.compile_datamodels(resdir)

        from Carbon.File import FSRef
        aliasdata = FSRef(script).FSNewAliasMinimal().data

        bootfn = '__boot__'
        bootfile = file(os.path.join(resdir, bootfn + '.py'), 'w')
        for fn in target.prescripts:
            bootfile.write(self.get_bootstrap_data(fn))
            bootfile.write('\n\n')
        bootfile.write('try:\n')
        bootfile.write('    _run((%r, %r))\n' % (
            aliasdata, os.path.realpath(script),
        ))
        bootfile.write('except KeyboardInterrupt:\n')
        bootfile.write('    pass\n')
        bootfile.close()

        target.appdir = appdir
        return appdir

    def build_executable(self, target, arcname, pkgexts, copyexts, script):
        # Build an executable for the target
        appdir, resdir, plist = self.create_bundle(target, script)

        for src, dest in self.iter_data_files():
            dest = os.path.join(resdir, dest)
            self.mkpath(os.path.dirname(dest))
            if os.path.isdir(src):
                self.copy_tree(src, dest, preserve_symlinks=True)
            else:
                self.copy_file(src, dest)

        self.compile_datamodels(resdir)

        bootfn = '__boot__'
        bootfile = file(os.path.join(resdir, bootfn + '.py'), 'w')
        for fn in target.prescripts:
            bootfile.write(self.get_bootstrap_data(fn))
            bootfile.write('\n\n')
        bootfile.write('_run(%r)\n' % (os.path.basename(script),))
        bootfile.close()

        self.copy_file(script, resdir)
        pydir = os.path.join(resdir, 'Python')
        self.mkpath(pydir)
        self.copy_file(arcname, pydir)
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
        for copyext in copyexts:
            fn = os.path.join(ext_dir,
                (copyext.identifier.replace('.', os.sep) +
                os.path.splitext(copyext.filename)[1])
            )
            self.mkpath(os.path.dirname(fn))
            self.copy_file(copyext.filename, fn)

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
