"""
Python mapping for the dispatch library on macOS

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions.
"""

import sys

import objc
import dispatch

sys.modules["libdispatch"] = mod = objc.ObjCLazyModule(
    "libdispatch",
    None,
    None,
    None,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (dispatch,),
)
