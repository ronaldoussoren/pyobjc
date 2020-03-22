"""
Python mapping for the ExternalAccessory framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from ExternalAccessory import _metadata
from ExternalAccessory import _ExternalAccessory

sys.modules["ExternalAccessory"] = mod = objc.ObjCLazyModule(
    "ExternalAccessory",
    "com.apple.externalaccessory",
    objc.pathForFramework("/System/Library/Frameworks/ExternalAccessory.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_ExternalAccessory, Foundation),
)


del sys.modules["ExternalAccessory._metadata"]
