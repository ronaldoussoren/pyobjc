
from PyObjCTools.TestSupport import *
from InstantMessage import *

class TestIMService (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(IMServiceStatusChangedNotification, unicode)
        self.failUnlessIsInstance(IMMyStatusChangedNotification, unicode)
        self.failUnlessIsInstance(IMPersonStatusChangedNotification, unicode)
        self.failUnlessIsInstance(IMPersonInfoChangedNotification, unicode)
        self.failUnlessIsInstance(IMStatusImagesChangedAppearanceNotification, unicode)

        self.failUnlessEqual(IMPersonStatusUnknown, 0)
        self.failUnlessEqual(IMPersonStatusOffline, 1)
        self.failUnlessEqual(IMPersonStatusIdle, 2)
        self.failUnlessEqual(IMPersonStatusAway, 3)
        self.failUnlessEqual(IMPersonStatusAvailable, 4)

        self.failUnlessIsInstance(IMPersonServiceNameKey, unicode)
        self.failUnlessIsInstance(IMPersonScreenNameKey, unicode)
        self.failUnlessIsInstance(IMPersonStatusKey, unicode)
        self.failUnlessIsInstance(IMPersonStatusMessageKey, unicode)
        self.failUnlessIsInstance(IMPersonIdleSinceKey, unicode)
        self.failUnlessIsInstance(IMPersonFirstNameKey, unicode)
        self.failUnlessIsInstance(IMPersonLastNameKey, unicode)
        self.failUnlessIsInstance(IMPersonEmailKey, unicode)
        self.failUnlessIsInstance(IMPersonPictureDataKey, unicode)
        self.failUnlessIsInstance(IMPersonAVBusyKey, unicode)
        self.failUnlessIsInstance(IMPersonCapabilitiesKey, unicode)
        self.failUnlessIsInstance(IMCapabilityText, unicode)
        self.failUnlessIsInstance(IMCapabilityDirectIM, unicode)
        self.failUnlessIsInstance(IMCapabilityFileTransfer, unicode)
        self.failUnlessIsInstance(IMCapabilityFileSharing, unicode)
        self.failUnlessIsInstance(IMCapabilityAudioConference, unicode)
        self.failUnlessIsInstance(IMCapabilityVideoConference, unicode)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessEqual(IMPersonStatusNoStatus, 5)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        v = IMComparePersonStatus(IMPersonStatusOffline, IMPersonStatusAway)
        self.failUnlessIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
