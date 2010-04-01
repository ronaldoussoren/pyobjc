
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSEntityMigrationPolicy (TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(NSMigrationManagerKey, unicode)
        self.assertIsInstance(NSMigrationSourceObjectKey, unicode)
        self.assertIsInstance(NSMigrationDestinationObjectKey, unicode)
        self.assertIsInstance(NSMigrationEntityMappingKey, unicode)
        self.assertIsInstance(NSMigrationPropertyMappingKey, unicode)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(NSEntityMigrationPolicy.beginEntityMapping_manager_error_)
        self.assertArgIsOut(NSEntityMigrationPolicy.beginEntityMapping_manager_error_, 2)

        self.assertResultIsBOOL(NSEntityMigrationPolicy.createDestinationInstancesForSourceInstance_entityMapping_manager_error_)
        self.assertArgIsOut(NSEntityMigrationPolicy.createDestinationInstancesForSourceInstance_entityMapping_manager_error_, 3)

        self.assertResultIsBOOL(NSEntityMigrationPolicy.endInstanceCreationForEntityMapping_manager_error_)
        self.assertArgIsOut(NSEntityMigrationPolicy.endInstanceCreationForEntityMapping_manager_error_, 2)

        self.assertResultIsBOOL(NSEntityMigrationPolicy.createRelationshipsForDestinationInstance_entityMapping_manager_error_)
        self.assertArgIsOut(NSEntityMigrationPolicy.createRelationshipsForDestinationInstance_entityMapping_manager_error_, 3)

        self.assertResultIsBOOL(NSEntityMigrationPolicy.endRelationshipCreationForEntityMapping_manager_error_)
        self.assertArgIsOut(NSEntityMigrationPolicy.endRelationshipCreationForEntityMapping_manager_error_, 2)

        self.assertResultIsBOOL(NSEntityMigrationPolicy.performCustomValidationForEntityMapping_manager_error_)
        self.assertArgIsOut(NSEntityMigrationPolicy.performCustomValidationForEntityMapping_manager_error_, 2)

        self.assertResultIsBOOL(NSEntityMigrationPolicy.endEntityMapping_manager_error_)
        self.assertArgIsOut(NSEntityMigrationPolicy.endEntityMapping_manager_error_, 2)

if __name__ == "__main__":
    main()
