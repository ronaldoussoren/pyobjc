'''
Python mapping for the XgridFoundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import sys
import objc
import Foundation

from XgridFoundation import _metadata

sys.modules['XgridFoundation'] = mod = objc.ObjCLazyModule('XgridFoundation',
    "com.apple.xgrid.foundation",
    objc.pathForFramework("/System/Library/Frameworks/XgridFoundation.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       'objc': objc,
    }, ( Foundation,))
