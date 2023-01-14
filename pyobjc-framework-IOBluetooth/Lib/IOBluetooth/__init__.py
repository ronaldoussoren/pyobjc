"""
Python mapping for the IOBluetooth framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import objc
from . import _metadata
from . import _IOBluetooth, _funcmacros


sys.modules["IOBluetooth"] = mod = objc.ObjCLazyModule(
    "IOBluetooth",
    "com.apple.IOBluetooth",
    objc.pathForFramework("/System/Library/Frameworks/IOBluetooth.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (
        _funcmacros,
        _IOBluetooth,
        Cocoa,
    ),
)

del sys.modules["IOBluetooth._metadata"]
