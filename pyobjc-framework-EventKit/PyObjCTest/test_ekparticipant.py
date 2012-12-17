import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2**32:
    import EventKit

    class TestEKParticipant (TestCase):
        @min_os_level('10.8')
        def testBasic(self):
            self.assertTrue(hasattr(EventKit, "EKParticipant"))

        @min_os_level('10.8')
        def testConstants10_8(self):
            self.assertEqual(EventKit.EKParticipantRoleUnknown, 0)
            self.assertEqual(EventKit.EKParticipantRoleRequired, 1)
            self.assertEqual(EventKit.EKParticipantRoleOptional, 2)
            self.assertEqual(EventKit.EKParticipantRoleChair, 3)
            self.assertEqual(EventKit.EKParticipantRoleNonParticipant, 4)

            self.assertEqual(EventKit.EKParticipantStatusUnknown, 0)
            self.assertEqual(EventKit.EKParticipantStatusPending, 1)
            self.assertEqual(EventKit.EKParticipantStatusAccepted, 2)
            self.assertEqual(EventKit.EKParticipantStatusDeclined, 3)
            self.assertEqual(EventKit.EKParticipantStatusTentative, 4)
            self.assertEqual(EventKit.EKParticipantStatusDelegated, 5)
            self.assertEqual(EventKit.EKParticipantStatusCompleted, 6)
            self.assertEqual(EventKit.EKParticipantStatusInProcess, 7)

            self.assertEqual(EventKit.EKParticipantTypeUnknown, 0)
            self.assertEqual(EventKit.EKParticipantTypePerson, 1)
            self.assertEqual(EventKit.EKParticipantTypeRoom, 2)
            self.assertEqual(EventKit.EKParticipantTypeResource, 3)
            self.assertEqual(EventKit.EKParticipantTypeGroup, 4)


if __name__ == '__main__':
    main()
