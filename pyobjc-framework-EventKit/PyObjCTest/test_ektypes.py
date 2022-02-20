from PyObjCTools.TestSupport import TestCase, min_os_level
import EventKit


class TestEKTypes(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(EventKit.EKAlarmProximity)
        self.assertIsEnumType(EventKit.EKAlarmType)
        self.assertIsEnumType(EventKit.EKAuthorizationStatus)
        self.assertIsEnumType(EventKit.EKCalendarEventAvailabilityMask)
        self.assertIsEnumType(EventKit.EKCalendarType)
        self.assertIsEnumType(EventKit.EKEntityMask)
        self.assertIsEnumType(EventKit.EKEntityType)
        self.assertIsEnumType(EventKit.EKParticipantRole)
        self.assertIsEnumType(EventKit.EKParticipantScheduleStatus)
        self.assertIsEnumType(EventKit.EKParticipantStatus)
        self.assertIsEnumType(EventKit.EKParticipantType)
        self.assertIsEnumType(EventKit.EKRecurrenceFrequency)
        self.assertIsEnumType(EventKit.EKReminderPriority)
        self.assertIsEnumType(EventKit.EKSourceType)
        self.assertIsEnumType(EventKit.EKWeekday)

    @min_os_level("10.8")
    def testConstacts(self):
        self.assertEqual(EventKit.EKAlarmProximityLeave, 2)

        self.assertEqual(EventKit.EKAuthorizationStatusNotDetermined, 0)
        self.assertEqual(EventKit.EKAuthorizationStatusRestricted, 1)
        self.assertEqual(EventKit.EKAuthorizationStatusDenied, 2)
        self.assertEqual(EventKit.EKAuthorizationStatusAuthorized, 3)

        self.assertEqual(EventKit.EKWeekdaySunday, 1)
        self.assertEqual(EventKit.EKWeekdayMonday, 2)
        self.assertEqual(EventKit.EKWeekdayTuesday, 3)
        self.assertEqual(EventKit.EKWeekdayWednesday, 4)
        self.assertEqual(EventKit.EKWeekdayThursday, 5)
        self.assertEqual(EventKit.EKWeekdayFriday, 6)
        self.assertEqual(EventKit.EKWeekdaySaturday, 7)

        self.assertEqual(EventKit.EKSunday, EventKit.EKWeekdaySunday)
        self.assertEqual(EventKit.EKMonday, EventKit.EKWeekdayMonday)
        self.assertEqual(EventKit.EKTuesday, EventKit.EKWeekdayTuesday)
        self.assertEqual(EventKit.EKWednesday, EventKit.EKWeekdayWednesday)
        self.assertEqual(EventKit.EKThursday, EventKit.EKWeekdayThursday)
        self.assertEqual(EventKit.EKFriday, EventKit.EKWeekdayFriday)
        self.assertEqual(EventKit.EKSaturday, EventKit.EKWeekdaySaturday)

        self.assertEqual(EventKit.EKRecurrenceFrequencyDaily, 0)
        self.assertEqual(EventKit.EKRecurrenceFrequencyWeekly, 1)
        self.assertEqual(EventKit.EKRecurrenceFrequencyMonthly, 2)
        self.assertEqual(EventKit.EKRecurrenceFrequencyYearly, 3)

        self.assertEqual(EventKit.EKParticipantTypeUnknown, 0)
        self.assertEqual(EventKit.EKParticipantTypePerson, 1)
        self.assertEqual(EventKit.EKParticipantTypeRoom, 2)
        self.assertEqual(EventKit.EKParticipantTypeResource, 3)
        self.assertEqual(EventKit.EKParticipantTypeGroup, 4)

        self.assertEqual(EventKit.EKParticipantRoleUnknown, 0)
        self.assertEqual(EventKit.EKParticipantRoleRequired, 1)
        self.assertEqual(EventKit.EKParticipantRoleOptional, 2)
        self.assertEqual(EventKit.EKParticipantRoleChair, 3)
        self.assertEqual(EventKit.EKParticipantRoleNonParticipant, 4)

        self.assertEqual(EventKit.EKParticipantScheduleStatusNone, 0)
        self.assertEqual(EventKit.EKParticipantScheduleStatusPending, 1)
        self.assertEqual(EventKit.EKParticipantScheduleStatusSent, 2)
        self.assertEqual(EventKit.EKParticipantScheduleStatusDelivered, 3)
        self.assertEqual(EventKit.EKParticipantScheduleStatusRecipientNotRecognized, 4)
        self.assertEqual(EventKit.EKParticipantScheduleStatusNoPrivileges, 5)
        self.assertEqual(EventKit.EKParticipantScheduleStatusDeliveryFailed, 6)
        self.assertEqual(EventKit.EKParticipantScheduleStatusCannotDeliver, 7)
        self.assertEqual(EventKit.EKParticipantScheduleStatusRecipientNotAllowed, 8)

        self.assertEqual(EventKit.EKParticipantStatusUnknown, 0)
        self.assertEqual(EventKit.EKParticipantStatusPending, 1)
        self.assertEqual(EventKit.EKParticipantStatusAccepted, 2)
        self.assertEqual(EventKit.EKParticipantStatusDeclined, 3)
        self.assertEqual(EventKit.EKParticipantStatusTentative, 4)
        self.assertEqual(EventKit.EKParticipantStatusDelegated, 5)
        self.assertEqual(EventKit.EKParticipantStatusCompleted, 6)
        self.assertEqual(EventKit.EKParticipantStatusInProcess, 7)

        self.assertEqual(EventKit.EKCalendarTypeLocal, 0)
        self.assertEqual(EventKit.EKCalendarTypeCalDAV, 1)
        self.assertEqual(EventKit.EKCalendarTypeExchange, 2)
        self.assertEqual(EventKit.EKCalendarTypeSubscription, 3)
        self.assertEqual(EventKit.EKCalendarTypeBirthday, 4)

        self.assertEqual(EventKit.EKCalendarEventAvailabilityNone, 0)
        self.assertEqual(EventKit.EKCalendarEventAvailabilityBusy, (1 << 0))
        self.assertEqual(EventKit.EKCalendarEventAvailabilityFree, (1 << 1))
        self.assertEqual(EventKit.EKCalendarEventAvailabilityTentative, (1 << 2))
        self.assertEqual(EventKit.EKCalendarEventAvailabilityUnavailable, (1 << 3))

        self.assertEqual(EventKit.EKSourceTypeLocal, 0)
        self.assertEqual(EventKit.EKSourceTypeExchange, 1)
        self.assertEqual(EventKit.EKSourceTypeCalDAV, 2)
        self.assertEqual(EventKit.EKSourceTypeMobileMe, 3)
        self.assertEqual(EventKit.EKSourceTypeSubscribed, 4)
        self.assertEqual(EventKit.EKSourceTypeBirthdays, 5)

        self.assertEqual(EventKit.EKEntityTypeEvent, 0)
        self.assertEqual(EventKit.EKEntityTypeReminder, 1)

        self.assertEqual(EventKit.EKEntityMaskEvent, (1 << EventKit.EKEntityTypeEvent))
        self.assertEqual(
            EventKit.EKEntityMaskReminder, (1 << EventKit.EKEntityTypeReminder)
        )

        self.assertEqual(EventKit.EKAlarmProximityNone, 0)
        self.assertEqual(EventKit.EKAlarmProximityEnter, 1)
        self.assertEqual(EventKit.EKAlarmProximityLeave, 2)

        self.assertEqual(EventKit.EKAlarmTypeDisplay, 0)
        self.assertEqual(EventKit.EKAlarmTypeAudio, 1)
        self.assertEqual(EventKit.EKAlarmTypeProcedure, 2)
        self.assertEqual(EventKit.EKAlarmTypeEmail, 3)

        self.assertEqual(EventKit.EKReminderPriorityNone, 0)
        self.assertEqual(EventKit.EKReminderPriorityHigh, 1)
        self.assertEqual(EventKit.EKReminderPriorityMedium, 5)
        self.assertEqual(EventKit.EKReminderPriorityLow, 9)
