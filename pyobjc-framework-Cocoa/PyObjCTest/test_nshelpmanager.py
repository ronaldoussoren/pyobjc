import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSHelpManager(TestCase):
    def test_constants(self):
        self.assertIsInstance(AppKit.NSContextHelpModeDidActivateNotification, str)
        self.assertIsInstance(AppKit.NSContextHelpModeDidDeactivateNotification, str)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSHelpManager.isContextHelpModeActive)
        self.assertArgIsBOOL(AppKit.NSHelpManager.setContextHelpModeActive_, 0)
        self.assertResultIsBOOL(
            AppKit.NSHelpManager.showContextHelpForObject_locationHint_
        )

    @min_os_level("10.11")
    def test_methods10_6(self):
        self.assertResultIsBOOL(AppKit.NSHelpManager.registerBooksInBundle_)
