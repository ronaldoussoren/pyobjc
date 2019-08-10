from PyObjCTools.TestSupport import *
import CoreData


class TestNSPersistentCloudKitContainer(TestCase):
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


if __name__ == "__main__":
    main()
