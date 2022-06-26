"""
Python mapping for the SharedWithYou framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import SharedWithYouCore
import objc
from SharedWithYou import _metadata
import SharedWithYou._SharedWithYou

sys.modules["SharedWithYou"] = mod = objc.ObjCLazyModule(
    "SharedWithYou",
    "com.apple.SharedWithYou",
    objc.pathForFramework("/System/Library/Frameworks/SharedWithYou.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,  # noqa: F405
        "__loader__": globals().get("__loader__", None),
    },
    (SharedWithYou._SharedWithYou, SharedWithYouCore),
)

del sys.modules["SharedWithYou._metadata"]
