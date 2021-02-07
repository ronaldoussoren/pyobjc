"""
Python mapping for the ReplayKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from ReplayKit import _metadata
from ReplayKit import _ReplayKit

sys.modules["ReplayKit"] = mod = objc.ObjCLazyModule(
    "ReplayKit",
    "com.apple.ReplayKit",
    objc.pathForFramework("/System/Library/Frameworks/ReplayKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_ReplayKit, Foundation),
)


del sys.modules["ReplayKit._metadata"]
