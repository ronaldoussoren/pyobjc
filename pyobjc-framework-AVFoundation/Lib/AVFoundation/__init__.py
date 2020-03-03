"""
Python mapping for the AVFoundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import CoreMedia
import Foundation
import objc
from AVFoundation import _metadata
import AVFoundation._AVFoundation
from AVFoundation._inlines import _inline_list_

sys.modules["AVFoundation"] = mod = objc.ObjCLazyModule(
    "AVFoundation",
    "com.apple.avfoundation",
    objc.pathForFramework("/System/Library/Frameworks/AVFoundation.framework"),
    _metadata.__dict__,
    _inline_list_,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,  # noqa: F405
        "__loader__": globals().get("__loader__", None),
    },
    (AVFoundation._AVFoundation, CoreMedia, Foundation),
)


del sys.modules["AVFoundation._metadata"]
