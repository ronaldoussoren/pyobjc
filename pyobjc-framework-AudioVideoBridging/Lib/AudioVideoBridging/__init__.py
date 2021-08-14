"""
Python mapping for the AudioVideoBridging framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from . import _metadata

sys.modules["AudioVideoBridging"] = mod = objc.ObjCLazyModule(
    "AudioVideoBridging",
    "com.apple.AudioVideoBridging",
    objc.pathForFramework("/System/Library/Frameworks/AudioVideoBridging.framework"),
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


del sys.modules["AudioVideoBridging._metadata"]
