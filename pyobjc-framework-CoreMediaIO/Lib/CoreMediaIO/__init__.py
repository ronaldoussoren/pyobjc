"""
Python mapping for the CoreMediaIO framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from CoreMediaIO import _CoreMediaIO, _metadata

sys.modules["CoreMediaIO"] = mod = objc.ObjCLazyModule(
    "CoreMediaIO",
    "com.apple.CoreMediaIO",
    objc.pathForFramework("/System/Library/Frameworks/CoreMediaIO.framework"),
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


del sys.modules["CoreMediaIO._metadata"]


for nm in dir(_CoreMediaIO):
    setattr(mod, nm, getattr(_CoreMediaIO, nm))


def CMIOGetNextSequenceNumber(value):
    if value == 0xFFFFFFFFFFFFFFFF:
        return 0
    return value + 1


mod.CMIOGetNextSequenceNumber = CMIOGetNextSequenceNumber


def CMIODiscontinuityFlagsHaveHardDiscontinuities(value):
    return (value & mod.kCMIOSampleBufferDiscontinuityFlag_DurationWasExtended) != 0


mod.CMIODiscontinuityFlagsHaveHardDiscontinuities = (
    CMIODiscontinuityFlagsHaveHardDiscontinuities
)
