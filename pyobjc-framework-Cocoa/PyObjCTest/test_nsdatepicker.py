from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDatePicker (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSDatePicker.isBezeled)
        self.assertArgIsBOOL(NSDatePicker.setBezeled_, 0)

        self.assertResultIsBOOL(NSDatePicker.isBordered)
        self.assertArgIsBOOL(NSDatePicker.setBordered_, 0)

        self.assertResultIsBOOL(NSDatePicker.drawsBackground)
        self.assertArgIsBOOL(NSDatePicker.setDrawsBackground_, 0)

if __name__ == "__main__":
    main()
