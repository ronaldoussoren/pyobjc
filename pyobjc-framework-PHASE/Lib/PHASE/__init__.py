"""
Python mapping for the PHASE framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import AVFoundation
import objc
from . import _metadata

sys.modules["PHASE"] = mod = objc.ObjCLazyModule(
    "PHASE",
    "com.apple.audio.PHASE",
    objc.pathForFramework("/System/Library/Frameworks/PHASE.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (AVFoundation,),
)
del sys.modules["PHASE._metadata"]
