import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersistentStoreCoordinator(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreData.NSPersistentStoreUbiquitousTransitionType)

    def testConstants(self):
        self.assertIsInstance(CoreData.NSSQLiteStoreType, str)
        self.assertIsInstance(CoreData.NSXMLStoreType, str)
        self.assertIsInstance(CoreData.NSBinaryStoreType, str)
        self.assertIsInstance(CoreData.NSInMemoryStoreType, str)
        self.assertIsInstance(CoreData.NSStoreTypeKey, str)
        self.assertIsInstance(CoreData.NSStoreUUIDKey, str)
        self.assertIsInstance(
            CoreData.NSPersistentStoreCoordinatorStoresDidChangeNotification, str
        )
        self.assertIsInstance(CoreData.NSAddedPersistentStoresKey, str)
        self.assertIsInstance(CoreData.NSRemovedPersistentStoresKey, str)
        self.assertIsInstance(CoreData.NSUUIDChangedPersistentStoresKey, str)
        self.assertIsInstance(CoreData.NSReadOnlyPersistentStoreOption, str)
        self.assertIsInstance(CoreData.NSValidateXMLStoreOption, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(CoreData.NSPersistentStoreTimeoutOption, str)
        self.assertIsInstance(CoreData.NSSQLitePragmasOption, str)
        self.assertIsInstance(CoreData.NSIgnorePersistentStoreVersioningOption, str)
        self.assertIsInstance(
            CoreData.NSMigratePersistentStoresAutomaticallyOption, str
        )
        self.assertIsInstance(CoreData.NSStoreModelVersionHashesKey, str)
        self.assertIsInstance(CoreData.NSStoreModelVersionIdentifiersKey, str)
        self.assertIsInstance(CoreData.NSPersistentStoreOSCompatibility, str)

        self.assertIsInstance(
            CoreData.NSPersistentStoreCoordinatorWillRemoveStoreNotification, str
        )
        self.assertIsInstance(CoreData.NSSQLiteAnalyzeOption, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(CoreData.NSSQLiteManualVacuumOption, str)
        self.assertIsInstance(CoreData.NSInferMappingModelAutomaticallyOption, str)
        self.assertIsInstance(CoreData.NSXMLExternalRecordType, str)
        self.assertIsInstance(CoreData.NSBinaryExternalRecordType, str)
        self.assertIsInstance(CoreData.NSExternalRecordsFileFormatOption, str)
        self.assertIsInstance(CoreData.NSExternalRecordsDirectoryOption, str)
        self.assertIsInstance(CoreData.NSExternalRecordExtensionOption, str)
        self.assertIsInstance(CoreData.NSEntityNameInPathKey, str)
        self.assertIsInstance(CoreData.NSStoreUUIDInPathKey, str)
        self.assertIsInstance(CoreData.NSStorePathKey, str)
        self.assertIsInstance(CoreData.NSModelPathKey, str)
        self.assertIsInstance(CoreData.NSObjectURIKey, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(CoreData.NSPersistentStoreUbiquitousContentNameKey, str)
        self.assertIsInstance(CoreData.NSPersistentStoreUbiquitousContentURLKey, str)
        self.assertIsInstance(
            CoreData.NSPersistentStoreDidImportUbiquitousContentChangesNotification, str
        )

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(CoreData.NSPersistentStoreForceDestroyOption, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(
            CoreData.NSPersistentStoreUbiquitousTransitionTypeAccountAdded, 1
        )
        self.assertEqual(
            CoreData.NSPersistentStoreUbiquitousTransitionTypeAccountRemoved, 2
        )
        self.assertEqual(
            CoreData.NSPersistentStoreUbiquitousTransitionTypeContentRemoved, 3
        )
        self.assertEqual(
            CoreData.NSPersistentStoreUbiquitousTransitionTypeInitialImportCompleted, 4
        )

        self.assertIsInstance(
            CoreData.NSPersistentStoreCoordinatorStoresWillChangeNotification, str
        )
        self.assertIsInstance(
            CoreData.NSPersistentStoreUbiquitousTransitionTypeKey, str
        )
        self.assertIsInstance(CoreData.NSPersistentStoreUbiquitousPeerTokenOption, str)
        self.assertIsInstance(
            CoreData.NSPersistentStoreRemoveUbiquitousMetadataOption, str
        )
        self.assertIsInstance(
            CoreData.NSPersistentStoreUbiquitousContainerIdentifierKey, str
        )
        self.assertIsInstance(
            CoreData.NSPersistentStoreRebuildFromUbiquitousContentOption, str
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(CoreData.NSPersistentStoreConnectionPoolMaxSizeKey, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(CoreData.NSPersistentHistoryTrackingKey, str)
        self.assertIsInstance(CoreData.NSBinaryStoreSecureDecodingClasses, str)
        self.assertIsInstance(
            CoreData.NSBinaryStoreInsecureDecodingCompatibilityOption, str
        )

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(CoreData.NSPersistentStoreRemoteChangeNotification, str)
        self.assertIsInstance(CoreData.NSPersistentStoreURLKey, str)
        self.assertIsInstance(CoreData.NSPersistentHistoryTokenKey, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            CoreData.NSPersistentStoreRemoteChangeNotificationPostOptionKey, str
        )

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(
            CoreData.NSPersistentStoreDeferredLightweightMigrationOptionKey, str
        )

    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsInstance(
            CoreData.NSPersistentStoreStagedMigrationManagerOptionKey, str
        )

    def testMethods(self):
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.addPersistentStoreWithType_configuration_URL_options_error_,
            4,
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreCoordinator.removePersistentStore_error_
        )
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.removePersistentStore_error_, 1
        )
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.migratePersistentStore_toURL_options_withType_error_,
            4,
        )
        self.assertResultIsBOOL(CoreData.NSPersistentStoreCoordinator.tryLock)
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.metadataForPersistentStoreWithURL_error_,
            1,
        )

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.metadataForPersistentStoreOfType_URL_error_,
            2,
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreCoordinator.setMetadata_forPersistentStoreOfType_URL_error_
        )
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.setMetadata_forPersistentStoreOfType_URL_error_,
            3,
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreCoordinator.setURL_forPersistentStore_
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.importStoreWithIdentifier_fromExternalRecordsDirectory_toURL_options_withType_error_,  # noqa: B950
            5,
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.executeRequest_withContext_error_, 2
        )

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.setMetadata_forPersistentStoreOfType_URL_options_error_,
            4,
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreCoordinator.setMetadata_forPersistentStoreOfType_URL_options_error_
        )

        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.removeUbiquitousContentAndPersistentStoreAtURL_options_error_,
            2,
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreCoordinator.removeUbiquitousContentAndPersistentStoreAtURL_options_error_
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            CoreData.NSPersistentStoreCoordinator.performBlock_, 0, b"v"
        )
        self.assertArgIsBlock(
            CoreData.NSPersistentStoreCoordinator.performBlockAndWait_, 0, b"v"
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.destroyPersistentStoreAtURL_withType_options_error_,
            3,
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreCoordinator.destroyPersistentStoreAtURL_withType_options_error_
        )

        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.replacePersistentStoreAtURL_destinationOptions_withPersistentStoreFromURL_sourceOptions_storeType_error_,  # noqa: B950
            5,
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreCoordinator.replacePersistentStoreAtURL_destinationOptions_withPersistentStoreFromURL_sourceOptions_storeType_error_  # noqa: B950
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBlock(
            CoreData.NSPersistentStoreCoordinator.addPersistentStoreWithDescription_completionHandler_,
            1,
            b"v@@",
        )

    @min_os_level("14.0")
    def testMethods14_0(self):
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreCoordinator.finishDeferredLightweightMigration_
        )
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.finishDeferredLightweightMigration_, 0
        )

        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreCoordinator.finishDeferredLightweightMigrationTask_
        )
        self.assertArgIsOut(
            CoreData.NSPersistentStoreCoordinator.finishDeferredLightweightMigrationTask_,
            0,
        )
