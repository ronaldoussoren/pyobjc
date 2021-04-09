"""
Python mapping for the CFNetwork framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import os
import sys

import CFNetwork._manual
import CoreFoundation
import objc
from CFNetwork import _metadata


def CFSocketStreamSOCKSGetError(err):
    return err.error & 0xFFFF


def CFSocketStreamSOCKSGetErrorSubdomain(err):
    return (err.error >> 16) & 0xFFFF


frameworkPath = "/System/Library/Frameworks/CFNetwork.framework"
if not os.path.exists(frameworkPath):
    frameworkPath = "/System/Library/Frameworks/CoreServices.framework"


sys.modules["CFNetwork"] = mod = objc.ObjCLazyModule(
    "CFNetwork",
    "com.apple.CFNetwork",
    objc.pathForFramework(frameworkPath),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "CFSocketStreamSOCKSGetError": CFSocketStreamSOCKSGetError,
        "CFSocketStreamSOCKSGetErrorSubdomain": CFSocketStreamSOCKSGetErrorSubdomain,
    },
    (CoreFoundation,),
)


for nm in dir(CFNetwork._manual):
    setattr(mod, nm, getattr(CFNetwork._manual, nm))


del sys.modules["CFNetwork._metadata"]
