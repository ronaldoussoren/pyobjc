import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSMigrationManager(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            CoreData.NSMigrationManager.migrateStoreFromURL_type_options_withMappingModel_toDestinationURL_destinationType_destinationOptions_error_  # noqa: B950
        )
        self.assertArgIsOut(
            CoreData.NSMigrationManager.migrateStoreFromURL_type_options_withMappingModel_toDestinationURL_destinationType_destinationOptions_error_,  # noqa: B950
            7,
        )

        self.assertArgIsBOOL(
            CoreData.NSMigrationManager.setUsesStoreSpecificMigrationManager_, 0
        )
        self.assertResultIsBOOL(
            CoreData.NSMigrationManager.usesStoreSpecificMigrationManager
        )
