
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSHelpManager (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSContextHelpModeDidActivateNotification, unicode)
        self.assertIsInstance(NSContextHelpModeDidDeactivateNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSHelpManager.isContextHelpModeActive)
        self.assertArgIsBOOL(NSHelpManager.setContextHelpModeActive_, 0)
        self.assertResultIsBOOL(NSHelpManager.showContextHelpForObject_locationHint_)

    @min_os_level('10.11')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSHelpManager.registerBooksInBundle_)


if __name__ == "__main__":
    main()
