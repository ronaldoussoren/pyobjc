"""
Python mapping for the AddressBook framework on MacOS X >= 10.2

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the AddressBook bundle, and gather all classes defined there
import objc

# AddressBook.framework has a dependency on AppKit.framework. Make sure we
# load AppKit ourselfes, otherwise we might not load the custom wrappers for it.
import AppKit
del AppKit

objc.loadBundle("AddressBook", globals(), bundle_path="/System/Library/Frameworks/AddressBook.framework")

from _AddressBook import *
del _AddressBook

import protocols  # no need to export these, just register with PyObjC

# Define useful utility methods here

objc.setSignatureForSelector('NSImagePickerController', 'setTarget:selector:userInfo:', 'v@:@:i')

# Not entirely correct...
objc.setSignatureForSelector('ABAuthenticationInfo', 'appliesToRequest:', 'c@:@')
objc.setSignatureForSelector('ABAuthenticationInfo', 'applyToRequest:', 'c@:@')
objc.setSignatureForSelector('ABDAVQuery', 'buildRequest', '@@:')

del objc
