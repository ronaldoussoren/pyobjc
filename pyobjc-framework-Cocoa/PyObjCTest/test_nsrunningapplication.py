from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSRunningApplication (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.assertEqual(NSApplicationActivateAllWindows, 1<<0)
        self.assertEqual(NSApplicationActivateIgnoringOtherApps, 1<<1)

        self.assertEqual(NSApplicationActivationPolicyRegular, 0)
        self.assertEqual(NSApplicationActivationPolicyAccessory, 1)
        self.assertEqual(NSApplicationActivationPolicyProhibited, 2)

    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(NSRunningApplication.isTerminated)
        self.assertResultIsBOOL(NSRunningApplication.isFinishedLaunching)
        self.assertResultIsBOOL(NSRunningApplication.isHidden)
        self.assertResultIsBOOL(NSRunningApplication.isActive)
        self.assertResultIsBOOL(NSRunningApplication.hide)
        self.assertResultIsBOOL(NSRunningApplication.unhide)
        self.assertResultIsBOOL(NSRunningApplication.activateWithOptions_)
        self.assertResultIsBOOL(NSRunningApplication.terminate)
        self.assertResultIsBOOL(NSRunningApplication.forceTerminate)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(NSRunningApplication.ownsMenuBar)


if __name__ == "__main__":
    main()
