'''
Python mapping for the SecurityInterface framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''

import objc
import sys
import AppKit

from SecurityInterface import _metadata
#from SecurityInterface._SecurityInterface import *
#from SecurityInterface._inlines import _inline_list_


sys.modules['SecurityInterface'] = mod = objc.ObjCLazyModule(
    "SecurityInterface",
    "com.apple.securityinterface",
    objc.pathForFramework("/System/Library/Frameworks/SecurityInterface.framework"),
    _metadata.__dict__, None, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    }, (AppKit,))

import sys
del sys.modules['SecurityInterface._metadata']
