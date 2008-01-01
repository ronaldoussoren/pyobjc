'''
Python mapping for the LaunchServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *
#import AE
#import CoreServices

try:
    __bundle__ = _objc.initFrameworkWrapper("LaunchServices",
        frameworkIdentifier="com.apple.LaunchServices",
        frameworkPath=_objc.pathForFramework(
            "/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework"),
        globals=globals())

except ImportError:
    __bundle__ = _objc.initFrameworkWrapper("LaunchServices",
        frameworkIdentifier="com.apple.LaunchServices",
        frameworkPath=_objc.pathForFramework(
            "/System/Library/Frameworks/ApplicationServices.framework/Frameworks/LaunchServices.framework"),
        globals=globals())

# 
# Load an undocumented, yet announced function. This function was announced
# in TN2029 (http://developer.apple.com/technotes/tn/tn2029.html)
_objc.loadBundleFunctions(
        __bundle__, globals(),
        [
            ('_LSCopyAllApplicationURLs', 'v^@', '', { 'arguments': { 0: { 'already_retained': True, 'type_modifier': 'o',  } } } ),
        ])
