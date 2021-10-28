import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSCoreDataCoreSpotlightDelegate(TestCase):
    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            CoreData.NSCoreDataCoreSpotlightDelegateIndexDidUpdateNotification, str
        )

    @min_os_level("10.13")
    def testMethods(self):
        self.assertArgIsBlock(
            CoreData.NSCoreDataCoreSpotlightDelegate.searchableIndex_reindexSearchableItemsWithIdentifiers_acknowledgementHandler_,
            2,
            b"v",
        )

    @min_os_level("12.0")
    def test_methods11_0(self):
        # Documented as 11.0+, but not available on 11.6
        self.assertArgIsBlock(
            CoreData.NSCoreDataCoreSpotlightDelegate.deleteSpotlightIndexWithCompletionHandler_,
            0,
            b"v@",
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            CoreData.NSCoreDataCoreSpotlightDelegate.isIndexingEnabled
        )
