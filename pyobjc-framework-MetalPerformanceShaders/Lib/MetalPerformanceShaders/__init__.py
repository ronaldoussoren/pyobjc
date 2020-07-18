"""
Python mapping for the Metal framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import objc
from MetalPerformanceShaders import _metadata
import Metal

sys.modules["Metal"] = mod = objc.ObjCLazyModule(
    "Metal",
    "com.apple.Metal",
    objc.pathForFramework("/System/Library/Frameworks/Metal.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (Metal,),
)


del sys.modules["Metal._metadata"]
