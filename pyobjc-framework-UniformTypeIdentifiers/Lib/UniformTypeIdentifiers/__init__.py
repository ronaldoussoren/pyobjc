"""
Python mapping for the UniformTypeIdentifiers framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from UniformTypeIdentifiers import _metadata

sys.modules["UniformTypeIdentifiers"] = mod = objc.ObjCLazyModule(
    "UniformTypeIdentifiers",
    "com.apple.UniformTypeIdentifiers",
    objc.pathForFramework(
        "/System/Library/Frameworks/UniformTypeIdentifiers.framework"
    ),
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


del sys.modules["UniformTypeIdentifiers._metadata"]
