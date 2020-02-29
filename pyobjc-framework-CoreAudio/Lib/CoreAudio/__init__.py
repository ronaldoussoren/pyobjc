"""
Python mapping for the CoreAudio framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import CoreAudio._CoreAudio
import Foundation
import objc
from CoreAudio import _metadata
from CoreAudio._inlines import _inline_list_

sys.modules["CoreAudio"] = mod = objc.ObjCLazyModule(
    "CoreAudio",
    "com.apple.CoreAudio",
    objc.pathForFramework("/System/Library/Frameworks/CoreAudio.framework"),
    _metadata.__dict__,
    _inline_list_,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (Foundation,),
)


del sys.modules["CoreAudio._metadata"]


for nm in dir(CoreAudio._CoreAudio):
    setattr(mod, nm, getattr(CoreAudio._CoreAudio, nm))
