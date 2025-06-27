from PyObjCTools.TestSupport import TestCase, min_os_level


import CoreSpotlight


class TestCSSearchableIndexHelper(CoreSpotlight.NSObject):
    def searchableIndex_reindexAllSearchableItemsWithAcknowledgementHandler_(
        self, i, h
    ):
        pass

    def searchableIndex_reindexSearchableItemsWithIdentifiers_acknowledgementHandler_(
        self, i, i2, a
    ):
        pass

    def dataForSearchableIndex_itemIdentifier_typeIdentifier_error_(self, i, ii, ti, e):
        pass

    def fileURLForSearchableIndex_itemIdentifier_typeIdentifier_inPlace_error_(
        self, i, ii, ti, ip, e
    ):
        pass

    def searchableItemsForIdentifiers_searchableItemsHandler_(self, a, b):
        pass


class TestCSSearchableIndex(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreSpotlight.CSIndexErrorCode)

    def testConstants(self):
        self.assertEqual(CoreSpotlight.CSIndexErrorCodeUnknownError, -1)
        self.assertEqual(CoreSpotlight.CSIndexErrorCodeIndexUnavailableError, -1000)
        self.assertEqual(CoreSpotlight.CSIndexErrorCodeInvalidItemError, -1001)
        self.assertEqual(CoreSpotlight.CSIndexErrorCodeInvalidClientStateError, -1002)
        self.assertEqual(CoreSpotlight.CSIndexErrorCodeRemoteConnectionError, -1003)
        self.assertEqual(CoreSpotlight.CSIndexErrorCodeQuotaExceeded, -1004)
        self.assertEqual(CoreSpotlight.CSIndexErrorCodeIndexingUnsupported, -1005)
        self.assertEqual(CoreSpotlight.CSIndexErrorCodeMismatchedClientState, -1006)

    def testMethods(self):
        self.assertResultIsBOOL(CoreSpotlight.CSSearchableIndex.isIndexingAvailable)
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchableIndex.indexSearchableItems_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchableIndex.deleteSearchableItemsWithIdentifiers_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchableIndex.deleteSearchableItemsWithDomainIdentifiers_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchableIndex.deleteAllSearchableItemsWithCompletionHandler_,
            0,
            b"v@",
        )

        self.assertArgIsBlock(
            CoreSpotlight.CSSearchableIndex.endIndexBatchWithClientState_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchableIndex.fetchLastClientStateWithCompletionHandler_,
            0,
            b"v@@",
        )

        self.assertArgIsBlock(
            TestCSSearchableIndexHelper.searchableIndex_reindexAllSearchableItemsWithAcknowledgementHandler_,
            1,
            b"v",
        )
        self.assertArgIsBlock(
            TestCSSearchableIndexHelper.searchableIndex_reindexSearchableItemsWithIdentifiers_acknowledgementHandler_,
            2,
            b"v",
        )
        self.assertArgIsOut(
            TestCSSearchableIndexHelper.dataForSearchableIndex_itemIdentifier_typeIdentifier_error_,
            3,
        )
        self.assertArgIsBOOL(
            TestCSSearchableIndexHelper.fileURLForSearchableIndex_itemIdentifier_typeIdentifier_inPlace_error_,
            3,
        )
        self.assertArgIsOut(
            TestCSSearchableIndexHelper.fileURLForSearchableIndex_itemIdentifier_typeIdentifier_inPlace_error_,
            4,
        )

        self.assertArgIsBlock(
            TestCSSearchableIndexHelper.searchableItemsForIdentifiers_searchableItemsHandler_,
            1,
            b"v@",
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchableIndex.fetchDataForBundleIdentifier_itemIdentifier_contentType_completionHandler_,
            3,
            b"v@@",
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchableIndex.endIndexBatchWithExpectedClientState_newClientState_completionHandler_,
            2,
            b"v@",
        )
