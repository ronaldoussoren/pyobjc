"""
Python mapping for the Contacts framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from Contacts import _metadata
from Contacts import _Contacts

sys.modules["Contacts"] = mod = objc.ObjCLazyModule(
    "Contacts",
    "com.apple.Contacts.framework",
    objc.pathForFramework("/System/Library/Frameworks/Contacts.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_Contacts, Foundation),
)


del sys.modules["Contacts._metadata"]
