import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSDatePicker(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSDatePicker.isBezeled)
        self.assertArgIsBOOL(AppKit.NSDatePicker.setBezeled_, 0)

        self.assertResultIsBOOL(AppKit.NSDatePicker.isBordered)
        self.assertArgIsBOOL(AppKit.NSDatePicker.setBordered_, 0)

        self.assertResultIsBOOL(AppKit.NSDatePicker.drawsBackground)
        self.assertArgIsBOOL(AppKit.NSDatePicker.setDrawsBackground_, 0)

    @min_os_level("10.15.4")
    def testMethods10_15_4(self):
        self.assertResultIsBOOL(AppKit.NSDatePicker.presentsCalendarOverlay)
        self.assertArgIsBOOL(AppKit.NSDatePicker.setPresentsCalendarOverlay_, 0)
