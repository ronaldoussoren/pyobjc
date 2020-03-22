"""
Python mapping for the CloudKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from CoreBluetooth import _CoreBluetooth, _metadata

sys.modules["CoreBluetooth"] = mod = objc.ObjCLazyModule(
    "CoreBluetooth",
    "com.apple.CoreBluetooth",
    objc.pathForFramework("/System/Library/Frameworks/CoreBluetooth.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_CoreBluetooth, Foundation),
)


del sys.modules["CoreBluetooth._metadata"]
del sys.modules["CoreBluetooth._CoreBluetooth"]
