import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSPersistentStoreResult(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreData.NSBatchDeleteRequestResultType)
        self.assertIsEnumType(CoreData.NSBatchInsertRequestResultType)
        self.assertIsEnumType(CoreData.NSBatchUpdateRequestResultType)
        self.assertIsEnumType(CoreData.NSPersistentCloudKitContainerEventResultType)
        self.assertIsEnumType(CoreData.NSPersistentHistoryResultType)

    def testConstants(self):
        self.assertEqual(CoreData.NSStatusOnlyResultType, 0)
        self.assertEqual(CoreData.NSUpdatedObjectIDsResultType, 1)
        self.assertEqual(CoreData.NSUpdatedObjectsCountResultType, 2)

        self.assertEqual(CoreData.NSBatchDeleteResultTypeStatusOnly, 0)
        self.assertEqual(CoreData.NSBatchDeleteResultTypeObjectIDs, 1)
        self.assertEqual(CoreData.NSBatchDeleteResultTypeCount, 2)

        self.assertEqual(CoreData.NSPersistentHistoryResultTypeStatusOnly, 0x0)
        self.assertEqual(CoreData.NSPersistentHistoryResultTypeObjectIDs, 0x1)
        self.assertEqual(CoreData.NSPersistentHistoryResultTypeCount, 0x2)
        self.assertEqual(CoreData.NSPersistentHistoryResultTypeTransactionsOnly, 0x3)
        self.assertEqual(CoreData.NSPersistentHistoryResultTypeChangesOnly, 0x4)
        self.assertEqual(
            CoreData.NSPersistentHistoryResultTypeTransactionsAndChanges, 0x5
        )

        self.assertEqual(CoreData.NSBatchInsertRequestResultTypeStatusOnly, 0x0)
        self.assertEqual(CoreData.NSBatchInsertRequestResultTypeObjectIDs, 0x1)
        self.assertEqual(CoreData.NSBatchInsertRequestResultTypeCount, 0x2)

        self.assertEqual(CoreData.NSPersistentCloudKitContainerEventResultTypeEvents, 0)
        self.assertEqual(
            CoreData.NSPersistentCloudKitContainerEventResultTypeCountEvents, 1
        )
