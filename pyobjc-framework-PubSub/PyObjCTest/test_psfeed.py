
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSFeed (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(PSErrorDomain, unicode)

        self.failUnlessEqual(PSInternalError, 1)
        self.failUnlessEqual(PSNotAFeedError, 2)

        self.failUnlessEqual(PSUnknownFormat, 0)
        self.failUnlessEqual(PSRSSFormat, 1)
        self.failUnlessEqual(PSAtomFormat, 2)

        self.failUnlessIsInstance(PSFeedRefreshingNotification, unicode)
        self.failUnlessIsInstance(PSFeedEntriesChangedNotification, unicode)
        self.failUnlessIsInstance(PSFeedAddedEntriesKey, unicode)
        self.failUnlessIsInstance(PSFeedRemovedEntriesKey, unicode)
        self.failUnlessIsInstance(PSFeedUpdatedEntriesKey, unicode)
        self.failUnlessIsInstance(PSFeedDidChangeEntryFlagsKey, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(PSFeed.isRefreshing)
        self.failUnlessResultIsBOOL(PSFeed.refresh_)
        self.failUnlessArgIsOut(PSFeed.refresh_, 0)


if __name__ == "__main__":
    main()
