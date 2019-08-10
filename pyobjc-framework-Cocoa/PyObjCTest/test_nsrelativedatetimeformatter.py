from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSRelativeDateTimeFormatter(TestCase):
    def test_constants(self):
        self.assertEqual(NSRelativeDateTimeFormatterStyleNumeric, 0)
        self.assertEqual(NSRelativeDateTimeFormatterStyleNamed, 1)

        self.assertEqual(NSRelativeDateTimeFormatterUnitsStyleFull, 0)
        self.assertEqual(NSRelativeDateTimeFormatterUnitsStyleSpellOut, 1)
        self.assertEqual(NSRelativeDateTimeFormatterUnitsStyleShort, 2)
        self.assertEqual(NSRelativeDateTimeFormatterUnitsStyleAbbreviated, 3)


if __name__ == "__main__":
    main()
