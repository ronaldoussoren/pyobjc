"""
Python mapping for the MultipeerConnectivity framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import MultipeerConnectivity._MultipeerConnectivity
import objc
from MultipeerConnectivity import _metadata

sys.modules["MultipeerConnectivity"] = mod = objc.ObjCLazyModule(
    "MultipeerConnectivity",
    "com.apple.MultipeerConnectivity",
    objc.pathForFramework("/System/Library/Frameworks/MultipeerConnectivity.framework"),
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


del sys.modules["MultipeerConnectivity._metadata"]
del sys.modules["MultipeerConnectivity._MultipeerConnectivity"]
