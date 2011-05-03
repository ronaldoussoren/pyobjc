'''
Python mapping for the PubSub framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("PubSub",
    frameworkIdentifier="com.apple.PubSub",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/PubSub.framework"),
    globals=globals())
