"""
Python mapping for the Collaboration framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from Collaboration import _metadata

sys.modules["Collaboration"] = objc.ObjCLazyModule(
    "Collaboration",
    "com.apple.Collaboration",
    objc.pathForFramework("/System/Library/Frameworks/Collaboration.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
    },
    (Foundation,),
)


del sys.modules["Collaboration._metadata"]
