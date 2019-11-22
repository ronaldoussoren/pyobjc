"""
Python mapping for the SystemExtensions framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import objc
import sys
import Foundation

from SystemExtensions import _metadata
from SystemExtensions import _SystemExtensions


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
    (Foundation,),
)

import sys

del sys.modules["SystemExtensions._metadata"]
