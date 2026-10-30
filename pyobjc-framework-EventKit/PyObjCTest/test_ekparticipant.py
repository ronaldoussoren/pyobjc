from PyObjCTools.TestSupport import TestCase
import EventKit


class TestEKParticipant(TestCase):
    def test_enums(self):
        self.assertIsEnumType(EventKit.EKParticipantRole)
        self.assertEqual(EventKit.EKParticipantRoleUnknown, 0)
        self.assertEqual(EventKit.EKParticipantRoleRequired, 1)
        self.assertEqual(EventKit.EKParticipantRoleOptional, 2)
        self.assertEqual(EventKit.EKParticipantRoleChair, 3)
        self.assertEqual(EventKit.EKParticipantRoleNonParticipant, 4)

        self.assertIsEnumType(EventKit.EKParticipantStatus)
        self.assertEqual(EventKit.EKParticipantStatusUnknown, 0)
        self.assertEqual(EventKit.EKParticipantStatusPending, 1)
        self.assertEqual(EventKit.EKParticipantStatusAccepted, 2)
        self.assertEqual(EventKit.EKParticipantStatusDeclined, 3)
        self.assertEqual(EventKit.EKParticipantStatusTentative, 4)
        self.assertEqual(EventKit.EKParticipantStatusDelegated, 5)
        self.assertEqual(EventKit.EKParticipantStatusCompleted, 6)
        self.assertEqual(EventKit.EKParticipantStatusInProcess, 7)

        self.assertIsEnumType(EventKit.EKParticipantType)
        self.assertEqual(EventKit.EKParticipantTypeUnknown, 0)
        self.assertEqual(EventKit.EKParticipantTypePerson, 1)
        self.assertEqual(EventKit.EKParticipantTypeRoom, 2)
        self.assertEqual(EventKit.EKParticipantTypeResource, 3)
        self.assertEqual(EventKit.EKParticipantTypeGroup, 4)

    def test_methods(self):
        self.assertResultIsBOOL(EventKit.EKParticipant.isCurrentUser)
