"""
Python mapping for the MetalKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import objc
import sys
import Foundation
#import Metal

from MetalKit import _metadata
from MetalKit import _MetalKit


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
    #(Metal, Foundation,),
    (Foundation,),
)

import sys

del sys.modules["MetalKit._metadata"]
