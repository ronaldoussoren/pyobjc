'''
Python mapping for the QTKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import sys
import objc
import Cocoa
import Quartz

from QTKit import _metadata

sys.modules['QTKit'] = mod = objc.ObjCLazyModule('QTKit',
    "com.apple.QTKit",
    objc.pathForFramework("/System/Library/Frameworks/QTKit.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       'objc': objc,
    }, ( Cocoa, Quartz,))
