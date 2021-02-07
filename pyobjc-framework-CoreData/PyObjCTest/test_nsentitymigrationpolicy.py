import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSEntityMigrationPolicy(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(CoreData.NSMigrationManagerKey, str)
        self.assertIsInstance(CoreData.NSMigrationSourceObjectKey, str)
        self.assertIsInstance(CoreData.NSMigrationDestinationObjectKey, str)
        self.assertIsInstance(CoreData.NSMigrationEntityMappingKey, str)
        self.assertIsInstance(CoreData.NSMigrationPropertyMappingKey, str)
        self.assertIsInstance(CoreData.NSMigrationEntityPolicyKey, str)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(
            CoreData.NSEntityMigrationPolicy.beginEntityMapping_manager_error_
        )
        self.assertArgIsOut(
            CoreData.NSEntityMigrationPolicy.beginEntityMapping_manager_error_, 2
        )

        self.assertResultIsBOOL(
            CoreData.NSEntityMigrationPolicy.createDestinationInstancesForSourceInstance_entityMapping_manager_error_
        )
        self.assertArgIsOut(
            CoreData.NSEntityMigrationPolicy.createDestinationInstancesForSourceInstance_entityMapping_manager_error_,
            3,
        )

        self.assertResultIsBOOL(
            CoreData.NSEntityMigrationPolicy.endInstanceCreationForEntityMapping_manager_error_
        )
        self.assertArgIsOut(
            CoreData.NSEntityMigrationPolicy.endInstanceCreationForEntityMapping_manager_error_,
            2,
        )

        self.assertResultIsBOOL(
            CoreData.NSEntityMigrationPolicy.createRelationshipsForDestinationInstance_entityMapping_manager_error_
        )
        self.assertArgIsOut(
            CoreData.NSEntityMigrationPolicy.createRelationshipsForDestinationInstance_entityMapping_manager_error_,
            3,
        )

        self.assertResultIsBOOL(
            CoreData.NSEntityMigrationPolicy.endRelationshipCreationForEntityMapping_manager_error_
        )
        self.assertArgIsOut(
            CoreData.NSEntityMigrationPolicy.endRelationshipCreationForEntityMapping_manager_error_,
            2,
        )

        self.assertResultIsBOOL(
            CoreData.NSEntityMigrationPolicy.performCustomValidationForEntityMapping_manager_error_
        )
        self.assertArgIsOut(
            CoreData.NSEntityMigrationPolicy.performCustomValidationForEntityMapping_manager_error_,
            2,
        )

        self.assertResultIsBOOL(
            CoreData.NSEntityMigrationPolicy.endEntityMapping_manager_error_
        )
        self.assertArgIsOut(
            CoreData.NSEntityMigrationPolicy.endEntityMapping_manager_error_, 2
        )
