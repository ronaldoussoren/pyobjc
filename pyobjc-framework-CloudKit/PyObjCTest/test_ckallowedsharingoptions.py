from PyObjCTools.TestSupport import TestCase
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
