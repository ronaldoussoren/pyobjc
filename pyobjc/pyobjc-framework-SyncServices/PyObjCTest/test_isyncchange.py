
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncChange (TestCase):
    def testConstants(self):
        self.failUnlessEqual(ISyncChangeTypeAdd, 1)
        self.failUnlessEqual(ISyncChangeTypeModify, 2)
        self.failUnlessEqual(ISyncChangeTypeDelete, 3)

        self.failUnlessIsInstance(ISyncChangePropertyActionKey, unicode)
        self.failUnlessIsInstance(ISyncChangePropertySet, unicode)
        self.failUnlessIsInstance(ISyncChangePropertyClear, unicode)
        self.failUnlessIsInstance(ISyncChangePropertyNameKey, unicode)
        self.failUnlessIsInstance(ISyncChangePropertyValueKey, unicode)

if __name__ == "__main__":
    main()
