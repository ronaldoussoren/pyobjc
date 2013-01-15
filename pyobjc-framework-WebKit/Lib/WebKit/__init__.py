'''
Python mapping for the WebKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import objc
import sys
import Foundation

from WebKit import _metadata
from WebKit._WebKit import *

sys.modules['WebKit'] = mod = objc.ObjCLazyModule(
    "WebKit",
    "com.apple.WebKit",
    objc.pathForFramework("/System/Library/Frameworks/WebKit.framework"),
    _metadata.__dict__, None, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
    }, (Foundation,))
