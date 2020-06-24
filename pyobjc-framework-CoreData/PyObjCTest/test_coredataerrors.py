import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCoreDataErrors(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreData.NSInferredMappingModelError, 134_190)
        self.assertEqual(CoreData.NSExternalRecordImportError, 134_200)
        self.assertEqual(CoreData.NSPersistentHistoryTokenExpiredError, 134_301)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(CoreData.NSSQLiteErrorDomain, str)

        self.assertEqual(CoreData.NSCoreDataError, 134_060)
        self.assertEqual(CoreData.NSPersistentStoreOperationError, 134_070)
        self.assertEqual(CoreData.NSPersistentStoreOpenError, 134_080)
        self.assertEqual(CoreData.NSPersistentStoreTimeoutError, 134_090)
        self.assertEqual(CoreData.NSPersistentStoreUnsupportedRequestTypeError, 134_091)
        self.assertEqual(
            CoreData.NSPersistentStoreIncompatibleVersionHashError, 134_100
        )
        self.assertEqual(CoreData.NSMigrationError, 134_110)
        self.assertEqual(CoreData.NSMigrationConstraintViolationError, 134_111)
        self.assertEqual(CoreData.NSMigrationCancelledError, 134_120)
        self.assertEqual(CoreData.NSMigrationMissingSourceModelError, 134_130)
        self.assertEqual(CoreData.NSMigrationMissingMappingModelError, 134_140)
        self.assertEqual(CoreData.NSMigrationManagerSourceStoreError, 134_150)
        self.assertEqual(CoreData.NSMigrationManagerDestinationStoreError, 134_160)
        self.assertEqual(CoreData.NSEntityMigrationPolicyError, 134_170)
        self.assertEqual(CoreData.NSSQLiteError, 134_180)

    def testConstants(self):
        self.assertIsInstance(CoreData.NSDetailedErrorsKey, str)
        self.assertIsInstance(CoreData.NSValidationObjectErrorKey, str)
        self.assertIsInstance(CoreData.NSValidationKeyErrorKey, str)
        self.assertIsInstance(CoreData.NSValidationPredicateErrorKey, str)
        self.assertIsInstance(CoreData.NSValidationValueErrorKey, str)
        self.assertIsInstance(CoreData.NSAffectedStoresErrorKey, str)
        self.assertIsInstance(CoreData.NSAffectedObjectsErrorKey, str)

        self.assertEqual(CoreData.NSManagedObjectValidationError, 1550)
        self.assertEqual(CoreData.NSManagedObjectConstraintValidationError, 1551)
        self.assertEqual(CoreData.NSValidationMultipleErrorsError, 1560)
        self.assertEqual(CoreData.NSValidationMissingMandatoryPropertyError, 1570)
        self.assertEqual(CoreData.NSValidationRelationshipLacksMinimumCountError, 1580)
        self.assertEqual(
            CoreData.NSValidationRelationshipExceedsMaximumCountError, 1590
        )
        self.assertEqual(CoreData.NSValidationRelationshipDeniedDeleteError, 1600)
        self.assertEqual(CoreData.NSValidationNumberTooLargeError, 1610)
        self.assertEqual(CoreData.NSValidationNumberTooSmallError, 1620)
        self.assertEqual(CoreData.NSValidationDateTooLateError, 1630)
        self.assertEqual(CoreData.NSValidationDateTooSoonError, 1640)
        self.assertEqual(CoreData.NSValidationInvalidDateError, 1650)
        self.assertEqual(CoreData.NSValidationStringTooLongError, 1660)
        self.assertEqual(CoreData.NSValidationStringTooShortError, 1670)
        self.assertEqual(CoreData.NSValidationStringPatternMatchingError, 1680)
        self.assertEqual(CoreData.NSValidationInvalidURIError, 1690)
        self.assertEqual(CoreData.NSManagedObjectContextLockingError, 132_000)
        self.assertEqual(CoreData.NSPersistentStoreCoordinatorLockingError, 132_010)
        self.assertEqual(CoreData.NSManagedObjectReferentialIntegrityError, 133_000)
        self.assertEqual(CoreData.NSManagedObjectExternalRelationshipError, 133_010)
        self.assertEqual(CoreData.NSManagedObjectMergeError, 133_020)
        self.assertEqual(CoreData.NSManagedObjectConstraintMergeError, 133_021)
        self.assertEqual(CoreData.NSPersistentStoreInvalidTypeError, 134_000)
        self.assertEqual(CoreData.NSPersistentStoreTypeMismatchError, 134_010)
        self.assertEqual(CoreData.NSPersistentStoreIncompatibleSchemaError, 134_020)
        self.assertEqual(CoreData.NSPersistentStoreSaveError, 134_030)
        self.assertEqual(CoreData.NSPersistentStoreIncompleteSaveError, 134_040)
        self.assertEqual(CoreData.NSPersistentStoreSaveConflictsError, 134_050)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(CoreData.NSPersistentStoreSaveConflictsErrorKey, str)
