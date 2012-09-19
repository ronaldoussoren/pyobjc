
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSManagedObject (TestCase):
    def testMethods(self):
        descr = NSEntityDescription.alloc().init()
        descr.setName_(b'Name'.decode('ascii'))
        o = NSManagedObject.alloc().initWithEntity_insertIntoManagedObjectContext_(descr, None)

        self.assertResultIsBOOL(o.isInserted)
        self.assertResultIsBOOL(o.isUpdated)
        self.assertResultIsBOOL(o.isDeleted)
        self.assertResultIsBOOL(o.isFault)

        self.assertResultIsBOOL(NSManagedObject.validateValue_forKey_error_)
        self.assertArgIsOut(NSManagedObject.validateValue_forKey_error_, 2)

        self.assertResultIsBOOL(NSManagedObject.validateForDelete_)
        self.assertArgIsOut(NSManagedObject.validateForDelete_, 0)

        self.assertResultIsBOOL(NSManagedObject.validateForInsert_)
        self.assertArgIsOut(NSManagedObject.validateForInsert_, 0)

        self.assertResultIsBOOL(NSManagedObject.validateForUpdate_)
        self.assertArgIsOut(NSManagedObject.validateForUpdate_, 0)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSManagedObject.hasFaultForRelationshipNamed_)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSSnapshotEventUndoInsertion, 1 << 1)
        self.assertEqual(NSSnapshotEventUndoDeletion, 1 << 2)
        self.assertEqual(NSSnapshotEventUndoUpdate, 1 << 3)
        self.assertEqual(NSSnapshotEventRollback, 1 << 4)
        self.assertEqual(NSSnapshotEventRefresh, 1 << 5)
        self.assertEqual(NSSnapshotEventMergePolicy, 1 << 6)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSManagedObject.hasChanges)


if __name__ == "__main__":
    main()
