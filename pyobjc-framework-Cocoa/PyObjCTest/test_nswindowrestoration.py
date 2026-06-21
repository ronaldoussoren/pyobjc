import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class RestorationHelper(AppKit.NSObject):
    def restoreWindowWithIdentifier_state_completionHandler_(self, a, b, c):
        pass


class TestNSWindowRestoration(TestCase):
    @min_os_level("10.7")
    def test_protocols10_7(self):
        self.assertProtocolExists("NSWindowRestoration", AppKit)
        self.assertArgIsBlock(
            RestorationHelper.restoreWindowWithIdentifier_state_completionHandler_,
            2,
            b"v@@",
        )

    @min_os_level("10.7")
    def test_methods10_7(self):
        self.assertResultIsBOOL(
            AppKit.NSApplication.restoreWindowWithIdentifier_state_completionHandler_
        )
        self.assertArgIsBlock(
            AppKit.NSApplication.restoreWindowWithIdentifier_state_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBOOL(AppKit.NSWindow.setRestorable_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.isRestorable)

        self.assertArgIsBlock(
            AppKit.NSDocument.restoreDocumentWindowWithIdentifier_state_completionHandler_,
            2,
            b"v@@",
        )

    @min_os_level("10.7")
    def test_constants10_7(self):
        self.assertIsInstance(
            AppKit.NSApplicationDidFinishRestoringWindowsNotification, str
        )
