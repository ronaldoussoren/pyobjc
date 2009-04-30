'''
Python mapping for the CFNetwork framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

from CoreFoundation import *

__bundle__ = objc.initFrameworkWrapper("CFNetwork",
    frameworkIdentifier="com.apple.CFNetwork",
    frameworkPath=objc.pathForFramework(
        "/System/Library/Frameworks/CoreServices.framework/Frameworks/CFNetwork.framework"),
    globals=globals())

def CFSocketStreamSOCKSGetError(err):
    return err.error & 0xFFFF

def CFSocketStreamSOCKSGetErrorSubdomain(err):
    return (err.error >> 16) & 0xFFFF

from CFNetwork._manual import *
