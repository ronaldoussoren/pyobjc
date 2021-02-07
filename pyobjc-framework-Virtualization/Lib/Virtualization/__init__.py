"""
Python mapping for the Virtualization framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from Virtualization import _metadata

from Virtualization import _Virtualization

sys.modules["Virtualization"] = mod = objc.ObjCLazyModule(
    "Virtualization",
    "com.apple.Virtualization",
    objc.pathForFramework("/System/Library/Frameworks/Virtualization.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_Virtualization, Foundation),
)


del sys.modules["Virtualization._metadata"]
