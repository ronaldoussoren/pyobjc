import AppKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level


class TestProtocolsExisting(TestCase):
    @min_sdk_level("10.10")
    def testProtocols10_10(self):
        self.assertProtocolExists("NSAlertDelegate")
        self.assertProtocolExists("NSApplicationDelegate")
        self.assertProtocolExists("NSCollectionViewDelegate")
        self.assertProtocolExists("NSDatePickerCellDelegate")
        self.assertProtocolExists("NSDockTilePlugIn")
        self.assertProtocolExists("NSDrawerDelegate")
        self.assertProtocolExists("NSImageDelegate")
        self.assertProtocolExists("NSPageControllerDelegate")
        self.assertProtocolExists("NSPathCellDelegate")
        self.assertProtocolExists("NSSoundDelegate")
        self.assertProtocolExists("NSSpeechRecognizerDelegate")
        self.assertProtocolExists("NSSpeechSynthesizerDelegate")
        self.assertProtocolExists("NSTextFinderClient")
        self.assertProtocolExists("NSTextStorageDelegate")
        self.assertProtocolExists("NSTokenFieldCellDelegate")
        self.assertProtocolExists("NSTokenFieldDelegate")
        self.assertProtocolExists("NSUserInterfaceItemSearching")
        self.assertProtocolExists("NSComboBoxCellDataSource")
        self.assertProtocolExists("NSSplitViewDelegate")
        self.assertProtocolExists("NSTabViewDelegate")

    @min_os_level("10.6")
    def testProtocols10_6(self):
        self.assertProtocolExists("NSAnimatablePropertyContainer")
        self.assertProtocolExists("NSAnimationDelegate")
        self.assertProtocolExists("NSBrowserDelegate")
        self.assertProtocolExists("NSChangeSpelling")
        self.assertProtocolExists("NSColorPickingCustom")
        self.assertProtocolExists("NSColorPickingDefault")
        self.assertProtocolExists("NSComboBoxDataSource")
        self.assertProtocolExists("NSComboBoxDelegate")
        self.assertProtocolExists("NSControlTextEditingDelegate")
        self.assertProtocolExists("NSDraggingInfo")
        self.assertProtocolExists("NSGlyphStorage")
        self.assertProtocolExists("NSIgnoreMisspelledWords")
        self.assertProtocolExists("NSInputServerMouseTracker")
        self.assertProtocolExists("NSInputServiceProvider")
        self.assertProtocolExists("NSLayoutManagerDelegate")
        self.assertProtocolExists("NSMatrixDelegate")
        self.assertProtocolExists("NSMenuDelegate")
        self.assertProtocolExists("NSOpenSavePanelDelegate")
        self.assertProtocolExists("NSOutlineViewDataSource")
        self.assertProtocolExists("NSOutlineViewDelegate")
        self.assertProtocolExists("NSPasteboardItemDataProvider")
        self.assertProtocolExists("NSPasteboardReading")
        self.assertProtocolExists("NSPasteboardWriting")
        self.assertProtocolExists("NSPathControlDelegate")
        self.assertProtocolExists("NSPrintPanelAccessorizing")
        self.assertProtocolExists("NSRuleEditorDelegate")
        self.assertProtocolExists("NSTableViewDataSource")
        self.assertProtocolExists("NSTableViewDelegate")
        self.assertProtocolExists("NSTextAttachmentCell")
        self.assertProtocolExists("NSTextDelegate")
        self.assertProtocolExists("NSTextFieldDelegate")
        self.assertProtocolExists("NSTextInput")
        self.assertProtocolExists("NSTextInputClient")
        self.assertProtocolExists("NSTextViewDelegate")
        self.assertProtocolExists("NSToolbarDelegate")
        self.assertProtocolExists("NSUserInterfaceValidations")
        self.assertProtocolExists("NSValidatedUserInterfaceItem")
        self.assertProtocolExists("NSWindowDelegate")

    @min_os_level("10.7")
    def testProtocols10_7(self):
        self.assertProtocolExists("NSDraggingDestination")
        self.assertProtocolExists("NSDraggingSource")
        self.assertProtocolExists("NSPopoverDelegate")
        self.assertProtocolExists("NSTextFinderBarContainer")
        self.assertProtocolExists("NSTextLayoutOrientationProvider")
        self.assertProtocolExists("NSUserInterfaceItemIdentification")
        self.assertProtocolExists("NSWindowRestoration")

    @min_sdk_level("10.8")
    def testProtocols10_8(self):
        self.assertProtocolExists("NSSharingServiceDelegate")
        self.assertProtocolExists("NSSharingServicePickerDelegate")
