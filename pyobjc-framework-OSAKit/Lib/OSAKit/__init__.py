"""
Python mapping for the OSAKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import objc
from OSAKit import _metadata

sys.modules["OSAKit"] = mod = objc.ObjCLazyModule(
    "OSAKit",
    "com.apple.OSAKit",
    objc.pathForFramework("/System/Library/Frameworks/OSAKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (Cocoa,),
)


del sys.modules["OSAKit._metadata"]
