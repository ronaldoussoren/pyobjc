"""
Python mapping for the SecurityInterface framework on MacOS X >= 10.3

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the SecurityInterface bundle, and gather all classes defined there
import objc

# For some reason SecurityFoundation.framework is currently documented as being
# part of SecurityInterface.
objc.loadBundle("SecurityInterface", globals(), bundle_path="/System/Library/Frameworks/SecurityFoundation.framework")

objc.loadBundle("SecurityInterface", globals(), bundle_path="/System/Library/Frameworks/SecurityInterface.framework")

from _SecurityInterface import *
del objc

import protocols  # no need to export these, just register with PyObjC

# Define useful utility methods here
