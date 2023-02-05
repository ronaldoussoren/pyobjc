"""
Python mapping for the xpc library on macOS

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions.
"""

import sys

import objc
from xpc import _metadata
from xpc import _xpc

sys.modules["xpc"] = mod = objc.ObjCLazyModule(
    "xpc",
    None,
    None,
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_xpc,),
)

del sys.modules["xpc._metadata"]
