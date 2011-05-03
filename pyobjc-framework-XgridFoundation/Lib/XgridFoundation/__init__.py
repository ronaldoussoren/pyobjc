'''
Python mapping for the XgridFoundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("XgridFoundation",
    frameworkIdentifier="com.apple.xgrid.foundation",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/XgridFoundation.framework"),
    globals=globals())
