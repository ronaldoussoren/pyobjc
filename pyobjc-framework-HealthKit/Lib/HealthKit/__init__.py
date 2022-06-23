"""
Python mapping for the HealthKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from HealthKit import _metadata
import HealthKit._HealthKit

sys.modules["HealthKit"] = mod = objc.ObjCLazyModule(
    "HealthKit",
    "com.apple.HealthKit",
    objc.pathForFramework("/System/Library/Frameworks/HealthKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,  # noqa: F405
        "__loader__": globals().get("__loader__", None),
    },
    (HealthKit._HealthKit, Foundation),
)

del sys.modules["HealthKit._metadata"]
