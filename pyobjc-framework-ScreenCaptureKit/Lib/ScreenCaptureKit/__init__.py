"""
Python mapping for the ScreenCaptureKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import CoreMedia
import objc
from . import _metadata, _ScreenCaptureKit

sys.modules["ScreenCaptureKit"] = mod = objc.ObjCLazyModule(
    "ScreenCaptureKit",
    "com.apple.ScreenCaptureKit",
    objc.pathForFramework("/System/Library/Frameworks/ScreenCaptureKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (
        _ScreenCaptureKit,
        CoreMedia,
    ),
)

del sys.modules["ScreenCaptureKit._metadata"]
