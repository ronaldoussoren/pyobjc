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

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(NSMetadataQueryUpdateAddedItemsKey, unicode)
        self.assertIsInstance(NSMetadataQueryUpdateChangedItemsKey, unicode)
        self.assertIsInstance(NSMetadataQueryUpdateRemovedItemsKey, unicode)
        self.assertIsInstance(NSMetadataQueryIndexedLocalComputerScope, unicode)
        self.assertIsInstance(NSMetadataQueryIndexedNetworkScope, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSMetadataQuery.startQuery)
        self.assertResultIsBOOL(NSMetadataQuery.isStarted)
        self.assertResultIsBOOL(NSMetadataQuery.isGathering)
        self.assertResultIsBOOL(NSMetadataQuery.isStopped)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsBlock(NSMetadataQuery.enumerateResultsUsingBlock_, 0, b'v@' + objc._C_NSUInteger + b'o^Z')
        self.assertArgIsBlock(NSMetadataQuery.enumerateResultsWithOptions_usingBlock_, 1, b'v@' + objc._C_NSUInteger + b'o^Z')

    @min_sdk_level('10.10')
    def testProtocolObjects(self):
        objc.protocolNamed('NSMetadataQueryDelegate')

if __name__ == "__main__":
    main()
