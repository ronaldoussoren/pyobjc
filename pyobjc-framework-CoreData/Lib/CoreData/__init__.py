'''
Python mapping for the CoreData framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("CoreData",
    frameworkIdentifier="com.apple.CoreData",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/CoreData.framework"),
    globals=globals())

import CoreData._convenience
