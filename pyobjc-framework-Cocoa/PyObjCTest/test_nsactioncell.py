from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSActionCell (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(NSActionCell.setBordered_, 0)
        self.assertArgIsBOOL(NSActionCell.setBezeled_, 0)
        self.assertArgIsBOOL(NSActionCell.setEnabled_, 0)
        self.assertArgIsBOOL(NSActionCell.setFloatingPointFormat_left_right_, 0)
        self.assertArgIsSEL(NSActionCell.setAction_, 0, b'v@:@')

if __name__ == "__main__":
    main()
