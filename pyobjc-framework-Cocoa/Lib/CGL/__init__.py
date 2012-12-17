'''
Python mapping for the Foundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''

import objc as _objc

__bundle__ = _objc.initFrameworkWrapper("CGL",
    frameworkIdentifier="com.apple.opengl",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/OpenGL.framework"),
    globals=globals())
