import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSSavePanelHelper(AppKit.NSObject):
    def panel_shouldShowFilename_(self, p, f):
        return 1

    def panel_compareFilename_with_caseSensitive_(self, p, f1, f2, i):
        return 1

    def panel_isValidFilename_(self, p, f):
        return 1

    def panel_userEnteredFilename_confirmed_(self, p, f, c):
        return 1

    def panel_willExpand_(self, s, e):
        return 1

    def panel_directoryDidChange_(self, s, p):
        pass

    def panelSelectionDidChange_(self, s):
        pass

    def panel_shouldEnableURL_(self, p, u):
        return 1

    def panel_validateURL_error_(self, p, u, e):
        return 1


class TestNSSavePanel(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSFileHandlingPanelCancelButton, AppKit.NSCancelButton)
        self.assertEqual(AppKit.NSFileHandlingPanelOKButton, AppKit.NSOKButton)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSavePanel.showsHiddenFiles)
        self.assertArgIsBOOL(AppKit.NSSavePanel.setShowsHiddenFiles_, 0)
        self.assertResultIsBOOL(AppKit.NSSavePanel.allowsOtherFileTypes)
        self.assertArgIsBOOL(AppKit.NSSavePanel.setAllowsOtherFileTypes_, 0)
        self.assertResultIsBOOL(AppKit.NSSavePanel.isExpanded)
        self.assertResultIsBOOL(AppKit.NSSavePanel.canCreateDirectories)
        self.assertArgIsBOOL(AppKit.NSSavePanel.setCanCreateDirectories_, 0)
        self.assertResultIsBOOL(AppKit.NSSavePanel.canSelectHiddenExtension)
        self.assertArgIsBOOL(AppKit.NSSavePanel.setCanSelectHiddenExtension_, 0)
        self.assertResultIsBOOL(AppKit.NSSavePanel.isExtensionHidden)
        self.assertArgIsBOOL(AppKit.NSSavePanel.setExtensionHidden_, 0)
        self.assertResultIsBOOL(AppKit.NSSavePanel.treatsFilePackagesAsDirectories)
        self.assertArgIsBOOL(AppKit.NSSavePanel.setTreatsFilePackagesAsDirectories_, 0)

        self.assertArgIsSEL(
            AppKit.NSSavePanel.beginSheetForDirectory_file_modalForWindow_modalDelegate_didEndSelector_contextInfo_,  # noqa: B950
            4,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSSavePanel.beginSheetForDirectory_file_modalForWindow_modalDelegate_didEndSelector_contextInfo_,  # noqa: B950
            5,
            b"^v",
        )

    @min_sdk_level("10.6")
    def testProtocolObjects(self):
        objc.protocolNamed("NSOpenSavePanelDelegate")

    def testProtocol(self):
        self.assertResultIsBOOL(TestNSSavePanelHelper.panel_shouldShowFilename_)
        self.assertResultHasType(
            TestNSSavePanelHelper.panel_compareFilename_with_caseSensitive_,
            objc._C_NSInteger,
        )
        self.assertArgIsBOOL(
            TestNSSavePanelHelper.panel_compareFilename_with_caseSensitive_, 3
        )
        self.assertResultIsBOOL(TestNSSavePanelHelper.panel_isValidFilename_)
        self.assertArgIsBOOL(
            TestNSSavePanelHelper.panel_userEnteredFilename_confirmed_, 2
        )
        self.assertArgIsBOOL(TestNSSavePanelHelper.panel_willExpand_, 1)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBlock(
            AppKit.NSSavePanel.beginWithCompletionHandler_, 0, b"v" + objc._C_NSInteger
        )

        self.assertResultIsBOOL(TestNSSavePanelHelper.panel_shouldEnableURL_)
        self.assertResultIsBOOL(TestNSSavePanelHelper.panel_validateURL_error_)
        self.assertArgHasType(TestNSSavePanelHelper.panel_validateURL_error_, 2, b"o^@")

        self.assertArgIsBlock(
            AppKit.NSSavePanel.beginSheetModalForWindow_completionHandler_,
            1,
            b"v" + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            AppKit.NSSavePanel.beginWithCompletionHandler_, 0, b"v" + objc._C_NSInteger
        )

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBOOL(AppKit.NSSavePanel.setShowsTagField_, 0)
        self.assertResultIsBOOL(AppKit.NSSavePanel.showsTagField)

    def test_issue282(self):
        panel = AppKit.NSSavePanel.savePanel()
        self.assertIsInstance(panel, AppKit.NSSavePanel)
