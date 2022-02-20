from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKShareParticipant(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CloudKit.CKShareParticipantAcceptanceStatus)
        self.assertIsEnumType(CloudKit.CKShareParticipantPermission)
        self.assertIsEnumType(CloudKit.CKShareParticipantRole)
        self.assertIsEnumType(CloudKit.CKShareParticipantType)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertEqual(CloudKit.CKShareParticipantAcceptanceStatusUnknown, 0)
        self.assertEqual(CloudKit.CKShareParticipantAcceptanceStatusPending, 1)
        self.assertEqual(CloudKit.CKShareParticipantAcceptanceStatusAccepted, 2)
        self.assertEqual(CloudKit.CKShareParticipantAcceptanceStatusRemoved, 3)
        self.assertEqual(CloudKit.CKShareParticipantPermissionUnknown, 0)
        self.assertEqual(CloudKit.CKShareParticipantPermissionNone, 1)
        self.assertEqual(CloudKit.CKShareParticipantPermissionReadOnly, 2)
        self.assertEqual(CloudKit.CKShareParticipantPermissionReadWrite, 3)
        self.assertEqual(CloudKit.CKShareParticipantTypeUnknown, 0)
        self.assertEqual(CloudKit.CKShareParticipantTypeOwner, 1)
        self.assertEqual(CloudKit.CKShareParticipantTypePrivateUser, 3)
        self.assertEqual(CloudKit.CKShareParticipantTypePublicUser, 4)

        self.assertEqual(CloudKit.CKShareParticipantRoleUnknown, 0)
        self.assertEqual(CloudKit.CKShareParticipantRoleOwner, 1)
        self.assertEqual(CloudKit.CKShareParticipantRolePrivateUser, 3)
        self.assertEqual(CloudKit.CKShareParticipantRolePublicUser, 4)
