'''
Python mapping for the ImageKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from AppKit import *
from Foundation import *
#from Quartz.QuartzCore import *

__bundle__ = _objc.initFrameworkWrapper("ImageKit",
    frameworkIdentifier="com.apple.imageKit",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/Quartz.framework/Frameworks/ImageKit.framework"),
    frameworkResourceName="Quartz.ImageKit",
    globals=globals())
