"""
Python mapping for the StoreKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from StoreKit import _metadata
from StoreKit import _StoreKit


def SKLocalizedString(x):
    return Foundation.NSLocalizedStringFromTableInBundle(
        x, None, mod.StoreKitBundle, ""
    )


sys.modules["StoreKit"] = mod = objc.ObjCLazyModule(
    "StoreKit",
    "com.apple.StoreKit",
    objc.pathForFramework("/System/Library/Frameworks/StoreKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "SKLocalizedString": SKLocalizedString,
    },
    (_StoreKit, Foundation),
)


del sys.modules["StoreKit._metadata"]
