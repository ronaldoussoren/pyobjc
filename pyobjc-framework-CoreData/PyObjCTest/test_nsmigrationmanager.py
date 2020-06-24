import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMigrationManager(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(
            CoreData.NSMigrationManager.migrateStoreFromURL_type_options_withMappingModel_toDestinationURL_destinationType_destinationOptions_error_  # noqa: B950
        )
        self.assertArgIsOut(
            CoreData.NSMigrationManager.migrateStoreFromURL_type_options_withMappingModel_toDestinationURL_destinationType_destinationOptions_error_,  # noqa: B950
            7,
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBOOL(
            CoreData.NSMigrationManager.setUsesStoreSpecificMigrationManager_, 0
        )
        self.assertResultIsBOOL(
            CoreData.NSMigrationManager.usesStoreSpecificMigrationManager
        )
