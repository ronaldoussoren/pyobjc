"""
Python mapping for the PassKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from PassKit import _metadata
from PassKit import _PassKit

sys.modules["PassKit"] = mod = objc.ObjCLazyModule(
    "PassKit",
    "com.apple.PassKit",
    objc.pathForFramework("/System/Library/Frameworks/PassKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_PassKit, Foundation),
)


del sys.modules["PassKit._metadata"]
