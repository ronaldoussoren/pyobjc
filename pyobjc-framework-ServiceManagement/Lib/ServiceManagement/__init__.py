'''
Python mapping for the ServiceManagement framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from CoreFoundation import *
#from Security import *

__bundle__ = _objc.initFrameworkWrapper("ServiceManagement",
    frameworkIdentifier="com.apple.bsd.ServiceManagement",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/ServiceManagement.framework"),
    globals=globals())
