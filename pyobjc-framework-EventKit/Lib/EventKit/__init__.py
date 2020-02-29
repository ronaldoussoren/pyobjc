"""
Python mapping for the EventKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from EventKit import _metadata

sys.modules["EventKit"] = mod = objc.ObjCLazyModule(
    "EventKit",
    "com.apple.ical.EventKit",
    objc.pathForFramework("/System/Library/Frameworks/EventKit.framework"),
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


del sys.modules["EventKit._metadata"]
