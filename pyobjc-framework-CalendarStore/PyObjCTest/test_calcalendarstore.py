import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalCalendarStore(TestCase):
    def testConstants(self):
        self.assertEqual(CalendarStore.CalSpanThisEvent, 0)
        self.assertEqual(CalendarStore.CalSpanFutureEvents, 1)
        self.assertEqual(CalendarStore.CalSpanAllEvents, 2)

        self.assertIsInstance(CalendarStore.CalCalendarsChangedNotification, str)
        self.assertIsInstance(CalendarStore.CalEventsChangedNotification, str)
        self.assertIsInstance(CalendarStore.CalTasksChangedNotification, str)
        self.assertIsInstance(
            CalendarStore.CalCalendarsChangedExternallyNotification, str
        )
        self.assertIsInstance(CalendarStore.CalEventsChangedExternallyNotification, str)
        self.assertIsInstance(CalendarStore.CalTasksChangedExternallyNotification, str)
        self.assertIsInstance(CalendarStore.CalInsertedRecordsKey, str)
        self.assertIsInstance(CalendarStore.CalUpdatedRecordsKey, str)
        self.assertIsInstance(CalendarStore.CalDeletedRecordsKey, str)
        self.assertIsInstance(CalendarStore.CalSenderProcessIDKey, str)
        self.assertIsInstance(CalendarStore.CalUserUIDKey, str)

    def testMethods(self):
        self.assertResultIsBOOL(CalendarStore.CalCalendarStore.saveCalendar_error_)
        self.assertResultIsBOOL(CalendarStore.CalCalendarStore.removeCalendar_error_)
        self.assertArgIsOut(CalendarStore.CalCalendarStore.saveCalendar_error_, 1)
        self.assertArgIsOut(CalendarStore.CalCalendarStore.removeCalendar_error_, 1)

        self.assertArgIsOut(CalendarStore.CalCalendarStore.saveEvent_span_error_, 2)
        self.assertResultIsBOOL(CalendarStore.CalCalendarStore.saveEvent_span_error_)

        self.assertArgIsOut(CalendarStore.CalCalendarStore.removeEvent_span_error_, 2)
        self.assertResultIsBOOL(CalendarStore.CalCalendarStore.removeEvent_span_error_)

        self.assertArgIsOut(CalendarStore.CalCalendarStore.saveTask_error_, 1)
        self.assertResultIsBOOL(CalendarStore.CalCalendarStore.saveTask_error_)

        self.assertArgIsOut(CalendarStore.CalCalendarStore.removeTask_error_, 1)
        self.assertResultIsBOOL(CalendarStore.CalCalendarStore.removeTask_error_)
