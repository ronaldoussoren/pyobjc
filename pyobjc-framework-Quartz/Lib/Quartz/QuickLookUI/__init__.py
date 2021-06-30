"""
Python mapping for the QuickLookUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

import Cocoa
import objc
from Quartz.QuickLookUI import _metadata
from Quartz.QuickLookUI import _QuickLookUI

sys.modules["Quartz.QuickLookUI"] = mod = objc.ObjCLazyModule(
    "Quartz.QuickLookUI",
    "com.apple.QuickLookUIFramework",
    objc.pathForFramework(
        # XXX: This moved to a separate framework in macOS 12
        "/System/Library/Frameworks/Quartz.framework/Frameworks/QuickLookUI.framework"
    ),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
    },
    (_QuickLookUI, Cocoa),
)


del sys.modules["Quartz.QuickLookUI._metadata"]
