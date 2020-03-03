"""
Python mapping for the AuthenticationServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from AuthenticationServices import _AuthenticationServices, _metadata

sys.modules["AuthenticationServices"] = mod = objc.ObjCLazyModule(
    "AuthenticationServices",
    "com.apple.AuthenticationServices",
    objc.pathForFramework(
        "/System/Library/Frameworks/AuthenticationServices.framework"
    ),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_AuthenticationServices, Foundation),
)


del sys.modules["AuthenticationServices._metadata"]
