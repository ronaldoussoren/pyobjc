
from PyObjCTools.TestSupport import *
from CoreData import *

class TestCoreDataErrors (TestCase):

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessIsInstance(NSSQLiteErrorDomain, unicode)

        self.failUnlessEqual(NSCoreDataError, 134060)
        self.failUnlessEqual(NSPersistentStoreOperationError, 134070)
        self.failUnlessEqual(NSPersistentStoreOpenError, 134080)
        self.failUnlessEqual(NSPersistentStoreTimeoutError, 134090)
        self.failUnlessEqual(NSPersistentStoreIncompatibleVersionHashError, 134100)
        self.failUnlessEqual(NSMigrationError, 134110)
        self.failUnlessEqual(NSMigrationCancelledError, 134120)
        self.failUnlessEqual(NSMigrationMissingSourceModelError, 134130)
        self.failUnlessEqual(NSMigrationMissingMappingModelError, 134140)
        self.failUnlessEqual(NSMigrationManagerSourceStoreError, 134150)
        self.failUnlessEqual(NSMigrationManagerDestinationStoreError, 134160)
        self.failUnlessEqual(NSEntityMigrationPolicyError, 134170)
        self.failUnlessEqual(NSSQLiteError, 134180)

    def testConstants(self):
        self.failUnlessIsInstance(NSDetailedErrorsKey, unicode)
        self.failUnlessIsInstance(NSValidationObjectErrorKey, unicode)
        self.failUnlessIsInstance(NSValidationKeyErrorKey, unicode)
        self.failUnlessIsInstance(NSValidationPredicateErrorKey, unicode)
        self.failUnlessIsInstance(NSValidationValueErrorKey, unicode)
        self.failUnlessIsInstance(NSAffectedStoresErrorKey, unicode)
        self.failUnlessIsInstance(NSAffectedObjectsErrorKey, unicode)


        self.failUnlessEqual(NSManagedObjectValidationError, 1550)
        self.failUnlessEqual(NSValidationMultipleErrorsError, 1560)
        self.failUnlessEqual(NSValidationMissingMandatoryPropertyError, 1570)
        self.failUnlessEqual(NSValidationRelationshipLacksMinimumCountError, 1580)
        self.failUnlessEqual(NSValidationRelationshipExceedsMaximumCountError, 1590)
        self.failUnlessEqual(NSValidationRelationshipDeniedDeleteError, 1600)
        self.failUnlessEqual(NSValidationNumberTooLargeError, 1610)
        self.failUnlessEqual(NSValidationNumberTooSmallError, 1620)
        self.failUnlessEqual(NSValidationDateTooLateError, 1630)
        self.failUnlessEqual(NSValidationDateTooSoonError, 1640)
        self.failUnlessEqual(NSValidationInvalidDateError, 1650)
        self.failUnlessEqual(NSValidationStringTooLongError, 1660)
        self.failUnlessEqual(NSValidationStringTooShortError, 1670)
        self.failUnlessEqual(NSValidationStringPatternMatchingError, 1680)
        self.failUnlessEqual(NSManagedObjectContextLockingError, 132000)
        self.failUnlessEqual(NSPersistentStoreCoordinatorLockingError, 132010)
        self.failUnlessEqual(NSManagedObjectReferentialIntegrityError, 133000)
        self.failUnlessEqual(NSManagedObjectExternalRelationshipError, 133010)
        self.failUnlessEqual(NSManagedObjectMergeError, 133020)
        self.failUnlessEqual(NSPersistentStoreInvalidTypeError, 134000)
        self.failUnlessEqual(NSPersistentStoreTypeMismatchError, 134010)
        self.failUnlessEqual(NSPersistentStoreIncompatibleSchemaError, 134020)
        self.failUnlessEqual(NSPersistentStoreSaveError, 134030)
        self.failUnlessEqual(NSPersistentStoreIncompleteSaveError, 134040)


if __name__ == "__main__":
    main()
