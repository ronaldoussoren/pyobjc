'''
Python mapping for the SystemConfiguration framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("SystemConfiguration",
    frameworkIdentifier="com.apple.SystemConfiguration",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/SystemConfiguration.framework"),
    globals=globals())

from SystemConfiguration._manual import *
