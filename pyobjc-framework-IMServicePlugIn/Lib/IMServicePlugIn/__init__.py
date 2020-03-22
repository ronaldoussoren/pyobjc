"""
Python mapping for the IMServicePlugIn framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import objc
from IMServicePlugIn import _IMServicePlugIn, _metadata

try:
    long
except NameError:
    long = int

sys.modules["IMServicePlugIn"] = mod = objc.ObjCLazyModule(
    "IMServicePlugIn",
    "com.apple.GameKit",
    objc.pathForFramework("/System/Library/Frameworks/GameKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_IMServicePlugIn, Cocoa),
)


del sys.modules["IMServicePlugIn._metadata"]
del sys.modules["IMServicePlugIn._IMServicePlugIn"]
