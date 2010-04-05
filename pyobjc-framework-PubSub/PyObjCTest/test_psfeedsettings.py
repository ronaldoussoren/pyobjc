
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSFeedSettings (TestCase):
    def testConstants(self):
        self.assertEqual(PSFeedSettingsIntervalDefault, 0.0)
        self.assertEqual(PSFeedSettingsIntervalNever, -1.0)
        self.assertEqual(PSFeedSettingsUnlimitedSize, 0)
        self.assertEqual(PSFeedSettingsAllTypes, None)

    def testMethods(self):
        self.assertResultIsBOOL(PSFeedSettings.refreshesInBackground)
        self.assertArgIsBOOL(PSFeedSettings.setRefreshesInBackground_, 0)

        self.assertResultIsBOOL(PSFeedSettings.downloadsEnclosures)
        self.assertArgIsBOOL(PSFeedSettings.setDownloadsEnclosures_, 0)

if __name__ == "__main__":
    main()
