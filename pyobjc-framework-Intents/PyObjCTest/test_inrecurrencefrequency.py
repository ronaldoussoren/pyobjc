from PyObjCTools.TestSupport import TestCase
import Intents


class TestINRecurrenceFrequency(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INRecurrenceFrequency)
        self.assertEqual(Intents.INRecurrenceFrequencyUnknown, 0)
        self.assertEqual(Intents.INRecurrenceFrequencyMinute, 1)
        self.assertEqual(Intents.INRecurrenceFrequencyHourly, 2)
        self.assertEqual(Intents.INRecurrenceFrequencyDaily, 3)
        self.assertEqual(Intents.INRecurrenceFrequencyWeekly, 4)
        self.assertEqual(Intents.INRecurrenceFrequencyMonthly, 5)
        self.assertEqual(Intents.INRecurrenceFrequencyYearly, 6)
