import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSMetaData(TestCase):
    def testConstants(self):
        self.assertIsInstance(
            Foundation.NSMetadataQueryDidStartGatheringNotification, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataQueryGatheringProgressNotification, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataQueryDidFinishGatheringNotification, str
        )
        self.assertIsInstance(Foundation.NSMetadataQueryDidUpdateNotification, str)
        self.assertIsInstance(
            Foundation.NSMetadataQueryResultContentRelevanceAttribute, str
        )
        self.assertIsInstance(Foundation.NSMetadataQueryUserHomeScope, str)
        self.assertIsInstance(Foundation.NSMetadataQueryLocalComputerScope, str)
        self.assertIsInstance(Foundation.NSMetadataQueryNetworkScope, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(Foundation.NSMetadataQueryLocalDocumentsScope, str)
        self.assertIsInstance(Foundation.NSMetadataQueryUbiquitousDocumentsScope, str)
        self.assertIsInstance(Foundation.NSMetadataQueryUbiquitousDataScope, str)

        self.assertIsInstance(Foundation.NSMetadataItemFSNameKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemDisplayNameKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemURLKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemPathKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFSSizeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFSCreationDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFSContentChangeDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemIsUbiquitousKey, str)
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemHasUnresolvedConflictsKey, str
        )
        self.assertIsInstance(Foundation.NSMetadataUbiquitousItemIsDownloadedKey, str)
        self.assertIsInstance(Foundation.NSMetadataUbiquitousItemIsDownloadingKey, str)
        self.assertIsInstance(Foundation.NSMetadataUbiquitousItemIsUploadedKey, str)
        self.assertIsInstance(Foundation.NSMetadataUbiquitousItemIsUploadingKey, str)
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemPercentDownloadedKey, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemPercentUploadedKey, str
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Foundation.NSMetadataQueryUpdateAddedItemsKey, str)
        self.assertIsInstance(Foundation.NSMetadataQueryUpdateChangedItemsKey, str)
        self.assertIsInstance(Foundation.NSMetadataQueryUpdateRemovedItemsKey, str)
        self.assertIsInstance(Foundation.NSMetadataQueryIndexedLocalComputerScope, str)
        self.assertIsInstance(Foundation.NSMetadataQueryIndexedNetworkScope, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            Foundation.NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope, str
        )

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSMetadataQuery.startQuery)
        self.assertResultIsBOOL(Foundation.NSMetadataQuery.isStarted)
        self.assertResultIsBOOL(Foundation.NSMetadataQuery.isGathering)
        self.assertResultIsBOOL(Foundation.NSMetadataQuery.isStopped)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBlock(
            Foundation.NSMetadataQuery.enumerateResultsUsingBlock_,
            0,
            b"v@" + objc._C_NSUInteger + b"o^Z",
        )
        self.assertArgIsBlock(
            Foundation.NSMetadataQuery.enumerateResultsWithOptions_usingBlock_,
            1,
            b"v@" + objc._C_NSUInteger + b"o^Z",
        )

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        objc.protocolNamed("NSMetadataQueryDelegate")
