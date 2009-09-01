from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSRunningApplication (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.failUnlessEqual(NSApplicationActivateAllWindows, 1<<0)
        self.failUnlessEqual(NSApplicationActivateIgnoringOtherApps, 1<<1)

        self.failUnlessEqual(NSApplicationActivationPolicyRegular, 0)
        self.failUnlessEqual(NSApplicationActivationPolicyAccessory, 1)
        self.failUnlessEqual(NSApplicationActivationPolicyProhibited, 2)

    @min_os_level('10.6')
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSRunningApplication.isTerminated)
        self.failUnlessResultIsBOOL(NSRunningApplication.isFinishedLaunching)
        self.failUnlessResultIsBOOL(NSRunningApplication.isHidden)
        self.failUnlessResultIsBOOL(NSRunningApplication.isActive)
        self.failUnlessResultIsBOOL(NSRunningApplication.hide)
        self.failUnlessResultIsBOOL(NSRunningApplication.unhide)
        self.failUnlessResultIsBOOL(NSRunningApplication.activateWithOptions_)
        self.failUnlessResultIsBOOL(NSRunningApplication.terminate)
        self.failUnlessResultIsBOOL(NSRunningApplication.forceTerminate)


if __name__ == "__main__":
    main()
