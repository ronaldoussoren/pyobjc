"""
Python mapping for the AddressBook framework on MacOS X >= 10.2

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the AddressBook bundle, and gather all classes defined there
import Foundation

Foundation._objc.loadBundle("AddressBook", globals(), bundle_path="/System/Library/Frameworks/AddressBook.framework")
Foundation._objc.recycle_autorelease_pool()

del Foundation

# Define usefull utility methods here
