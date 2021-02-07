import PubSub
from PyObjCTools.TestSupport import TestCase


class TestPSFeed(TestCase):
    def testConstants(self):
        self.assertIsInstance(PubSub.PSErrorDomain, str)

        self.assertEqual(PubSub.PSInternalError, 1)
        self.assertEqual(PubSub.PSNotAFeedError, 2)

        self.assertEqual(PubSub.PSUnknownFormat, 0)
        self.assertEqual(PubSub.PSRSSFormat, 1)
        self.assertEqual(PubSub.PSAtomFormat, 2)

        self.assertIsInstance(PubSub.PSFeedRefreshingNotification, str)
        self.assertIsInstance(PubSub.PSFeedEntriesChangedNotification, str)
        self.assertIsInstance(PubSub.PSFeedAddedEntriesKey, str)
        self.assertIsInstance(PubSub.PSFeedRemovedEntriesKey, str)
        self.assertIsInstance(PubSub.PSFeedUpdatedEntriesKey, str)
        self.assertIsInstance(PubSub.PSFeedDidChangeEntryFlagsKey, str)

    def testMethods(self):
        self.assertResultIsBOOL(PubSub.PSFeed.isRefreshing)
        self.assertResultIsBOOL(PubSub.PSFeed.refresh_)
        self.assertArgIsOut(PubSub.PSFeed.refresh_, 0)
        self.assertArgIsBOOL(PubSub.PSFeed.XMLRepresentationWithEntries_, 0)
