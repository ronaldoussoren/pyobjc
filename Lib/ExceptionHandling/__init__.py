"""
Python mapping for the ExceptionHandling framework on MacOS X

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the ExceptionHandling bundle, and gather all classes defined there
import objc

objc.loadBundle("ExceptionHandling", globals(), bundle_path="/System/Library/Frameworks/ExceptionHandling.framework")

from _ExceptionHandling import *
del objc

import protocols  # no need to export these, just register with PyObjC

# Define useful utility methods here
