"""
Python mapping for the Speech framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import objc
import sys
import Foundation

from Speech import _metadata
from Speech import _Speech


sys.modules["Speech"] = mod = objc.ObjCLazyModule(
    "Speech",
    "com.apple.Speech",
    objc.pathForFramework("/System/Library/Frameworks/Speech.framework"),
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

import sys

del sys.modules["Speech._metadata"]
