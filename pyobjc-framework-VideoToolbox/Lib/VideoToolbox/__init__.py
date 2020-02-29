"""
Python mapping for the VideoToolbox framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import CoreMedia
import Foundation
import objc
import Quartz
import VideoToolbox._VideoToolbox
from VideoToolbox import _metadata

sys.modules["VideoToolbox"] = mod = objc.ObjCLazyModule(
    "VideoToolbox",
    "com.apple.VideoToolbox",
    objc.pathForFramework("/System/Library/Frameworks/VideoToolbox.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (VideoToolbox._VideoToolbox, Quartz, CoreMedia, Foundation),
)


del sys.modules["VideoToolbox._metadata"]
