from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSMetaData (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSMetadataQueryDidStartGatheringNotification, unicode)
        self.assertIsInstance(NSMetadataQueryGatheringProgressNotification, unicode)
        self.assertIsInstance(NSMetadataQueryDidFinishGatheringNotification, unicode)
        self.assertIsInstance(NSMetadataQueryDidUpdateNotification, unicode)
        self.assertIsInstance(NSMetadataQueryResultContentRelevanceAttribute, unicode)
        self.assertIsInstance(NSMetadataQueryUserHomeScope, unicode)
        self.assertIsInstance(NSMetadataQueryLocalComputerScope, unicode)
        self.assertIsInstance(NSMetadataQueryNetworkScope, unicode)
    def testMethods(self):
        self.assertResultIsBOOL(NSMetadataQuery.startQuery)
        self.assertResultIsBOOL(NSMetadataQuery.isStarted)
        self.assertResultIsBOOL(NSMetadataQuery.isGathering)
        self.assertResultIsBOOL(NSMetadataQuery.isStopped)


if __name__ == "__main__":
    main()
