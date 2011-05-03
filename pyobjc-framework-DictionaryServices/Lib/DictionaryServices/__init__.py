'''
Python mapping for the DictionaryServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
#import ApplicationServices
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("DictionaryServices",
    frameworkIdentifier="com.apple.DictionaryServices",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/CoreServices.framework/Frameworks/DictionaryServices.framework"),
    globals=globals())
