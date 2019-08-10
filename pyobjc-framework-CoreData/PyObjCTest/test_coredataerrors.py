from PyObjCTools.TestSupport import *
from CoreData import *


class TestCoreDataErrors(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(NSInferredMappingModelError, 134_190)
        self.assertEqual(NSExternalRecordImportError, 134_200)
        self.assertEqual(NSPersistentHistoryTokenExpiredError, 134_301)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(NSSQLiteErrorDomain, unicode)

        self.assertEqual(NSCoreDataError, 134_060)
        self.assertEqual(NSPersistentStoreOperationError, 134_070)
        self.assertEqual(NSPersistentStoreOpenError, 134_080)
        self.assertEqual(NSPersistentStoreTimeoutError, 134_090)
        self.assertEqual(NSPersistentStoreUnsupportedRequestTypeError, 134_091)
        self.assertEqual(NSPersistentStoreIncompatibleVersionHashError, 134_100)
        self.assertEqual(NSMigrationError, 134_110)
        self.assertEqual(NSMigrationConstraintViolationError, 134_111)
        self.assertEqual(NSMigrationCancelledError, 134_120)
        self.assertEqual(NSMigrationMissingSourceModelError, 134_130)
        self.assertEqual(NSMigrationMissingMappingModelError, 134_140)
        self.assertEqual(NSMigrationManagerSourceStoreError, 134_150)
        self.assertEqual(NSMigrationManagerDestinationStoreError, 134_160)
        self.assertEqual(NSEntityMigrationPolicyError, 134_170)
        self.assertEqual(NSSQLiteError, 134_180)

    def testConstants(self):
        self.assertIsInstance(NSDetailedErrorsKey, unicode)
        self.assertIsInstance(NSValidationObjectErrorKey, unicode)
        self.assertIsInstance(NSValidationKeyErrorKey, unicode)
        self.assertIsInstance(NSValidationPredicateErrorKey, unicode)
        self.assertIsInstance(NSValidationValueErrorKey, unicode)
        self.assertIsInstance(NSAffectedStoresErrorKey, unicode)
        self.assertIsInstance(NSAffectedObjectsErrorKey, unicode)

        self.assertEqual(NSManagedObjectValidationError, 1550)
        self.assertEqual(NSManagedObjectConstraintValidationError, 1551)
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
        self.assertEqual(NSValidationInvalidURIError, 1690)
        self.assertEqual(NSManagedObjectContextLockingError, 132_000)
        self.assertEqual(NSPersistentStoreCoordinatorLockingError, 132_010)
        self.assertEqual(NSManagedObjectReferentialIntegrityError, 133_000)
        self.assertEqual(NSManagedObjectExternalRelationshipError, 133_010)
        self.assertEqual(NSManagedObjectMergeError, 133_020)
        self.assertEqual(NSManagedObjectConstraintMergeError, 133_021)
        self.assertEqual(NSPersistentStoreInvalidTypeError, 134_000)
        self.assertEqual(NSPersistentStoreTypeMismatchError, 134_010)
        self.assertEqual(NSPersistentStoreIncompatibleSchemaError, 134_020)
        self.assertEqual(NSPersistentStoreSaveError, 134_030)
        self.assertEqual(NSPersistentStoreIncompleteSaveError, 134_040)
        self.assertEqual(NSPersistentStoreSaveConflictsError, 134_050)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(NSPersistentStoreSaveConflictsErrorKey, unicode)


if __name__ == "__main__":
    main()
