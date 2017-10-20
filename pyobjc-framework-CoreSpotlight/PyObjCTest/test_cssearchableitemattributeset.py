from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:

    import CoreSpotlight

    class TestCSSearchableItemAttributeSet (TestCase):
        def testMethods(self):
            self.assertArgIsBOOL(CoreSpotlight.CSCustomAttributeKey.initWithKeyName_searchable_searchableByDefault_unique_multiValued_, 1)
            self.assertArgIsBOOL(CoreSpotlight.CSCustomAttributeKey.initWithKeyName_searchable_searchableByDefault_unique_multiValued_, 2)
            self.assertArgIsBOOL(CoreSpotlight.CSCustomAttributeKey.initWithKeyName_searchable_searchableByDefault_unique_multiValued_, 3)
            self.assertArgIsBOOL(CoreSpotlight.CSCustomAttributeKey.initWithKeyName_searchable_searchableByDefault_unique_multiValued_, 4)

            self.assertArgIsBOOL(CoreSpotlight.CSCustomAttributeKey.setSearchable_, 0)
            self.assertArgIsBOOL(CoreSpotlight.CSCustomAttributeKey.setSearchableByDefault_, 0)
            self.assertArgIsBOOL(CoreSpotlight.CSCustomAttributeKey.setUnique_, 0)
            self.assertArgIsBOOL(CoreSpotlight.CSCustomAttributeKey.setMultiValued_, 0)

            self.assertResultIsBOOL(CoreSpotlight.CSCustomAttributeKey.isSearchable)
            self.assertResultIsBOOL(CoreSpotlight.CSCustomAttributeKey.isSearchableByDefault)
            self.assertResultIsBOOL(CoreSpotlight.CSCustomAttributeKey.isUnique)
            self.assertResultIsBOOL(CoreSpotlight.CSCustomAttributeKey.isMultiValued)

if __name__ == "__main__":
    main()
