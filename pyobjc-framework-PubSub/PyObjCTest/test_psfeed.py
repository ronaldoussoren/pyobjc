
from PyObjCTools.TestSupport import *
from PubSub import *

try:
    unicode
except NameError:
    unicode = str

class TestPSFeed (TestCase):
    def testConstants(self):
        self.assertIsInstance(PSErrorDomain, unicode)

        self.assertEqual(PSInternalError, 1)
        self.assertEqual(PSNotAFeedError, 2)

        self.assertEqual(PSUnknownFormat, 0)
        self.assertEqual(PSRSSFormat, 1)
        self.assertEqual(PSAtomFormat, 2)

        self.assertIsInstance(PSFeedRefreshingNotification, unicode)
        self.assertIsInstance(PSFeedEntriesChangedNotification, unicode)
        self.assertIsInstance(PSFeedAddedEntriesKey, unicode)
        self.assertIsInstance(PSFeedRemovedEntriesKey, unicode)
        self.assertIsInstance(PSFeedUpdatedEntriesKey, unicode)
        self.assertIsInstance(PSFeedDidChangeEntryFlagsKey, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(PSFeed.isRefreshing)
        self.assertResultIsBOOL(PSFeed.refresh_)
        self.assertArgIsOut(PSFeed.refresh_, 0)


if __name__ == "__main__":
    main()
