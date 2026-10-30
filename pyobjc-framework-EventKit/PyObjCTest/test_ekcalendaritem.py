from PyObjCTools.TestSupport import TestCase

import EventKit


class TestEKCalendarItem(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(EventKit.EKCalendarItem.hasAlarms)
        self.assertResultIsBOOL(EventKit.EKCalendarItem.hasAttendees)
        self.assertResultIsBOOL(EventKit.EKCalendarItem.hasNotes)
        self.assertResultIsBOOL(EventKit.EKCalendarItem.hasRecurrenceRules)
