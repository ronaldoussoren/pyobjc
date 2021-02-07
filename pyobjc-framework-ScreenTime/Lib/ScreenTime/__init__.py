"""
Python mapping for the ScreenTime framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from ScreenTime import _metadata

sys.modules["ScreenTime"] = mod = objc.ObjCLazyModule(
    "ScreenTime",
    "com.apple.ScreenTime",
    objc.pathForFramework("/System/Library/Frameworks/ScreenTime.framework"),
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


del sys.modules["ScreenTime._metadata"]
