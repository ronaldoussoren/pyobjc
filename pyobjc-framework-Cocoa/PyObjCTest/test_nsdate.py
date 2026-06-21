import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSDate(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSDate.isEqualToDate_)

    def test_constants(self):
        self.assertEqual(AppKit.NSTimeIntervalSince1970, 978_307_200.0)

    @min_os_level("10.6")
    def test_constants10_6(self):
        self.assertIsInstance(AppKit.NSSystemClockDidChangeNotification, str)
