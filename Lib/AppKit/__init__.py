"""
Python mapping for the Cocoa AppKit.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import _AppKitSignatures 
import objc as _objc

# We first register special methods signatures with the runtime. The module
# is not used for anything else.

from _AppKit import *


# We try to import a module containing support code, the code
# is only ever used from the C side.
import _AppKitMapping 

# Load the Cocoa bundle, and gather all classes defined there
import Foundation
Foundation._objc.loadBundle("AppKit", globals(), bundle_path="/System/Library/Frameworks/AppKit.framework")
Foundation._objc.recycle_autorelease_pool()
del Foundation


# Define usefull utility methods here
NSClassForName = _objc.lookUpClass


def NSEndSheetMethod(meth):
    """
    Return a selector that can be used as the delegate callback for
    sheet methods
    """
    return _objc.selector(meth, signature='v@:@@i')

def NSMakePoint(p1, p2):
    return (float(p1), float(p2))

def NSMakeSize(h, w):
    return (float(h), float(w))

def NSMakeRect(p1, p2, h, w):
    return ((p1, p2), (h, w))


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
