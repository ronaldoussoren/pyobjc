import OSLog
from PyObjCTools.TestSupport import TestCase


class TestMessageComponent(TestCase):
    def test_constants(self):
        self.assertEqual(OSLog.OSLogMessageComponentArgumentCategoryUndefined, 0)
        self.assertEqual(OSLog.OSLogMessageComponentArgumentCategoryData, 1)
        self.assertEqual(OSLog.OSLogMessageComponentArgumentCategoryDouble, 2)
        self.assertEqual(OSLog.OSLogMessageComponentArgumentCategoryInt64, 3)
        self.assertEqual(OSLog.OSLogMessageComponentArgumentCategoryString, 4)
        self.assertEqual(OSLog.OSLogMessageComponentArgumentCategoryUInt64, 5)
