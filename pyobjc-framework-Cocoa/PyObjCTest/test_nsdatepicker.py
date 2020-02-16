from PyObjCTools.TestSupport import *
from AppKit import *


class TestNSDatePicker(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSDatePicker.isBezeled)
        self.assertArgIsBOOL(NSDatePicker.setBezeled_, 0)

        self.assertResultIsBOOL(NSDatePicker.isBordered)
        self.assertArgIsBOOL(NSDatePicker.setBordered_, 0)

        self.assertResultIsBOOL(NSDatePicker.drawsBackground)
        self.assertArgIsBOOL(NSDatePicker.setDrawsBackground_, 0)

    @min_os_level('10.15.4')
    def testMethods10_15_4(self):
        self.assertResultIsBOOL(NSDatePicker.presentsCalendarOverlay)
        self.assertArgIsBOOL(NSDatePicker.setPresentsCalendarOverlay_, 0)

if __name__ == "__main__":
    main()
