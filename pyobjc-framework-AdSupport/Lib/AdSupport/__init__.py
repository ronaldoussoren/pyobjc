"""
Python mapping for the AdSupport framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from AdSupport import _metadata

sys.modules["AdSupport"] = mod = objc.ObjCLazyModule(
    "AdSupport",
    "com.apple.AdSupport",
    objc.pathForFramework("/System/Library/Frameworks/AdSupport.framework"),
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


del sys.modules["AdSupport._metadata"]
