"""
Python mapping for the PreferencePanes framework on MacOS X >= 10.1

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the PreferencePanes bundle, and gather all classes defined there
import objc as _objc
import AppKit as _AppKit
from _PreferencePanes import *

if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "PreferencePanes",
        globals(),
        bundle_identifier='com.apple.frameworks.preferencepanes',
    )
else:
    _objc.loadBundle(
        "PreferencePanes",
        globals(),
        bundle_path=_objc.pathForFramework(
            "/System/Library/Frameworks/PreferencePanes.framework",
        ),
    )

# Define useful utility methods here
