
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSHelpManager (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSContextHelpModeDidActivateNotification, unicode)
        self.failUnlessIsInstance(NSContextHelpModeDidDeactivateNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSHelpManager.isContextHelpModeActive)
        self.failUnlessArgIsBOOL(NSHelpManager.setContextHelpModeActive_, 0)
        self.failUnlessResultIsBOOL(NSHelpManager.showContextHelpForObject_locationHint_)


if __name__ == "__main__":
    main()
