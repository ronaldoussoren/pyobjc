# generated from '/System/Library/Frameworks/AppKit.framework'
import objc as _objc


NSAccessibility = _objc.informal_protocol(
    "NSAccessibility",
    [
# (NSString *)accessibilityActionDescription:(NSString *)action
        _objc.selector(
            None,
            selector='accessibilityActionDescription:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSArray *)accessibilityActionNames
        _objc.selector(
            None,
            selector='accessibilityActionNames',
            signature='@@:',
            isRequired=0,
        ),
# (NSArray *)accessibilityAttributeNames
        _objc.selector(
            None,
            selector='accessibilityAttributeNames',
            signature='@@:',
            isRequired=0,
        ),
# (id)accessibilityAttributeValue:(NSString *)attribute
        _objc.selector(
            None,
            selector='accessibilityAttributeValue:',
            signature='@@:@',
            isRequired=0,
        ),
# (id)accessibilityAttributeValue:(NSString *)attribute forParameter:(id)parameter
        _objc.selector(
            None,
            selector='accessibilityAttributeValue:forParameter:',
            signature='@@:@@',
            isRequired=0,
        ),
# (id)accessibilityFocusedUIElement
        _objc.selector(
            None,
            selector='accessibilityFocusedUIElement',
            signature='@@:',
            isRequired=0,
        ),
# (id)accessibilityHitTest:(NSPoint)point
        _objc.selector(
            None,
            selector='accessibilityHitTest:',
            signature='@@:{_NSPoint=ff}',
            isRequired=0,
        ),
# (BOOL)accessibilityIsAttributeSettable:(NSString *)attribute
        _objc.selector(
            None,
            selector='accessibilityIsAttributeSettable:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)accessibilityIsIgnored
        _objc.selector(
            None,
            selector='accessibilityIsIgnored',
            signature='c@:',
            isRequired=0,
        ),
# (NSArray *)accessibilityParameterizedAttributeNames
        _objc.selector(
            None,
            selector='accessibilityParameterizedAttributeNames',
            signature='@@:',
            isRequired=0,
        ),
# (void)accessibilityPerformAction:(NSString *)action
        _objc.selector(
            None,
            selector='accessibilityPerformAction:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)accessibilitySetValue:(id)value forAttribute:(NSString *)attribute
        _objc.selector(
            None,
            selector='accessibilitySetValue:forAttribute:',
            signature='v@:@@',
            isRequired=0,
        ),
    ]
)

NSAlertDelegate = _objc.informal_protocol(
    "NSAlertDelegate",
    [
# (BOOL)alertShowHelp:(NSAlert *)alert
        _objc.selector(
            None,
            selector='alertShowHelp:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSApplicationDelegate = _objc.informal_protocol(
    "NSApplicationDelegate",
    [
# (BOOL)application:(NSApplication *)sender openFile:(NSString *)filename
        _objc.selector(
            None,
            selector='application:openFile:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)application:(id)sender openFileWithoutUI:(NSString *)filename
        _objc.selector(
            None,
            selector='application:openFileWithoutUI:',
            signature='c@:@@',
            isRequired=0,
        ),
# (void)application:(NSApplication *)sender openFiles:(NSArray *)filenames
        _objc.selector(
            None,
            selector='application:openFiles:',
            signature='v@:@@',
            isRequired=0,
        ),
# (BOOL)application:(NSApplication *)sender openTempFile:(NSString *)filename
        _objc.selector(
            None,
            selector='application:openTempFile:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)application:(NSApplication *)sender printFile:(NSString *)filename
        _objc.selector(
            None,
            selector='application:printFile:',
            signature='c@:@@',
            isRequired=0,
        ),
# (void)application:(NSApplication *)sender printFiles:(NSArray *)filenames
        _objc.selector(
            None,
            selector='application:printFiles:',
            signature='v@:@@',
            isRequired=0,
        ),
# (NSMenu *)applicationDockMenu:(NSApplication *)sender
        _objc.selector(
            None,
            selector='applicationDockMenu:',
            signature='@@:@',
            isRequired=0,
        ),
# (BOOL)applicationOpenUntitledFile:(NSApplication *)sender
        _objc.selector(
            None,
            selector='applicationOpenUntitledFile:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)applicationShouldHandleReopen:(NSApplication *)sender hasVisibleWindows:(BOOL)flag
        _objc.selector(
            None,
            selector='applicationShouldHandleReopen:hasVisibleWindows:',
            signature='c@:@c',
            isRequired=0,
        ),
# (BOOL)applicationShouldOpenUntitledFile:(NSApplication *)sender
        _objc.selector(
            None,
            selector='applicationShouldOpenUntitledFile:',
            signature='c@:@',
            isRequired=0,
        ),
# (NSApplicationTerminateReply)applicationShouldTerminate:(NSApplication *)sender
        _objc.selector(
            None,
            selector='applicationShouldTerminate:',
            signature='i@:@',
            isRequired=0,
        ),
# (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender
        _objc.selector(
            None,
            selector='applicationShouldTerminateAfterLastWindowClosed:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSApplicationNotifications = _objc.informal_protocol(
    "NSApplicationNotifications",
    [
# (void)applicationDidBecomeActive:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationDidBecomeActive:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationDidChangeScreenParameters:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationDidChangeScreenParameters:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationDidFinishLaunching:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationDidFinishLaunching:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationDidHide:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationDidHide:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationDidResignActive:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationDidResignActive:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationDidUnhide:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationDidUnhide:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationDidUpdate:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationDidUpdate:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationWillBecomeActive:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationWillBecomeActive:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationWillFinishLaunching:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationWillFinishLaunching:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationWillHide:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationWillHide:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationWillResignActive:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationWillResignActive:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationWillTerminate:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationWillTerminate:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationWillUnhide:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationWillUnhide:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)applicationWillUpdate:(NSNotification *)notification
        _objc.selector(
            None,
            selector='applicationWillUpdate:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSApplicationScriptingDelegation = _objc.informal_protocol(
    "NSApplicationScriptingDelegation",
    [
# (BOOL)application:(NSApplication *)sender delegateHandlesKey:(NSString *)key
        _objc.selector(
            None,
            selector='application:delegateHandlesKey:',
            signature='c@:@@',
            isRequired=0,
        ),
    ]
)

NSBrowserDelegate = _objc.informal_protocol(
    "NSBrowserDelegate",
    [
# (void)browser:(NSBrowser *)sender createRowsForColumn:(int)column inMatrix:(NSMatrix *)matrix
        _objc.selector(
            None,
            selector='browser:createRowsForColumn:inMatrix:',
            signature='v@:@i@',
            isRequired=0,
        ),
# (BOOL)browser:(NSBrowser *)sender isColumnValid:(int)column
        _objc.selector(
            None,
            selector='browser:isColumnValid:',
            signature='c@:@i',
            isRequired=0,
        ),
# (int)browser:(NSBrowser *)sender numberOfRowsInColumn:(int)column
        _objc.selector(
            None,
            selector='browser:numberOfRowsInColumn:',
            signature='i@:@i',
            isRequired=0,
        ),
# (BOOL)browser:(NSBrowser *)sender selectCellWithString:(NSString *)title inColumn:(int)column
        _objc.selector(
            None,
            selector='browser:selectCellWithString:inColumn:',
            signature='c@:@@i',
            isRequired=0,
        ),
# (BOOL)browser:(NSBrowser *)sender selectRow:(int)row inColumn:(int)column
        _objc.selector(
            None,
            selector='browser:selectRow:inColumn:',
            signature='c@:@ii',
            isRequired=0,
        ),
# (float)browser:(NSBrowser *)browser shouldSizeColumn:(int)columnIndex forUserResize:(BOOL)forUserResize toWidth:(float)suggestedWidth
        _objc.selector(
            None,
            selector='browser:shouldSizeColumn:forUserResize:toWidth:',
            signature='f@:@icf',
            isRequired=0,
        ),
# (float)browser:(NSBrowser *)browser sizeToFitWidthOfColumn:(int)columnIndex
        _objc.selector(
            None,
            selector='browser:sizeToFitWidthOfColumn:',
            signature='f@:@i',
            isRequired=0,
        ),
# (NSString *)browser:(NSBrowser *)sender titleOfColumn:(int)column
        _objc.selector(
            None,
            selector='browser:titleOfColumn:',
            signature='@@:@i',
            isRequired=0,
        ),
# (void)browser:(NSBrowser *)sender willDisplayCell:(id)cell atRow:(int)row column:(int)column
        _objc.selector(
            None,
            selector='browser:willDisplayCell:atRow:column:',
            signature='v@:@@ii',
            isRequired=0,
        ),
# (void)browserColumnConfigurationDidChange:(NSNotification *)notification
        _objc.selector(
            None,
            selector='browserColumnConfigurationDidChange:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)browserDidScroll:(NSBrowser *)sender
        _objc.selector(
            None,
            selector='browserDidScroll:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)browserWillScroll:(NSBrowser *)sender
        _objc.selector(
            None,
            selector='browserWillScroll:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSChangeSpelling = _objc.informal_protocol(
    "NSChangeSpelling",
    [
# (void)changeSpelling:(id)sender
        _objc.selector(
            None,
            selector='changeSpelling:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSColorPanelResponderMethod = _objc.informal_protocol(
    "NSColorPanelResponderMethod",
    [
# (void)changeColor:(id)sender
        _objc.selector(
            None,
            selector='changeColor:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSColorPickingCustom = _objc.informal_protocol(
    "NSColorPickingCustom",
    [
# (int)currentMode
        _objc.selector(
            None,
            selector='currentMode',
            signature='i@:',
            isRequired=0,
        ),
# (NSView *)provideNewView:(BOOL)initialRequest
        _objc.selector(
            None,
            selector='provideNewView:',
            signature='@@:c',
            isRequired=0,
        ),
# (void)setColor:(NSColor *)newColor
        _objc.selector(
            None,
            selector='setColor:',
            signature='v@:@',
            isRequired=0,
        ),
# (BOOL)supportsMode:(int)mode
        _objc.selector(
            None,
            selector='supportsMode:',
            signature='c@:i',
            isRequired=0,
        ),
    ]
)

NSColorPickingDefault = _objc.informal_protocol(
    "NSColorPickingDefault",
    [
# (void)alphaControlAddedOrRemoved:(id)sender
        _objc.selector(
            None,
            selector='alphaControlAddedOrRemoved:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)attachColorList:(NSColorList *)colorList
        _objc.selector(
            None,
            selector='attachColorList:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)detachColorList:(NSColorList *)colorList
        _objc.selector(
            None,
            selector='detachColorList:',
            signature='v@:@',
            isRequired=0,
        ),
# (id)initWithPickerMask:(int)mask colorPanel:(NSColorPanel *)owningColorPanel
        _objc.selector(
            None,
            selector='initWithPickerMask:colorPanel:',
            signature='@@:i@',
            isRequired=0,
        ),
# (void)insertNewButtonImage:(NSImage *)newButtonImage in:(NSButtonCell *)buttonCell
        _objc.selector(
            None,
            selector='insertNewButtonImage:in:',
            signature='v@:@@',
            isRequired=0,
        ),
# (NSImage *)provideNewButtonImage
        _objc.selector(
            None,
            selector='provideNewButtonImage',
            signature='@@:',
            isRequired=0,
        ),
# (void)setMode:(int)mode
        _objc.selector(
            None,
            selector='setMode:',
            signature='v@:i',
            isRequired=0,
        ),
# (void)viewSizeChanged:(id)sender
        _objc.selector(
            None,
            selector='viewSizeChanged:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSComboBoxCellDataSource = _objc.informal_protocol(
    "NSComboBoxCellDataSource",
    [
# (NSString *)comboBoxCell:(NSComboBoxCell *)aComboBoxCell completedString:(NSString *)uncompletedString
        _objc.selector(
            None,
            selector='comboBoxCell:completedString:',
            signature='@@:@@',
            isRequired=0,
        ),
# (unsigned int)comboBoxCell:(NSComboBoxCell *)aComboBoxCell indexOfItemWithStringValue:(NSString *)string
        _objc.selector(
            None,
            selector='comboBoxCell:indexOfItemWithStringValue:',
            signature='I@:@@',
            isRequired=0,
        ),
# (id)comboBoxCell:(NSComboBoxCell *)aComboBoxCell objectValueForItemAtIndex:(int)index
        _objc.selector(
            None,
            selector='comboBoxCell:objectValueForItemAtIndex:',
            signature='@@:@i',
            isRequired=0,
        ),
# (int)numberOfItemsInComboBoxCell:(NSComboBoxCell *)comboBoxCell
        _objc.selector(
            None,
            selector='numberOfItemsInComboBoxCell:',
            signature='i@:@',
            isRequired=0,
        ),
    ]
)

NSComboBoxDataSource = _objc.informal_protocol(
    "NSComboBoxDataSource",
    [
# (NSString *)comboBox:(NSComboBox *)aComboBox completedString:(NSString *)string
        _objc.selector(
            None,
            selector='comboBox:completedString:',
            signature='@@:@@',
            isRequired=0,
        ),
# (unsigned int)comboBox:(NSComboBox *)aComboBox indexOfItemWithStringValue:(NSString *)string
        _objc.selector(
            None,
            selector='comboBox:indexOfItemWithStringValue:',
            signature='I@:@@',
            isRequired=0,
        ),
# (id)comboBox:(NSComboBox *)aComboBox objectValueForItemAtIndex:(int)index
        _objc.selector(
            None,
            selector='comboBox:objectValueForItemAtIndex:',
            signature='@@:@i',
            isRequired=0,
        ),
# (int)numberOfItemsInComboBox:(NSComboBox *)aComboBox
        _objc.selector(
            None,
            selector='numberOfItemsInComboBox:',
            signature='i@:@',
            isRequired=0,
        ),
    ]
)

NSComboBoxNotifications = _objc.informal_protocol(
    "NSComboBoxNotifications",
    [
# (void)comboBoxSelectionDidChange:(NSNotification *)notification
        _objc.selector(
            None,
            selector='comboBoxSelectionDidChange:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)comboBoxSelectionIsChanging:(NSNotification *)notification
        _objc.selector(
            None,
            selector='comboBoxSelectionIsChanging:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)comboBoxWillDismiss:(NSNotification *)notification
        _objc.selector(
            None,
            selector='comboBoxWillDismiss:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)comboBoxWillPopUp:(NSNotification *)notification
        _objc.selector(
            None,
            selector='comboBoxWillPopUp:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSControlSubclassDelegate = _objc.informal_protocol(
    "NSControlSubclassDelegate",
    [
# (BOOL)control:(NSControl *)control didFailToFormatString:(NSString *)string errorDescription:(NSString *)error
        _objc.selector(
            None,
            selector='control:didFailToFormatString:errorDescription:',
            signature='c@:@@@',
            isRequired=0,
        ),
# (void)control:(NSControl *)control didFailToValidatePartialString:(NSString *)string errorDescription:(NSString *)error
        _objc.selector(
            None,
            selector='control:didFailToValidatePartialString:errorDescription:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (BOOL)control:(NSControl *)control isValidObject:(id)obj
        _objc.selector(
            None,
            selector='control:isValidObject:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)control:(NSControl *)control textShouldBeginEditing:(NSText *)fieldEditor
        _objc.selector(
            None,
            selector='control:textShouldBeginEditing:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)control:(NSControl *)control textShouldEndEditing:(NSText *)fieldEditor
        _objc.selector(
            None,
            selector='control:textShouldEndEditing:',
            signature='c@:@@',
            isRequired=0,
        ),
# (NSArray *)control:(NSControl *)control textView:(NSTextView *)textView completions:(NSArray *)words forPartialWordRange:(NSRange)charRange indexOfSelectedItem:(int *)index
        _objc.selector(
            None,
            selector='control:textView:completions:forPartialWordRange:indexOfSelectedItem:',
            signature='@@:@@@{_NSRange=II}N^i',
            isRequired=0,
        ),
# (BOOL)control:(NSControl *)control textView:(NSTextView *)textView doCommandBySelector:(SEL)commandSelector
        _objc.selector(
            None,
            selector='control:textView:doCommandBySelector:',
            signature='c@:@@:',
            isRequired=0,
        ),
    ]
)

NSControlSubclassNotifications = _objc.informal_protocol(
    "NSControlSubclassNotifications",
    [
# (void)controlTextDidBeginEditing:(NSNotification *)obj
        _objc.selector(
            None,
            selector='controlTextDidBeginEditing:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)controlTextDidChange:(NSNotification *)obj
        _objc.selector(
            None,
            selector='controlTextDidChange:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)controlTextDidEndEditing:(NSNotification *)obj
        _objc.selector(
            None,
            selector='controlTextDidEndEditing:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSDraggingDestination = _objc.informal_protocol(
    "NSDraggingDestination",
    [
# (void)concludeDragOperation:(id <NSDraggingInfo>)sender
        _objc.selector(
            None,
            selector='concludeDragOperation:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)draggingEnded:(id <NSDraggingInfo>)sender
        _objc.selector(
            None,
            selector='draggingEnded:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSDragOperation)draggingEntered:(id <NSDraggingInfo>)sender
        _objc.selector(
            None,
            selector='draggingEntered:',
            signature='I@:@',
            isRequired=0,
        ),
# (void)draggingExited:(id <NSDraggingInfo>)sender
        _objc.selector(
            None,
            selector='draggingExited:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSDragOperation)draggingUpdated:(id <NSDraggingInfo>)sender
        _objc.selector(
            None,
            selector='draggingUpdated:',
            signature='I@:@',
            isRequired=0,
        ),
# (BOOL)performDragOperation:(id <NSDraggingInfo>)sender
        _objc.selector(
            None,
            selector='performDragOperation:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)prepareForDragOperation:(id <NSDraggingInfo>)sender
        _objc.selector(
            None,
            selector='prepareForDragOperation:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSDraggingInfo = _objc.informal_protocol(
    "NSDraggingInfo",
    [
# (NSImage *)draggedImage
        _objc.selector(
            None,
            selector='draggedImage',
            signature='@@:',
            isRequired=0,
        ),
# (NSPoint)draggedImageLocation
        _objc.selector(
            None,
            selector='draggedImageLocation',
            signature='{_NSPoint=ff}@:',
            isRequired=0,
        ),
# (NSWindow *)draggingDestinationWindow
        _objc.selector(
            None,
            selector='draggingDestinationWindow',
            signature='@@:',
            isRequired=0,
        ),
# (NSPoint)draggingLocation
        _objc.selector(
            None,
            selector='draggingLocation',
            signature='{_NSPoint=ff}@:',
            isRequired=0,
        ),
# (NSPasteboard *)draggingPasteboard
        _objc.selector(
            None,
            selector='draggingPasteboard',
            signature='@@:',
            isRequired=0,
        ),
# (int)draggingSequenceNumber
        _objc.selector(
            None,
            selector='draggingSequenceNumber',
            signature='i@:',
            isRequired=0,
        ),
# (id)draggingSource
        _objc.selector(
            None,
            selector='draggingSource',
            signature='@@:',
            isRequired=0,
        ),
# (NSDragOperation)draggingSourceOperationMask
        _objc.selector(
            None,
            selector='draggingSourceOperationMask',
            signature='I@:',
            isRequired=0,
        ),
# (NSArray *)namesOfPromisedFilesDroppedAtDestination:(NSURL *)dropDestination
        _objc.selector(
            None,
            selector='namesOfPromisedFilesDroppedAtDestination:',
            signature='@@:@',
            isRequired=0,
        ),
# (void)slideDraggedImageTo:(NSPoint)screenPoint
        _objc.selector(
            None,
            selector='slideDraggedImageTo:',
            signature='v@:{_NSPoint=ff}',
            isRequired=0,
        ),
    ]
)

NSDraggingSource = _objc.informal_protocol(
    "NSDraggingSource",
    [
# (void)draggedImage:(NSImage *)image beganAt:(NSPoint)screenPoint
        _objc.selector(
            None,
            selector='draggedImage:beganAt:',
            signature='v@:@{_NSPoint=ff}',
            isRequired=0,
        ),
# (void)draggedImage:(NSImage *)image endedAt:(NSPoint)screenPoint deposited:(BOOL)flag
        _objc.selector(
            None,
            selector='draggedImage:endedAt:deposited:',
            signature='v@:@{_NSPoint=ff}c',
            isRequired=0,
        ),
# (void)draggedImage:(NSImage *)image endedAt:(NSPoint)screenPoint operation:(NSDragOperation)operation
        _objc.selector(
            None,
            selector='draggedImage:endedAt:operation:',
            signature='v@:@{_NSPoint=ff}I',
            isRequired=0,
        ),
# (void)draggedImage:(NSImage *)image movedTo:(NSPoint)screenPoint
        _objc.selector(
            None,
            selector='draggedImage:movedTo:',
            signature='v@:@{_NSPoint=ff}',
            isRequired=0,
        ),
# (NSDragOperation)draggingSourceOperationMaskForLocal:(BOOL)flag
        _objc.selector(
            None,
            selector='draggingSourceOperationMaskForLocal:',
            signature='I@:c',
            isRequired=0,
        ),
# (BOOL)ignoreModifierKeysWhileDragging
        _objc.selector(
            None,
            selector='ignoreModifierKeysWhileDragging',
            signature='c@:',
            isRequired=0,
        ),
# (NSArray *)namesOfPromisedFilesDroppedAtDestination:(NSURL *)dropDestination
        _objc.selector(
            None,
            selector='namesOfPromisedFilesDroppedAtDestination:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

NSDrawerDelegate = _objc.informal_protocol(
    "NSDrawerDelegate",
    [
# (BOOL)drawerShouldClose:(NSDrawer *)sender
        _objc.selector(
            None,
            selector='drawerShouldClose:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)drawerShouldOpen:(NSDrawer *)sender
        _objc.selector(
            None,
            selector='drawerShouldOpen:',
            signature='c@:@',
            isRequired=0,
        ),
# (NSSize)drawerWillResizeContents:(NSDrawer *)sender toSize:(NSSize)contentSize
        _objc.selector(
            None,
            selector='drawerWillResizeContents:toSize:',
            signature='{_NSSize=ff}@:@{_NSSize=ff}',
            isRequired=0,
        ),
    ]
)

NSDrawerNotifications = _objc.informal_protocol(
    "NSDrawerNotifications",
    [
# (void)drawerDidClose:(NSNotification *)notification
        _objc.selector(
            None,
            selector='drawerDidClose:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)drawerDidOpen:(NSNotification *)notification
        _objc.selector(
            None,
            selector='drawerDidOpen:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)drawerWillClose:(NSNotification *)notification
        _objc.selector(
            None,
            selector='drawerWillClose:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)drawerWillOpen:(NSNotification *)notification
        _objc.selector(
            None,
            selector='drawerWillOpen:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSEditor = _objc.informal_protocol(
    "NSEditor",
    [
# (BOOL)commitEditing
        _objc.selector(
            None,
            selector='commitEditing',
            signature='c@:',
            isRequired=0,
        ),
# (void)discardEditing
        _objc.selector(
            None,
            selector='discardEditing',
            signature='v@:',
            isRequired=0,
        ),
    ]
)

NSEditorRegistration = _objc.informal_protocol(
    "NSEditorRegistration",
    [
# (void)objectDidBeginEditing:(id)editor
        _objc.selector(
            None,
            selector='objectDidBeginEditing:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)objectDidEndEditing:(id)editor
        _objc.selector(
            None,
            selector='objectDidEndEditing:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSFontManagerDelegate = _objc.informal_protocol(
    "NSFontManagerDelegate",
    [
# (BOOL)fontManager:(id)sender willIncludeFont:(NSString *)fontName
        _objc.selector(
            None,
            selector='fontManager:willIncludeFont:',
            signature='c@:@@',
            isRequired=0,
        ),
    ]
)

NSFontManagerResponderMethod = _objc.informal_protocol(
    "NSFontManagerResponderMethod",
    [
# (void)changeFont:(id)sender
        _objc.selector(
            None,
            selector='changeFont:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSFontPanelValidationAdditions = _objc.informal_protocol(
    "NSFontPanelValidationAdditions",
    [
# (unsigned int) validModesForFontPanel: (NSFontPanel *) fontPanel
        _objc.selector(
            None,
            selector='validModesForFontPanel:',
            signature='I@:@',
            isRequired=0,
        ),
    ]
)

NSGlyphStorage = _objc.informal_protocol(
    "NSGlyphStorage",
    [
# (NSAttributedString *)attributedString
        _objc.selector(
            None,
            selector='attributedString',
            signature='@@:',
            isRequired=0,
        ),
# (void)insertGlyphs:(const NSGlyph *)glyphs length:(unsigned int)length forStartingGlyphAtIndex:(unsigned int)glyphIndex characterIndex:(unsigned int)charIndex
        _objc.selector(
            None,
            selector='insertGlyphs:length:forStartingGlyphAtIndex:characterIndex:',
            signature='v@:^IIII',
            isRequired=0,
        ),
# (unsigned int)layoutOptions
        _objc.selector(
            None,
            selector='layoutOptions',
            signature='I@:',
            isRequired=0,
        ),
# (void)setIntAttribute:(int)attributeTag value:(int)val forGlyphAtIndex:(unsigned)glyphIndex
        _objc.selector(
            None,
            selector='setIntAttribute:value:forGlyphAtIndex:',
            signature='v@:iiI',
            isRequired=0,
        ),
    ]
)

NSIgnoreMisspelledWords = _objc.informal_protocol(
    "NSIgnoreMisspelledWords",
    [
# (void)ignoreSpelling:(id)sender
        _objc.selector(
            None,
            selector='ignoreSpelling:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSImageDelegate = _objc.informal_protocol(
    "NSImageDelegate",
    [
# (void)image:(NSImage*)image didLoadPartOfRepresentation:(NSImageRep*)rep withValidRows:(int)rows
        _objc.selector(
            None,
            selector='image:didLoadPartOfRepresentation:withValidRows:',
            signature='v@:@@i',
            isRequired=0,
        ),
# (void)image:(NSImage*)image didLoadRepresentation:(NSImageRep*)rep withStatus:(NSImageLoadStatus)status
        _objc.selector(
            None,
            selector='image:didLoadRepresentation:withStatus:',
            signature='v@:@@i',
            isRequired=0,
        ),
# (void)image:(NSImage*)image didLoadRepresentationHeader:(NSImageRep*)rep
        _objc.selector(
            None,
            selector='image:didLoadRepresentationHeader:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)image:(NSImage*)image willLoadRepresentation:(NSImageRep*)rep
        _objc.selector(
            None,
            selector='image:willLoadRepresentation:',
            signature='v@:@@',
            isRequired=0,
        ),
# (NSImage *)imageDidNotDraw:(id)sender inRect:(NSRect)aRect
        _objc.selector(
            None,
            selector='imageDidNotDraw:inRect:',
            signature='@@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}',
            isRequired=0,
        ),
    ]
)

NSInputServerMouseTracker = _objc.informal_protocol(
    "NSInputServerMouseTracker",
    [
# (BOOL) mouseDownOnCharacterIndex:(unsigned)theIndex atCoordinate:(NSPoint)thePoint withModifier:(unsigned int)theFlags client:(id)sender
        _objc.selector(
            None,
            selector='mouseDownOnCharacterIndex:atCoordinate:withModifier:client:',
            signature='c@:I{_NSPoint=ff}I@',
            isRequired=0,
        ),
# (BOOL) mouseDraggedOnCharacterIndex:(unsigned)theIndex atCoordinate:(NSPoint)thePoint withModifier:(unsigned int)theFlags client:(id)sender
        _objc.selector(
            None,
            selector='mouseDraggedOnCharacterIndex:atCoordinate:withModifier:client:',
            signature='c@:I{_NSPoint=ff}I@',
            isRequired=0,
        ),
# (void) mouseUpOnCharacterIndex:(unsigned)theIndex atCoordinate:(NSPoint)thePoint withModifier:(unsigned int)theFlags client:(id)sender
        _objc.selector(
            None,
            selector='mouseUpOnCharacterIndex:atCoordinate:withModifier:client:',
            signature='v@:I{_NSPoint=ff}I@',
            isRequired=0,
        ),
    ]
)

NSInputServiceProvider = _objc.informal_protocol(
    "NSInputServiceProvider",
    [
# (void) activeConversationChanged:(id)sender toNewConversation:(long)newConversation
        _objc.selector(
            None,
            selector='activeConversationChanged:toNewConversation:',
            signature='v@:@l',
            isRequired=0,
        ),
# (void) activeConversationWillChange:(id)sender fromOldConversation:(long)oldConversation
        _objc.selector(
            None,
            selector='activeConversationWillChange:fromOldConversation:',
            signature='v@:@l',
            isRequired=0,
        ),
# (BOOL) canBeDisabled
        _objc.selector(
            None,
            selector='canBeDisabled',
            signature='c@:',
            isRequired=0,
        ),
# (void) doCommandBySelector:(SEL)aSelector client:(id)sender
        _objc.selector(
            None,
            selector='doCommandBySelector:client:',
            signature='v@::@',
            isRequired=0,
        ),
# (void) inputClientBecomeActive:(id)sender
        _objc.selector(
            None,
            selector='inputClientBecomeActive:',
            signature='v@:@',
            isRequired=0,
        ),
# (void) inputClientDisabled:(id)sender
        _objc.selector(
            None,
            selector='inputClientDisabled:',
            signature='v@:@',
            isRequired=0,
        ),
# (void) inputClientEnabled:(id)sender
        _objc.selector(
            None,
            selector='inputClientEnabled:',
            signature='v@:@',
            isRequired=0,
        ),
# (void) inputClientResignActive:(id)sender
        _objc.selector(
            None,
            selector='inputClientResignActive:',
            signature='v@:@',
            isRequired=0,
        ),
# (void) insertText:(id)aString client:(id)sender
        _objc.selector(
            None,
            selector='insertText:client:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void) markedTextAbandoned:(id)sender
        _objc.selector(
            None,
            selector='markedTextAbandoned:',
            signature='v@:@',
            isRequired=0,
        ),
# (void) markedTextSelectionChanged:(NSRange)newSel client:(id)sender
        _objc.selector(
            None,
            selector='markedTextSelectionChanged:client:',
            signature='v@:{_NSRange=II}@',
            isRequired=0,
        ),
# (void) terminate:(id)sender
        _objc.selector(
            None,
            selector='terminate:',
            signature='v@:@',
            isRequired=0,
        ),
# (BOOL) wantsToDelayTextChangeNotifications
        _objc.selector(
            None,
            selector='wantsToDelayTextChangeNotifications',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL) wantsToHandleMouseEvents
        _objc.selector(
            None,
            selector='wantsToHandleMouseEvents',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL) wantsToInterpretAllKeystrokes
        _objc.selector(
            None,
            selector='wantsToInterpretAllKeystrokes',
            signature='c@:',
            isRequired=0,
        ),
    ]
)

NSKeyValueBindingCreation = _objc.informal_protocol(
    "NSKeyValueBindingCreation",
    [
# (void)bind:(NSString *)binding toObject:(id)observable withKeyPath:(NSString *)keyPath options:(NSDictionary *)options
        _objc.selector(
            None,
            selector='bind:toObject:withKeyPath:options:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (NSArray *)exposedBindings
        _objc.selector(
            None,
            selector='exposedBindings',
            signature='@@:',
            isRequired=0,
        ),
# (void)unbind:(NSString *)binding
        _objc.selector(
            None,
            selector='unbind:',
            signature='v@:@',
            isRequired=0,
        ),
# (Class)valueClassForBinding:(NSString *)binding
        _objc.selector(
            None,
            selector='valueClassForBinding:',
            signature='#@:@',
            isRequired=0,
        ),
    ]
)

NSLayoutManagerDelegate = _objc.informal_protocol(
    "NSLayoutManagerDelegate",
    [
# (void)layoutManager:(NSLayoutManager *)layoutManager didCompleteLayoutForTextContainer:(NSTextContainer *)textContainer atEnd:(BOOL)layoutFinishedFlag
        _objc.selector(
            None,
            selector='layoutManager:didCompleteLayoutForTextContainer:atEnd:',
            signature='v@:@@c',
            isRequired=0,
        ),
# (void)layoutManagerDidInvalidateLayout:(NSLayoutManager *)sender
        _objc.selector(
            None,
            selector='layoutManagerDidInvalidateLayout:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSMenuDelegate = _objc.informal_protocol(
    "NSMenuDelegate",
    [
# (BOOL)menu:(NSMenu*)menu updateItem:(NSMenuItem*)item atIndex:(int)index shouldCancel:(BOOL)shouldCancel
        _objc.selector(
            None,
            selector='menu:updateItem:atIndex:shouldCancel:',
            signature='c@:@@ic',
            isRequired=0,
        ),
# (BOOL)menuHasKeyEquivalent:(NSMenu*)menu forEvent:(NSEvent*)event target:(id*)target action:(SEL*)action
        _objc.selector(
            None,
            selector='menuHasKeyEquivalent:forEvent:target:action:',
            signature='c@:@@^@^:',
            isRequired=0,
        ),
# (void)menuNeedsUpdate:(NSMenu*)menu
        _objc.selector(
            None,
            selector='menuNeedsUpdate:',
            signature='v@:@',
            isRequired=0,
        ),
# (int)numberOfItemsInMenu:(NSMenu*)menu
        _objc.selector(
            None,
            selector='numberOfItemsInMenu:',
            signature='i@:@',
            isRequired=0,
        ),
    ]
)

NSMenuItem = _objc.informal_protocol(
    "NSMenuItem",
    [
# (void)add:(id)sender
        _objc.selector(
            None,
            selector='add:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)addObject:(id)object
        _objc.selector(
            None,
            selector='addObject:',
            signature='v@:@',
            isRequired=0,
        ),
# (BOOL)automaticallyPreparesContent
        _objc.selector(
            None,
            selector='automaticallyPreparesContent',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)canAdd
        _objc.selector(
            None,
            selector='canAdd',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)canRemove
        _objc.selector(
            None,
            selector='canRemove',
            signature='c@:',
            isRequired=0,
        ),
# (id)content
        _objc.selector(
            None,
            selector='content',
            signature='@@:',
            isRequired=0,
        ),
# (id)initWithContent:(id)content
        _objc.selector(
            None,
            selector='initWithContent:',
            signature='@@:@',
            isRequired=0,
        ),
# (BOOL)isEditable
        _objc.selector(
            None,
            selector='isEditable',
            signature='c@:',
            isRequired=0,
        ),
# (id)newObject
        _objc.selector(
            None,
            selector='newObject',
            signature='@@:',
            isRequired=0,
        ),
# (Class)objectClass
        _objc.selector(
            None,
            selector='objectClass',
            signature='#@:',
            isRequired=0,
        ),
# (void)prepareContent
        _objc.selector(
            None,
            selector='prepareContent',
            signature='v@:',
            isRequired=0,
        ),
# (void)remove:(id)sender
        _objc.selector(
            None,
            selector='remove:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)removeObject:(id)object
        _objc.selector(
            None,
            selector='removeObject:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSArray *)selectedObjects
        _objc.selector(
            None,
            selector='selectedObjects',
            signature='@@:',
            isRequired=0,
        ),
# (id)selection
        _objc.selector(
            None,
            selector='selection',
            signature='@@:',
            isRequired=0,
        ),
# (void)setAutomaticallyPreparesContent:(BOOL)flag
        _objc.selector(
            None,
            selector='setAutomaticallyPreparesContent:',
            signature='v@:c',
            isRequired=0,
        ),
# (void)setContent:(id)content
        _objc.selector(
            None,
            selector='setContent:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)setEditable:(BOOL)flag
        _objc.selector(
            None,
            selector='setEditable:',
            signature='v@:c',
            isRequired=0,
        ),
# (void)setObjectClass:(Class)objectClass
        _objc.selector(
            None,
            selector='setObjectClass:',
            signature='v@:#',
            isRequired=0,
        ),
# (BOOL)validateMenuItem:(id <NSMenuItem>)menuItem
        _objc.selector(
            None,
            selector='validateMenuItem:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSMenuValidation = _objc.informal_protocol(
    "NSMenuValidation",
    [
# (BOOL)validateMenuItem:(id <NSMenuItem>)menuItem
        _objc.selector(
            None,
            selector='validateMenuItem:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSNibAwaking = _objc.informal_protocol(
    "NSNibAwaking",
    [
# (void)awakeFromNib
        _objc.selector(
            None,
            selector='awakeFromNib',
            signature='v@:',
            isRequired=0,
        ),
    ]
)

NSOutlineViewDataSource = _objc.informal_protocol(
    "NSOutlineViewDataSource",
    [
# (BOOL)outlineView:(NSOutlineView*)olv acceptDrop:(id <NSDraggingInfo>)info item:(id)item childIndex:(int)index
        _objc.selector(
            None,
            selector='outlineView:acceptDrop:item:childIndex:',
            signature='c@:@@@i',
            isRequired=0,
        ),
# (id)outlineView:(NSOutlineView *)outlineView child:(int)index ofItem:(id)item
        _objc.selector(
            None,
            selector='outlineView:child:ofItem:',
            signature='@@:@i@',
            isRequired=0,
        ),
# (BOOL)outlineView:(NSOutlineView *)outlineView isItemExpandable:(id)item
        _objc.selector(
            None,
            selector='outlineView:isItemExpandable:',
            signature='c@:@@',
            isRequired=0,
        ),
# (id)outlineView:(NSOutlineView *)outlineView itemForPersistentObject:(id)object
        _objc.selector(
            None,
            selector='outlineView:itemForPersistentObject:',
            signature='@@:@@',
            isRequired=0,
        ),
# (int)outlineView:(NSOutlineView *)outlineView numberOfChildrenOfItem:(id)item
        _objc.selector(
            None,
            selector='outlineView:numberOfChildrenOfItem:',
            signature='i@:@@',
            isRequired=0,
        ),
# (id)outlineView:(NSOutlineView *)outlineView objectValueForTableColumn:(NSTableColumn *)tableColumn byItem:(id)item
        _objc.selector(
            None,
            selector='outlineView:objectValueForTableColumn:byItem:',
            signature='@@:@@@',
            isRequired=0,
        ),
# (id)outlineView:(NSOutlineView *)outlineView persistentObjectForItem:(id)item
        _objc.selector(
            None,
            selector='outlineView:persistentObjectForItem:',
            signature='@@:@@',
            isRequired=0,
        ),
# (void)outlineView:(NSOutlineView *)outlineView setObjectValue:(id)object forTableColumn:(NSTableColumn *)tableColumn byItem:(id)item
        _objc.selector(
            None,
            selector='outlineView:setObjectValue:forTableColumn:byItem:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (void)outlineView:(NSOutlineView *)outlineView sortDescriptorsDidChange:(NSArray *)oldDescriptors
        _objc.selector(
            None,
            selector='outlineView:sortDescriptorsDidChange:',
            signature='v@:@@',
            isRequired=0,
        ),
# (NSDragOperation)outlineView:(NSOutlineView*)olv validateDrop:(id <NSDraggingInfo>)info proposedItem:(id)item proposedChildIndex:(int)index
        _objc.selector(
            None,
            selector='outlineView:validateDrop:proposedItem:proposedChildIndex:',
            signature='I@:@@@i',
            isRequired=0,
        ),
# (BOOL)outlineView:(NSOutlineView *)olv writeItems:(NSArray*)items toPasteboard:(NSPasteboard*)pboard
        _objc.selector(
            None,
            selector='outlineView:writeItems:toPasteboard:',
            signature='c@:@@@',
            isRequired=0,
        ),
    ]
)

NSOutlineViewDelegate = _objc.informal_protocol(
    "NSOutlineViewDelegate",
    [
# (void)outlineView:(NSOutlineView *)outlineView didClickTableColumn:(NSTableColumn *)tableColumn
        _objc.selector(
            None,
            selector='outlineView:didClickTableColumn:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)outlineView:(NSOutlineView *)outlineView didDragTableColumn:(NSTableColumn *)tableColumn
        _objc.selector(
            None,
            selector='outlineView:didDragTableColumn:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)outlineView:(NSOutlineView *)outlineView mouseDownInHeaderOfTableColumn:(NSTableColumn *)tableColumn
        _objc.selector(
            None,
            selector='outlineView:mouseDownInHeaderOfTableColumn:',
            signature='v@:@@',
            isRequired=0,
        ),
# (BOOL)outlineView:(NSOutlineView *)outlineView shouldCollapseItem:(id)item
        _objc.selector(
            None,
            selector='outlineView:shouldCollapseItem:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)outlineView:(NSOutlineView *)outlineView shouldEditTableColumn:(NSTableColumn *)tableColumn item:(id)item
        _objc.selector(
            None,
            selector='outlineView:shouldEditTableColumn:item:',
            signature='c@:@@@',
            isRequired=0,
        ),
# (BOOL)outlineView:(NSOutlineView *)outlineView shouldExpandItem:(id)item
        _objc.selector(
            None,
            selector='outlineView:shouldExpandItem:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)outlineView:(NSOutlineView *)outlineView shouldSelectItem:(id)item
        _objc.selector(
            None,
            selector='outlineView:shouldSelectItem:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)outlineView:(NSOutlineView *)outlineView shouldSelectTableColumn:(NSTableColumn *)tableColumn
        _objc.selector(
            None,
            selector='outlineView:shouldSelectTableColumn:',
            signature='c@:@@',
            isRequired=0,
        ),
# (void)outlineView:(NSOutlineView *)outlineView willDisplayCell:(id)cell forTableColumn:(NSTableColumn *)tableColumn item:(id)item
        _objc.selector(
            None,
            selector='outlineView:willDisplayCell:forTableColumn:item:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (void)outlineView:(NSOutlineView *)outlineView willDisplayOutlineCell:(id)cell forTableColumn:(NSTableColumn *)tableColumn item:(id)item
        _objc.selector(
            None,
            selector='outlineView:willDisplayOutlineCell:forTableColumn:item:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (BOOL)selectionShouldChangeInOutlineView:(NSOutlineView *)outlineView
        _objc.selector(
            None,
            selector='selectionShouldChangeInOutlineView:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSOutlineViewNotifications = _objc.informal_protocol(
    "NSOutlineViewNotifications",
    [
# (void)outlineViewColumnDidMove:(NSNotification *)notification
        _objc.selector(
            None,
            selector='outlineViewColumnDidMove:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)outlineViewColumnDidResize:(NSNotification *)notification
        _objc.selector(
            None,
            selector='outlineViewColumnDidResize:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)outlineViewItemDidCollapse:(NSNotification *)notification
        _objc.selector(
            None,
            selector='outlineViewItemDidCollapse:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)outlineViewItemDidExpand:(NSNotification *)notification
        _objc.selector(
            None,
            selector='outlineViewItemDidExpand:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)outlineViewItemWillCollapse:(NSNotification *)notification
        _objc.selector(
            None,
            selector='outlineViewItemWillCollapse:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)outlineViewItemWillExpand:(NSNotification *)notification
        _objc.selector(
            None,
            selector='outlineViewItemWillExpand:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)outlineViewSelectionDidChange:(NSNotification *)notification
        _objc.selector(
            None,
            selector='outlineViewSelectionDidChange:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)outlineViewSelectionIsChanging:(NSNotification *)notification
        _objc.selector(
            None,
            selector='outlineViewSelectionIsChanging:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSPasteboardOwner = _objc.informal_protocol(
    "NSPasteboardOwner",
    [
# (void)pasteboard:(NSPasteboard *)sender provideDataForType:(NSString *)type
        _objc.selector(
            None,
            selector='pasteboard:provideDataForType:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)pasteboardChangedOwner:(NSPasteboard *)sender
        _objc.selector(
            None,
            selector='pasteboardChangedOwner:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSPlaceholders = _objc.informal_protocol(
    "NSPlaceholders",
    [
    ]
)

NSSavePanelDelegate = _objc.informal_protocol(
    "NSSavePanelDelegate",
    [
# (NSComparisonResult)panel:(id)sender compareFilename:(NSString *)name1 with:(NSString *)name2 caseSensitive:(BOOL)caseSensitive
        _objc.selector(
            None,
            selector='panel:compareFilename:with:caseSensitive:',
            signature='i@:@@@c',
            isRequired=0,
        ),
# (void)panel:(id)sender directoryDidChange:(NSString *)path
        _objc.selector(
            None,
            selector='panel:directoryDidChange:',
            signature='v@:@@',
            isRequired=0,
        ),
# (BOOL)panel:(id)sender isValidFilename:(NSString *)filename
        _objc.selector(
            None,
            selector='panel:isValidFilename:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)panel:(id)sender shouldShowFilename:(NSString *)filename
        _objc.selector(
            None,
            selector='panel:shouldShowFilename:',
            signature='c@:@@',
            isRequired=0,
        ),
# (NSString *)panel:(id)sender userEnteredFilename:(NSString *)filename confirmed:(BOOL)okFlag
        _objc.selector(
            None,
            selector='panel:userEnteredFilename:confirmed:',
            signature='@@:@@c',
            isRequired=0,
        ),
# (void)panel:(id)sender willExpand:(BOOL)expanding
        _objc.selector(
            None,
            selector='panel:willExpand:',
            signature='v@:@c',
            isRequired=0,
        ),
# (void)panelSelectionDidChange:(id)sender
        _objc.selector(
            None,
            selector='panelSelectionDidChange:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSServicesRequests = _objc.informal_protocol(
    "NSServicesRequests",
    [
# (BOOL)readSelectionFromPasteboard:(NSPasteboard *)pboard
        _objc.selector(
            None,
            selector='readSelectionFromPasteboard:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)writeSelectionToPasteboard:(NSPasteboard *)pboard types:(NSArray *)types
        _objc.selector(
            None,
            selector='writeSelectionToPasteboard:types:',
            signature='c@:@@',
            isRequired=0,
        ),
    ]
)

NSSoundDelegateMethods = _objc.informal_protocol(
    "NSSoundDelegateMethods",
    [
# (void)sound:(NSSound *)sound didFinishPlaying:(BOOL)aBool
        _objc.selector(
            None,
            selector='sound:didFinishPlaying:',
            signature='v@:@c',
            isRequired=0,
        ),
    ]
)

NSSpeechRecognizerDelegate = _objc.informal_protocol(
    "NSSpeechRecognizerDelegate",
    [
# (void)speechRecognizer:(NSSpeechRecognizer *)sender didRecognizeCommand:(id)command
        _objc.selector(
            None,
            selector='speechRecognizer:didRecognizeCommand:',
            signature='v@:@@',
            isRequired=0,
        ),
    ]
)

NSSpeechSynthesizerDelegate = _objc.informal_protocol(
    "NSSpeechSynthesizerDelegate",
    [
# (void)speechSynthesizer:(NSSpeechSynthesizer *)sender didFinishSpeaking:(BOOL)finishedSpeaking
        _objc.selector(
            None,
            selector='speechSynthesizer:didFinishSpeaking:',
            signature='v@:@c',
            isRequired=0,
        ),
# (void)speechSynthesizer:(NSSpeechSynthesizer *)sender willSpeakPhoneme:(short)phonemeOpcode
        _objc.selector(
            None,
            selector='speechSynthesizer:willSpeakPhoneme:',
            signature='v@:@s',
            isRequired=0,
        ),
# (void)speechSynthesizer:(NSSpeechSynthesizer *)sender willSpeakWord:(NSRange)characterRange ofString:(NSString *)string
        _objc.selector(
            None,
            selector='speechSynthesizer:willSpeakWord:ofString:',
            signature='v@:@{_NSRange=II}@',
            isRequired=0,
        ),
    ]
)

NSSplitViewDelegate = _objc.informal_protocol(
    "NSSplitViewDelegate",
    [
# (BOOL)splitView:(NSSplitView *)sender canCollapseSubview:(NSView *)subview
        _objc.selector(
            None,
            selector='splitView:canCollapseSubview:',
            signature='c@:@@',
            isRequired=0,
        ),
# (float)splitView:(NSSplitView *)sender constrainMaxCoordinate:(float)proposedCoord ofSubviewAt:(int)offset
        _objc.selector(
            None,
            selector='splitView:constrainMaxCoordinate:ofSubviewAt:',
            signature='f@:@fi',
            isRequired=0,
        ),
# (float)splitView:(NSSplitView *)sender constrainMinCoordinate:(float)proposedCoord ofSubviewAt:(int)offset
        _objc.selector(
            None,
            selector='splitView:constrainMinCoordinate:ofSubviewAt:',
            signature='f@:@fi',
            isRequired=0,
        ),
# (float)splitView:(NSSplitView *)splitView constrainSplitPosition:(float)proposedPosition ofSubviewAt:(int)index
        _objc.selector(
            None,
            selector='splitView:constrainSplitPosition:ofSubviewAt:',
            signature='f@:@fi',
            isRequired=0,
        ),
# (void)splitView:(NSSplitView *)sender resizeSubviewsWithOldSize:(NSSize)oldSize
        _objc.selector(
            None,
            selector='splitView:resizeSubviewsWithOldSize:',
            signature='v@:@{_NSSize=ff}',
            isRequired=0,
        ),
# (void)splitViewDidResizeSubviews:(NSNotification *)notification
        _objc.selector(
            None,
            selector='splitViewDidResizeSubviews:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)splitViewWillResizeSubviews:(NSNotification *)notification
        _objc.selector(
            None,
            selector='splitViewWillResizeSubviews:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSTabViewDelegate = _objc.informal_protocol(
    "NSTabViewDelegate",
    [
# (void)tabView:(NSTabView *)tabView didSelectTabViewItem:(NSTabViewItem *)tabViewItem
        _objc.selector(
            None,
            selector='tabView:didSelectTabViewItem:',
            signature='v@:@@',
            isRequired=0,
        ),
# (BOOL)tabView:(NSTabView *)tabView shouldSelectTabViewItem:(NSTabViewItem *)tabViewItem
        _objc.selector(
            None,
            selector='tabView:shouldSelectTabViewItem:',
            signature='c@:@@',
            isRequired=0,
        ),
# (void)tabView:(NSTabView *)tabView willSelectTabViewItem:(NSTabViewItem *)tabViewItem
        _objc.selector(
            None,
            selector='tabView:willSelectTabViewItem:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)tabViewDidChangeNumberOfTabViewItems:(NSTabView *)TabView
        _objc.selector(
            None,
            selector='tabViewDidChangeNumberOfTabViewItems:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSTableDataSource = _objc.informal_protocol(
    "NSTableDataSource",
    [
# (int)numberOfRowsInTableView:(NSTableView *)tableView
        _objc.selector(
            None,
            selector='numberOfRowsInTableView:',
            signature='i@:@',
            isRequired=0,
        ),
# (BOOL)tableView:(NSTableView*)tv acceptDrop:(id <NSDraggingInfo>)info row:(int)row dropOperation:(NSTableViewDropOperation)op
        _objc.selector(
            None,
            selector='tableView:acceptDrop:row:dropOperation:',
            signature='c@:@@ii',
            isRequired=0,
        ),
# (id)tableView:(NSTableView *)tableView objectValueForTableColumn:(NSTableColumn *)tableColumn row:(int)row
        _objc.selector(
            None,
            selector='tableView:objectValueForTableColumn:row:',
            signature='@@:@@i',
            isRequired=0,
        ),
# (void)tableView:(NSTableView *)tableView setObjectValue:(id)object forTableColumn:(NSTableColumn *)tableColumn row:(int)row
        _objc.selector(
            None,
            selector='tableView:setObjectValue:forTableColumn:row:',
            signature='v@:@@@i',
            isRequired=0,
        ),
# (void)tableView:(NSTableView *)tableView sortDescriptorsDidChange:(NSArray *)oldDescriptors
        _objc.selector(
            None,
            selector='tableView:sortDescriptorsDidChange:',
            signature='v@:@@',
            isRequired=0,
        ),
# (NSDragOperation)tableView:(NSTableView*)tv validateDrop:(id <NSDraggingInfo>)info proposedRow:(int)row proposedDropOperation:(NSTableViewDropOperation)op
        _objc.selector(
            None,
            selector='tableView:validateDrop:proposedRow:proposedDropOperation:',
            signature='I@:@@ii',
            isRequired=0,
        ),
# (BOOL)tableView:(NSTableView *)tv writeRows:(NSArray*)rows toPasteboard:(NSPasteboard*)pboard
        _objc.selector(
            None,
            selector='tableView:writeRows:toPasteboard:',
            signature='c@:@@@',
            isRequired=0,
        ),
    ]
)

NSTableViewDelegate = _objc.informal_protocol(
    "NSTableViewDelegate",
    [
# (BOOL)selectionShouldChangeInTableView:(NSTableView *)aTableView
        _objc.selector(
            None,
            selector='selectionShouldChangeInTableView:',
            signature='c@:@',
            isRequired=0,
        ),
# (void) tableView:(NSTableView*)tableView didClickTableColumn:(NSTableColumn *)tableColumn
        _objc.selector(
            None,
            selector='tableView:didClickTableColumn:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void) tableView:(NSTableView*)tableView didDragTableColumn:(NSTableColumn *)tableColumn
        _objc.selector(
            None,
            selector='tableView:didDragTableColumn:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void) tableView:(NSTableView*)tableView mouseDownInHeaderOfTableColumn:(NSTableColumn *)tableColumn
        _objc.selector(
            None,
            selector='tableView:mouseDownInHeaderOfTableColumn:',
            signature='v@:@@',
            isRequired=0,
        ),
# (BOOL)tableView:(NSTableView *)tableView shouldEditTableColumn:(NSTableColumn *)tableColumn row:(int)row
        _objc.selector(
            None,
            selector='tableView:shouldEditTableColumn:row:',
            signature='c@:@@i',
            isRequired=0,
        ),
# (BOOL)tableView:(NSTableView *)tableView shouldSelectRow:(int)row
        _objc.selector(
            None,
            selector='tableView:shouldSelectRow:',
            signature='c@:@i',
            isRequired=0,
        ),
# (BOOL)tableView:(NSTableView *)tableView shouldSelectTableColumn:(NSTableColumn *)tableColumn
        _objc.selector(
            None,
            selector='tableView:shouldSelectTableColumn:',
            signature='c@:@@',
            isRequired=0,
        ),
# (void)tableView:(NSTableView *)tableView willDisplayCell:(id)cell forTableColumn:(NSTableColumn *)tableColumn row:(int)row
        _objc.selector(
            None,
            selector='tableView:willDisplayCell:forTableColumn:row:',
            signature='v@:@@@i',
            isRequired=0,
        ),
    ]
)

NSTableViewNotifications = _objc.informal_protocol(
    "NSTableViewNotifications",
    [
# (void)tableViewColumnDidMove:(NSNotification *)notification
        _objc.selector(
            None,
            selector='tableViewColumnDidMove:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)tableViewColumnDidResize:(NSNotification *)notification
        _objc.selector(
            None,
            selector='tableViewColumnDidResize:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)tableViewSelectionDidChange:(NSNotification *)notification
        _objc.selector(
            None,
            selector='tableViewSelectionDidChange:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)tableViewSelectionIsChanging:(NSNotification *)notification
        _objc.selector(
            None,
            selector='tableViewSelectionIsChanging:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSTextAttachmentCell = _objc.informal_protocol(
    "NSTextAttachmentCell",
    [
# (NSTextAttachment *)attachment
        _objc.selector(
            None,
            selector='attachment',
            signature='@@:',
            isRequired=0,
        ),
# (NSPoint)cellBaselineOffset
        _objc.selector(
            None,
            selector='cellBaselineOffset',
            signature='{_NSPoint=ff}@:',
            isRequired=0,
        ),
# (NSRect)cellFrameForTextContainer:(NSTextContainer *)textContainer proposedLineFragment:(NSRect)lineFrag glyphPosition:(NSPoint)position characterIndex:(unsigned)charIndex
        _objc.selector(
            None,
            selector='cellFrameForTextContainer:proposedLineFragment:glyphPosition:characterIndex:',
            signature='{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}{_NSPoint=ff}I',
            isRequired=0,
        ),
# (NSSize)cellSize
        _objc.selector(
            None,
            selector='cellSize',
            signature='{_NSSize=ff}@:',
            isRequired=0,
        ),
# (void)drawWithFrame:(NSRect)cellFrame inView:(NSView *)controlView
        _objc.selector(
            None,
            selector='drawWithFrame:inView:',
            signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@',
            isRequired=0,
        ),
# (void)drawWithFrame:(NSRect)cellFrame inView:(NSView *)controlView characterIndex:(unsigned)charIndex
        _objc.selector(
            None,
            selector='drawWithFrame:inView:characterIndex:',
            signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I',
            isRequired=0,
        ),
# (void)drawWithFrame:(NSRect)cellFrame inView:(NSView *)controlView characterIndex:(unsigned)charIndex layoutManager:(NSLayoutManager *)layoutManager
        _objc.selector(
            None,
            selector='drawWithFrame:inView:characterIndex:layoutManager:',
            signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I@',
            isRequired=0,
        ),
# (void)highlight:(BOOL)flag withFrame:(NSRect)cellFrame inView:(NSView *)controlView
        _objc.selector(
            None,
            selector='highlight:withFrame:inView:',
            signature='v@:c{_NSRect={_NSPoint=ff}{_NSSize=ff}}@',
            isRequired=0,
        ),
# (void)setAttachment:(NSTextAttachment *)anObject
        _objc.selector(
            None,
            selector='setAttachment:',
            signature='v@:@',
            isRequired=0,
        ),
# (BOOL)trackMouse:(NSEvent *)theEvent inRect:(NSRect)cellFrame ofView:(NSView *)controlView atCharacterIndex:(unsigned)charIndex untilMouseUp:(BOOL)flag
        _objc.selector(
            None,
            selector='trackMouse:inRect:ofView:atCharacterIndex:untilMouseUp:',
            signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@Ic',
            isRequired=0,
        ),
# (BOOL)trackMouse:(NSEvent *)theEvent inRect:(NSRect)cellFrame ofView:(NSView *)controlView untilMouseUp:(BOOL)flag
        _objc.selector(
            None,
            selector='trackMouse:inRect:ofView:untilMouseUp:',
            signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@c',
            isRequired=0,
        ),
# (BOOL)wantsToTrackMouse
        _objc.selector(
            None,
            selector='wantsToTrackMouse',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)wantsToTrackMouseForEvent:(NSEvent *)theEvent inRect:(NSRect)cellFrame ofView:(NSView *)controlView atCharacterIndex:(unsigned)charIndex
        _objc.selector(
            None,
            selector='wantsToTrackMouseForEvent:inRect:ofView:atCharacterIndex:',
            signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I',
            isRequired=0,
        ),
    ]
)

NSTextDelegate = _objc.informal_protocol(
    "NSTextDelegate",
    [
# (void)textDidBeginEditing:(NSNotification *)notification
        _objc.selector(
            None,
            selector='textDidBeginEditing:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)textDidChange:(NSNotification *)notification
        _objc.selector(
            None,
            selector='textDidChange:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)textDidEndEditing:(NSNotification *)notification
        _objc.selector(
            None,
            selector='textDidEndEditing:',
            signature='v@:@',
            isRequired=0,
        ),
# (BOOL)textShouldBeginEditing:(NSText *)textObject
        _objc.selector(
            None,
            selector='textShouldBeginEditing:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)textShouldEndEditing:(NSText *)textObject
        _objc.selector(
            None,
            selector='textShouldEndEditing:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSTextInput = _objc.informal_protocol(
    "NSTextInput",
    [
# (NSAttributedString *) attributedSubstringFromRange:(NSRange)theRange
        _objc.selector(
            None,
            selector='attributedSubstringFromRange:',
            signature='@@:{_NSRange=II}',
            isRequired=0,
        ),
# (unsigned int)characterIndexForPoint:(NSPoint)thePoint
        _objc.selector(
            None,
            selector='characterIndexForPoint:',
            signature='I@:{_NSPoint=ff}',
            isRequired=0,
        ),
# (long) conversationIdentifier
        _objc.selector(
            None,
            selector='conversationIdentifier',
            signature='l@:',
            isRequired=0,
        ),
# (void) doCommandBySelector:(SEL)aSelector
        _objc.selector(
            None,
            selector='doCommandBySelector:',
            signature='v@::',
            isRequired=0,
        ),
# (NSRect) firstRectForCharacterRange:(NSRange)theRange
        _objc.selector(
            None,
            selector='firstRectForCharacterRange:',
            signature='{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:{_NSRange=II}',
            isRequired=0,
        ),
# (BOOL) hasMarkedText
        _objc.selector(
            None,
            selector='hasMarkedText',
            signature='c@:',
            isRequired=0,
        ),
# (void) insertText:(id)aString
        _objc.selector(
            None,
            selector='insertText:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSRange) markedRange
        _objc.selector(
            None,
            selector='markedRange',
            signature='{_NSRange=II}@:',
            isRequired=0,
        ),
# (NSRange) selectedRange
        _objc.selector(
            None,
            selector='selectedRange',
            signature='{_NSRange=II}@:',
            isRequired=0,
        ),
# (void) setMarkedText:(id)aString selectedRange:(NSRange)selRange
        _objc.selector(
            None,
            selector='setMarkedText:selectedRange:',
            signature='v@:@{_NSRange=II}',
            isRequired=0,
        ),
# (void) unmarkText
        _objc.selector(
            None,
            selector='unmarkText',
            signature='v@:',
            isRequired=0,
        ),
# (NSArray*) validAttributesForMarkedText
        _objc.selector(
            None,
            selector='validAttributesForMarkedText',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

NSTextStorageDelegate = _objc.informal_protocol(
    "NSTextStorageDelegate",
    [
# (void)textStorageDidProcessEditing:(NSNotification *)notification
        _objc.selector(
            None,
            selector='textStorageDidProcessEditing:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)textStorageWillProcessEditing:(NSNotification *)notification
        _objc.selector(
            None,
            selector='textStorageWillProcessEditing:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSTextViewDelegate = _objc.informal_protocol(
    "NSTextViewDelegate",
    [
# (void)textView:(NSTextView *)textView clickedOnCell:(id <NSTextAttachmentCell>)cell inRect:(NSRect)cellFrame
        _objc.selector(
            None,
            selector='textView:clickedOnCell:inRect:',
            signature='v@:@@{_NSRect={_NSPoint=ff}{_NSSize=ff}}',
            isRequired=0,
        ),
# (void)textView:(NSTextView *)textView clickedOnCell:(id <NSTextAttachmentCell>)cell inRect:(NSRect)cellFrame atIndex:(unsigned)charIndex
        _objc.selector(
            None,
            selector='textView:clickedOnCell:inRect:atIndex:',
            signature='v@:@@{_NSRect={_NSPoint=ff}{_NSSize=ff}}I',
            isRequired=0,
        ),
# (BOOL)textView:(NSTextView *)textView clickedOnLink:(id)link
        _objc.selector(
            None,
            selector='textView:clickedOnLink:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)textView:(NSTextView *)textView clickedOnLink:(id)link atIndex:(unsigned)charIndex
        _objc.selector(
            None,
            selector='textView:clickedOnLink:atIndex:',
            signature='c@:@@I',
            isRequired=0,
        ),
# (NSArray *)textView:(NSTextView *)textView completions:(NSArray *)words forPartialWordRange:(NSRange)charRange indexOfSelectedItem:(int *)index
        _objc.selector(
            None,
            selector='textView:completions:forPartialWordRange:indexOfSelectedItem:',
            signature='@@:@@{_NSRange=II}N^i',
            isRequired=0,
        ),
# (BOOL)textView:(NSTextView *)textView doCommandBySelector:(SEL)commandSelector
        _objc.selector(
            None,
            selector='textView:doCommandBySelector:',
            signature='c@:@:',
            isRequired=0,
        ),
# (void)textView:(NSTextView *)textView doubleClickedOnCell:(id <NSTextAttachmentCell>)cell inRect:(NSRect)cellFrame
        _objc.selector(
            None,
            selector='textView:doubleClickedOnCell:inRect:',
            signature='v@:@@{_NSRect={_NSPoint=ff}{_NSSize=ff}}',
            isRequired=0,
        ),
# (void)textView:(NSTextView *)textView doubleClickedOnCell:(id <NSTextAttachmentCell>)cell inRect:(NSRect)cellFrame atIndex:(unsigned)charIndex
        _objc.selector(
            None,
            selector='textView:doubleClickedOnCell:inRect:atIndex:',
            signature='v@:@@{_NSRect={_NSPoint=ff}{_NSSize=ff}}I',
            isRequired=0,
        ),
# (void)textView:(NSTextView *)view draggedCell:(id <NSTextAttachmentCell>)cell inRect:(NSRect)rect event:(NSEvent *)event
        _objc.selector(
            None,
            selector='textView:draggedCell:inRect:event:',
            signature='v@:@@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@',
            isRequired=0,
        ),
# (void)textView:(NSTextView *)view draggedCell:(id <NSTextAttachmentCell>)cell inRect:(NSRect)rect event:(NSEvent *)event atIndex:(unsigned)charIndex
        _objc.selector(
            None,
            selector='textView:draggedCell:inRect:event:atIndex:',
            signature='v@:@@{_NSRect={_NSPoint=ff}{_NSSize=ff}}@I',
            isRequired=0,
        ),
# (BOOL)textView:(NSTextView *)textView shouldChangeTextInRange:(NSRange)affectedCharRange replacementString:(NSString *)replacementString
        _objc.selector(
            None,
            selector='textView:shouldChangeTextInRange:replacementString:',
            signature='c@:@{_NSRange=II}@',
            isRequired=0,
        ),
# (NSRange)textView:(NSTextView *)textView willChangeSelectionFromCharacterRange:(NSRange)oldSelectedCharRange toCharacterRange:(NSRange)newSelectedCharRange
        _objc.selector(
            None,
            selector='textView:willChangeSelectionFromCharacterRange:toCharacterRange:',
            signature='{_NSRange=II}@:@{_NSRange=II}{_NSRange=II}',
            isRequired=0,
        ),
# (NSString *)textView:(NSTextView *)textView willDisplayToolTip:(NSString *)tooltip forCharacterAtIndex:(unsigned)characterIndex
        _objc.selector(
            None,
            selector='textView:willDisplayToolTip:forCharacterAtIndex:',
            signature='@@:@@I',
            isRequired=0,
        ),
# (NSArray *)textView:(NSTextView *)view writablePasteboardTypesForCell:(id <NSTextAttachmentCell>)cell atIndex:(unsigned)charIndex
        _objc.selector(
            None,
            selector='textView:writablePasteboardTypesForCell:atIndex:',
            signature='@@:@@I',
            isRequired=0,
        ),
# (BOOL)textView:(NSTextView *)view writeCell:(id <NSTextAttachmentCell>)cell atIndex:(unsigned)charIndex toPasteboard:(NSPasteboard *)pboard type:(NSString *)type
        _objc.selector(
            None,
            selector='textView:writeCell:atIndex:toPasteboard:type:',
            signature='c@:@@I@@',
            isRequired=0,
        ),
# (void)textViewDidChangeSelection:(NSNotification *)notification
        _objc.selector(
            None,
            selector='textViewDidChangeSelection:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)textViewDidChangeTypingAttributes:(NSNotification *)notification
        _objc.selector(
            None,
            selector='textViewDidChangeTypingAttributes:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSUndoManager *)undoManagerForTextView:(NSTextView *)view
        _objc.selector(
            None,
            selector='undoManagerForTextView:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

NSToolTipOwner = _objc.informal_protocol(
    "NSToolTipOwner",
    [
# (NSString *)view:(NSView *)view stringForToolTip:(NSToolTipTag)tag point:(NSPoint)point userData:(void *)data
        _objc.selector(
            None,
            selector='view:stringForToolTip:point:userData:',
            signature='@@:@i{_NSPoint=ff}^v',
            isRequired=0,
        ),
    ]
)

NSToolbarDelegate = _objc.informal_protocol(
    "NSToolbarDelegate",
    [
# (NSToolbarItem *)toolbar:(NSToolbar *)toolbar itemForItemIdentifier:(NSString *)itemIdentifier willBeInsertedIntoToolbar:(BOOL)flag
        _objc.selector(
            None,
            selector='toolbar:itemForItemIdentifier:willBeInsertedIntoToolbar:',
            signature='@@:@@c',
            isRequired=0,
        ),
# (NSArray *)toolbarAllowedItemIdentifiers:(NSToolbar*)toolbar
        _objc.selector(
            None,
            selector='toolbarAllowedItemIdentifiers:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSArray *)toolbarDefaultItemIdentifiers:(NSToolbar*)toolbar
        _objc.selector(
            None,
            selector='toolbarDefaultItemIdentifiers:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSArray *)toolbarSelectableItemIdentifiers:(NSToolbar *)toolbar
        _objc.selector(
            None,
            selector='toolbarSelectableItemIdentifiers:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

NSToolbarItemValidation = _objc.informal_protocol(
    "NSToolbarItemValidation",
    [
# (BOOL)validateToolbarItem:(NSToolbarItem *)theItem
        _objc.selector(
            None,
            selector='validateToolbarItem:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSToolbarNotifications = _objc.informal_protocol(
    "NSToolbarNotifications",
    [
# (void)toolbarDidRemoveItem: (NSNotification *)notification
        _objc.selector(
            None,
            selector='toolbarDidRemoveItem:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)toolbarWillAddItem: (NSNotification *)notification
        _objc.selector(
            None,
            selector='toolbarWillAddItem:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSUserInterfaceValidations = _objc.informal_protocol(
    "NSUserInterfaceValidations",
    [
# (BOOL)validateUserInterfaceItem:(id <NSValidatedUserInterfaceItem>)anItem
        _objc.selector(
            None,
            selector='validateUserInterfaceItem:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSValidatedUserInterfaceItem = _objc.informal_protocol(
    "NSValidatedUserInterfaceItem",
    [
# (SEL)action
        _objc.selector(
            None,
            selector='action',
            signature=':@:',
            isRequired=0,
        ),
# (int)tag
        _objc.selector(
            None,
            selector='tag',
            signature='i@:',
            isRequired=0,
        ),
    ]
)

NSWindowDelegate = _objc.informal_protocol(
    "NSWindowDelegate",
    [
# (NSRect)window:(NSWindow *)window willPositionSheet:(NSWindow *)sheet usingRect:(NSRect)rect
        _objc.selector(
            None,
            selector='window:willPositionSheet:usingRect:',
            signature='{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:@@{_NSRect={_NSPoint=ff}{_NSSize=ff}}',
            isRequired=0,
        ),
# (BOOL)windowShouldClose:(id)sender
        _objc.selector(
            None,
            selector='windowShouldClose:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)windowShouldZoom:(NSWindow *)window toFrame:(NSRect)newFrame
        _objc.selector(
            None,
            selector='windowShouldZoom:toFrame:',
            signature='c@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}',
            isRequired=0,
        ),
# (NSSize)windowWillResize:(NSWindow *)sender toSize:(NSSize)frameSize
        _objc.selector(
            None,
            selector='windowWillResize:toSize:',
            signature='{_NSSize=ff}@:@{_NSSize=ff}',
            isRequired=0,
        ),
# (id)windowWillReturnFieldEditor:(NSWindow *)sender toObject:(id)client
        _objc.selector(
            None,
            selector='windowWillReturnFieldEditor:toObject:',
            signature='@@:@@',
            isRequired=0,
        ),
# (NSUndoManager *)windowWillReturnUndoManager:(NSWindow *)window
        _objc.selector(
            None,
            selector='windowWillReturnUndoManager:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSRect)windowWillUseStandardFrame:(NSWindow *)window defaultFrame:(NSRect)newFrame
        _objc.selector(
            None,
            selector='windowWillUseStandardFrame:defaultFrame:',
            signature='{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}',
            isRequired=0,
        ),
    ]
)

NSWindowNotifications = _objc.informal_protocol(
    "NSWindowNotifications",
    [
# (void)windowDidBecomeKey:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidBecomeKey:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidBecomeMain:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidBecomeMain:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidChangeScreen:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidChangeScreen:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidDeminiaturize:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidDeminiaturize:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidEndSheet:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidEndSheet:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidExpose:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidExpose:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidMiniaturize:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidMiniaturize:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidMove:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidMove:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidResignKey:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidResignKey:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidResignMain:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidResignMain:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidResize:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidResize:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowDidUpdate:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowDidUpdate:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowWillBeginSheet:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowWillBeginSheet:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowWillClose:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowWillClose:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowWillMiniaturize:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowWillMiniaturize:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)windowWillMove:(NSNotification *)notification
        _objc.selector(
            None,
            selector='windowWillMove:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

