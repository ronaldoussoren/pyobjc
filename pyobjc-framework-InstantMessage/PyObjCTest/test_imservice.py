
from PyObjCTools.TestSupport import *
from InstantMessage import *

class TestIMService (TestCase):
    def testConstants(self):
        self.assertIsInstance(IMServiceStatusChangedNotification, unicode)
        self.assertIsInstance(IMMyStatusChangedNotification, unicode)
        self.assertIsInstance(IMPersonStatusChangedNotification, unicode)
        self.assertIsInstance(IMPersonInfoChangedNotification, unicode)
        self.assertIsInstance(IMStatusImagesChangedAppearanceNotification, unicode)

        self.assertEqual(IMPersonStatusUnknown, 0)
        self.assertEqual(IMPersonStatusOffline, 1)
        self.assertEqual(IMPersonStatusIdle, 2)
        self.assertEqual(IMPersonStatusAway, 3)
        self.assertEqual(IMPersonStatusAvailable, 4)

        self.assertIsInstance(IMPersonServiceNameKey, unicode)
        self.assertIsInstance(IMPersonScreenNameKey, unicode)
        self.assertIsInstance(IMPersonStatusKey, unicode)
        self.assertIsInstance(IMPersonStatusMessageKey, unicode)
        self.assertIsInstance(IMPersonIdleSinceKey, unicode)
        self.assertIsInstance(IMPersonFirstNameKey, unicode)
        self.assertIsInstance(IMPersonLastNameKey, unicode)
        self.assertIsInstance(IMPersonEmailKey, unicode)
        self.assertIsInstance(IMPersonPictureDataKey, unicode)
        self.assertIsInstance(IMPersonAVBusyKey, unicode)
        self.assertIsInstance(IMPersonCapabilitiesKey, unicode)
        self.assertIsInstance(IMCapabilityText, unicode)
        self.assertIsInstance(IMCapabilityDirectIM, unicode)
        self.assertIsInstance(IMCapabilityFileTransfer, unicode)
        self.assertIsInstance(IMCapabilityFileSharing, unicode)
        self.assertIsInstance(IMCapabilityAudioConference, unicode)
        self.assertIsInstance(IMCapabilityVideoConference, unicode)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(IMPersonStatusNoStatus, 5)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        v = IMComparePersonStatus(IMPersonStatusOffline, IMPersonStatusAway)
        self.assertIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
