"""
Python mapping for the CoreMedia framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from CoreMedia import _CoreMedia, _macros, _metadata

sys.modules["CoreMedia"] = mod = objc.ObjCLazyModule(
    "CoreMedia",
    "com.apple.CoreMedia",
    objc.pathForFramework("/System/Library/Frameworks/CoreMedia.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_macros, _CoreMedia, Foundation),
)


del sys.modules["CoreMedia._metadata"]
