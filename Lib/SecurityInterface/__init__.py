"""
Python mapping for the SecurityInterface framework on MacOS X >= 10.3

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the SecurityInterface bundle, and gather all classes defined there
import objc as _objc

# For some reason SecurityFoundation.framework is currently documented as being
# part of SecurityInterface.
from _SecurityInterface import *
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "SecurityInterface",
        globals(),
        bundle_identifier='com.apple.securityinterface',
    )
    _objc.loadBundle(
        "SecurityInterface",
        globals(),
        bundle_identifier='com.apple.securityfoundation',
    )
else:
    _objc.loadBundle(
        "SecurityInterface",
        globals(),
        bundle_path=_objc.pathForFramework(
            "/System/Library/Frameworks/SecurityFoundation.framework",
        )
    )
    _objc.loadBundle(
        "SecurityInterface",
        globals(),
        bundle_path=_objc.pathForFramework(
            "/System/Library/Frameworks/SecurityInterface.framework",
        ),
    )

import protocols  # no need to export these, just register with PyObjC

# Define useful utility methods here
