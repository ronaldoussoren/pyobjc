'''
Python mapping for the InstantMessage framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *
from Quartz import *


__bundle__ = _objc.initFrameworkWrapper("InstantMessage",
    frameworkIdentifier="com.apple.IMFramework",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/InstantMessage.framework"),
    globals=globals())
