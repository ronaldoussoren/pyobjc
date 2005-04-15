__all__ = ['inject']

import os
import sys

def _ensure_path(p):
    p = os.path.realpath(p)
    if isinstance(p, unicode):
        p = p.encode(sys.getfilesystemencoding())
    return p

def inject(pid, bundle, useMainThread=True):
    """Loads the given MH_BUNDLE in the target process identified by pid"""
    try:
        from _objc import _inject
        from _dyld import dyld_find
    except ImportError:
        raise NotImplementedError("objc.inject is only supported on Mac OS X 10.3 and later")
    bundlePath = bundle
    systemPath = dyld_find('/usr/lib/libSystem.dylib')
    carbonPath = dyld_find('/System/Library/Frameworks/Carbon.framework/Carbon')
    paths = map(_ensure_path, (bundlePath, systemPath, carbonPath))
    return _inject(
        pid,
        useMainThread,
        *paths
    )
