"""
Python mapping for the CloudKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Accounts
import CoreData
import CoreLocation
import Foundation
import objc
from CloudKit import _metadata

sys.modules["CloudKit"] = mod = objc.ObjCLazyModule(
    "CloudKit",
    "com.apple.CloudKit",
    objc.pathForFramework("/System/Library/Frameworks/CloudKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (CoreData, CoreLocation, Accounts, Foundation),
)


del sys.modules["CloudKit._metadata"]
