"""
Python mapping for the Cocoa AppKit.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import AppKit
del AppKit
import objc as _objc

# We first register special methods signatures with the runtime. The module
# is not used for anything else.

from _WebKit import *

# Load the Cocoa bundle, and gather all classes defined there
_objc.loadBundle("WebKit", globals(), bundle_path="/System/Library/Frameworks/WebKit.framework")
_objc.recyleAutoreleasePool()

import protocols  # no need to export these, just register with PyObjC
del _objc
