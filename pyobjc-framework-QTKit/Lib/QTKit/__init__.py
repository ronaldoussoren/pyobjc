'''
Python mapping for the QTKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Cocoa import *
from Quartz import *
#import QuickTime

__bundle__ = _objc.initFrameworkWrapper("QTKit",
    frameworkIdentifier="com.apple.QTKit",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/QTKit.framework"),
    globals=globals())
