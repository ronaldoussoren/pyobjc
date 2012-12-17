'''
Python mapping for the InstantMessage framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import sys
import objc
import Foundation
import Quartz

from InstantMessage import _metadata

sys.modules['InstantMessage'] = mod = objc.ObjCLazyModule('InstantMessage',
    "com.apple.IMFramework",
    objc.pathForFramework("/System/Library/Frameworks/InstantMessage.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       'objc': objc,
    }, ( Foundation, Quartz,))
