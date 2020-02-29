"""
Python mapping for the ExceptionHandling framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

import Foundation
import objc
from ExceptionHandling import _metadata

sys.modules["ExceptionHandling"] = mod = objc.ObjCLazyModule(
    "ExceptionHandling",
    "com.apple.ExceptionHandling",
    objc.pathForFramework("/System/Library/Frameworks/ExceptionHandling.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
    },
    (Foundation,),
)


del sys.modules["ExceptionHandling._metadata"]
