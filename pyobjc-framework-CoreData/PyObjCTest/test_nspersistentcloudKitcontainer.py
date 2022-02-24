import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersistentCloudKitContainer(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(
            CoreData.NSPersistentCloudKitContainerSchemaInitializationOptions
        )

    def test_constants(self):
        self.assertEqual(
            CoreData.NSPersistentCloudKitContainerSchemaInitializationOptionsNone, 0
        )
        self.assertEqual(
            CoreData.NSPersistentCloudKitContainerSchemaInitializationOptionsDryRun,
            1 << 1,
        )
        self.assertEqual(
            CoreData.NSPersistentCloudKitContainerSchemaInitializationOptionsPrintSchema,
            1 << 2,
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            CoreData.NSPersistentCloudKitContainer.initializeCloudKitSchemaWithOptions_error_
        )
        self.assertArgIsOut(
            CoreData.NSPersistentCloudKitContainer.initializeCloudKitSchemaWithOptions_error_,
            1,
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(
            CoreData.NSPersistentCloudKitContainer.canUpdateRecordForManagedObjectWithID_
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentCloudKitContainer.canDeleteRecordForManagedObjectWithID_
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentCloudKitContainer.canModifyManagedObjectsInStore_
        )
