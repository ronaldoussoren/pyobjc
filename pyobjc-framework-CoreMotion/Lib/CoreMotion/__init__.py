"""
Python mapping for the CoreMotion framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from CoreMotion import _metadata
from CoreMotion import _CoreMotion

sys.modules["CoreMotion"] = mod = objc.ObjCLazyModule(
    "CoreMotion",
    "com.apple.CoreMotion",
    objc.pathForFramework("/System/Library/Frameworks/CoreMotion.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (
        _CoreMotion,
        Foundation,
    ),
)


del sys.modules["CoreMotion._metadata"]
