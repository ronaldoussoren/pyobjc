"""
Python mapping for the AVRouting framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from AVRouting import _metadata, _AVRouting

sys.modules["AVRouting"] = mod = objc.ObjCLazyModule(
    "AVRouting",
    "com.apple.AVRouting",
    objc.pathForFramework("/System/Library/Frameworks/AVRouting.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (
        _AVRouting,
        Foundation,
    ),
)


del sys.modules["AVRouting._metadata"]
