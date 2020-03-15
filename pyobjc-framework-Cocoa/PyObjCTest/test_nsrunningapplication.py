import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSRunningApplication(TestCase):
    @min_os_level("10.6")
    def testConstants(self):
        self.assertEqual(AppKit.NSApplicationActivateAllWindows, 1 << 0)
        self.assertEqual(AppKit.NSApplicationActivateIgnoringOtherApps, 1 << 1)

        self.assertEqual(AppKit.NSApplicationActivationPolicyRegular, 0)
        self.assertEqual(AppKit.NSApplicationActivationPolicyAccessory, 1)
        self.assertEqual(AppKit.NSApplicationActivationPolicyProhibited, 2)

    @min_os_level("10.6")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSRunningApplication.isTerminated)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.isFinishedLaunching)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.isHidden)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.isActive)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.hide)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.unhide)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.activateWithOptions_)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.terminate)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.forceTerminate)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSRunningApplication.ownsMenuBar)
