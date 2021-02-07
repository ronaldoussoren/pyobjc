"""
Python mapping for the CallKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from CallKit import _metadata

sys.modules["CallKit"] = mod = objc.ObjCLazyModule(
    "CallKit",
    "com.apple.CallKit",
    objc.pathForFramework("/System/Library/Frameworks/CallKit.framework"),
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


del sys.modules["CallKit._metadata"]
