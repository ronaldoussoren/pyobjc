"""
Python mapping for the ShazamKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import objc
from . import _metadata, _ShazamKit

sys.modules["ShazamKit"] = mod = objc.ObjCLazyModule(
    "ShazamKit",
    "com.apple.ShazamKit",
    objc.pathForFramework("/System/Library/Frameworks/ShazamKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (
        _ShazamKit,
        Cocoa,
    ),
)

del sys.modules["ShazamKit._metadata"]
