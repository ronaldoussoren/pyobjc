import os, sys, imp, shutil, stat, operator
from modulegraph.util import *

def fsencoding(s, encoding=sys.getfilesystemencoding()):
    if isinstance(s, unicode):
        s = s.encode(encoding)
    return s

def makedirs(path):
    path = fsencoding(path)
    if not os.path.exists(path):
        os.makedirs(path)

def mergecopy(src, dest):
    if os.path.exists(dest) and os.stat(dest).st_mtime >= os.stat(src).st_mtime:
        return
    copy2(src, dest)
    
def mergetree(src, dst, condition=None, copyfn=mergecopy):
    """Recursively merge a directory tree using mergecopy()."""
    # XXX - symlinks
    src = fsencoding(src)
    dst = fsencoding(dst)
    names = os.listdir(src)
    if not os.path.exists(dst):
        os.mkdir(dst)
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        if condition is not None and not condition(srcname):
            continue
        try:
            if os.path.isdir(srcname):
                mergetree(srcname, dstname, condition=condition)
            else:
                copyfn(srcname, dstname)
        except (IOError, os.error), why:
            errors.append((srcname, dstname, why))
    if errors:
        raise IOError, errors

def move(src, dst):
    shutil.move(fsencoding(src), fsencoding(dst))

def copy2(src, dst):
    shutil.copy2(fsencoding(src), fsencoding(dst))

def fancy_split(s, sep=","):
    # a split which also strips whitespace from the items
    # passing a list or tuple will return it unchanged
    if s is None:
        return []
    if hasattr(s, "split"):
        return [item.strip() for item in s.split(sep)]
    return s

class writablefile(file):
    def __init__(self, fn, *args, **kwargs):
        if not os.access(fn, os.W_OK):
            self._old_mode = os.stat(fn).st_mode
            os.chmod(fn, stat.S_IWRITE | self._old_mode)
        file.__init__(self, fn, *args, **kwargs)

    def close(self):
        name, mode = self.name, getattr(self, '_old_mode', None)
        file.close(self)
        if mode is not None:
            os.chmod(name, mode)

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
        from distutils.dep_util import newer
        from distutils.file_util import copy_file

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
                    if suffix == ".py":
                        compile(mod.filename, cfile, dfile)
                    elif suffix in _py_suffixes:
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

def skipscm(ofn):
    ofn = fsencoding(ofn)
    fn = os.path.basename(ofn)
    if fn == 'CVS' or fn == '.svn':
        return False
    return True

def get_magic(platform=sys.platform):
    if platform == 'darwin':
        import struct
        import macholib.mach_o
        return struct.pack('!L', macholib.mach_o.MH_MAGIC)
    elif platform == 'linux2':
        return '\x7fELF'
    elif platform == 'win32':
        return 'MZ'
    return None

def strip_path(path, dry_run=0, verbose=0, magic=get_magic(), argv_max=(256 * 1024)):
    from distutils import log
    from distutils.util import spawn
    if dry_run or not magic:
        return
    STRIPCMD = ['/usr/bin/strip', '-x', '-S', '-']
    stripfiles = []
    unstripped = 0L
    magic_len = len(magic)
    for root, dirs, files in os.walk(path):
        for fn in files:
            fn = os.path.join(root, fn)
            # Mach-O magic
            if open(fn).read(magic_len) == magic:
                unstripped += os.stat(fn).st_size
                stripfiles.append(fn)
                log.info('stripping %s', os.path.basename(fn))

    # account for obscenely long paths
    tostrip = list(stripfiles)
    while tostrip:
        cmd = list(STRIPCMD)
        pathlen = reduce(operator.add, [len(s)+1 for s in cmd])
        try:
            while pathlen < argv_max:
                cmd.append(tostrip.pop())
                pathlen += len(cmd[-1]) + 1
            else:
                tostrip.append(cmd.pop())
        except IndexError:
            pass

        spawn(cmd, verbose=verbose, dry_run=dry_run)

    stripped = 0L
    for fn in stripfiles:
        stripped += os.stat(fn).st_size
    log.info('stripping saved %d bytes (%d / %d)', unstripped - stripped, stripped, unstripped)

def copy_tree(src, dst,
        preserve_mode=1,
        preserve_times=1,
        preserve_symlinks=0,
        update=0,
        verbose=0,
        dry_run=0,
        condition=None):

    """Copy an entire directory tree 'src' to a new location 'dst'.  Both
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
       'update' and 'verbose' are the same as for 'copy_file'."""


    from distutils.dir_util import mkpath
    from distutils.file_util import copy_file
    from distutils.dep_util import newer
    from distutils.errors import DistutilsFileError
    from distutils import log

    src = fsencoding(src)
    dst = fsencoding(dst)

    if condition is None:
        condition = skipscm

    if not dry_run and not os.path.isdir(src):
        raise DistutilsFileError, \
              "cannot copy tree '%s': not a directory" % src
    try:
        names = os.listdir(src)
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

        if preserve_symlinks and os.path.islink(src_name):
            link_dest = os.readlink(src_name)
            log.info("linking %s -> %s", dst_name, link_dest)
            if not dry_run:
                if update and not newer(src, dst_name):
                    pass
                else:
                    if os.path.exists(dst_name):
                        os.remove(dst_name)
                    os.symlink(link_dest, dst_name)
            outputs.append(dst_name)

        elif os.path.isdir(src_name):
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
