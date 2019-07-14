'''
Python mapping for the WiFi framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''

import objc
import sys
import Foundation

from WiFi import _metadata

sys.modules['WiFi'] = mod = objc.ObjCLazyModule(
    "WiFi",
    "com.apple.wifi",
    objc.pathForFramework("/System/Library/Frameworks/WiFi.framework"),
    _metadata.__dict__, None, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    }, (Foundation,))

import sys
del sys.modules['WiFi._metadata']
