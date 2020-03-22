"""
Python mapping for the CoreData framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from CoreData import _metadata
from CoreData import _CoreData

sys.modules["CoreData"] = objc.ObjCLazyModule(
    "CoreData",
    "com.apple.CoreData",
    objc.pathForFramework("/System/Library/Frameworks/CoreData.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
    },
    (_CoreData, Foundation),
)

from CoreData import _convenience  # isort: ignore  # noqa: E402, F401

del sys.modules["CoreData._metadata"]
