import InstantMessage
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestIMService(TestCase):
    def testConstants(self):
        self.assertIsInstance(InstantMessage.IMServiceStatusChangedNotification, str)
        self.assertIsInstance(InstantMessage.IMMyStatusChangedNotification, str)
        self.assertIsInstance(InstantMessage.IMPersonStatusChangedNotification, str)
        self.assertIsInstance(InstantMessage.IMPersonInfoChangedNotification, str)
        self.assertIsInstance(
            InstantMessage.IMStatusImagesChangedAppearanceNotification, str
        )

        self.assertEqual(InstantMessage.IMPersonStatusUnknown, 0)
        self.assertEqual(InstantMessage.IMPersonStatusOffline, 1)
        self.assertEqual(InstantMessage.IMPersonStatusIdle, 2)
        self.assertEqual(InstantMessage.IMPersonStatusAway, 3)
        self.assertEqual(InstantMessage.IMPersonStatusAvailable, 4)
        self.assertEqual(InstantMessage.IMPersonStatusNoStatus, 5)

        self.assertEqual(InstantMessage.IMServiceStatusLoggedOut, 0)
        self.assertEqual(InstantMessage.IMServiceStatusDisconnected, 1)
        self.assertEqual(InstantMessage.IMServiceStatusLoggingOut, 2)
        self.assertEqual(InstantMessage.IMServiceStatusLoggingIn, 3)
        self.assertEqual(InstantMessage.IMServiceStatusLoggedIn, 4)

        self.assertIsInstance(InstantMessage.IMPersonServiceNameKey, str)
        self.assertIsInstance(InstantMessage.IMPersonScreenNameKey, str)
        self.assertIsInstance(InstantMessage.IMPersonStatusKey, str)
        self.assertIsInstance(InstantMessage.IMPersonStatusMessageKey, str)
        self.assertIsInstance(InstantMessage.IMPersonIdleSinceKey, str)
        self.assertIsInstance(InstantMessage.IMPersonFirstNameKey, str)
        self.assertIsInstance(InstantMessage.IMPersonLastNameKey, str)
        self.assertIsInstance(InstantMessage.IMPersonEmailKey, str)
        self.assertIsInstance(InstantMessage.IMPersonPictureDataKey, str)
        self.assertIsInstance(InstantMessage.IMPersonAVBusyKey, str)
        self.assertIsInstance(InstantMessage.IMPersonCapabilitiesKey, str)
        self.assertIsInstance(InstantMessage.IMCapabilityText, str)
        self.assertIsInstance(InstantMessage.IMCapabilityDirectIM, str)
        self.assertIsInstance(InstantMessage.IMCapabilityFileTransfer, str)
        self.assertIsInstance(InstantMessage.IMCapabilityFileSharing, str)
        self.assertIsInstance(InstantMessage.IMCapabilityAudioConference, str)
        self.assertIsInstance(InstantMessage.IMCapabilityVideoConference, str)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        v = InstantMessage.IMComparePersonStatus(
            InstantMessage.IMPersonStatusOffline, InstantMessage.IMPersonStatusAway
        )
        self.assertIsInstance(v, int)
