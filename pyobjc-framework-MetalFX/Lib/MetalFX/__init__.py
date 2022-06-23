"""
Python mapping for the MetalFX framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Metal
import objc
from MetalFX import _metadata
import MetalFX._MetalFX

sys.modules["MetalFX"] = mod = objc.ObjCLazyModule(
    "MetalFX",
    "com.apple.MetalFX",
    objc.pathForFramework("/System/Library/Frameworks/MetalFX.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,  # noqa: F405
        "__loader__": globals().get("__loader__", None),
    },
    (MetalFX._MetalFX, Metal),
)

del sys.modules["MetalFX._metadata"]
