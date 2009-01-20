
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSEntityMigrationPolicy (TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.failUnlessIsInstance(NSMigrationManagerKey, unicode)
        self.failUnlessIsInstance(NSMigrationSourceObjectKey, unicode)
        self.failUnlessIsInstance(NSMigrationDestinationObjectKey, unicode)
        self.failUnlessIsInstance(NSMigrationEntityMappingKey, unicode)
        self.failUnlessIsInstance(NSMigrationPropertyMappingKey, unicode)

    @min_os_level("10.5")
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSEntityMigrationPolicy.beginEntityMapping_manager_error_)
        self.failUnlessArgIsOut(NSEntityMigrationPolicy.beginEntityMapping_manager_error_, 2)
        
        self.failUnlessResultIsBOOL(NSEntityMigrationPolicy.createDestinationInstancesForSourceInstance_entityMapping_manager_error_)
        self.failUnlessArgIsOut(NSEntityMigrationPolicy.createDestinationInstancesForSourceInstance_entityMapping_manager_error_, 3)

        self.failUnlessResultIsBOOL(NSEntityMigrationPolicy.endInstanceCreationForEntityMapping_manager_error_)
        self.failUnlessArgIsOut(NSEntityMigrationPolicy.endInstanceCreationForEntityMapping_manager_error_, 2)

        self.failUnlessResultIsBOOL(NSEntityMigrationPolicy.createRelationshipsForDestinationInstance_entityMapping_manager_error_)
        self.failUnlessArgIsOut(NSEntityMigrationPolicy.createRelationshipsForDestinationInstance_entityMapping_manager_error_, 3)

        self.failUnlessResultIsBOOL(NSEntityMigrationPolicy.endRelationshipCreationForEntityMapping_manager_error_)
        self.failUnlessArgIsOut(NSEntityMigrationPolicy.endRelationshipCreationForEntityMapping_manager_error_, 2)

        self.failUnlessResultIsBOOL(NSEntityMigrationPolicy.performCustomValidationForEntityMapping_manager_error_)
        self.failUnlessArgIsOut(NSEntityMigrationPolicy.performCustomValidationForEntityMapping_manager_error_, 2)

        self.failUnlessResultIsBOOL(NSEntityMigrationPolicy.endEntityMapping_manager_error_)
        self.failUnlessArgIsOut(NSEntityMigrationPolicy.endEntityMapping_manager_error_, 2)

if __name__ == "__main__":
    main()
