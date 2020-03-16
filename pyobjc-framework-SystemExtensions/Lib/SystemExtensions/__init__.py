"""
Python mapping for the SystemExtensions framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from SystemExtensions import _metadata, _SystemExtensions

sys.modules["SystemExtensions"] = mod = objc.ObjCLazyModule(
    "SystemExtensions",
    "com.apple.SystemExtensions",
    objc.pathForFramework("/System/Library/Frameworks/SystemExtensions.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_SystemExtensions, Foundation),
)


del sys.modules["SystemExtensions._metadata"]
