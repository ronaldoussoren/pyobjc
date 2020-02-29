"""
Python mapping for the DeviceCheck framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from DeviceCheck import _metadata

sys.modules["DeviceCheck"] = mod = objc.ObjCLazyModule(
    "DeviceCheck",
    "com.apple.devicecheck",
    objc.pathForFramework("/System/Library/Frameworks/DeviceCheck.framework"),
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


del sys.modules["DeviceCheck._metadata"]
