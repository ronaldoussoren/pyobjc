import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSDateIntervalFormatter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSDateIntervalFormatterStyle)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(Foundation.NSDateIntervalFormatterNoStyle, 0)
        self.assertEqual(Foundation.NSDateIntervalFormatterShortStyle, 1)
        self.assertEqual(Foundation.NSDateIntervalFormatterMediumStyle, 2)
        self.assertEqual(Foundation.NSDateIntervalFormatterLongStyle, 3)
        self.assertEqual(Foundation.NSDateIntervalFormatterFullStyle, 4)
