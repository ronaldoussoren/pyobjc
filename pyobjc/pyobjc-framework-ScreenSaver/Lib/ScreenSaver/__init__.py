'''
Python mapping for the ScreenSaver framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from AppKit import *

from ScreenSaver._inlines import _inline_list_

__bundle__ = _objc.initFrameworkWrapper("ScreenSaver",
    frameworkIdentifier="com.apple.ScreenSaver",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/ScreenSaver.framework"),
    globals=globals(), 
    inlineTab=_inline_list_)

