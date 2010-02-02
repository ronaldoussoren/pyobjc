
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPopUpButton (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSPopUpButtonWillPopUpNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSPopUpButton.pullsDown)
        self.assertArgIsBOOL(NSPopUpButton.setPullsDown_, 0)
        self.assertResultIsBOOL(NSPopUpButton.autoenablesItems)
        self.assertArgIsBOOL(NSPopUpButton.setAutoenablesItems_, 0)
        self.assertResultIsBOOL(NSPopUpButton.selectItemWithTag_)

if __name__ == "__main__":
    main()
