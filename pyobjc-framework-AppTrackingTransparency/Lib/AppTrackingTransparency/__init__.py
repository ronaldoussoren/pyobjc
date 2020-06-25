"""
Python mapping for the AppTrackingTransparency framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from AppTrackingTransparency import _metadata

sys.modules["AppTrackingTransparency"] = mod = objc.ObjCLazyModule(
    "AppTrackingTransparency",
    "com.apple.AppTrackingTransparency",
    objc.pathForFramework(
        "/System/Library/Frameworks/AppTrackingTransparency.framework"
    ),
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


del sys.modules["AppTrackingTransparency._metadata"]
