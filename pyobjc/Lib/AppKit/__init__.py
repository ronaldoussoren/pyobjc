"""
Python mapping for the Cocoa AppKit.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import objc as _objc

# We first register special methods signatures with the runtime. The module
# is not used for anything else.
import _AppKitSignatures as dummy
del dummy

from _AppKit 		import *


# We try to import a module containing support code, the code
# is only ever used from the C side.
#import _AppKitMapping 

# Load the Cocoa bundle, and gather all classes defined there
import Foundation
class_list = Foundation.load_bundle(
	'/System/Library/Frameworks/AppKit.framework')
gl = globals()
for cls in class_list:
	gl[cls.__name__] = cls

Foundation._objc.recycle_autorelease_pool()

# clean-up after ourselves.
del class_list
del cls
del gl
del Foundation



# Define usefull utility methods here
NSClassForName = _objc.lookup_class


#
# (Informal) protocols
#
# These can be used as (secondary) base-classes when subclassing an 
# Objective-C class, but won't show up in the inheritance tree.
#
# NOTE: This currently lists all protocols in the AppKit, should remove
# all protocols that are not actually used by user code.

NSAccessibility = _objc.informal_protocol(
	'NSAccessibility',
	[
		_objc.selector(
			None, 
			selector='accessibilityActionDescription:',
			signature='@@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='accessibilityActionNames',
			signature='@@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='accessibilityAtributeNames',
			signature='@@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='accessibilityAttributeValue:',
			signature='@@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='accessibilityFocusedUIElement',
			signature='@@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='accessibilityHitTest:',
			signature='@@:{_NSPoint=ff}',
			required=True
		),
		_objc.selector(
			None, 
			selector='accessibilityIsAttributeSettable',
			signature='c@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='accessibilityIsIgnored',
			signature='c@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='accessibilityPerformAction:',
			signature='v@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='accessibilitySetValue:ForAttribute:',
			signature='@@:@@',
			required=True
		),
	]
)

NSChangeSpelling = _objc.informal_protocol(
	'NSChangeSpelling', [
		_objc.selector(
			None, 
			selector='changeSpelling:',
			signature='v@:@',
			required=True
		),
	]
)

NSColorPickingCustom = _objc.informal_protocol(
	'NSColorPickingCustom',
	[
		_objc.selector(
			None, 
			selector='currentMode',
			signature='i@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='provideNewView:',
			signature='@@:c',
			required=True
		),
		_objc.selector(
			None, 
			selector='setColor:',
			signature='v@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='supportsMode:',
			signature='c@:i',
			required=True
		),
	]
)

NSColorPickingDefault = _objc.informal_protocol(
	'NSColorPickingDefault',
	[
		_objc.selector(
			None, 
			selector='alphaControlAddedOrRemoved:',
			signature='v@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='attachColorList:',
			signature='v@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='detachColorList:',
			signature='v@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='initWithPickerMask:colorPanel:',
			signature='@@:i@',
			required=True
		),
		_objc.selector(
			None, 
			selector='insertNewButtonImage:in:',
			signature='@@:@@',
			required=True
		),
		_objc.selector(
			None, 
			selector='provideNewButtonImage',
			signature='@@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='setMode:',
			signature='v@:i',
			required=True
		),
		_objc.selector(
			None, 
			selector='viewSizeChanged:',
			signature='v@:@',
			required=True
		),
	]
)

NSComboBoxCellDataSource = _objc.informal_protocol(
	'NSComboBoxCellDataSource',
	[
		_objc.selector(
			None, 
			selector='comboBoxCell:completedString:',
			signature='@@:@',
			required=False
		),
		_objc.selector(
			None, 
			selector='comboBoxCell:indexOfItemWithStringValue:',
			signature='I@:@@',
			required=False
		),
		_objc.selector(
			None, 
			selector='comboBoxCell:objectValueForItemAtIndex:',
			signature='@@:@i',
			required=True
		),
		_objc.selector(
			None, 
			selector='numberOfItemsInComboBoxCell:',
			signature='i@:@',
			required=True
		),
	]
)

NSComboBoxDataSource = _objc.informal_protocol(
	'NSComboBoxDataSource',
	[
		_objc.selector(
			None, 
			selector='comboBox:completedString:',
			signature='@@:@@',
			required=False
		),
		_objc.selector(
			None, 
			selector='comboBox:indexOfItemWithStringValue:',
			signature='I@:@@',
			required=False
		),
		_objc.selector(
			None, 
			selector='comboxBox:objectValueForItemAtIndex:',
			signature='@@:@i',
			required=True
		),
		_objc.selector(
			None, 
			selector='numberOfItemsInComboBox:',
			signature='i@:@',
			required=True
		),
	]
)

NSDraggingDestination = _objc.informal_protocol(
	'NSDraggingDestination',
	[
		_objc.selector(
			None, 
			selector='concludeDragOperation:',
			signature='v@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggingEnded:',
			signature='v@:@',
			required=False # Not implemented yet (10.2)
		),
		_objc.selector(
			None, 
			selector='draggingEntered',
			signature='i@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggingExited:',
			signature='v@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggingUpdated:',
			signature='i@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='performDragOperation:',
			signature='c@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='prepareForDragOperation:',
			signature='c@:@',
			required=True
		),
	]
)

NSDraggingInfo = _objc.informal_protocol(
	'NSDraggingInfo',
	[
		_objc.selector(
			None, 
			selector='draggedImage',
			signature='@@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggedImageLocation',
			signature='{_NSPoint=ff}@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggingDestinationWindow',
			signature='@@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggingLocation',
			signature='{_NSPoint=ff}@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggingPasteboard',
			signature='@@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggingSequenceNumber',
			signature='i@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggingSource',
			signature='@@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggingSourceOperationMask',
			signature='i@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='namesOfPromisedFilesDroppedAtDestination:',
			signature='@@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='slideDraggedImageTo:',
			signature='v@:{_NSPoint=ff}',
			required=True
		),
	]
)

NSDraggingSource = _objc.informal_protocol(
	'NSDraggingSource',
	[
		_objc.selector(
			None, 
			selector='draggedImage:beganAt:',
			signature='v@:@{_NSPoint=ff}',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggedImage:endedAt:deposited:',
			signature='v@:@{_NSPoint=ff}c',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggedImage:endedAt:operation:',
			signature='v@:@{_NSPoint=ff}i',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggedImage:movedTo:',
			signature='v@:@{_NSPoint=ff}',
			required=True
		),
		_objc.selector(
			None, 
			selector='draggingSourceOperationMaskForLocal:',
			signature='I@:c',
			required=True
		),
		_objc.selector(
			None, 
			selector='ignoreModifierKeysWhileDragging',
			signature='c@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='namesOfPromisedFilesDroppedAtDestination:',
			signature='@@:@',
			required=True
		),
	]
)

NSIgnoreMisspelledWords = _objc.informal_protocol(
	'NSIgnoreMisspelledWords',
	[
		_objc.selector(
			None, 
			selector='ignoreSpelling:',
			signature='v@:@',
			required=True
		),
	]
)

NSInputServerMouseTracker = _objc.informal_protocol(
	'NSInputServerMouseTracker',
	[
		_objc.selector(
			None, 
			selector='mouseDownOnCharacterIndex:atCoordinate:withModifier:client:',
			signature='c@:I{_NSPoint=ff}I@',
			required=True
		),
		_objc.selector(
			None, 
			selector='mouseDraggedOnCharacterIndex:atCoordinate:withModifier:client:',
			signature='c@:I{_NSPoint=ff}I@',
			required=True
		),
		_objc.selector(
			None, 
			selector='mouseUpOnCharacterIndex:atCoordinate:withModifier:client:',
			signature='c@:I{_NSPoint=ff}I@',
			required=True
		),
	]
)


# TODO: NSInputServiceProvider

NSMenuValidation = _objc.informal_protocol(
	'NSMenuValidation',
	[
		_objc.selector(
			None, 
			selector='validateMenuItem:',
			signature='c@:@',
			required=True
		),
	]
)

NSNibAwakening = _objc.informal_protocol(
	'NSNibAwakening',
	[
		_objc.selector(
			None, 
			selector='awakeFromNib',
			signature='v@:',
			required=True
		),
	]
)

NSOutlineViewDataSource = _objc.informal_protocol(
	'NSOutlineViewDataSource',
	[
		_objc.selector(
			None, 
			selector='outlineView:accepDrop:item:childIndex:',
			signature='c@@@i',
			required=False
		),
		_objc.selector(
			None, 
			selector='outlineView:child:ofItem:',
			signature='@@:@i@',
			required=True
		),
		_objc.selector(
			None, 
			selector='outlineView:isItemExpandable:',
			signature='c@:@@',
			required=True
		),
		_objc.selector(
			None, 
			selector='outlineView:itemForPersistentObject:',
			signature='@@:@@',
			required=False
		),
		_objc.selector(
			None, 
			selector='outlineView:numberOfChildrenOfItem:',
			signature='i@:@@',
			required=True
		),
		_objc.selector(
			None, 
			selector='outlineView:objectValueForTableColumn:byItem:',
			signature='@@:@@@',
			required=True
		),
		_objc.selector(
			None, 
			selector='outlineView:persistentObjectForItem:',
			signature='@@:@@',
			required=False
		),
		_objc.selector(
			None, 
			selector='outlineView:setObjectValue:forTableColumn:byItem:',
			signature='v@:@@@@',
			required=False
		),
		_objc.selector(
			None, 
			selector='outlineView:validateDrop:proposedItem:proposedChildIndex:',
			signature='i@:@@@i',
			required=False
		),
		_objc.selector(
			None, 
			selector='outlineView:writeItems:toPasteBoard:',
			signature='c@:@@@',
			required=False
		),
	]
)

NSServicesRequests = _objc.informal_protocol(
	'NSServicesRequests',
	[
		_objc.selector(
			None, 
			selector='readSelectionFromPasteboard:',
			signature='c@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='writeSelectionToPasteboard:types:',
			signature='c@:@@',
			required=True
		),
	]
)

NSTableDataSource = _objc.informal_protocol(
	'NSTableDataSource',
	[
		_objc.selector(
			None, 
			selector='numberOfRowsInTableView:',
			signature='i@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='tableView:acceptDrop:row:dropOperation:',
			signature='c@:@@ii',
			required=False
		),
		_objc.selector(
			None, 
			selector='tableView:objectValueForTableColumn:row:',
			signature='@@:@@i',
			required=True
		),
		_objc.selector(
			None, 
			selector='tableView:setObjectValue:forTableColumn:row:',
			signature='@@:@@@i',
			required=False
		),
		_objc.selector(
			None, 
			selector='tableView:validateDrop:proposedRow:proposedOperation:',
			signature='i@:@@ii',
			required=False
		),
		_objc.selector(
			None, 
			selector='tableView:writeRows:toPasteboard:',
			signature='c@:@@@',
			required=False
		),
	]
)		

NSTextAttachmentCell = _objc.informal_protocol(
	'NSTextAttachmentCell',
	[
		_objc.selector(
			None, 
			selector='attachment',
			signature='@@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='cellBaselineOffset',
			signature='{_NSPoint=ff}@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='cellFrameforTextContainer:proposedLineFragment:glyphPosition:characterIndex:',
			signature='{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}{_NSPoint=ff}I',
			required=True
		),
		_objc.selector(
			None, 
			selector='cellSize',
			signature='{_NSSize=ff}@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='drawWithFrame:inView:',
			signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@',
			required=True
		),
		_objc.selector(
			None, 
			selector='drawWithFrame:inView:characterIndex:',
			signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I',
			required=True
		),
		_objc.selector(
			None, 
			selector='drawWithFrame:inView:characterIndex:layoutManager:',
			signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I@',
			required=True
		),
		_objc.selector(
			None, 
			selector='highlight:withFrame:inView:',
			signature='v@:c{_NSRect={_NSPoint=ff}{_NSSize=ff}}@',
			required=True
		),
		_objc.selector(
			None, 
			selector='setAttachment:',
			signature='v@:@',
			required=True
		),
		_objc.selector(
			None, 
			selector='trackMouse:inRect:ofView:untilMouseUp:',
			signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@c',
			required=True
		),
		_objc.selector(
			None, 
			selector='trackMouse:inRect:ofView:atCharacterIndex:untilMouseUp:',
			signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@Ic',
			required=True
		),
		_objc.selector(
			None, 
			selector='wantsToTrackMouse',
			signature='c@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='wantsToTrackMouseForEvent:inRect:ofView:atCharacterIndex:',
			signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I',
			required=True
		),
	]
)

# TODO: NSTextInput

# TODO: NSTextStorageScripting

NSToolTipOwner = _objc.informal_protocol(
	'NSToolTipOwner',
	[
		_objc.selector(
			None, 
			selector='view:stringForToolTip:point:userData:',
			signature='@@:@i{_NSPoint=ff}i^v',
			required=True
		),
	]
)

NSToolbarItemValidation = _objc.informal_protocol(
	'NSToolbarItemValidation',
	[
		_objc.selector(
			None, 
			selector='validateToolbarItem:',
			signature='c@:@',
			required=True
		),
	]
)


NSUserInterfaceValidations = _objc.informal_protocol(
	'NSUserInterfaceValidations',
	[
		_objc.selector(
			None, 
			selector='validateUserInterfaceItem:',
			signature='c@:@',
			required=True
		),
	]
)


NSValidatedUserInterfaceItem = _objc.informal_protocol(
	'NSValidatedUserInterfaceItem',
	[
		_objc.selector(
			None, 
			selector='action',
			signature=':@:',
			required=True
		),
		_objc.selector(
			None, 
			selector='tag',
			signature='i@:',
			required=True
		),
	]
)

# TODO: NSWindowScripting
