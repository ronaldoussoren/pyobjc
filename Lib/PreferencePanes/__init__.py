"""
Python mapping for the PreferencePanes framework on MacOS X >= 10.1

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the AddressBook bundle, and gather all classes defined there
import objc 

objc.loadBundle("PreferencePanes", globals(), bundle_path="/System/Library/Frameworks/PreferencePanes.framework")

del objc
from _PreferencePanes import *
del _PreferencePanes

# Define usefull utility methods here
