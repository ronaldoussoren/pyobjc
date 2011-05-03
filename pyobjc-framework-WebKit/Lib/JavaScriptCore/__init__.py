'''
Python mapping for the JavaScriptCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from CoreFoundation import *


__bundle__ = _objc.initFrameworkWrapper("JavaScriptCore",
    frameworkIdentifier="com.apple.JavaScriptCore",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/WebKit.framework/Frameworks/JavaScriptCore.framework"),
    globals=globals())
