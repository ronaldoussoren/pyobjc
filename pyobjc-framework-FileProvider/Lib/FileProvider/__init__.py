"""
Python mapping for the FileProvider framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from FileProvider import _metadata
from FileProvider import _FileProvider

sys.modules["FileProvider"] = mod = objc.ObjCLazyModule(
    "FileProvider",
    "com.apple.FileProvider",
    objc.pathForFramework("/System/Library/Frameworks/FileProvider.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_FileProvider, Foundation,),
)


del sys.modules["FileProvider._metadata"]
