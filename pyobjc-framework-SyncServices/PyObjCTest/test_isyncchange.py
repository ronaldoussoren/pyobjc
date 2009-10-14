
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncChange (TestCase):
    def testConstants(self):
        self.failUnlessEqual(ISyncChangeTypeNone, 0)
        self.failUnlessEqual(ISyncChangeTypeAdd, 1)
        self.failUnlessEqual(ISyncChangeTypeModify, 2)
        self.failUnlessEqual(ISyncChangeTypeDelete, 3)

        self.failUnlessIsInstance(ISyncChangePropertyActionKey, unicode)
        self.failUnlessIsInstance(ISyncChangePropertySet, unicode)
        self.failUnlessIsInstance(ISyncChangePropertyClear, unicode)
        self.failUnlessIsInstance(ISyncChangePropertyNameKey, unicode)
        self.failUnlessIsInstance(ISyncChangePropertyValueKey, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(ISyncChangePropertyValueIsDefaultKey, unicode)

if __name__ == "__main__":
    main()
