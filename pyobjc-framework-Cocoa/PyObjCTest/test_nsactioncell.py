from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSActionCell (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSActionCell.setBordered_, 0)
        self.failUnlessArgIsBOOL(NSActionCell.setBezeled_, 0)
        self.failUnlessArgIsBOOL(NSActionCell.setEnabled_, 0)
        self.failUnlessArgIsBOOL(NSActionCell.setFloatingPointFormat_left_right_, 0)


if __name__ == "__main__":
    main()
