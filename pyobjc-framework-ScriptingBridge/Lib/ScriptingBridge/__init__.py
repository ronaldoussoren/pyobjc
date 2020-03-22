"""
Python mapping for the ScriptingBridge framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

import Foundation

# Override the default behaviour of the bridge to ensure that we
# make the minimal amount of AppleScript calls.
import objc
from ScriptingBridge import _metadata
from ScriptingBridge import _ScriptingBridge

sys.modules["ScriptingBridge"] = mod = objc.ObjCLazyModule(
    "ScriptingBridge",
    "com.apple.ScriptingBridge",
    objc.pathForFramework("/System/Library/Frameworks/ScriptingBridge.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
    },
    (_ScriptingBridge, Foundation),
)


del sys.modules["ScriptingBridge._metadata"]


objc.addConvenienceForClass(
    "SBElementArray", [("__iter__", lambda self: iter(self.objectEnumerator()))]
)
