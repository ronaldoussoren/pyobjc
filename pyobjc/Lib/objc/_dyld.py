from __future__ import generators
"""
dyld emulation
"""

__all__ = [
    'dyld_framework', 'dyld_library', 'dyld_find', 'pathForFramework',
    'infoForFramework',
]

import os
from _framework import infoForFramework

# These are the defaults as per man dyld(1)
#
DEFAULT_FRAMEWORK_FALLBACK = ':'.join([
    os.path.expanduser("~/Library/Frameworks"),
    "/Library/Frameworks",
    "/Network/Library/Frameworks",
    "/System/Library/Frameworks",
])

DEFAULT_LIBRARY_FALLBACK = ':'.join([
    os.path.expanduser("~/lib"),
    "/usr/local/lib",
    "/lib",
    "/usr/lib",
])

def ensure_utf8(s):
    """Not all of PyObjC understands unicode paths very well yet"""
    if isinstance(s, unicode):
        return s.encode('utf8')
    return s

def injectSuffixes(iterator):
    suffix = os.environ.get('DYLD_IMAGE_SUFFIX', None)
    if suffix is None:
        return iterator
    def _inject(iterator=iterator,suffix=suffix):
        for path in iterator:
            if path.endswith('.dylib'):
                yield path[:-6] + suffix + '.dylib'
            else:
                yield path + suffix
            yield path
    return _inject()

def dyld_framework(filename, framework_name, version=None):
    """Find a framework using dyld semantics"""
    filename = ensure_utf8(filename)
    framework_name = ensure_utf8(framework_name)
    version = ensure_utf8(version)

    def _search():
        spath = os.environ.get('DYLD_FRAMEWORK_PATH', None)
        if spath is not None:
            for path in spath.split(':'):
                if version:
                    yield os.path.join(
                        path, framework_name+'.framework',
                        'Versions', version, framework_name
                    )
                else:
                    yield os.path.join(
                        path, framework_name+'.framework', framework_name
                    )
        yield filename
        spath = os.environ.get(
            'DYLD_FALLBACK_FRAMEWORK_PATH', DEFAULT_FRAMEWORK_FALLBACK
        )
        for path in spath.split(':'):
            if version:
                yield os.path.join(
                    path, framework_name+'.framework', 'Versions',
                    version, framework_name
                )
            else:
                yield os.path.join(
                    path, framework_name+'.framework', framework_name
                )
    
    
    for f in injectSuffixes(_search()):
        if os.path.exists(f):
            return f
    # raise ..
    raise ValueError, "Framework %s could not be found" % (framework_name,)

def dyld_library(filename, libname):
    """Find a dylib using dyld semantics"""
    filename = ensure_utf8(filename)
    libname = ensure_utf8(libname)
    def _search():
        spath = os.environ.get('DYLD_LIBRARY_PATH', None)
        if spath is not None:
            for path in spath.split(':'):
                yield os.path.join(path, libname)
        yield filename
        spath = os.environ.get(
            'DYLD_FALLBACK_LIBRARY_PATH', DEFAULT_LIBRARY_FALLBACK
        )
        for path in spath.split(':'):
            yield os.path.join(path, libname)
    for f in injectSuffixes(_search()):
        if os.path.exists(f):
            return f
    raise ValueError, "dylib %s could not be found" % (filename,)

def dyld_find(filename):
    """Generic way to locate a dyld framework or dyld"""
    # if they passed in a framework directory, not a mach-o file
    # then go ahead and look where one would expect to find the mach-o
    filename = ensure_utf8(filename)
    if os.path.isdir(filename):
        filename = os.path.join(
            filename,
            os.path.basename(filename)[:-len(os.path.splitext(filename)[-1])]
        )
    filename = os.path.realpath(filename)
    res = infoForFramework(filename)
    if res:
        framework_loc, framework_name, version = res
        return dyld_framework(filename, framework_name, version)
    else:
        return dyld_library(filename, os.path.basename(filename))

def pathForFramework(path):
    fpath, name, version = infoForFramework(dyld_find(path))
    return os.path.join(fpath, name+'.framework')
