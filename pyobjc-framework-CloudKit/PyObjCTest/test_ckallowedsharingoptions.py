from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKAllowedSharingOptions(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CloudKit.CKSharingParticipantAccessOption)
        self.assertEqual(
            CloudKit.CKSharingParticipantAccessOptionAnyoneWithLink, 1 << 0
        )
        self.assertEqual(
            CloudKit.CKSharingParticipantAccessOptionSpecifiedRecipientsOnly, 1 << 1
        )
        self.assertEqual(
            CloudKit.CKSharingParticipantAccessOptionAny,
            CloudKit.CKSharingParticipantAccessOptionAnyoneWithLink
            | CloudKit.CKSharingParticipantAccessOptionSpecifiedRecipientsOnly,
        )

        self.assertIsEnumType(CloudKit.CKSharingParticipantPermissionOption)
        self.assertEqual(CloudKit.CKSharingParticipantPermissionOptionReadOnly, 1 << 0)
        self.assertEqual(CloudKit.CKSharingParticipantPermissionOptionReadWrite, 1 << 1)
        self.assertEqual(
            CloudKit.CKSharingParticipantPermissionOptionAny,
            CloudKit.CKSharingParticipantPermissionOptionReadOnly
            | CloudKit.CKSharingParticipantPermissionOptionReadWrite,
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(
            CloudKit.CKAllowedSharingOptions.allowsParticipantsToInviteOthers
        )
        self.assertArgIsBOOL(
            CloudKit.CKAllowedSharingOptions.setAllowsParticipantsToInviteOthers_, 0
        )

        self.assertResultIsBOOL(CloudKit.CKAllowedSharingOptions.allowsAccessRequests)
        self.assertArgIsBOOL(
            CloudKit.CKAllowedSharingOptions.setAllowsAccessRequests_, 0
        )
