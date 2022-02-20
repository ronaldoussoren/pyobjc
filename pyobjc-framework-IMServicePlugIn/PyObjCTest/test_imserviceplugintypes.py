import IMServicePlugIn
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestIMServicePlugInChatRoomSupport(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(IMServicePlugIn.IMGroupListPermissions)
        self.assertIsEnumType(IMServicePlugIn.IMHandleAuthorizationStatus)
        self.assertIsEnumType(IMServicePlugIn.IMHandleAvailability)
        self.assertIsEnumType(IMServicePlugIn.IMSessionAvailability)

    @expectedFailure  # Definitions are likely part of the host application
    def testConstantsStr(self):
        self.assertIsInstance(IMServicePlugIn.IMAccountSettingServerHost, str)
        self.assertIsInstance(IMServicePlugIn.IMAccountSettingServerPort, str)
        self.assertIsInstance(IMServicePlugIn.IMAccountSettingLoginHandle, str)
        self.assertIsInstance(IMServicePlugIn.IMAccountSettingPassword, str)
        self.assertIsInstance(IMServicePlugIn.IMAccountSettingUsesSSL, str)

        self.assertIsInstance(IMServicePlugIn.IMSessionPropertyAvailability, str)
        self.assertIsInstance(IMServicePlugIn.IMSessionPropertyStatusMessage, str)
        self.assertIsInstance(IMServicePlugIn.IMSessionPropertyPictureData, str)
        self.assertIsInstance(IMServicePlugIn.IMSessionPropertyIdleDate, str)
        self.assertIsInstance(IMServicePlugIn.IMSessionPropertyIsInvisible, str)

        self.assertIsInstance(IMServicePlugIn.IMGroupListDefaultGroup, str)
        self.assertIsInstance(IMServicePlugIn.IMGroupListNameKey, str)
        self.assertIsInstance(IMServicePlugIn.IMGroupListPermissionsKey, str)
        self.assertIsInstance(IMServicePlugIn.IMGroupListHandlesKey, str)

        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyAvailability, str)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyStatusMessage, str)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyAuthorizationStatus, str)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyIdleDate, str)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyAlias, str)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyFirstName, str)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyLastName, str)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyEmailAddress, str)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyPictureIdentifier, str)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyPictureData, str)

        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyCapabilities, str)
        self.assertIsInstance(IMServicePlugIn.IMHandleCapabilityMessaging, str)
        self.assertIsInstance(IMServicePlugIn.IMHandleCapabilityOfflineMessaging, str)
        self.assertIsInstance(IMServicePlugIn.IMHandleCapabilityChatRoom, str)
        self.assertIsInstance(IMServicePlugIn.IMHandleCapabilityHandlePicture, str)
        self.assertIsInstance(IMServicePlugIn.IMHandleCapabilityFileTransfer, str)

        self.assertIsInstance(IMServicePlugIn.IMAttributeFontFamily, str)
        self.assertIsInstance(IMServicePlugIn.IMAttributeFontSize, str)
        self.assertIsInstance(IMServicePlugIn.IMAttributeItalic, str)
        self.assertIsInstance(IMServicePlugIn.IMAttributeBold, str)
        self.assertIsInstance(IMServicePlugIn.IMAttributeUnderline, str)
        self.assertIsInstance(IMServicePlugIn.IMAttributeStrikethrough, str)
        self.assertIsInstance(IMServicePlugIn.IMAttributeLink, str)
        self.assertIsInstance(IMServicePlugIn.IMAttributePreformatted, str)
        self.assertIsInstance(IMServicePlugIn.IMAttributeBaseWritingDirection, str)

        self.assertIsInstance(IMServicePlugIn.IMAttributeForegroundColor, str)
        self.assertIsInstance(IMServicePlugIn.IMAttributeBackgroundColor, str)
        self.assertIsInstance(IMServicePlugIn.IMAttributeMessageBackgroundColor, str)

    def testConstantsNum(self):
        self.assertEqual(IMServicePlugIn.IMSessionAvailabilityAway, 0)
        self.assertEqual(IMServicePlugIn.IMSessionAvailabilityAvailable, 1)

        self.assertEqual(IMServicePlugIn.IMGroupListCanReorderGroup, (1 << 0))
        self.assertEqual(IMServicePlugIn.IMGroupListCanRenameGroup, (1 << 1))
        self.assertEqual(IMServicePlugIn.IMGroupListCanAddNewMembers, (1 << 2))
        self.assertEqual(IMServicePlugIn.IMGroupListCanRemoveMembers, (1 << 3))
        self.assertEqual(IMServicePlugIn.IMGroupListCanReorderMembers, (1 << 4))

        self.assertEqual(IMServicePlugIn.IMHandleAvailabilityUnknown, -2)
        self.assertEqual(IMServicePlugIn.IMHandleAvailabilityOffline, -1)
        self.assertEqual(IMServicePlugIn.IMHandleAvailabilityAway, 0)
        self.assertEqual(IMServicePlugIn.IMHandleAvailabilityAvailable, 1)

        self.assertEqual(IMServicePlugIn.IMHandleAuthorizationStatusAccepted, 0)
        self.assertEqual(IMServicePlugIn.IMHandleAuthorizationStatusPending, 1)
        self.assertEqual(IMServicePlugIn.IMHandleAuthorizationStatusDeclined, 2)
