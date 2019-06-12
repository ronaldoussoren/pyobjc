'''
Python mapping for the Logging framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''

import objc
import sys
import Foundation

from Logging import _metadata

sys.modules['Logging'] = mod = objc.ObjCLazyModule(
    "Logging",
    "com.apple.logging",
    objc.pathForFramework("/System/Library/Frameworks/Logging.framework"),
    _metadata.__dict__, _inline_list_, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    }, (Foundation,))

import sys
del sys.modules['Logging._metadata']
