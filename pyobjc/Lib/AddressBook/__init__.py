"""
Python mapping for the AddressBook framework on MacOS X >= 10.2

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the AddressBook bundle, and gather all classes defined there
import objc as _objc

# AddressBook.framework has a dependency on AppKit.framework. Make sure we
# load AppKit ourselves, otherwise we might not load the custom wrappers for it.
import AppKit as _AppKit

from _AddressBook import *
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "AddressBook",
        globals(),
        bundle_identifier=u'com.apple.AddressBook.framework',
    )
else:
    _objc.loadBundle(
        "AddressBook",
        globals(),
        bundle_path=_objc.pathForFramework(
            u"/System/Library/Frameworks/AddressBook.framework",
        ),
    )

import protocols  # no need to export these, just register with PyObjC

# Define useful utility methods here

_objc.setSignatureForSelector('NSImagePickerController', 'setTarget:selector:userInfo:', 'v@:@:i')

# Not entirely correct...
_objc.setSignatureForSelector('ABAuthenticationInfo', 'appliesToRequest:', 'c@:@')
_objc.setSignatureForSelector('ABAuthenticationInfo', 'applyToRequest:', 'c@:@')
_objc.setSignatureForSelector('ABDAVQuery', 'buildRequest', '@@:')
_objc.setSignatureForSelector('ABPerson', 'encodedDataForValue:charsetName:', '@@:@o^@')
