"""
Python mapping for the CoreMIDI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from CoreMIDI import _metadata
from CoreMIDI import _CoreMIDI

sys.modules["CoreMIDI"] = mod = objc.ObjCLazyModule(
    "CoreMIDI",
    "com.apple.audio.midi.CoreMIDI",
    "/System/Library/Frameworks/CoreMIDI.framework",
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_CoreMIDI, Foundation),
)


del sys.modules["CoreMIDI._metadata"]
