"""
Python mapping for the FileProvider framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import objc
import sys
import Foundation

from FileProvider import _metadata


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
    (Foundation,),
)

import sys

del sys.modules["FileProvider._metadata"]
