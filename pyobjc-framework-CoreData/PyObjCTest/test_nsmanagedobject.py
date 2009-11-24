
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSManagedObject (TestCase):
    def testMethods(self):
        o = NSManagedObject.alloc().init()
        self.failUnlessResultIsBOOL(o.isInserted)
        self.failUnlessResultIsBOOL(o.isUpdated)
        self.failUnlessResultIsBOOL(o.isDeleted)
        self.failUnlessResultIsBOOL(o.isFault)

        self.failUnlessResultIsBOOL(NSManagedObject.validateValue_forKey_error_)
        self.failUnlessArgIsOut(NSManagedObject.validateValue_forKey_error_, 2)

        self.failUnlessResultIsBOOL(NSManagedObject.validateForDelete_)
        self.failUnlessArgIsOut(NSManagedObject.validateForDelete_, 0)

        self.failUnlessResultIsBOOL(NSManagedObject.validateForInsert_)
        self.failUnlessArgIsOut(NSManagedObject.validateForInsert_, 0)

        self.failUnlessResultIsBOOL(NSManagedObject.validateForUpdate_)
        self.failUnlessArgIsOut(NSManagedObject.validateForUpdate_, 0)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSManagedObject.hasFaultForRelationshipNamed_)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(NSSnapshotEventUndoInsertion, 1 << 1)
        self.failUnlessEqual(NSSnapshotEventUndoDeletion, 1 << 2)
        self.failUnlessEqual(NSSnapshotEventUndoUpdate, 1 << 3)
        self.failUnlessEqual(NSSnapshotEventRollback, 1 << 4)
        self.failUnlessEqual(NSSnapshotEventRefresh, 1 << 5)
        self.failUnlessEqual(NSSnapshotEventMergePolicy, 1 << 6)


if __name__ == "__main__":
    main()
