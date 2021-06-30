"""
Python mapping for the MailKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import objc
from . import _metadata

sys.modules["MailKit"] = mod = objc.ObjCLazyModule(
    "Accessibility",
    "com.apple.MailKit",
    objc.pathForFramework("/System/Library/Frameworks/MailKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (Cocoa,),
)


del sys.modules["MailKit._metadata"]
