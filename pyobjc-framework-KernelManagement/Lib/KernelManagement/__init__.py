"""
Python mapping for the KernelManagement framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from KernelManagement import _metadata

sys.modules["KernelManagement"] = mod = objc.ObjCLazyModule(
    "KernelManagement",
    "com.apple.KernelManagement",
    objc.pathForFramework("/System/Library/Frameworks/KernelManagement.framework"),
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


del sys.modules["KernelManagement._metadata"]
