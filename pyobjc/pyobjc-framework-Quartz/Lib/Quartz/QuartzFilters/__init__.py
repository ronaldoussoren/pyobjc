'''
Python mapping for the QuartzCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("QuartFilters",
    frameworkIdentifier="com.apple.quartzfilters",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/Quartz.framework/Frameworks/QuartzFilters.framework"),
    frameworkResourceName="Quartz.QuartzFilters",
    globals=globals())

