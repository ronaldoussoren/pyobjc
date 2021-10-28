"""
Python mapping for the Accessibility framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Quartz
import objc
from . import _metadata
from . import _Accessibility

sys.modules["Accessibility"] = mod = objc.ObjCLazyModule(
    "Accessibility",
    "com.apple.Accessibility",
    objc.pathForFramework("/System/Library/Frameworks/Accessibility.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_Accessibility, Quartz),
)

for cls in (
    "AXNumericDataAxisDescriptor",
    "AXDataPointValue",
    "AXDataPoint",
    "AXChartDescriptor",
):
    try:
        getattr(mod, cls).__objc_final__ = True
    except AttributeError:
        pass

del sys.modules["Accessibility._metadata"]
