'''
Python mapping for the InterfaceBuilderKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from AppKit import *

__bundle__ = _objc.initFrameworkWrapper("InterfaceBuilderKit",
    frameworkIdentifier="com.apple.InterfaceBuilderKit",
    frameworkPath=_objc.pathForFramework(
        "/Developer/Library/Frameworks/InterfaceBuilderKit.framework"),
    globals=globals())
