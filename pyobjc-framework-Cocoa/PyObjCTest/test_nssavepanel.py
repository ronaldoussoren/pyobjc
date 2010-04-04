
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSavePanelHelper (NSObject):
    def panel_shouldShowFilename_(self, p, f): return 1
    def panel_compareFilename_with_caseSensitive_(self, p, f1, f2, i): return 1
    def panel_isValidFilename_(self, p, f): return 1
    def panel_userEnteredFilename_confirmed_(self, p, f, c): return 1
    def panel_willExpand_(self, s, e): return 1
    def panel_directoryDidChange_(self, s, p): pass
    def panelSelectionDidChange_(self, s): pass
    def panel_shouldEnableURL_(self, p, u): return 1
    def panel_validateURL_error_(self, p, u, e): return 1

class TestNSSavePanel (TestCase):
    def testConstants(self):
        self.assertEqual(NSFileHandlingPanelCancelButton, NSCancelButton)
        self.assertEqual(NSFileHandlingPanelOKButton, NSOKButton)

    def testMethods(self):
        self.assertResultIsBOOL(NSSavePanel.showsHiddenFiles)
        self.assertArgIsBOOL(NSSavePanel.setShowsHiddenFiles_, 0)
        self.assertResultIsBOOL(NSSavePanel.allowsOtherFileTypes)
        self.assertArgIsBOOL(NSSavePanel.setAllowsOtherFileTypes_, 0)
        self.assertResultIsBOOL(NSSavePanel.isExpanded)
        self.assertResultIsBOOL(NSSavePanel.canCreateDirectories)
        self.assertArgIsBOOL(NSSavePanel.setCanCreateDirectories_, 0)
        self.assertResultIsBOOL(NSSavePanel.canSelectHiddenExtension)
        self.assertArgIsBOOL(NSSavePanel.setCanSelectHiddenExtension_, 0)
        self.assertResultIsBOOL(NSSavePanel.isExtensionHidden)
        self.assertArgIsBOOL(NSSavePanel.setExtensionHidden_, 0)
        self.assertResultIsBOOL(NSSavePanel.treatsFilePackagesAsDirectories)
        self.assertArgIsBOOL(NSSavePanel.setTreatsFilePackagesAsDirectories_, 0)

        self.assertArgIsSEL(NSSavePanel.beginSheetForDirectory_file_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 4, b'v@:@' + objc._C_NSInteger + b'^v')
        self.assertArgHasType(NSSavePanel.beginSheetForDirectory_file_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 5, b'^v')

    def testProtocol(self):
        self.assertResultIsBOOL(TestNSSavePanelHelper.panel_shouldShowFilename_)
        self.assertResultHasType(TestNSSavePanelHelper.panel_compareFilename_with_caseSensitive_, objc._C_NSInteger)
        self.assertArgIsBOOL(TestNSSavePanelHelper.panel_compareFilename_with_caseSensitive_, 3)
        self.assertResultIsBOOL(TestNSSavePanelHelper.panel_isValidFilename_)
        self.assertArgIsBOOL(TestNSSavePanelHelper.panel_userEnteredFilename_confirmed_, 2)
        self.assertArgIsBOOL(TestNSSavePanelHelper.panel_willExpand_, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBlock(NSSavePanel.beginWithCompletionHandler_, 0, b'v' + objc._C_NSInteger)

        self.assertResultIsBOOL(TestNSSavePanelHelper.panel_shouldEnableURL_)
        self.assertResultIsBOOL(TestNSSavePanelHelper.panel_validateURL_error_)
        self.assertArgHasType(TestNSSavePanelHelper.panel_validateURL_error_, 2, b'o^@')

        self.assertArgIsBlock(NSSavePanel.beginSheetModalForWindow_completionHandler_, 1, b'v'+objc._C_NSInteger)
        self.assertArgIsBlock(NSSavePanel.beginWithCompletionHandler_, 0, b'v'+objc._C_NSInteger)

if __name__ == "__main__":
    main()
