'''
Python mapping for the ImageIO framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
import CoreFoundation
#from Quartz.CoreGraphics import *

__bundle__ = _objc.initFrameworkWrapper("ImageIO",
    frameworkIdentifier="com.apple.ImageIO.framework",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/ApplicationServices.framework/Frameworks/ImageIO.framework"),
    globals=globals(),
    frameworkResourceName="Quartz.ImageIO",
    scan_classes=False)
