import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSDate(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSDate.isEqualToDate_)

    def test_constants(self):
        self.assertEqual(AppKit.NSTimeIntervalSince1970, 978_307_200.0)

        self.assertIsInstance(AppKit.NSSystemClockDidChangeNotification, str)
