"""
Python mapping for the iTunesLibrary framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import os
import sys


import Foundation
import objc
from iTunesLibrary import _metadata

if os.path.exists("/System/Library/Frameworks/iTunesLibrary.framework"):
    # macOS 11
    framework_path = "/System/Library/Frameworks/iTunesLibrary.framework"
else:
    # macOS 10.15 or earlier
    framework_path = "/Library/Frameworks/iTunesLibrary.framework"

sys.modules["iTunesLibrary"] = mod = objc.ObjCLazyModule(
    "iTunesLibrary",
    "com.apple.iTunesLibrary",
    objc.pathForFramework(framework_path),
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


del sys.modules["iTunesLibrary._metadata"]
