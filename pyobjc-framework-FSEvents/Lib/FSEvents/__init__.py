'''
Python mapping for the FSEvents framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("FSEvents",
    frameworkIdentifier="com.apple.CoreServices",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/CoreServices.framework"),
    globals=globals())

from FSEvents._callbacks import *
