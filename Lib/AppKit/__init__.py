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
	cls.__module__ = 'AppKit'

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
			required=1
		),
		_objc.selector(
			None, 
			selector='accessibilityActionNames',
			signature='@@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='accessibilityAtributeNames',
			signature='@@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='accessibilityAttributeValue:',
			signature='@@:@',
			required=1
		),
		_objc.selector(
			None, 
			selector='accessibilityFocusedUIElement',
			signature='@@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='accessibilityHitTest:',
			signature='@@:{_NSPoint=ff}',
			required=1
		),
		_objc.selector(
			None, 
			selector='accessibilityIsAttributeSettable',
			signature='c@:@',
			required=1
		),
		_objc.selector(
			None, 
			selector='accessibilityIsIgnored',
			signature='c@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='accessibilityPerformAction:',
			signature='v@:@',
			required=1
		),
		_objc.selector(
			None, 
			selector='accessibilitySetValue:ForAttribute:',
			signature='@@:@@',
			required=1
		),
	]
)

NSChangeSpelling = _objc.informal_protocol(
	'NSChangeSpelling', [
		_objc.selector(
			None, 
			selector='changeSpelling:',
			signature='v@:@',
			required=1
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
			required=1
		),
		_objc.selector(
			None, 
			selector='provideNewView:',
			signature='@@:c',
			required=1
		),
		_objc.selector(
			None, 
			selector='setColor:',
			signature='v@:@',
			required=1
		),
		_objc.selector(
			None, 
			selector='supportsMode:',
			signature='c@:i',
			required=1
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
			required=1
		),
		_objc.selector(
			None, 
			selector='attachColorList:',
			signature='v@:@',
			required=1
		),
		_objc.selector(
			None, 
			selector='detachColorList:',
			signature='v@:@',
			required=1
		),
		_objc.selector(
			None, 
			selector='initWithPickerMask:colorPanel:',
			signature='@@:i@',
			required=1
		),
		_objc.selector(
			None, 
			selector='insertNewButtonImage:in:',
			signature='@@:@@',
			required=1
		),
		_objc.selector(
			None, 
			selector='provideNewButtonImage',
			signature='@@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='setMode:',
			signature='v@:i',
			required=1
		),
		_objc.selector(
			None, 
			selector='viewSizeChanged:',
			signature='v@:@',
			required=1
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
			required=0
		),
		_objc.selector(
			None, 
			selector='comboBoxCell:indexOfItemWithStringValue:',
			signature='I@:@@',
			required=0
		),
		_objc.selector(
			None, 
			selector='comboBoxCell:objectValueForItemAtIndex:',
			signature='@@:@i',
			required=1
		),
		_objc.selector(
			None, 
			selector='numberOfItemsInComboBoxCell:',
			signature='i@:@',
			required=1
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
			required=0
		),
		_objc.selector(
			None, 
			selector='comboBox:indexOfItemWithStringValue:',
			signature='I@:@@',
			required=0
		),
		_objc.selector(
			None, 
			selector='comboBox:objectValueForItemAtIndex:',
			signature='@@:@i',
			required=1
		),
		_objc.selector(
			None, 
			selector='numberOfItemsInComboBox:',
			signature='i@:@',
			required=1
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
			required=0
		),
		_objc.selector(
			None, 
			selector='draggingEnded:',
			signature='v@:@',
			required=0 # Not implemented yet (10.2)
		),
		_objc.selector(
			None, 
			selector='draggingEntered:',
			signature='i@:@',
			required=0
		),
		_objc.selector(
			None, 
			selector='draggingExited:',
			signature='v@:@',
			required=0
		),
		_objc.selector(
			None, 
			selector='draggingUpdated:',
			signature='i@:@',
			required=0
		),
		_objc.selector(
			None, 
			selector='performDragOperation:',
			signature='c@:@',
			required=0
		),
		_objc.selector(
			None, 
			selector='prepareForDragOperation:',
			signature='c@:@',
			required=0
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
			required=1
		),
		_objc.selector(
			None, 
			selector='draggedImageLocation',
			signature='{_NSPoint=ff}@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='draggingDestinationWindow',
			signature='@@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='draggingLocation',
			signature='{_NSPoint=ff}@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='draggingPasteboard',
			signature='@@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='draggingSequenceNumber',
			signature='i@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='draggingSource',
			signature='@@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='draggingSourceOperationMask',
			signature='i@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='namesOfPromisedFilesDroppedAtDestination:',
			signature='@@:@',
			required=1
		),
		_objc.selector(
			None, 
			selector='slideDraggedImageTo:',
			signature='v@:{_NSPoint=ff}',
			required=1
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
			required=1
		),
		_objc.selector(
			None, 
			selector='draggedImage:endedAt:deposited:',
			signature='v@:@{_NSPoint=ff}c',
			required=1
		),
		_objc.selector(
			None, 
			selector='draggedImage:endedAt:operation:',
			signature='v@:@{_NSPoint=ff}i',
			required=1
		),
		_objc.selector(
			None, 
			selector='draggedImage:movedTo:',
			signature='v@:@{_NSPoint=ff}',
			required=1
		),
		_objc.selector(
			None, 
			selector='draggingSourceOperationMaskForLocal:',
			signature='I@:c',
			required=1
		),
		_objc.selector(
			None, 
			selector='ignoreModifierKeysWhileDragging',
			signature='c@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='namesOfPromisedFilesDroppedAtDestination:',
			signature='@@:@',
			required=1
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
			required=1
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
			required=1
		),
		_objc.selector(
			None, 
			selector='mouseDraggedOnCharacterIndex:atCoordinate:withModifier:client:',
			signature='c@:I{_NSPoint=ff}I@',
			required=1
		),
		_objc.selector(
			None, 
			selector='mouseUpOnCharacterIndex:atCoordinate:withModifier:client:',
			signature='c@:I{_NSPoint=ff}I@',
			required=1
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
			required=1
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
			required=1
		),
	]
)

NSOutlineViewDataSource = _objc.informal_protocol(
	'NSOutlineViewDataSource',
	[
		_objc.selector(
			None, 
			selector='outlineView:acceptDrop:item:childIndex:',
			signature='c@@@i',
			required=0
		),
		_objc.selector(
			None, 
			selector='outlineView:child:ofItem:',
			signature='@@:@i@',
			required=1
		),
		_objc.selector(
			None, 
			selector='outlineView:isItemExpandable:',
			signature='c@:@@',
			required=1
		),
		_objc.selector(
			None, 
			selector='outlineView:itemForPersistentObject:',
			signature='@@:@@',
			required=0
		),
		_objc.selector(
			None, 
			selector='outlineView:numberOfChildrenOfItem:',
			signature='i@:@@',
			required=1
		),
		_objc.selector(
			None, 
			selector='outlineView:objectValueForTableColumn:byItem:',
			signature='@@:@@@',
			required=1
		),
		_objc.selector(
			None, 
			selector='outlineView:persistentObjectForItem:',
			signature='@@:@@',
			required=0
		),
		_objc.selector(
			None, 
			selector='outlineView:setObjectValue:forTableColumn:byItem:',
			signature='v@:@@@@',
			required=0
		),
		_objc.selector(
			None, 
			selector='outlineView:validateDrop:proposedItem:proposedChildIndex:',
			signature='i@:@@@i',
			required=0
		),
		_objc.selector(
			None, 
			selector='outlineView:writeItems:toPasteBoard:',
			signature='c@:@@@',
			required=0
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
			required=1
		),
		_objc.selector(
			None, 
			selector='writeSelectionToPasteboard:types:',
			signature='c@:@@',
			required=1
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
			required=1
		),
		_objc.selector(
			None, 
			selector='tableView:acceptDrop:row:dropOperation:',
			signature='c@:@@ii',
			required=0
		),
		_objc.selector(
			None, 
			selector='tableView:objectValueForTableColumn:row:',
			signature='@@:@@i',
			required=1
		),
		_objc.selector(
			None, 
			selector='tableView:setObjectValue:forTableColumn:row:',
			signature='@@:@@@i',
			required=0
		),
		_objc.selector(
			None, 
			selector='tableView:validateDrop:proposedRow:proposedOperation:',
			signature='i@:@@ii',
			required=0
		),
		_objc.selector(
			None, 
			selector='tableView:writeRows:toPasteboard:',
			signature='c@:@@@',
			required=0
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
			required=1
		),
		_objc.selector(
			None, 
			selector='cellBaselineOffset',
			signature='{_NSPoint=ff}@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='cellFrameforTextContainer:proposedLineFragment:glyphPosition:characterIndex:',
			signature='{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}{_NSPoint=ff}I',
			required=1
		),
		_objc.selector(
			None, 
			selector='cellSize',
			signature='{_NSSize=ff}@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='drawWithFrame:inView:',
			signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@',
			required=1
		),
		_objc.selector(
			None, 
			selector='drawWithFrame:inView:characterIndex:',
			signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I',
			required=1
		),
		_objc.selector(
			None, 
			selector='drawWithFrame:inView:characterIndex:layoutManager:',
			signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I@',
			required=1
		),
		_objc.selector(
			None, 
			selector='highlight:withFrame:inView:',
			signature='v@:c{_NSRect={_NSPoint=ff}{_NSSize=ff}}@',
			required=1
		),
		_objc.selector(
			None, 
			selector='setAttachment:',
			signature='v@:@',
			required=1
		),
		_objc.selector(
			None, 
			selector='trackMouse:inRect:ofView:untilMouseUp:',
			signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@c',
			required=1
		),
		_objc.selector(
			None, 
			selector='trackMouse:inRect:ofView:atCharacterIndex:untilMouseUp:',
			signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@Ic',
			required=1
		),
		_objc.selector(
			None, 
			selector='wantsToTrackMouse',
			signature='c@:',
			required=1
		),
		_objc.selector(
			None, 
			selector='wantsToTrackMouseForEvent:inRect:ofView:atCharacterIndex:',
			signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I',
			required=1
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
			required=1
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
			required=1
		),
	]
)

NSToolbarDelegate = _objc.informal_protocol(
	'NSToolbarDelegate',
	[
	_objc.selector(
	None,
	selector='toolbar:itemForItemIdentifier:willBeInsertedIntoToolbar:',
	signature='@@:@@c',
	required=1
	),
	_objc.selector(
	None,
	selector='toolbarDefaultItemIdentifiers:',
	signature='@@:@',
	required=1
	),
	_objc.selector(
	None,
	selector='toolbarAllowedItemIdentifiers:',
	signature='@@:@',
	required=1
	),

	### The following are really notifications.  However, they are
	# automatically invoked on the delegate, if the delegate implements the
	# method. 
	_objc.selector(
	None,
	selector='toolbarWillAddItem:',
	signature='v@:@',
	required=0
	),
	_objc.selector(
	None,
	selector='toolbarDidRemoveItem:',
	signature='v@:@',
	required=0
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
			required=1
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
			required=1
		),
		_objc.selector(
			None, 
			selector='tag',
			signature='i@:',
			required=1
		),
	]
)

# TODO: NSWindowScripting
