"""
Python mapping for the Cocoa AppKit.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import _AppKitSignatures
import objc as _objc

# Import contansts and global functions.
from _AppKit import *

# Load the Cocoa bundle, and gather all classes defined there
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "AppKit",
        globals(),
        bundle_identifier=u'com.apple.AppKit',
    )
else:
    _objc.loadBundle(
        "AppKit",
        globals(),
        bundle_path=_objc.pathForFramework(
            u"/System/Library/Frameworks/AppKit.framework",
        ),
    )
_objc.recycleAutoreleasePool()


# Define useful utility methods here
NSClassForName = _objc.lookUpClass

# The used to be defined here as pure python functions, these aliasses
# are left here for backward compatibility.
from Foundation import NSMakePoint, NSMakeSize, NSMakeRect

import protocols  # no need to export these, just register with PyObjC

# NSView declares, but does not implement this method. This
# additional protocol is needed to ensure that python implementations of
# the method pick up the right signature.
protocols.NSWindowPrinting = _objc.informal_protocol(
    "NSWindowPrinting",
    [
        # - (BOOL)knowsPageRange:(NSRangePointer)range;
        _objc.selector(
            None,
            selector='knowsPageRange:',
            signature='C@:o^{_NSRange=II}',
            isRequired=0,
        ),
    ]
)


#
# (informal) protocols exported for b/w compatibility
#
from protocols import NSAccessibility, NSChangeSpelling, NSColorPickingCustom, \
                      NSColorPickingDefault, NSComboBoxCellDataSource, \
                      NSComboBoxDataSource, NSDraggingDestination, \
                      NSDraggingInfo, NSDraggingSource, \
                      NSIgnoreMisspelledWords, NSInputServerMouseTracker, \
                      NSMenuValidation, NSOutlineViewDelegate, \
                      NSOutlineViewDataSource, NSServicesRequests, \
                      NSTableViewDelegate, NSTableDataSource, NSToolTipOwner, \
                      NSToolbarItemValidation, NSToolbarDelegate, \
                      NSUserInterfaceValidations, \
                      NSValidatedUserInterfaceItem, NSApplicationDelegate, \
                      NSTextViewDelegate
