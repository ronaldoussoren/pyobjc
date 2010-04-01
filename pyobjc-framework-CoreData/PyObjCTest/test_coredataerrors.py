
from PyObjCTools.TestSupport import *
from CoreData import *

class TestCoreDataErrors (TestCase):

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSInferredMappingModelError, 134190)
        self.assertEqual(NSExternalRecordImportError, 134200)


    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(NSSQLiteErrorDomain, unicode)

        self.assertEqual(NSCoreDataError, 134060)
        self.assertEqual(NSPersistentStoreOperationError, 134070)
        self.assertEqual(NSPersistentStoreOpenError, 134080)
        self.assertEqual(NSPersistentStoreTimeoutError, 134090)
        self.assertEqual(NSPersistentStoreIncompatibleVersionHashError, 134100)
        self.assertEqual(NSMigrationError, 134110)
        self.assertEqual(NSMigrationCancelledError, 134120)
        self.assertEqual(NSMigrationMissingSourceModelError, 134130)
        self.assertEqual(NSMigrationMissingMappingModelError, 134140)
        self.assertEqual(NSMigrationManagerSourceStoreError, 134150)
        self.assertEqual(NSMigrationManagerDestinationStoreError, 134160)
        self.assertEqual(NSEntityMigrationPolicyError, 134170)
        self.assertEqual(NSSQLiteError, 134180)

    def testConstants(self):
        self.assertIsInstance(NSDetailedErrorsKey, unicode)
        self.assertIsInstance(NSValidationObjectErrorKey, unicode)
        self.assertIsInstance(NSValidationKeyErrorKey, unicode)
        self.assertIsInstance(NSValidationPredicateErrorKey, unicode)
        self.assertIsInstance(NSValidationValueErrorKey, unicode)
        self.assertIsInstance(NSAffectedStoresErrorKey, unicode)
        self.assertIsInstance(NSAffectedObjectsErrorKey, unicode)


        self.assertEqual(NSManagedObjectValidationError, 1550)
        self.assertEqual(NSValidationMultipleErrorsError, 1560)
        self.assertEqual(NSValidationMissingMandatoryPropertyError, 1570)
        self.assertEqual(NSValidationRelationshipLacksMinimumCountError, 1580)
        self.assertEqual(NSValidationRelationshipExceedsMaximumCountError, 1590)
        self.assertEqual(NSValidationRelationshipDeniedDeleteError, 1600)
        self.assertEqual(NSValidationNumberTooLargeError, 1610)
        self.assertEqual(NSValidationNumberTooSmallError, 1620)
        self.assertEqual(NSValidationDateTooLateError, 1630)
        self.assertEqual(NSValidationDateTooSoonError, 1640)
        self.assertEqual(NSValidationInvalidDateError, 1650)
        self.assertEqual(NSValidationStringTooLongError, 1660)
        self.assertEqual(NSValidationStringTooShortError, 1670)
        self.assertEqual(NSValidationStringPatternMatchingError, 1680)
        self.assertEqual(NSManagedObjectContextLockingError, 132000)
        self.assertEqual(NSPersistentStoreCoordinatorLockingError, 132010)
        self.assertEqual(NSManagedObjectReferentialIntegrityError, 133000)
        self.assertEqual(NSManagedObjectExternalRelationshipError, 133010)
        self.assertEqual(NSManagedObjectMergeError, 133020)
        self.assertEqual(NSPersistentStoreInvalidTypeError, 134000)
        self.assertEqual(NSPersistentStoreTypeMismatchError, 134010)
        self.assertEqual(NSPersistentStoreIncompatibleSchemaError, 134020)
        self.assertEqual(NSPersistentStoreSaveError, 134030)
        self.assertEqual(NSPersistentStoreIncompleteSaveError, 134040)


if __name__ == "__main__":
    main()
