from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINRecurrenceFrequency(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INRecurrenceFrequency)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INRecurrenceFrequencyUnknown, 0)
        self.assertEqual(Intents.INRecurrenceFrequencyMinute, 1)
        self.assertEqual(Intents.INRecurrenceFrequencyHourly, 2)
        self.assertEqual(Intents.INRecurrenceFrequencyDaily, 3)
        self.assertEqual(Intents.INRecurrenceFrequencyWeekly, 4)
        self.assertEqual(Intents.INRecurrenceFrequencyMonthly, 5)
        self.assertEqual(Intents.INRecurrenceFrequencyYearly, 6)
