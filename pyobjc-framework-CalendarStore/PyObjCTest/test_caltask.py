import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalTask(TestCase):
    def testConstants(self):
        self.assertEqual(CalendarStore.CalPriorityNone, 0)
        self.assertEqual(CalendarStore.CalPriorityHigh, 1)
        self.assertEqual(CalendarStore.CalPriorityMedium, 5)
        self.assertEqual(CalendarStore.CalPriorityLow, 9)

    def testMethods(self):
        self.assertResultIsBOOL(CalendarStore.CalTask.isCompleted)
        self.assertArgIsBOOL(CalendarStore.CalTask.setIsCompleted_, 0)
