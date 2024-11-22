import AppKit
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_level_key,
    os_release,
    skipUnless,
)
import objc


class TestOpenPanel(TestCase):
    @skipUnless(
        not (
            os_level_key("10.13") <= os_level_key(os_release()) < os_level_key("10.15")
        ),
        "Crash on 10.13, 10.14??",
    )
    @skipUnless(
        not (os_level_key("15.0") <= os_level_key(os_release()) < os_level_key("16.0")),
        "Crash on macOS 15",
    )
    def testOpenPanelSignature(self):
        o = AppKit.NSOpenPanel.openPanel()
        sig = (
            o.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_.signature  # noqa: B950
        )
        sig = b"".join(objc.splitSignature(sig))
        self.assertEqual(sig, b"v@:@@@@@:^v")

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSOpenPanel.resolvesAliases)
        self.assertArgIsBOOL(AppKit.NSOpenPanel.setResolvesAliases_, 0)
        self.assertResultIsBOOL(AppKit.NSOpenPanel.canChooseDirectories)
        self.assertArgIsBOOL(AppKit.NSOpenPanel.setCanChooseDirectories_, 0)
        self.assertResultIsBOOL(AppKit.NSOpenPanel.allowsMultipleSelection)
        self.assertArgIsBOOL(AppKit.NSOpenPanel.setAllowsMultipleSelection_, 0)
        self.assertResultIsBOOL(AppKit.NSOpenPanel.canChooseFiles)
        self.assertArgIsBOOL(AppKit.NSOpenPanel.setCanChooseFiles_, 0)

        self.assertArgIsSEL(
            AppKit.NSOpenPanel.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_,  # noqa: B950
            5,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSOpenPanel.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_,  # noqa: B950
            6,
            b"^v",
        )

        self.assertArgIsSEL(
            AppKit.NSOpenPanel.beginForDirectory_file_types_modelessDelegate_didEndSelector_contextInfo_,  # noqa: B950
            4,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSOpenPanel.beginForDirectory_file_types_modelessDelegate_didEndSelector_contextInfo_,  # noqa: B950
            5,
            b"^v",
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSOpenPanel.canResolveUbiquitousConflicts)
        self.assertArgIsBOOL(AppKit.NSOpenPanel.setCanResolveUbiquitousConflicts_, 0)
        self.assertResultIsBOOL(AppKit.NSOpenPanel.canDownloadUbiquitousContents)
        self.assertArgIsBOOL(AppKit.NSOpenPanel.setCanDownloadUbiquitousContents_, 0)

    @skipUnless(
        not (
            os_level_key("10.13") <= os_level_key(os_release()) < os_level_key("10.15")
        ),
        "Crash on 10.13, 10.14??",
    )
    @skipUnless(
        not (os_level_key("15.0") <= os_level_key(os_release()) < os_level_key("16.0")),
        "Crash on macOS 15",
    )
    def test_issue_272(self):
        panel = AppKit.NSOpenPanel.openPanel()
        panel.setAllowedFileTypes_([".html", ".txt"])
