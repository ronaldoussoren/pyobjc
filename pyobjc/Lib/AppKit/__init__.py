"""
Python mapping for the Cocoa AppKit.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import Foundation
import _AppKitSignatures 
import objc as _objc

# We first register special methods signatures with the runtime. The module
# is not used for anything else.

from _AppKit import *


# We try to import a module containing support code, the code
# is only ever used from the C side.
import _AppKitMapping 

# Load the Cocoa bundle, and gather all classes defined there
_objc.loadBundle("AppKit", globals(), bundle_path="/System/Library/Frameworks/AppKit.framework")
_objc.recyleAutoreleasePool()


# Define usefull utility methods here
NSClassForName = _objc.lookUpClass

# The used to be defined here as pure python functions, these aliasses
# are left here for backward compatibility.
NSMakePoint = Foundation.NSMakePoint
NSMakeSize = Foundation.NSMakeSize
NSMakeRect = Foundation.NSMakeRect

del Foundation

import protocols  # no need to export these, just register with PyObjC

#
# (informal) protocols eported for b/w compatibility
#
from protocols import NSAccessibility, NSChangeSpelling, NSColorPickingCustom, \
                       NSColorPickingDefault, NSComboBoxCellDataSource, NSComboBoxDataSource, \
                       NSDraggingDestination, NSDraggingInfo, NSDraggingSource, \
                       NSIgnoreMisspelledWords, NSInputServerMouseTracker, NSMenuValidation, \
                       NSOutlineViewDelegate, NSOutlineViewDataSource, NSServicesRequests, \
                       NSTableViewDelegate, NSTableDataSource, NSToolTipOwner, \
                       NSToolbarItemValidation, NSToolbarDelegate, NSUserInterfaceValidations, \
                       NSValidatedUserInterfaceItem, NSApplicationDelegate, NSTextViewDelegate

