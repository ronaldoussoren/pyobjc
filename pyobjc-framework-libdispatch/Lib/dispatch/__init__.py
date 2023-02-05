"""
Python mapping for the dispatch library on macOS

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions.
"""

import sys

import objc
from dispatch import _metadata
from dispatch._inlines import _inline_list_

sys.modules["dispatch"] = mod = objc.ObjCLazyModule(
    "dispatch",
    None,
    None,
    _metadata.__dict__,
    _inline_list_,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
)


import dispatch._dispatch as _manual  # isort:skip # noqa: E402

for nm in dir(_manual):
    if nm.startswith("__"):
        continue
    setattr(mod, nm, getattr(_manual, nm))


del sys.modules["dispatch._metadata"]
