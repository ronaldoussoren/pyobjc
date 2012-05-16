'''
Python mapping for the InterfaceBuilderKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''
import sys
import objc
import AppKit

from InterfaceBuilderKit import _metadata

sys.modules['InterfaceBuilderKit'] = mod = objc.ObjCLazyModule('InterfaceBuilderKit',
    "com.apple.InterfaceBuilderKit",
    objc.pathForFramework("/Developer//Library/Frameworks/InterfaceBuilderKit.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       'objc': objc,
    }, ( AppKit,))
