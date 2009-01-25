
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSFeedSettings (TestCase):
    def testConstants(self):
        self.failUnlessEqual(PSFeedSettingsIntervalDefault, 0.0)
        self.failUnlessEqual(PSFeedSettingsIntervalNever, -1.0)
        self.failUnlessEqual(PSFeedSettingsUnlimitedSize, 0)
        self.failUnlessEqual(PSFeedSettingsAllTypes, None)

    def testMethods(self):
        self.failUnlessResultIsBOOL(PSFeedSettings.refreshesInBackground)
        self.failUnlessArgIsBOOL(PSFeedSettings.setRefreshesInBackground_, 0)

        self.failUnlessResultIsBOOL(PSFeedSettings.downloadsEnclosures)
        self.failUnlessArgIsBOOL(PSFeedSettings.setDownloadsEnclosures_, 0)

if __name__ == "__main__":
    main()
