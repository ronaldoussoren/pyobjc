from pkg_resources import require
require("modulegraph", "altgraph", "macholib")

import os, sys, imp, zipfile, time
from modulegraph.find_modules import PY_SUFFIXES, C_SUFFIXES
from modulegraph.util import *
from modulegraph.modulegraph import os_listdir
from altgraph.compat import *
import macholib.util

def os_path_islink(path):
    """
    os.path.islink with zipfile support.

    Luckily zipfiles cannot contain symlink, therefore the implementation is
    trivial.
    """
    return os.path.islink(path)

def os_readlink(path):
    """
    os.readlink with zipfile support.

    Luckily zipfiles cannot contain symlink, therefore the implementation is
    trivial.
    """
    return os.readlink(path)

def os_path_isdir(path):
    """
    os.path.isdir that understands zipfiles.

    Assumes that you're checking a path the is the result of os_listdir and 
    might give false positives otherwise.
    """
    while path.endswith('/') and path != '/':
        path = path[:-1]

    zf, zp = path_to_zip(path)
    if zf is None:
        return os.path.isdir(zp)

    else:
        zip = zipfile.ZipFile(zf)
        try:
            info = zip.getinfo(zp)

        except KeyError:
            return True

        else:
            # Not quite true, you can store information about directories in
            # zipfiles, but those have a lash at the end of the filename
            return False

def copy_file(source, destination, dry_run=0):
    zf, zp = path_to_zip(source)
    if zf is None:
        data = open(zp,'rb').read()
    else:
        data = get_zip_data(zf, zp)

    if not dry_run:
        fp = open(destination, 'wb')
        fp.write(data)
        fp.close()

def get_zip_data(path_to_zip, path_in_zip):
    zf = zipfile.ZipFile(path_to_zip)
    return zf.read(path_in_zip)

def path_to_zip(path):
    """
    Returns (pathtozip, pathinzip). If path isn't in a zipfile pathtozip
    will be None
    """
    from distutils.errors import DistutilsFileError
    if os.path.exists(path):
        return (None, path)

    else:
        rest = ''
        while not os.path.exists(path):
            path, r = os.path.split(path)
            rest = os.path.join(r, rest)

        if not os.path.isfile(path):
            # Directory really doesn't exist
            raise DistutilsFileError(path)

        try:
           zf = zipfile.ZipFile(path)
        except zipfile.BadZipfile:
           raise DistutilsFileError(path)

        if rest.endswith('/'):
            rest = rest[:-1]

        return path, rest


def get_mtime(path, mustExist=True):
    """
    Get mtime of a path, even if it is inside a zipfile
    """

    try:
        return os.stat(path).st_mtime

    except os.error:
        from distutils.errors import DistutilsFileError
        try:
            path, rest = path_to_zip(path)
        except DistutilsFileError:
            if not mustExist:
                return -1
            raise

        zf = zipfile.ZipFile(path)
        info = zf.getinfo(rest)
        return time.mktime(info.date_time + (0, 0, 0))

def newer(source, target):
    """
    distutils.dep_utils.newer with zipfile support
    """

    msource = get_mtime(source)
    mtarget = get_mtime(target, mustExist=False)

    return msource > mtarget



def find_version(fn):
    """
    Try to find a __version__ assignment in a source file
    """
    import compiler
    from compiler.ast import Module, Stmt, Assign, AssName, Const
    ast = compiler.parseFile(fn)
    if not isinstance(ast, Module):
        raise ValueError, "expecting Module"
    statements = ast.getChildNodes()
    if not (len(statements) == 1 and isinstance(statements[0], Stmt)):
        raise ValueError, "expecting one Stmt"
    for node in statements[0].getChildNodes():
        if not isinstance(node, Assign):
            continue
        if not len(node.nodes) == 1:
            continue
        assName = node.nodes[0]
        if not (
                isinstance(assName, AssName) and
                isinstance(node.expr, Const) and
                assName.flags == 'OP_ASSIGN' and
                assName.name == '__version__'
                ):
            continue
        return node.expr.value
    else:
        raise ValueError, "Version not found"

def in_system_path(filename):
    """
    Return True if the file is in a system path
    """
    return macholib.util.in_system_path(filename)

def fsencoding(s, encoding=sys.getfilesystemencoding()):
    return macholib.util.fsencoding(s, encoding=encoding)

def make_exec(path):
    mask = os.umask(0)
    os.umask(mask)
    os.chmod(path, os.stat(path).st_mode | (0111 & ~mask))

def makedirs(path):
    path = fsencoding(path)
    if not os.path.exists(path):
        os.makedirs(path)

def mergecopy(src, dest):
    return macholib.util.mergecopy(src, dest)

def mergetree(src, dst, condition=None, copyfn=mergecopy):
    """Recursively merge a directory tree using mergecopy()."""
    return macholib.util.mergetree(src, dst, condition=condition, copyfn=copyfn)

def move(src, dst):
    return macholib.util.move(src, dst)

def copy2(src, dst):
    return macholib.util.copy2(src, dst)

def fancy_split(s, sep=","):
    # a split which also strips whitespace from the items
    # passing a list or tuple will return it unchanged
    if s is None:
        return []
    if hasattr(s, "split"):
        return [item.strip() for item in s.split(sep)]
    return s

class FileSet(object):
    # A case insensitive but case preserving set of files
    def __init__(self, iterable=None):
        self._dict = {}
        if iterable is not None:
            for arg in iterable:
                self.add(arg)

    def __repr__(self):
        return "<FileSet %s at %x>" % (self._dict.values(), id(self))

    def add(self, fname):
        self._dict[fname.upper()] = fname

    def remove(self, fname):
        del self._dict[fname.upper()]

    def __contains__(self, fname):
        return fname.upper() in self._dict.keys()

    def __getitem__(self, index):
        key = self._dict.keys()[index]
        return self._dict[key]

    def __len__(self):
        return len(self._dict)

    def copy(self):
        res = FileSet()
        res._dict.update(self._dict)
        return res

LOADER = """
def __load():
    import imp, os, sys
    ext = %r
    for path in sys.path:
        if not path.endswith('lib-dynload'):
            continue
        ext = os.path.join(path, ext)
        if os.path.exists(ext):
            #print "py2app extension module", __name__, "->", ext
            mod = imp.load_dynamic(__name__, ext)
            #mod.frozen = 1
            break
        else:
            raise ImportError, repr(ext) + " not found"
    else:
        raise ImportError, "lib-dynload not found"
__load()
del __load
"""

def make_loader(fn):
    return LOADER % fn

def byte_compile(py_files, optimize=0, force=0,
                 target_dir=None, verbose=1, dry_run=0,
                 direct=None):

    if direct is None:
        direct = (__debug__ and optimize == 0)

    # "Indirect" byte-compilation: write a temporary script and then
    # run it with the appropriate flags.
    if not direct:
        from tempfile import mktemp
        from distutils.util import execute, spawn
        script_name = mktemp(".py")
        if verbose:
            print "writing byte-compilation script '%s'" % script_name
        if not dry_run:
            script = open(script_name, "w")
            script.write("""
from py2app.util import byte_compile
from modulegraph.modulegraph import *
files = [
""")

            for f in py_files:
                script.write(repr(f) + ",\n")
            script.write("]\n")
            script.write("""
byte_compile(files, optimize=%r, force=%r,
             target_dir=%r,
             verbose=%r, dry_run=0,
             direct=1)
""" % (optimize, force, target_dir, verbose))

            script.close()

        cmd = [sys.executable, script_name]
        if optimize == 1:
            cmd.insert(1, "-O")
        elif optimize == 2:
            cmd.insert(1, "-OO")
        spawn(cmd, verbose=verbose, dry_run=dry_run)
        execute(os.remove, (script_name,), "removing %s" % script_name,
                verbose=verbose, dry_run=dry_run)


    else:
        from py_compile import compile
        from distutils.dir_util import mkpath

        for mod in py_files:
            # Terminology from the py_compile module:
            #   cfile - byte-compiled file
            #   dfile - purported source filename (same as 'file' by default)
            if mod.filename == mod.identifier:
                cfile = os.path.basename(mod.filename)
                dfile = cfile + (__debug__ and 'c' or 'o')
            else:
                cfile = mod.identifier.replace('.', os.sep)

                if mod.packagepath:
                    dfile = cfile + os.sep + '__init__.py' + (__debug__ and 'c' or 'o')
                else:
                    dfile = cfile + '.py' + (__debug__ and 'c' or 'o')
            if target_dir:
                cfile = os.path.join(target_dir, dfile)

            if force or newer(mod.filename, cfile):
                if verbose:
                    print "byte-compiling %s to %s" % (mod.filename, dfile)
                if not dry_run:
                    mkpath(os.path.dirname(cfile))
                    suffix = os.path.splitext(mod.filename)[1]

                    if suffix in ('.py', '.pyw'):
                        zfile, pth = path_to_zip(mod.filename)
                        if zfile is None:
                            compile(mod.filename, cfile, dfile)
                        else:
                            fn = dfile + '.py'
                            open(fn, 'wb').write(get_zip_data(zfile, pth))
                            compile(mod.filename, cfile, dfile)
                            os.unlink(fn)

                    elif suffix in PY_SUFFIXES:
                        # Minor problem: This will happily copy a file
                        # <mod>.pyo to <mod>.pyc or <mod>.pyc to
                        # <mod>.pyo, but it does seem to work.
                        copy_file(mod.filename, cfile)
                    else:
                        raise RuntimeError \
                              ("Don't know how to handle %r" % mod.filename)
            else:
                if verbose:
                    print "skipping byte-compilation of %s to %s" % \
                          (mod.filename, dfile)

SCMDIRS = ['CVS', '.svn']
def skipscm(ofn):
    ofn = fsencoding(ofn)
    fn = os.path.basename(ofn)
    if fn in SCMDIRS:
        return False
    return True

def skipfunc(junk=(), junk_exts=(), chain=()):
    junk = set(junk)
    junk_exts = set(junk_exts)
    chain = tuple(chain)
    def _skipfunc(fn):
        if os.path.basename(fn) in junk:
            return False
        elif os.path.splitext(fn)[1] in junk_exts:
            return False
        for func in chain:
            if not func(fn):
                return False
        else:
            return True
    return _skipfunc

JUNK = ['.DS_Store', '.gdb_history', 'build', 'dist'] + SCMDIRS
JUNK_EXTS = ['.pbxuser', '.pyc', '.pyo', '.swp']
skipjunk = skipfunc(JUNK, JUNK_EXTS)

def get_magic(platform=sys.platform):
    if platform == 'darwin':
        import struct
        import macholib.mach_o
        return [
            struct.pack('!L', macholib.mach_o.MH_MAGIC),
            struct.pack('!L', macholib.mach_o.MH_CIGAM),
            struct.pack('!L', macholib.mach_o.MH_MAGIC_64),
            struct.pack('!L', macholib.mach_o.MH_CIGAM_64),
            struct.pack('!L', macholib.mach_o.FAT_MAGIC),
        ]
    elif platform == 'linux2':
        return ['\x7fELF']
    elif platform == 'win32':
        return ['MZ']
    return None

def iter_platform_files(path, is_platform_file=macholib.util.is_platform_file):
    """
    Iterate over all of the platform files in a directory
    """
    for root, dirs, files in os.walk(path):
        for fn in files:
            fn = os.path.join(root, fn)
            if is_platform_file(fn):
                yield fn

def strip_files(files, dry_run=0, verbose=0):
    """
    Strip the given set of files
    """
    if dry_run:
        return
    return macholib.util.strip_files(files)

def copy_tree(src, dst,
        preserve_mode=1,
        preserve_times=1,
        preserve_symlinks=0,
        update=0,
        verbose=0,
        dry_run=0,
        condition=None):

    """
    Copy an entire directory tree 'src' to a new location 'dst'.  Both
    'src' and 'dst' must be directory names.  If 'src' is not a
    directory, raise DistutilsFileError.  If 'dst' does not exist, it is
    created with 'mkpath()'.  The end result of the copy is that every
    file in 'src' is copied to 'dst', and directories under 'src' are
    recursively copied to 'dst'.  Return the list of files that were
    copied or might have been copied, using their output name.  The
    return value is unaffected by 'update' or 'dry_run': it is simply
    the list of all files under 'src', with the names changed to be
    under 'dst'.

    'preserve_mode' and 'preserve_times' are the same as for
    'copy_file'; note that they only apply to regular files, not to
    directories.  If 'preserve_symlinks' is true, symlinks will be
    copied as symlinks (on platforms that support them!); otherwise
    (the default), the destination of the symlink will be copied.
    'update' and 'verbose' are the same as for 'copy_file'.
    """


    from distutils.dir_util import mkpath
    from distutils.file_util import copy_file
    from distutils.dep_util import newer
    from distutils.errors import DistutilsFileError
    from distutils import log

    src = fsencoding(src)
    dst = fsencoding(dst)

    if condition is None:
        condition = skipscm

    if not dry_run and not os_path_isdir(src):
        raise DistutilsFileError, \
              "cannot copy tree '%s': not a directory" % src
    try:
        names = os_listdir(src)
    except os.error, (errno, errstr):
        if dry_run:
            names = []
        else:
            raise DistutilsFileError, \
                  "error listing files in '%s': %s" % (src, errstr)

    if not dry_run:
        mkpath(dst)

    outputs = []

    for n in names:
        src_name = os.path.join(src, n)
        dst_name = os.path.join(dst, n)
        if (condition is not None) and (not condition(src_name)):
            continue

        if preserve_symlinks and os_path_islink(src_name):
            link_dest = os_readlink(src_name)
            log.info("linking %s -> %s", dst_name, link_dest)
            if not dry_run:
                if update and not newer(src, dst_name):
                    pass
                else:
                    if os_path_islink(dst_name):
                        os.remove(dst_name)
                    os.symlink(link_dest, dst_name)
            outputs.append(dst_name)

        elif os_path_isdir(src_name):
            outputs.extend(
                copy_tree(src_name, dst_name, preserve_mode,
                          preserve_times, preserve_symlinks, update,
                          dry_run=dry_run, condition=condition))
        else:
            copy_file(src_name, dst_name, preserve_mode,
                      preserve_times, update, dry_run=dry_run)
            outputs.append(dst_name)

    return outputs


def walk_files(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            yield f

def find_app(app):
    dpath = os.path.realpath(app)
    if os.path.exists(dpath):
        return dpath
    if os.path.isabs(app):
        return None
    for path in os.environ.get('PATH', '').split(':'):
        dpath = os.path.realpath(os.path.join(path, app))
        if os.path.exists(dpath):
            return dpath
    return None

MOMC = '/Library/Application Support/Apple/Developer Tools/Plug-ins/XDCoreDataModel.xdplugin/Contents/Resources/momc'
if not os.path.exists(MOMC):
    MOMC = '/Developer/Library/Xcode/Plug-ins/XDCoreDataModel.xdplugin/Contents/Resources/momc'

def momc(src, dst):
    os.spawnv(os.P_WAIT, MOMC, [MOMC, src, dst])

MAPC = '/Developer/Library/Xcode/Plug-ins/XDMappingModel.xdplugin/Contents/Resources/mapc'
def mapc(src, dst):
    os.spawnv(os.P_WAIT, MAPC, [MAPC, src, dst])
