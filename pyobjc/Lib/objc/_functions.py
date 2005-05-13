__all__ = ['inject', 'signature']

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

def signature(signature, **kw):
    """
    A Python method decorator that allows easy specification
    of Objective-C selectors.

    Usage::
        
        @objc.signature('i@:if')
        def methodWithX_andY_(self, x, y):
            return 0
    """
    from _objc import selector
    kw['signature'] = signature
    def makeSignature(func):
        return selector(func, **kw)
    return makeSignature
