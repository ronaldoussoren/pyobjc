"""
Python mapping for the SafetyKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from . import _metadata
from . import _SafetyKit

sys.modules["SafetyKit"] = mod = objc.ObjCLazyModule(
    "SafetyKit",
    "com.apple.SafetyKit",
    objc.pathForFramework("/System/Library/Frameworks/SafetyKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (
        _SafetyKit,
        Foundation,
    ),
)

del sys.modules["SafetyKit._metadata"]
