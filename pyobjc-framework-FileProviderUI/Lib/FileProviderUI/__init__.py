"""
Python mapping for the FileProviderUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import objc
import FileProvider
from FileProviderUI import _metadata

sys.modules["FileProviderUI"] = mod = objc.ObjCLazyModule(
    "FileProviderUI",
    "com.apple.FileProviderUI",
    objc.pathForFramework("/System/Library/Frameworks/FileProviderUI.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (FileProvider,),
)


del sys.modules["FileProviderUI._metadata"]
