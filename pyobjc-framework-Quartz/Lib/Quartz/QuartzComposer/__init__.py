'''
Python mapping for the QuartzComposer framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Quartz.CoreGraphics import *
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("QuartzComposer",
    frameworkIdentifier="com.apple.QuartzComposer",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/Quartz.framework/Frameworks/QuartzComposer.framework"),
    frameworkResourceName="Quartz.QuartzComposer",
    globals=globals())
