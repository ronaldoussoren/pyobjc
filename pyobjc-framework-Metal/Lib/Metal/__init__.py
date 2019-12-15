"""
Python mapping for the Metal framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import objc
import sys
import Foundation

from Metal import _metadata
from Metal import _Metal
from Metal._inlines import _inline_list_


sys.modules["Metal"] = mod = objc.ObjCLazyModule(
    "Metal",
    "com.apple.Metal",
    objc.pathForFramework("/System/Library/Frameworks/Metal.framework"),
    _metadata.__dict__,
    _inline_list_,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (Foundation,),
)

import sys

del sys.modules["Metal._metadata"]
