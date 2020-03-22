"""
Python mapping for the PDFKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

import AppKit
import objc
from Quartz.PDFKit import _metadata, _PDFKit

# XXX: Moved to topelevel framework in 10.15

sys.modules["Quartz.PDFKit"] = mod = objc.ObjCLazyModule(
    "Quartz.PDFKit",
    "com.apple.PDFKit",
    objc.pathForFramework(
        "/System/Library/Frameworks/Quartz.framework/Frameworks/PDFKit.framework"
    ),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
    },
    (_PDFKit, AppKit),
)


del sys.modules["Quartz.PDFKit._metadata"]
