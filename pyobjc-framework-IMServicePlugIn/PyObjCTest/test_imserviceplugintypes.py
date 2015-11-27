from PyObjCTools.TestSupport import *
import IMServicePlugIn
import objc

class TestIMServicePlugInChatRoomSupport (TestCase):
    @expectedFailure # Definitions are likely part of the host application
    def testConstantsStr(self):
        self.assertIsInstance(IMServicePlugIn.IMAccountSettingServerHost, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAccountSettingServerPort, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAccountSettingLoginHandle, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAccountSettingPassword, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAccountSettingUsesSSL, unicode)

        self.assertIsInstance(IMServicePlugIn.IMSessionPropertyAvailability, unicode)
        self.assertIsInstance(IMServicePlugIn.IMSessionPropertyStatusMessage, unicode)
        self.assertIsInstance(IMServicePlugIn.IMSessionPropertyPictureData, unicode)
        self.assertIsInstance(IMServicePlugIn.IMSessionPropertyIdleDate, unicode)
        self.assertIsInstance(IMServicePlugIn.IMSessionPropertyIsInvisible, unicode)

        self.assertIsInstance(IMServicePlugIn.IMGroupListDefaultGroup, unicode)
        self.assertIsInstance(IMServicePlugIn.IMGroupListNameKey, unicode)
        self.assertIsInstance(IMServicePlugIn.IMGroupListPermissionsKey, unicode)
        self.assertIsInstance(IMServicePlugIn.IMGroupListHandlesKey, unicode)

        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyAvailability, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyStatusMessage, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyAuthorizationStatus, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyIdleDate, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyAlias, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyFirstName, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyLastName, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyEmailAddress, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyPictureIdentifier, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyPictureData, unicode)

        self.assertIsInstance(IMServicePlugIn.IMHandlePropertyCapabilities, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandleCapabilityMessaging, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandleCapabilityOfflineMessaging, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandleCapabilityChatRoom, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandleCapabilityHandlePicture, unicode)
        self.assertIsInstance(IMServicePlugIn.IMHandleCapabilityFileTransfer, unicode)

        self.assertIsInstance(IMServicePlugIn.IMAttributeFontFamily, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAttributeFontSize, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAttributeItalic, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAttributeBold, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAttributeUnderline, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAttributeStrikethrough, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAttributeLink, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAttributePreformatted, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAttributeBaseWritingDirection, unicode)

        self.assertIsInstance(IMServicePlugIn.IMAttributeForegroundColor, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAttributeBackgroundColor, unicode)
        self.assertIsInstance(IMServicePlugIn.IMAttributeMessageBackgroundColor, unicode)

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

if __name__ == "__main__":
    main()
