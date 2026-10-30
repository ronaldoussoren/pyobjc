import AppKit
from PyObjCTools.TestSupport import TestCase


class RestorationHelper(AppKit.NSObject):
    def restoreWindowWithIdentifier_state_completionHandler_(self, a, b, c):
        pass


class TestNSWindowRestoration(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            AppKit.NSApplicationDidFinishRestoringWindowsNotification, str
        )

    def test_methods(self):
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

    def test_protocols(self):
        self.assertProtocolExists("NSWindowRestoration", AppKit)

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            RestorationHelper.restoreWindowWithIdentifier_state_completionHandler_,
            2,
            b"v@@",
        )
