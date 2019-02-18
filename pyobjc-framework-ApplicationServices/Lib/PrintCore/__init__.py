'''
Python mapping for the PrintCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import sys
import objc
import Cocoa

from PrintCore import _metadata

sys.modules['PrintCore'] = mod = objc.ObjCLazyModule('PrintCore',
    "com.apple.ApplicationServices",
    objc.pathForFramework("/System/Library/Frameworks/ApplicationServices.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       '__loader__': globals().get('__loader__', None),
       'objc': objc,
    }, ( Cocoa, ))

import sys
del sys.modules['PrintCore._metadata']
