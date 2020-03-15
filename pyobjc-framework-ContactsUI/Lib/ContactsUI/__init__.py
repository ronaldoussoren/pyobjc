"""
Python mapping for the ContactsUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import AppKit
import Contacts
import objc
from ContactsUI import _metadata
from ContactsUI import _ContactsUI

sys.modules["ContactsUI"] = mod = objc.ObjCLazyModule(
    "ContactsUI",
    "com.apple.ContactsUI.framework",
    objc.pathForFramework("/System/Library/Frameworks/ContactsUI.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_ContactsUI, AppKit, Contacts),
)


del sys.modules["ContactsUI._metadata"]
