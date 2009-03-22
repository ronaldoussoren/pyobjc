
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextFieldCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTextFieldSquareBezel, 0)
        self.failUnlessEqual(NSTextFieldRoundedBezel, 1)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTextFieldCell.drawsBackground)
        self.failUnlessArgIsBOOL(NSTextFieldCell.setDrawsBackground_, 0)
        self.failUnlessArgIsBOOL(NSTextFieldCell.setWantsNotificationForMarkedText_, 0)


if __name__ == "__main__":
    main()
