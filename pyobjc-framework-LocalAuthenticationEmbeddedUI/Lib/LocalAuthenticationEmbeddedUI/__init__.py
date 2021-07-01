"""
Python mapping for the LocalAuthenticationEmbeddedUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import LocalAuthentication
import objc
from . import _metadata

sys.modules["LocalAuthenticationEmbeddedUI"] = mod = objc.ObjCLazyModule(
    "LocalAuthenticationEmbeddedUI",
    "com.apple.LocalAuthenticationEmbeddedUI",
    objc.pathForFramework(
        "/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework"
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

del sys.modules["LocalAuthenticationEmbeddedUI._metadata"]
