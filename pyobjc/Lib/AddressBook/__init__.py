"""
Python mapping for the AddressBook framework on MacOS X >= 10.2

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the AddressBook bundle, and gather all classes defined there
import Foundation
class_list = Foundation.load_bundle(
    '/System/Library/Frameworks/AddressBook.framework')
gl = globals()
for cls in class_list:
    gl[cls.__name__] = cls

# clean-up after ourselves.
del class_list
del cls
del gl
del Foundation

# Define usefull utility methods here
