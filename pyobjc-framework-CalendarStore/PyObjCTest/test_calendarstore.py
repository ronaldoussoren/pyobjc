'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import CalendarStore

class TestCalendarStore (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(CalendarStore, 'CalAlarm') )
        self.assert_( isinstance(CalendarStore.CalAlarm, objc.objc_class) )
        self.assert_( hasattr(CalendarStore, 'CalNthWeekDay') )
        self.assert_( isinstance(CalendarStore.CalNthWeekDay, objc.objc_class) )

    def testValues(self):
        # Integer values:
        self.assert_( hasattr(CalendarStore, 'CalSpanThisEvent') )
        self.assert_( isinstance(CalendarStore.CalSpanThisEvent, (int, long)) )
        self.assertEquals(CalendarStore.CalSpanThisEvent, 0)

        self.assert_( hasattr(CalendarStore, 'CalRecurrenceYearly') )
        self.assert_( isinstance(CalendarStore.CalRecurrenceYearly, (int, long)) )
        self.assertEquals(CalendarStore.CalRecurrenceYearly, 3)

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        self.assert_( hasattr(CalendarStore, 'CalAlarmActionDisplay') )
        self.assert_( isinstance(CalendarStore.CalAlarmActionDisplay, unicode) )
        self.assert_( hasattr(CalendarStore, 'CalAttendeeStatusDeclined') )
        self.assert_( isinstance(CalendarStore.CalAttendeeStatusDeclined, unicode) )
        self.assert_( hasattr(CalendarStore, 'CalUpdatedRecordsKey') )
        self.assert_( isinstance(CalendarStore.CalUpdatedRecordsKey, unicode) )

        self.assert_( hasattr(CalendarStore, 'CalDefaultRecurrenceInterval') )
        self.assert_( isinstance(CalendarStore.CalDefaultRecurrenceInterval, (int, long)) )

if __name__ == "__main__":
    unittest.main()

