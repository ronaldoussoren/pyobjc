import PubSub
from PyObjCTools.TestSupport import TestCase


class TestPSFeedSettings(TestCase):
    def testConstants(self):
        self.assertEqual(PubSub.PSFeedSettingsIntervalDefault, 0.0)
        self.assertEqual(PubSub.PSFeedSettingsIntervalNever, -1.0)
        self.assertEqual(PubSub.PSFeedSettingsUnlimitedSize, 0)
        self.assertEqual(PubSub.PSFeedSettingsAllTypes, None)

    def testMethods(self):
        self.assertResultIsBOOL(PubSub.PSFeedSettings.refreshesInBackground)
        self.assertArgIsBOOL(PubSub.PSFeedSettings.setRefreshesInBackground_, 0)

        self.assertResultIsBOOL(PubSub.PSFeedSettings.downloadsEnclosures)
        self.assertArgIsBOOL(PubSub.PSFeedSettings.setDownloadsEnclosures_, 0)
