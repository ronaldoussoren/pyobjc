"""
Python mapping for the QuickLookThumbnailing framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from QuickLookThumbnailing import _metadata

sys.modules["QuickLookThumbnailing"] = mod = objc.ObjCLazyModule(
    "QuickLookThumbnailing",
    "com.apple.quicklookthumbnailing",
    objc.pathForFramework("/System/Library/Frameworks/QuickLookThumbnailing.framework"),
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


del sys.modules["QuickLookThumbnailing._metadata"]
