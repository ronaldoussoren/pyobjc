'''
Python mapping for the CoreVideo framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from CoreFoundation import *

__bundle__ = _objc.initFrameworkWrapper("CoreVideo",
    frameworkIdentifier="com.apple.CoreVideo",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/CoreVideo.framework"),
    globals=globals(),
    frameworkResourceName="Quartz.CoreVideo",
    scan_classes=False) 

from Quartz.CoreVideo._CVPixelBuffer import *
