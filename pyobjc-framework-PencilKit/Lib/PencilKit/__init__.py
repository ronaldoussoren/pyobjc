"""
Python mapping for the PencilKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from PencilKit import _metadata

sys.modules["PencilKit"] = mod = objc.ObjCLazyModule(
    "PencilKit",
    "com.apple.pencilkit",
    objc.pathForFramework("/System/Library/Frameworks/PencilKit.framework"),
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


del sys.modules["PencilKit._metadata"]
