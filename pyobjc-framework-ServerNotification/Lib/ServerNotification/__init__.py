'''
Python mapping for the ServerNotification framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import sys
import objc
import Foundation

from ServerNotification import _metadata

sys.modules['ServerNotification'] = mod = objc.ObjCLazyModule('ServerNotification',
    "com.apple.NSServerNotificationCenter",
    objc.pathForFramework("/System/Library/Frameworks/ServerNotification.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       'objc': objc,
    }, ( Foundation,))
