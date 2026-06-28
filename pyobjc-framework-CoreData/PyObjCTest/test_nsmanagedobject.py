import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSManagedObject(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreData.NSSnapshotEventType)
        self.assertEqual(CoreData.NSSnapshotEventUndoInsertion, 1 << 1)
        self.assertEqual(CoreData.NSSnapshotEventUndoDeletion, 1 << 2)
        self.assertEqual(CoreData.NSSnapshotEventUndoUpdate, 1 << 3)
        self.assertEqual(CoreData.NSSnapshotEventRollback, 1 << 4)
        self.assertEqual(CoreData.NSSnapshotEventRefresh, 1 << 5)
        self.assertEqual(CoreData.NSSnapshotEventMergePolicy, 1 << 6)

    def test_methods(self):
        descr = CoreData.NSEntityDescription.alloc().init()
        descr.setName_("Name")
        o = CoreData.NSManagedObject.alloc().initWithEntity_insertIntoManagedObjectContext_(
            descr, None
        )

        self.assertResultIsBOOL(o.isInserted)
        self.assertResultIsBOOL(o.isUpdated)
        self.assertResultIsBOOL(o.isDeleted)
        self.assertResultIsBOOL(o.isFault)

        self.assertResultIsBOOL(CoreData.NSManagedObject.validateValue_forKey_error_)
        self.assertArgIsOut(CoreData.NSManagedObject.validateValue_forKey_error_, 2)

        self.assertResultIsBOOL(CoreData.NSManagedObject.validateForDelete_)
        self.assertArgIsOut(CoreData.NSManagedObject.validateForDelete_, 0)

        self.assertResultIsBOOL(CoreData.NSManagedObject.validateForInsert_)
        self.assertArgIsOut(CoreData.NSManagedObject.validateForInsert_, 0)

        self.assertResultIsBOOL(CoreData.NSManagedObject.validateForUpdate_)
        self.assertArgIsOut(CoreData.NSManagedObject.validateForUpdate_, 0)

        self.assertResultIsBOOL(CoreData.NSManagedObject.hasFaultForRelationshipNamed_)

        self.assertResultIsBOOL(
            CoreData.NSManagedObject.contextShouldIgnoreUnmodeledPropertyChanges
        )

        self.assertResultIsBOOL(CoreData.NSManagedObject.hasChanges)

        self.assertResultIsBOOL(CoreData.NSManagedObject.hasPersistentChangedValues)
