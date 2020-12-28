"""
Python mapping for the AdServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from AdServices import _metadata

sys.modules["AdServices"] = mod = objc.ObjCLazyModule(
    "AdServices",
    "com.apple.AdServices",
    objc.pathForFramework("/System/Library/Frameworks/AdServices.framework"),
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


del sys.modules["AdServices._metadata"]
