"""
Python mapping for the AddressBook framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import objc
import Quartz
from AVKit import _AVKit, _metadata

sys.modules["AVKit"] = mod = objc.ObjCLazyModule(
    "AVKit",
    "com.apple.AVKit",
    objc.pathForFramework("/System/Library/Frameworks/AVKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_AVKit, Cocoa, Quartz),
)


del sys.modules["AVKit._metadata"]
del sys.modules["AVKit._AVKit"]
