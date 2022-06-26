"""
Python mapping for the SharedWithYouCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import AppKit
import objc
from SharedWithYouCore import _metadata
import SharedWithYouCore._SharedWithYouCore

sys.modules["SharedWithYouCore"] = mod = objc.ObjCLazyModule(
    "SharedWithYouCore",
    "com.apple.SharedWithYouCore",
    objc.pathForFramework("/System/Library/Frameworks/SharedWithYouCore.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,  # noqa: F405
        "__loader__": globals().get("__loader__", None),
    },
    (SharedWithYouCore._SharedWithYouCore, AppKit),
)

del sys.modules["SharedWithYouCore._metadata"]
