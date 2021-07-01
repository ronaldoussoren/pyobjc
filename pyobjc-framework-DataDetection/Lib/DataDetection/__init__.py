"""
Python mapping for the DataDetection framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from . import _metadata

sys.modules["DataDetection"] = mod = objc.ObjCLazyModule(
    "DataDetection",
    "com.apple.DataDetection",
    objc.pathForFramework("/System/Library/Frameworks/DataDetection.framework"),
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


del sys.modules["DataDetection._metadata"]
