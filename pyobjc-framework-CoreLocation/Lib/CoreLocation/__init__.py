'''
Python mapping for the CoreLocation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import sys
import objc
import Foundation

from CoreLocation import _metadata

sys.modules['CoreLocation'] = objc.ObjCLazyModule(
    "CoreLocation", "com.apple.corelocation",
    objc.pathForFramework("/System/Library/Frameworks/CoreLocation.framework"),
    _metadata.__dict__, None, {
        '__doc__': __doc__,
        '__path__': __path__,
        'objc': objc
    }, (Foundation,))
