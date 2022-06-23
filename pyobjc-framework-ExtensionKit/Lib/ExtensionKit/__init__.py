"""
Python mapping for the ExtensionKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import AppKit
import objc
from ExtensionKit import _metadata
import ExtensionKit._ExtensionKit

sys.modules["ExtensionKit"] = mod = objc.ObjCLazyModule(
    "ExtensionKit",
    "com.apple.ExtensionKit",
    objc.pathForFramework("/System/Library/Frameworks/ExtensionKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,  # noqa: F405
        "__loader__": globals().get("__loader__", None),
    },
    (ExtensionKit._ExtensionKit, AppKit),
)

del sys.modules["ExtensionKit._metadata"]
