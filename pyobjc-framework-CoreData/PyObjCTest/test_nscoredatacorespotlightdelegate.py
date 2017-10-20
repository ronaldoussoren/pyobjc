from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSCoreDataCoreSpotlightDelegate (TestCase):

    @onlyOn64Bit
    @min_os_level('10.13')
    def testMethods(self):
        self.assertArgIsBlock(NSCoreDataCoreSpotlightDelegate.searchableIndex_reindexSearchableItemsWithIdentifiers_acknowledgementHandler_, 2, b'v')


if __name__ == "__main__":
    main()
