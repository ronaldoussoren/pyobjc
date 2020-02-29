"""
Python mapping for the JavaScriptCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

import CoreFoundation
import JavaScriptCore._util
import objc
from JavaScriptCore import _metadata

sys.modules["JavaScriptCore"] = mod = objc.ObjCLazyModule(
    "JavaScriptCore",
    "com.apple.JavaScriptCore",
    objc.pathForFramework("/System/Library/Frameworks/JavaScriptCore.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (CoreFoundation,),
)


del sys.modules["JavaScriptCore._metadata"]


mod.autoreleasing = JavaScriptCore._util.autoreleasing
