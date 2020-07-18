"""
Python mapping for the MetalPerformanceShadersGraph framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import MetalPerformanceShaders
import objc
from MetalPerformanceShadersGraph import _metadata

sys.modules["MetalPerformanceShadersGraph"] = mod = objc.ObjCLazyModule(
    "MetalPerformanceShadersGraph",
    "com.apple.MetalPerformanceShadersGraph",
    objc.pathForFramework(
        "/System/Library/Frameworks/MetalPerformanceShadersGraph.framework"
    ),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (MetalPerformanceShaders,),
)


del sys.modules["MetalPerformanceShadersGraph._metadata"]
