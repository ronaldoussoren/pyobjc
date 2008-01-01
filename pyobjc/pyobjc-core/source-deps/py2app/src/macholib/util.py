from altgraph.compat import *
from modulegraph.util import *
import os
import sys
import stat
import operator
import struct
import shutil
import tempfile
from macholib.mach_o import MH_MAGIC, MH_CIGAM, MH_MAGIC_64, MH_CIGAM_64, FAT_MAGIC
MAGIC = [struct.pack('!L', _) for _ in [MH_MAGIC, MH_CIGAM, MH_MAGIC_64, MH_CIGAM_64, FAT_MAGIC]]
MAGIC_LEN = 4
STRIPCMD = ['/usr/bin/strip', '-x', '-S', '-']

def fsencoding(s, encoding=sys.getfilesystemencoding()):
    if isinstance(s, unicode):
        s = s.encode(encoding)
    return s

def move(src, dst):
    shutil.move(fsencoding(src), fsencoding(dst))

def copy2(src, dst):
    shutil.copy2(fsencoding(src), fsencoding(dst))

def flipwritable(fn, mode=None):
    if os.access(fn, os.W_OK):
        return None
    old_mode = os.stat(fn).st_mode
    os.chmod(fn, stat.S_IWRITE | old_mode)
    return old_mode

class writablefile(file):
    def __init__(self, fn, *args, **kwargs):
        self._old_mode = flipwritable(fn)
        file.__init__(self, fn, *args, **kwargs)

    def close(self):
        file.close(self)
        flipwritable(self.name, self._old_mode)

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
    try:
        os.makedirs(dst)
    except OSError:
        pass
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

def sdk_normalize(filename):
    if filename.startswith('/Developer/SDKs/'):
        pathcomp = filename.split('/')
        del pathcomp[1:4]
        filename = '/'.join(pathcomp)
    return filename

def in_system_path(filename):
    """
    Return True if the file is in a system path
    """
    fn = sdk_normalize(os.path.realpath(filename))
    if fn.startswith('/usr/local/'):
        return False
    elif fn.startswith('/System/') or fn.startswith('/usr/'):
        return True
    else:
        return False

def has_filename_filter(module):
    """
    Return False if the module does not have a filename attribute
    """
    return getattr(module, 'filename', None) is not None

def get_magic():
    return MAGIC

def is_platform_file(path):
    if not os.path.exists(path) or os.path.islink(path):
        return False
    bytes = file(path).read(MAGIC_LEN)
    for magic in MAGIC:
        if bytes == magic:
            return True
    return False

def iter_platform_files(dst):
    for root, dirs, files in os.walk(dst):
        for fn in files:
            fn = os.path.join(root, fn)
            if is_platform_file(fn):
                yield fn

def strip_files(files, argv_max=(256 * 1024)):
    tostrip = [(fn, flipwritable(fn)) for fn in files]
    while tostrip:
        cmd = list(STRIPCMD)
        flips = []
        pathlen = reduce(operator.add, [len(s)+1 for s in cmd])
        while pathlen < argv_max:
            if not tostrip:
                break
            added, flip = tostrip.pop()
            pathlen += len(added) + 1
            cmd.append(added)
            flips.append((added, flip))
        else:
            cmd.pop()
            tostrip.append(flips.pop())
        os.spawnv(os.P_WAIT, cmd[0], cmd)
        for args in flips:
            flipwritable(*args)

def thin_to_archs(fn, archs):
    tempfd, tempname = tempfile.mkstemp()
    command = ["/usr/bin/lipo", fn, "-output", tempname]
    for arch in archs:
        command.extend(["-extract", arch])

    print "Thinning %s to %s" % (fn, ', '.join(archs))
    retval = os.spawnv(os.P_WAIT, command[0], command) != 0
    if retval:
        raise ValueError, 'Error %d returned by: %s' % (retval, ''.join(["'%s'" % arg for arg in command]))
    
    shutil.copyfile(tempname, fn)
