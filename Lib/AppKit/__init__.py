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
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='accessibilityActionNames',
            signature='@@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='accessibilityAtributeNames',
            signature='@@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='accessibilityAttributeValue:',
            signature='@@:@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='accessibilityFocusedUIElement',
            signature='@@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='accessibilityHitTest:',
            signature='@@:{_NSPoint=ff}',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='accessibilityIsAttributeSettable',
            signature='c@:@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='accessibilityIsIgnored',
            signature='c@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='accessibilityPerformAction:',
            signature='v@:@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='accessibilitySetValue:ForAttribute:',
            signature='@@:@@',
            isRequired=1
        ),
    ]
)

NSChangeSpelling = _objc.informal_protocol(
    'NSChangeSpelling', [
        _objc.selector(
            None, 
            selector='changeSpelling:',
            signature='v@:@',
            isRequired=1
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
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='provideNewView:',
            signature='@@:c',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='setColor:',
            signature='v@:@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='supportsMode:',
            signature='c@:i',
            isRequired=1
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
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='attachColorList:',
            signature='v@:@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='detachColorList:',
            signature='v@:@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='initWithPickerMask:colorPanel:',
            signature='@@:i@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='insertNewButtonImage:in:',
            signature='@@:@@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='provideNewButtonImage',
            signature='@@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='setMode:',
            signature='v@:i',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='viewSizeChanged:',
            signature='v@:@',
            isRequired=1
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
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='comboBoxCell:indexOfItemWithStringValue:',
            signature='I@:@@',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='comboBoxCell:objectValueForItemAtIndex:',
            signature='@@:@i',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='numberOfItemsInComboBoxCell:',
            signature='i@:@',
            isRequired=1
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
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='comboBox:indexOfItemWithStringValue:',
            signature='I@:@@',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='comboBox:objectValueForItemAtIndex:',
            signature='@@:@i',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='numberOfItemsInComboBox:',
            signature='i@:@',
            isRequired=1
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
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='draggingEnded:',
            signature='v@:@',
            isRequired=0 # Not implemented yet (10.2)
        ),
        _objc.selector(
            None, 
            selector='draggingEntered:',
            signature='i@:@',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='draggingExited:',
            signature='v@:@',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='draggingUpdated:',
            signature='i@:@',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='performDragOperation:',
            signature='c@:@',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='prepareForDragOperation:',
            signature='c@:@',
            isRequired=0
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
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggedImageLocation',
            signature='{_NSPoint=ff}@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggingDestinationWindow',
            signature='@@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggingLocation',
            signature='{_NSPoint=ff}@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggingPasteboard',
            signature='@@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggingSequenceNumber',
            signature='i@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggingSource',
            signature='@@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggingSourceOperationMask',
            signature='i@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='namesOfPromisedFilesDroppedAtDestination:',
            signature='@@:@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='slideDraggedImageTo:',
            signature='v@:{_NSPoint=ff}',
            isRequired=1
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
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggedImage:endedAt:deposited:',
            signature='v@:@{_NSPoint=ff}c',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggedImage:endedAt:operation:',
            signature='v@:@{_NSPoint=ff}i',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggedImage:movedTo:',
            signature='v@:@{_NSPoint=ff}',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='draggingSourceOperationMaskForLocal:',
            signature='I@:c',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='ignoreModifierKeysWhileDragging',
            signature='c@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='namesOfPromisedFilesDroppedAtDestination:',
            signature='@@:@',
            isRequired=1
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
            isRequired=1
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
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='mouseDraggedOnCharacterIndex:atCoordinate:withModifier:client:',
            signature='c@:I{_NSPoint=ff}I@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='mouseUpOnCharacterIndex:atCoordinate:withModifier:client:',
            signature='c@:I{_NSPoint=ff}I@',
            isRequired=1
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
            isRequired=1
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
            isRequired=1
        ),
    ]
)

NSOutlineViewDelegate = _objc.informal_protocol(
    'NSTableViewDelegate',
    [
# - (void)outlineView:(NSOutlineView *)outlineView willDisplayCell:(id)cell forTableColumn:(NSTableColumn *)tableColumn item:(id)item;
    _objc.selector(
    None,
    selector='outlineView:willDisplayCell:forTableColumn:item:',
    signature='v@:@@@@',
    isRequired=0
    ),

# - (BOOL)outlineView:(NSOutlineView *)outlineView shouldEditTableColumn:(NSTableColumn *)tableColumn item:(id)item;
    _objc.selector(
    None,
    selector='outlineView:shouldEditTableColumn:item:',
    signature='c@:@@@',
    isRequired=0
    ),

# - (BOOL)selectionShouldChangeInOutlineView:(NSOutlineView *)outlineView;
    _objc.selector(
    None,
    selector='selectionShouldChangeInOutlineView:',
    signature='c@:@',
    isRequired=0
    ),

# - (BOOL)outlineView:(NSOutlineView *)outlineView shouldSelectItem:(id)item;
    _objc.selector(
    None,
    selector='outlineView:shouldSelectItem:',
    signature='c@:@@',
    isRequired=0
    ),

# - (BOOL)outlineView:(NSOutlineView *)outlineView shouldSelectTableColumn:(NSTableColumn *)tableColumn;
    _objc.selector(
    None,
    selector='outlineView:shouldSelectTableColumn:',
    signature='c@:@@',
    isRequired=0
    ),

# // NSOutlineView specific
# - (BOOL)outlineView:(NSOutlineView *)outlineView shouldExpandItem:(id)item;
    _objc.selector(
    None,
    selector='outlineView:shouldExpandItem:',
    signature='c@:@@',
    isRequired=0
    ),

# - (BOOL)outlineView:(NSOutlineView *)outlineView shouldCollapseItem:(id)item;
    _objc.selector(
    None,
    selector='outlineView:shouldCollapseItem:',
    signature='c@:@@',
    isRequired=0
    ),

# - (void)outlineView:(NSOutlineView *)outlineView willDisplayOutlineCell:(id)cell forTableColumn:(NSTableColumn *)tableColumn item:(id)item;
    _objc.selector(
    None,
    selector='outlineView:willDisplayOutlineCell:forTableColumn:item:',
    signature='v@:@@@@',
    isRequired=0
    )
    ]
    )

NSOutlineViewDataSource = _objc.informal_protocol(
    'NSOutlineViewDataSource',
    [
        _objc.selector(
            None, 
            selector='outlineView:acceptDrop:item:childIndex:',
            signature='c@@@i',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='outlineView:child:ofItem:',
            signature='@@:@i@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='outlineView:isItemExpandable:',
            signature='c@:@@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='outlineView:itemForPersistentObject:',
            signature='@@:@@',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='outlineView:numberOfChildrenOfItem:',
            signature='i@:@@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='outlineView:objectValueForTableColumn:byItem:',
            signature='@@:@@@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='outlineView:persistentObjectForItem:',
            signature='@@:@@',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='outlineView:setObjectValue:forTableColumn:byItem:',
            signature='v@:@@@@',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='outlineView:validateDrop:proposedItem:proposedChildIndex:',
            signature='i@:@@@i',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='outlineView:writeItems:toPasteBoard:',
            signature='c@:@@@',
            isRequired=0
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
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='writeSelectionToPasteboard:types:',
            signature='c@:@@',
            isRequired=1
        ),
    ]
)

NSTableViewDelegate = _objc.informal_protocol(
    'NSTableViewDelegate',
    [
    # - (void)tableView:(NSTableView *)tableView willDisplayCell:(id)cell forTableColumn:(NSTableColumn *)tableColumn row:(int)row;
    _objc.selector(
    None,
    selector='tableView:willDisplayCell:forTableColumn:row:',
    signature='v@:@@@i',
    isRequired=0
    ),
    
# - (BOOL)tableView:(NSTableView *)tableView shouldEditTableColumn:(NSTableColumn *)tableColumn row:(int)row;
    _objc.selector(
    None,
    selector='tableView:shouldEditTableColumn:row:',
    signature='c@:@@i',
    isRequired=0
    ),
    
# - (BOOL)selectionShouldChangeInTableView:(NSTableView *)aTableView;
    _objc.selector(
    None,
    selector='selectionShouldChangeInTableView:',
    signature='c@:@',
    isRequired=0
    ),
    
# - (BOOL)tableView:(NSTableView *)tableView shouldSelectRow:(int)row;
    _objc.selector(
    None,
    selector='tableView:shouldSelectRow:',
    signature='c@:@i',
    isRequired=0
    ),
    
# - (BOOL)tableView:(NSTableView *)tableView shouldSelectTableColumn:(NSTableColumn *)tableColumn;
    _objc.selector(
    None,
    selector='tableView:shouldSelectTableColumn:',
    signature='c@:@@',
    isRequired=0
    ),

#- (void) tableView:(NSTableView*)tableView mouseDownInHeaderOfTableColumn:(NSTableColumn *)tableColumn;
    _objc.selector(
    None,
    selector='tableView:mouseDownInHeaderOfTableColumn:',
    signature='v@:@@',
    isRequired=0
    ),

# - (void) tableView:(NSTableView*)tableView didClickTableColumn:(NSTableColumn *)tableColumn;
    _objc.selector(
    None,
    selector='tableView:didClickTableColumn:',
    signature='v@:@@',
    isRequired=0
    ),

# - (void) tableView:(NSTableView*)tableView didDragTableColumn:(NSTableColumn *)tableColumn;
    _objc.selector(
    None,
    selector='tableView:didDragTableColumn:',
    signature='v@:@@',
    isRequired=0
    )
    ]
    )

NSTableDataSource = _objc.informal_protocol(
    'NSTableDataSource',
    [
        _objc.selector(
            None, 
            selector='numberOfRowsInTableView:',
            signature='i@:@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='tableView:acceptDrop:row:dropOperation:',
            signature='c@:@@ii',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='tableView:objectValueForTableColumn:row:',
            signature='@@:@@i',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='tableView:setObjectValue:forTableColumn:row:',
            signature='@@:@@@i',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='tableView:validateDrop:proposedRow:proposedDropOperation:',
            signature='i@:@@ii',
            isRequired=0
        ),
        _objc.selector(
            None, 
            selector='tableView:writeRows:toPasteboard:',
            signature='c@:@@@',
            isRequired=0
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
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='cellBaselineOffset',
            signature='{_NSPoint=ff}@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='cellFrameforTextContainer:proposedLineFragment:glyphPosition:characterIndex:',
            signature='{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}{_NSPoint=ff}I',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='cellSize',
            signature='{_NSSize=ff}@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='drawWithFrame:inView:',
            signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='drawWithFrame:inView:characterIndex:',
            signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='drawWithFrame:inView:characterIndex:layoutManager:',
            signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='highlight:withFrame:inView:',
            signature='v@:c{_NSRect={_NSPoint=ff}{_NSSize=ff}}@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='setAttachment:',
            signature='v@:@',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='trackMouse:inRect:ofView:untilMouseUp:',
            signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@c',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='trackMouse:inRect:ofView:atCharacterIndex:untilMouseUp:',
            signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@Ic',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='wantsToTrackMouse',
            signature='c@:',
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='wantsToTrackMouseForEvent:inRect:ofView:atCharacterIndex:',
            signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I',
            isRequired=1
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
            isRequired=1
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
            isRequired=1
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
    isRequired=1
    ),
    _objc.selector(
    None,
    selector='toolbarDefaultItemIdentifiers:',
    signature='@@:@',
    isRequired=1
    ),
    _objc.selector(
    None,
    selector='toolbarAllowedItemIdentifiers:',
    signature='@@:@',
    isRequired=1
    ),

    ### The following are really notifications.  However, they are
    # automatically invoked on the delegate, if the delegate implements the
    # method. 
    _objc.selector(
    None,
    selector='toolbarWillAddItem:',
    signature='v@:@',
    isRequired=0
    ),
    _objc.selector(
    None,
    selector='toolbarDidRemoveItem:',
    signature='v@:@',
    isRequired=0
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
            isRequired=1
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
            isRequired=1
        ),
        _objc.selector(
            None, 
            selector='tag',
            signature='i@:',
            isRequired=1
        ),
    ]
)

NSApplicationDelegate = _objc.informal_protocol(
    'NSApplicationDelegate',
    [
# - (NSApplicationTerminateReply)applicationShouldTerminate:(NSApplication *)sender;
    _objc.selector(
    None,
    selector='applicationShouldTerminate:',
    signature='i@:@',
    isRequired=0
    ),

# - (BOOL)application:(NSApplication *)sender openFile:(NSString *)filename;
    _objc.selector(
    None,
    selector='application:openFile:',
    signature='c@:@@',
    isRequired=0
    ),

# - (BOOL)application:(NSApplication *)sender openTempFile:(NSString *)filename;
    _objc.selector(
    None,
    selector='application:openTempFile:',
    signature='c@:@@',
    isRequired=0
    ),
    
# - (BOOL)applicationShouldOpenUntitledFile:(NSApplication *)sender;
    _objc.selector(
    None,
    selector='applicationShouldOpenUntitledFile:',
    signature='c@:@',
    isRequired=0
    ),
    
# - (BOOL)applicationOpenUntitledFile:(NSApplication *)sender;
    _objc.selector(
    None,
    selector='applicationOpenUntitledFile:',
    signature='c@:@',
    isRequired=0
    ),

# - (BOOL)application:(id)sender openFileWithoutUI:(NSString *)filename;
    _objc.selector(
    None,
    selector='application:openFileWithoutUI:',
    signature='c@:@@',
    isRequired=0
    ),

# - (BOOL)application:(NSApplication *)sender printFile:(NSString *)filename;
    _objc.selector(
    None,
    selector='application:printFile:',
    signature='c@:@@',
    isRequired=0
    ),

# - (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender;
    _objc.selector(
    None,
    selector='applicationShouldTerminateAfterLastWindowClosed:',
    signature='c@:@',
    isRequired=0
    ),

# - (BOOL)applicationShouldHandleReopen:(NSApplication *)sender hasVisibleWindows:(BOOL)flag;
    _objc.selector(
    None,
    selector='applicationShouldHandleReopen:hasVisibleWindows:',
    signature='c@:@c',
    isRequired=0
    ),

# - (NSMenu *)applicationDockMenu:(NSApplication *)sender;
    _objc.selector(
    None,
    selector='applicationDockMenu:',
    signature='@@:@',
    isRequired=0
    ),
    ]
)

# TODO:
# NSWindowScripting
# NSTextViewDelegate
