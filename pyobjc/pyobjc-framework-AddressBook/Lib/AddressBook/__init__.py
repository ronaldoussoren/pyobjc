'''
Python mapping for the AddressBook framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("AddressBook",
    frameworkIdentifier="com.apple.AddressBook.framework",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/AddressBook.framework"),
    globals=globals())

# Implementation of functions that cannot be wrapped automaticly.
from AddressBook._callback import *
