'''
Python mapping for the QuickLookUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''
import objc as _objc
from AppKit import *
from Foundation import *
#from QuickLook import *

__bundle__ = _objc.initFrameworkWrapper("QuickLookUI",
    frameworkIdentifier="com.apple.QuickLookUIFramework",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/Quartz.framework/Frameworks/QuickLookUI.framework"),
    globals=globals(),
    frameworkResourceName="Quartz.QuickLookUI",
    )
