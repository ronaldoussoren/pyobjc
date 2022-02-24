import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSManagedObject(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreData.NSSnapshotEventType)

    def testMethods(self):
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

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(CoreData.NSManagedObject.hasFaultForRelationshipNamed_)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(
            CoreData.NSManagedObject.contextShouldIgnoreUnmodeledPropertyChanges
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(CoreData.NSManagedObject.hasChanges)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(CoreData.NSManagedObject.hasPersistentChangedValues)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreData.NSSnapshotEventUndoInsertion, 1 << 1)
        self.assertEqual(CoreData.NSSnapshotEventUndoDeletion, 1 << 2)
        self.assertEqual(CoreData.NSSnapshotEventUndoUpdate, 1 << 3)
        self.assertEqual(CoreData.NSSnapshotEventRollback, 1 << 4)
        self.assertEqual(CoreData.NSSnapshotEventRefresh, 1 << 5)
        self.assertEqual(CoreData.NSSnapshotEventMergePolicy, 1 << 6)
