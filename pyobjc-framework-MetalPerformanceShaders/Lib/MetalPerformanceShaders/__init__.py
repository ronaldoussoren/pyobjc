"""
Python mapping for the Metal framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import objc
import Metal
from MetalPerformanceShaders import _metadata
from MetalPerformanceShaders import _MetalPerformanceShaders
from MetalPerformanceShaders._inlines import _inline_list_

sys.modules["MetalPerformanceShaders"] = mod = objc.ObjCLazyModule(
    "MetalPerformanceShaders",
    "com.apple.MetalPerformanceShaders",
    objc.pathForFramework(
        "/System/Library/Frameworks/MetalPerformanceShaders.framework"
    ),
    _metadata.__dict__,
    _inline_list_,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_MetalPerformanceShaders, Metal),
)


del sys.modules["MetalPerformanceShaders._metadata"]
