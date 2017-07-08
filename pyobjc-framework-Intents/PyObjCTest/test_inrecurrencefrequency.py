import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINRecurrenceFrequency (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INRecurrenceFrequencyUnknown, 0)
            self.assertEqual(Intents.INRecurrenceFrequencyMinute, 1)
            self.assertEqual(Intents.INRecurrenceFrequencyHourly, 2)
            self.assertEqual(Intents.INRecurrenceFrequencyDaily, 3)
            self.assertEqual(Intents.INRecurrenceFrequencyWeekly, 4)
            self.assertEqual(Intents.INRecurrenceFrequencyMonthly, 5)
            self.assertEqual(Intents.INRecurrenceFrequencyYearly, 6)


if __name__ == "__main__":
    main()
