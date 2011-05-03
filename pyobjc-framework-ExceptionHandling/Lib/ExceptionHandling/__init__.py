'''
Python mapping for the ExceptionHandling framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("ExceptionHandling",
    frameworkIdentifier="com.apple.ExceptionHandling",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/ExceptionHandling.framework"),
    globals=globals())
