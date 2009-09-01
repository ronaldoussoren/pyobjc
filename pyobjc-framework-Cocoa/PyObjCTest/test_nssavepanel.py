
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
        self.failUnlessEqual(NSFileHandlingPanelCancelButton, NSCancelButton)
        self.failUnlessEqual(NSFileHandlingPanelOKButton, NSOKButton)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSavePanel.showsHiddenFiles)
        self.failUnlessArgIsBOOL(NSSavePanel.setShowsHiddenFiles_, 0)
        self.failUnlessResultIsBOOL(NSSavePanel.allowsOtherFileTypes)
        self.failUnlessArgIsBOOL(NSSavePanel.setAllowsOtherFileTypes_, 0)
        self.failUnlessResultIsBOOL(NSSavePanel.isExpanded)
        self.failUnlessResultIsBOOL(NSSavePanel.canCreateDirectories)
        self.failUnlessArgIsBOOL(NSSavePanel.setCanCreateDirectories_, 0)
        self.failUnlessResultIsBOOL(NSSavePanel.canSelectHiddenExtension)
        self.failUnlessArgIsBOOL(NSSavePanel.setCanSelectHiddenExtension_, 0)
        self.failUnlessResultIsBOOL(NSSavePanel.isExtensionHidden)
        self.failUnlessArgIsBOOL(NSSavePanel.setExtensionHidden_, 0)
        self.failUnlessResultIsBOOL(NSSavePanel.treatsFilePackagesAsDirectories)
        self.failUnlessArgIsBOOL(NSSavePanel.setTreatsFilePackagesAsDirectories_, 0)

        self.failUnlessArgIsSEL(NSSavePanel.beginSheetForDirectory_file_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 4, 'v@:@' + objc._C_NSInteger + '^v')
        self.failUnlessArgHasType(NSSavePanel.beginSheetForDirectory_file_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 5, '^v')

    def testProtocol(self):
        self.failUnlessResultIsBOOL(TestNSSavePanelHelper.panel_shouldShowFilename_)
        self.failUnlessResultHasType(TestNSSavePanelHelper.panel_compareFilename_with_caseSensitive_, objc._C_NSInteger)
        self.failUnlessArgIsBOOL(TestNSSavePanelHelper.panel_compareFilename_with_caseSensitive_, 3)
        self.failUnlessResultIsBOOL(TestNSSavePanelHelper.panel_isValidFilename_)
        self.failUnlessArgIsBOOL(TestNSSavePanelHelper.panel_userEnteredFilename_confirmed_, 2)
        self.failUnlessArgIsBOOL(TestNSSavePanelHelper.panel_willExpand_, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsBlock(NSSavePanel.beginWithCompletionHandler_, 0, 'v' + objc._C_NSInteger)

        self.failUnlessResultIsBOOL(TestNSSavePanelHelper.panel_shouldEnableURL_)
        self.failUnlessResultIsBOOL(TestNSSavePanelHelper.panel_validateURL_error_)
        self.failUnlessArgHasType(TestNSSavePanelHelper.panel_validateURL_error_, 2, 'o^@')

        self.failUnlessArgIsBlock(NSSavePanel.beginSheetModalForWindow_completionHandler_, 1, 'v'+objc._C_NSInteger)
        self.failUnlessArgIsBlock(NSSavePanel.beginWithCompletionHandler_, 0, 'v'+objc._C_NSInteger)

if __name__ == "__main__":
    main()
