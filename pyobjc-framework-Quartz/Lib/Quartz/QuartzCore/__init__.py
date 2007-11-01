'''
Python mapping for the QuartzCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Quartz.CoreVideo import *
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("QuartzCore",
    frameworkIdentifier="com.apple.QuartzCore",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/QuartzCore.framework"),
    globals=globals())

