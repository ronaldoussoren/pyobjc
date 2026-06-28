import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSDateIntervalFormatter(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSDateIntervalFormatterStyle)
        self.assertEqual(Foundation.NSDateIntervalFormatterNoStyle, 0)
        self.assertEqual(Foundation.NSDateIntervalFormatterShortStyle, 1)
        self.assertEqual(Foundation.NSDateIntervalFormatterMediumStyle, 2)
        self.assertEqual(Foundation.NSDateIntervalFormatterLongStyle, 3)
        self.assertEqual(Foundation.NSDateIntervalFormatterFullStyle, 4)
