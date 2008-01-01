"""
dyld emulation
"""

__all__ = [
    'dyld_framework', 'dyld_library', 'dyld_find', 'pathForFramework',
    'infoForFramework',
]

import os, sys
from _framework import infoForFramework


# These are the defaults as per man dyld(1)
#
DEFAULT_FRAMEWORK_FALLBACK = u':'.join([
    os.path.expanduser(u"~/Library/Frameworks"),
    u"/Library/Frameworks",
    u"/Network/Library/Frameworks",
    u"/System/Library/Frameworks",
])

DEFAULT_LIBRARY_FALLBACK = u':'.join([
    os.path.expanduser(u"~/lib"),
    u"/usr/local/lib",
    u"/lib",
    u"/usr/lib",
])

def ensure_unicode(s):
    """Not all of PyObjC understands unicode paths very well yet"""
    if isinstance(s, str):
        return unicode(s, 'utf8')
    return s

def injectSuffixes(iterator):
    suffix = ensure_unicode(os.environ.get('DYLD_IMAGE_SUFFIX', None))
    if suffix is None:
        return iterator
    def _inject(iterator=iterator,suffix=suffix):
        for path in iterator:
            if path.endswith(u'.dylib'):
                yield path[:-6] + suffix + u'.dylib'
            else:
                yield path + suffix
            yield path
    return _inject()

def dyld_framework(filename, framework_name, version=None):
    """Find a framework using dyld semantics"""
    filename = ensure_unicode(filename)
    framework_name = ensure_unicode(framework_name)
    version = ensure_unicode(version)

    def _search():
        spath = ensure_unicode(os.environ.get('DYLD_FRAMEWORK_PATH', None))
        if spath is not None:
            for path in spath.split(u':'):
                if version:
                    yield os.path.join(
                        path, framework_name + u'.framework',
                        u'Versions', version, framework_name
                    )
                else:
                    yield os.path.join(
                        path, framework_name + u'.framework', framework_name
                    )
        yield filename
        spath = ensure_unicode(os.environ.get(
            'DYLD_FALLBACK_FRAMEWORK_PATH', DEFAULT_FRAMEWORK_FALLBACK
        ))
        for path in spath.split(u':'):
            if version:
                yield os.path.join(
                    path, framework_name + u'.framework', u'Versions',
                    version, framework_name
                )
            else:
                yield os.path.join(
                    path, framework_name + u'.framework', framework_name
                )


    for f in injectSuffixes(_search()):
        if os.path.exists(f):
            return f
    # raise ..
    raise ImportError("Framework %s could not be found" % (framework_name,))

def dyld_library(filename, libname):
    """Find a dylib using dyld semantics"""
    filename = ensure_unicode(filename)
    libname = ensure_unicode(libname)
    def _search():
        spath = ensure_unicode(os.environ.get('DYLD_LIBRARY_PATH', None))
        if spath is not None:
            for path in spath.split(u':'):
                yield os.path.join(path, libname)
        yield filename
        spath = ensure_unicode(os.environ.get(
            'DYLD_FALLBACK_LIBRARY_PATH', DEFAULT_LIBRARY_FALLBACK
        ))
        for path in spath.split(u':'):
            yield os.path.join(path, libname)
    for f in injectSuffixes(_search()):
        if os.path.exists(f):
            return f
    raise ValueError, "dylib %s could not be found" % (filename,)

# Python version upto (at least) 2.5 do not propertly convert unicode
# arguments to os.readlink, the code below works around that.
if sys.version_info[:3] >= (2,6,0):
    _realpath = os.path.realpath

else:
    def _realpath(path):
        """
        Unicode-safe version of os.path.realpath.
        """
        if isinstance(path, unicode):
            fsenc = sys.getfilesystemencoding()
            return os.path.realpath(path.encode(fsenc)).decode(fsenc)

        return os.path.realpath(path)


def dyld_find(filename):
    """Generic way to locate a dyld framework or dyld"""
    # if they passed in a framework directory, not a mach-o file
    # then go ahead and look where one would expect to find the mach-o
#    filename = ensure_unicode(filename)
#    if os.path.isdir(filename):
#        filename = os.path.join(
#            filename,
#            os.path.basename(filename)[:-len(os.path.splitext(filename)[-1])]
#        )
    filename = _realpath(filename)
    res = infoForFramework(filename)
    if res:
        framework_loc, framework_name, version = res
        return dyld_framework(filename, framework_name, version)
    else:
        return dyld_library(filename, os.path.basename(filename))

def pathForFramework(path):
    fpath, name, version = infoForFramework(dyld_find(path))
    return os.path.join(fpath, name + u'.framework')
