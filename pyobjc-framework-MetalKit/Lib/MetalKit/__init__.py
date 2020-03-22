"""
Python mapping for the MetalKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import Metal
import objc
from MetalKit import _metadata, _MetalKit

sys.modules["MetalKit"] = mod = objc.ObjCLazyModule(
    "MetalKit",
    "com.apple.MetalKit",
    objc.pathForFramework("/System/Library/Frameworks/MetalKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_MetalKit, Metal, Foundation),
)


del sys.modules["MetalKit._metadata"]
