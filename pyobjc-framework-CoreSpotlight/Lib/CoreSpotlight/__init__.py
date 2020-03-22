"""
Python mapping for the CoreSpotlight framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from CoreSpotlight import _metadata
from CoreSpotlight import _CoreSpotlight

sys.modules["CoreSpotlight"] = mod = objc.ObjCLazyModule(
    "CoreSpotlight",
    "com.apple.CoreSpotlight",
    objc.pathForFramework("/System/Library/Frameworks/CoreSpotlight.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_CoreSpotlight, Foundation),
)


del sys.modules["CoreSpotlight._metadata"]
