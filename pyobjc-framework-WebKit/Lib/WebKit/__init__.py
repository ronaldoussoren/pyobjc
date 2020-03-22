"""
Python mapping for the WebKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

import Foundation
import objc
from WebKit import _metadata
from WebKit import _WebKit

objc.addConvenienceForBasicSequence("WebScriptObject", True)

sys.modules["WebKit"] = mod = objc.ObjCLazyModule(
    "WebKit",
    "com.apple.WebKit",
    objc.pathForFramework("/System/Library/Frameworks/WebKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_WebKit, Foundation),
)


del sys.modules["WebKit._metadata"]
