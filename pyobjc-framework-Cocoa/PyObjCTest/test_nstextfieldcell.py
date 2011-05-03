
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextFieldCell (TestCase):
    def testConstants(self):
        self.assertEqual(NSTextFieldSquareBezel, 0)
        self.assertEqual(NSTextFieldRoundedBezel, 1)

    def testMethods(self):
        self.assertResultIsBOOL(NSTextFieldCell.drawsBackground)
        self.assertArgIsBOOL(NSTextFieldCell.setDrawsBackground_, 0)
        self.assertArgIsBOOL(NSTextFieldCell.setWantsNotificationForMarkedText_, 0)


if __name__ == "__main__":
    main()
