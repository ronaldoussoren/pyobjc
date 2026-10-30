import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSRunningApplication(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSApplicationActivationOptions)
        self.assertEqual(AppKit.NSApplicationActivationPolicyRegular, 0)
        self.assertEqual(AppKit.NSApplicationActivationPolicyAccessory, 1)
        self.assertEqual(AppKit.NSApplicationActivationPolicyProhibited, 2)

        self.assertIsEnumType(AppKit.NSApplicationActivationPolicy)
        self.assertEqual(AppKit.NSApplicationActivateAllWindows, 1 << 0)
        self.assertEqual(AppKit.NSApplicationActivateIgnoringOtherApps, 1 << 1)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSRunningApplication.isTerminated)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.isFinishedLaunching)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.isHidden)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.isActive)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.hide)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.unhide)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.activateWithOptions_)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.terminate)
        self.assertResultIsBOOL(AppKit.NSRunningApplication.forceTerminate)

        self.assertResultIsBOOL(AppKit.NSRunningApplication.ownsMenuBar)

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            AppKit.NSRunningApplication.activateFromApplication_options_
        )
