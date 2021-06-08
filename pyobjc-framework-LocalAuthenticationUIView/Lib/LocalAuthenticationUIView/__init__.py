"""
Python mapping for the LocalAuthenticationUIView framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import LocalAuthentication
import objc
from . import _metadata

sys.modules["LocalAuthenticationUIView"] = mod = objc.ObjCLazyModule(
    "LocalAuthenticationUIView",
    "com.apple.LocalAuthenticationUIView",
    objc.pathForFramework(
        "/System/Library/Frameworks/LocalAuthenticationUIView.framework"
    ),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (
        LocalAuthentication,
        Cocoa,
    ),
)

del sys.modules["LocalAuthenticationUIView._metadata"]
