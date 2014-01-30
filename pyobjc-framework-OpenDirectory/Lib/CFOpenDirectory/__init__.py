'''
Python mapping for the CFOpenDirectory framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import sys
import objc
import CoreFoundation
import Foundation

from CFOpenDirectory import _metadata

sys.modules['CFOpenDirectory'] = mod = objc.ObjCLazyModule('CFOpenDirectory',
    "com.apple.CFOpenDirectory",
    objc.pathForFramework("/System/Library/Frameworks/OpenDirectory.framework/Frameworks/CFOpenDirectory.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       '__loader__': globals().get('__loader__', None),
       'objc': objc,
    }, ( CoreFoundation, Foundation,))

import sys
del sys.modules['CFOpenDirectory._metadata']
