'''
Python mapping for the InputMethodKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
#import Carbon
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("InputMethodKit",
    frameworkIdentifier="com.apple.InputMethodKit",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/InputMethodKit.framework"),
    globals=globals())
