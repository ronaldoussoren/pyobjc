"""
Python mapping for the IOBluetoothUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import IOBluetooth
import objc
from . import _metadata


sys.modules["IOBluetoothUI"] = mod = objc.ObjCLazyModule(
    "IOBluetoothUI",
    "com.apple.BluetoothUI",
    objc.pathForFramework("/System/Library/Frameworks/IOBluetoothUI.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (IOBluetooth,),
)

del sys.modules["IOBluetoothUI._metadata"]
