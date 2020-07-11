"""
Python mapping for the ClassKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from ClassKit import _metadata
from ClassKit import _ClassKit

sys.modules["ClassKit"] = mod = objc.ObjCLazyModule(
    "ClassKit",
    "com.apple.ClassKit",
    objc.pathForFramework("/System/Library/Frameworks/ClassKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_ClassKit, Foundation),
)


del sys.modules["ClassKit._metadata"]
