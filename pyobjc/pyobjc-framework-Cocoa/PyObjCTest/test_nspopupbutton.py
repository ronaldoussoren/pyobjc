
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPopUpButton (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSPopUpButtonWillPopUpNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPopUpButton.pullsDown)
        self.failUnlessArgIsBOOL(NSPopUpButton.setPullsDown_, 0)
        self.failUnlessResultIsBOOL(NSPopUpButton.autoenablesItems)
        self.failUnlessArgIsBOOL(NSPopUpButton.setAutoenablesItems_, 0)
        self.failUnlessResultIsBOOL(NSPopUpButton.selectItemWithTag_)

if __name__ == "__main__":
    main()
