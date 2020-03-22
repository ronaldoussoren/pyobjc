"""
Python mapping for the PushKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from PushKit import _metadata, _PushKit

sys.modules["PushKit"] = mod = objc.ObjCLazyModule(
    "PushKit",
    "com.apple.pushkit",
    objc.pathForFramework("/System/Library/Frameworks/PushKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_PushKit, Foundation),
)


del sys.modules["PushKit._metadata"]
