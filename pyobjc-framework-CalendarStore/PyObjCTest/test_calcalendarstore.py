
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalCalendarStore (TestCase):
    def testConstants(self):
        self.failUnlessEqual(CalSpanThisEvent, 0)
        self.failUnlessEqual(CalSpanFutureEvents, 1)
        self.failUnlessEqual(CalSpanAllEvents, 2)

        self.failUnlessIsInstance(CalCalendarsChangedNotification, unicode)
        self.failUnlessIsInstance(CalEventsChangedNotification, unicode)
        self.failUnlessIsInstance(CalTasksChangedNotification, unicode)
        self.failUnlessIsInstance(CalCalendarsChangedExternallyNotification, unicode)
        self.failUnlessIsInstance(CalEventsChangedExternallyNotification, unicode)
        self.failUnlessIsInstance(CalTasksChangedExternallyNotification, unicode)
        self.failUnlessIsInstance(CalInsertedRecordsKey, unicode)
        self.failUnlessIsInstance(CalUpdatedRecordsKey, unicode)
        self.failUnlessIsInstance(CalDeletedRecordsKey, unicode)
        self.failUnlessIsInstance(CalSenderProcessIDKey, unicode)
        self.failUnlessIsInstance(CalUserUIDKey, unicode)

    def testMethods(self):
        self.failUnlessArgIsOut(CalCalendarStore.saveCalendar_error_, 1)
        self.failUnlessArgIsOut(CalCalendarStore.removeCalendar_error_, 1)

        self.failUnlessArgIsOut(CalCalendarStore.saveEvent_span_error_, 2)
        self.failUnlessResultIsBOOL(CalCalendarStore.saveEvent_span_error_)

        self.failUnlessArgIsOut(CalCalendarStore.removeEvent_span_error_, 2)
        self.failUnlessResultIsBOOL(CalCalendarStore.removeEvent_span_error_)

        self.failUnlessArgIsOut(CalCalendarStore.saveTask_error_, 1)
        self.failUnlessResultIsBOOL(CalCalendarStore.saveTask_error_)

        self.failUnlessArgIsOut(CalCalendarStore.removeTask_error_, 1)
        self.failUnlessResultIsBOOL(CalCalendarStore.removeTask_error_)

if __name__ == "__main__":
    main()
