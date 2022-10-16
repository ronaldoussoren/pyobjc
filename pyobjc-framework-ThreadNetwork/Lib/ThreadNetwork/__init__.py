"""
Python mapping for the ThreadNetwork framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from ThreadNetwork import _metadata

sys.modules["ThreadNetwork"] = mod = objc.ObjCLazyModule(
    "ThreadNetwork",
    "com.apple.ThreadNetwork",
    objc.pathForFramework("/System/Library/Frameworks/ThreadNetwork.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,  # noqa: F405
        "__loader__": globals().get("__loader__", None),
    },
    (Foundation,),
)

del sys.modules["ThreadNetwork._metadata"]
