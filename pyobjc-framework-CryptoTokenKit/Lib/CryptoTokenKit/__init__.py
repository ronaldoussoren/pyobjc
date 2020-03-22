"""
Python mapping for the CryptoTokenKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from CryptoTokenKit import _metadata
from CryptoTokenKit import _CryptoTokenKit

sys.modules["CryptoTokenKit"] = mod = objc.ObjCLazyModule(
    "CryptoTokenKit",
    "com.apple.CryptoTokenKit",
    objc.pathForFramework("/System/Library/Frameworks/CryptoTokenKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_CryptoTokenKit, Foundation),
)


del sys.modules["CryptoTokenKit._metadata"]
