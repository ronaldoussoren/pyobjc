from Foundation import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str

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

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(NSMetadataQueryLocalDocumentsScope, unicode)
        self.assertIsInstance(NSMetadataQueryUbiquitousDocumentsScope, unicode)
        self.assertIsInstance(NSMetadataQueryUbiquitousDataScope, unicode)

        self.assertIsInstance(NSMetadataItemFSNameKey, unicode)
        self.assertIsInstance(NSMetadataItemDisplayNameKey, unicode)
        self.assertIsInstance(NSMetadataItemURLKey, unicode)
        self.assertIsInstance(NSMetadataItemPathKey, unicode)
        self.assertIsInstance(NSMetadataItemFSSizeKey, unicode)
        self.assertIsInstance(NSMetadataItemFSCreationDateKey, unicode)
        self.assertIsInstance(NSMetadataItemFSContentChangeDateKey, unicode)
        self.assertIsInstance(NSMetadataItemIsUbiquitousKey, unicode)
        self.assertIsInstance(NSMetadataUbiquitousItemHasUnresolvedConflictsKey, unicode)
        self.assertIsInstance(NSMetadataUbiquitousItemIsDownloadedKey, unicode)
        self.assertIsInstance(NSMetadataUbiquitousItemIsDownloadingKey, unicode)
        self.assertIsInstance(NSMetadataUbiquitousItemIsUploadedKey, unicode)
        self.assertIsInstance(NSMetadataUbiquitousItemIsUploadingKey, unicode)
        self.assertIsInstance(NSMetadataUbiquitousItemPercentDownloadedKey, unicode)
        self.assertIsInstance(NSMetadataUbiquitousItemPercentUploadedKey, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSMetadataQuery.startQuery)
        self.assertResultIsBOOL(NSMetadataQuery.isStarted)
        self.assertResultIsBOOL(NSMetadataQuery.isGathering)
        self.assertResultIsBOOL(NSMetadataQuery.isStopped)


if __name__ == "__main__":
    main()
