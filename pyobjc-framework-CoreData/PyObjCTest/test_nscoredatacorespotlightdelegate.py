import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSCoreDataCoreSpotlightDelegate(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertArgIsBlock(
            CoreData.NSCoreDataCoreSpotlightDelegate.searchableIndex_reindexSearchableItemsWithIdentifiers_acknowledgementHandler_,
            2,
            b"v",
        )
