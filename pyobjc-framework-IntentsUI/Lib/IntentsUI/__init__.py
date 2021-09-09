"""
Python mapping for the IntentsUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Intents
import objc
from IntentsUI import _metadata, _IntentsUI

sys.modules["IntentsUI"] = mod = objc.ObjCLazyModule(
    "IntentsUI",
    "com.apple.IntentsUI",
    objc.pathForFramework("/System/Library/Frameworks/IntentsUI.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_IntentsUI, Intents),
)


del sys.modules["IntentsUI._metadata"]
