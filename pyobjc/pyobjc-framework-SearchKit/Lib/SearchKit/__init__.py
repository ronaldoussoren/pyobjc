'''
Python mapping for the SearchKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from CoreFoundation import *

__bundle__ = _objc.initFrameworkWrapper("SearchKit",
    frameworkIdentifier="com.apple.SearchKit",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/CoreServices.framework/Frameworks/SearchKit.framework"),
    globals=globals())
