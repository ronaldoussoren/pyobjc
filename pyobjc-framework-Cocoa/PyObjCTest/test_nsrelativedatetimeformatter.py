import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSRelativeDateTimeFormatter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSRelativeDateTimeFormatterStyle)
        self.assertIsEnumType(Foundation.NSRelativeDateTimeFormatterUnitsStyle)

    def test_constants(self):
        self.assertEqual(Foundation.NSRelativeDateTimeFormatterStyleNumeric, 0)
        self.assertEqual(Foundation.NSRelativeDateTimeFormatterStyleNamed, 1)

        self.assertEqual(Foundation.NSRelativeDateTimeFormatterUnitsStyleFull, 0)
        self.assertEqual(Foundation.NSRelativeDateTimeFormatterUnitsStyleSpellOut, 1)
        self.assertEqual(Foundation.NSRelativeDateTimeFormatterUnitsStyleShort, 2)
        self.assertEqual(Foundation.NSRelativeDateTimeFormatterUnitsStyleAbbreviated, 3)
