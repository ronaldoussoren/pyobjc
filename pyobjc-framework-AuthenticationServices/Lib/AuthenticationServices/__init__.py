"""
Python mapping for the AuthenticationServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import objc
import sys
import Foundation

from AuthenticationServices import _metadata
from AuthenticationServices import _AuthenticationServices


sys.modules["AuthenticationServices"] = mod = objc.ObjCLazyModule(
    "AuthenticationServices",
    "com.apple.AuthenticationServices",
    objc.pathForFramework("/System/Library/Frameworks/AuthenticationServices.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (Foundation,),
)

import sys

del sys.modules["AuthenticationServices._metadata"]
