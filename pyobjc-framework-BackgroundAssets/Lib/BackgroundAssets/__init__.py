"""
Python mapping for the BackgroundAssets framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from BackgroundAssets import _metadata
import BackgroundAssets._BackgroundAssets

sys.modules["BackgroundAssets"] = mod = objc.ObjCLazyModule(
    "BackgroundAssets",
    "com.apple.BackgroundAssets",
    objc.pathForFramework("/System/Library/Frameworks/BackgroundAssets.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,  # noqa: F405
        "__loader__": globals().get("__loader__", None),
    },
    (BackgroundAssets._BackgroundAssets, Foundation),
)

del sys.modules["BackgroundAssets._metadata"]
