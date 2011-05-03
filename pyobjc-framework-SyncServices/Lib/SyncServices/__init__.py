'''
Python mapping for the SyncServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from CoreData import *

__bundle__ = _objc.initFrameworkWrapper("SyncServices",
    frameworkIdentifier="com.apple.syncservices",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/SyncServices.framework"),
    globals=globals())
