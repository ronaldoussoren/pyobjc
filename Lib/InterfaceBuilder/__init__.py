"""
Python mapping for the InterfaceBuilder framework

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the AddressBook bundle, and gather all classes defined there
import objc as _objc

import AppKit as _AppKit
from _InterfaceBuilder import *

if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "InterfaceBuilder",
        globals(),
        bundle_identifier=u'com.apple.InterfaceBuilderFramework',
    )
else:
    _objc.loadBundle(
        "InterfaceBuilder",
        globals(),
        bundle_path=_objc.pathForFramework(
            u"/System/Library/Frameworks/InterfaceBuilder.framework",
        ),
    )

import protocols  # no need to export these, just register with PyObjC

# Define useful utility methods here
