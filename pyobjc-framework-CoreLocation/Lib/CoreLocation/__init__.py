"""
Python mapping for the CoreLocation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import os
import sys

import Foundation
import objc
from CoreLocation import _metadata
from CoreLocation import _CoreLocation

if int(os.uname()[2].split(".")[0]) < 12:
    # OSX <= 10.7
    kCLErrorGeocodeFoundNoResult = 7
    kCLErrorGeocodeCanceled = 8
else:
    # OSX 10.8 or later
    kCLErrorGeocodeFoundNoResult = 8
    kCLErrorGeocodeCanceled = 10

sys.modules["CoreLocation"] = mod = objc.ObjCLazyModule(
    "CoreLocation",
    "com.apple.corelocation",
    objc.pathForFramework("/System/Library/Frameworks/CoreLocation.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
        "kCLErrorGeocodeFoundNoResult": kCLErrorGeocodeFoundNoResult,
        "kCLErrorGeocodeCanceled": kCLErrorGeocodeCanceled,
    },
    (_CoreLocation, Foundation),
)


del sys.modules["CoreLocation._metadata"]
