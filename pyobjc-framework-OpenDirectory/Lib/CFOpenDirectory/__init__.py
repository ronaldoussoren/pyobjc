'''
Python mapping for the CFOpenDirectory framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from CoreFoundation import *
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("CFOpenDirectory",
    frameworkIdentifier="com.apple.CFOpenDirectory",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/OpenDirectory.framework/Frameworks/CFOpenDirectory.framework"),
    globals=globals())
