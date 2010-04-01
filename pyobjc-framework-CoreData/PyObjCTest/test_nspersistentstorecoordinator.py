
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPersistentStoreCoordinator (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSSQLiteStoreType, unicode)
        self.assertIsInstance(NSXMLStoreType, unicode)
        self.assertIsInstance(NSBinaryStoreType, unicode)
        self.assertIsInstance(NSInMemoryStoreType, unicode)
        self.assertIsInstance(NSStoreTypeKey, unicode)
        self.assertIsInstance(NSStoreUUIDKey, unicode)
        self.assertIsInstance(NSPersistentStoreCoordinatorStoresDidChangeNotification, unicode)
        self.assertIsInstance(NSAddedPersistentStoresKey, unicode)
        self.assertIsInstance(NSRemovedPersistentStoresKey, unicode)
        self.assertIsInstance(NSUUIDChangedPersistentStoresKey, unicode)
        self.assertIsInstance(NSReadOnlyPersistentStoreOption, unicode)
        self.assertIsInstance(NSValidateXMLStoreOption, unicode)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(NSPersistentStoreTimeoutOption, unicode)
        self.assertIsInstance(NSSQLitePragmasOption, unicode)
        self.assertIsInstance(NSIgnorePersistentStoreVersioningOption, unicode)
        self.assertIsInstance(NSMigratePersistentStoresAutomaticallyOption, unicode)
        self.assertIsInstance(NSStoreModelVersionHashesKey, unicode)
        self.assertIsInstance(NSStoreModelVersionIdentifiersKey, unicode)
        self.assertIsInstance(NSPersistentStoreOSCompatibility, unicode)

        self.assertIsInstance(NSPersistentStoreCoordinatorWillRemoveStoreNotification, unicode)
        self.assertIsInstance(NSSQLiteAnalyzeOption, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSSQLiteManualVacuumOption, unicode)
        self.assertIsInstance(NSInferMappingModelAutomaticallyOption, unicode)
        self.assertIsInstance(NSXMLExternalRecordType, unicode)
        self.assertIsInstance(NSBinaryExternalRecordType, unicode)
        self.assertIsInstance(NSExternalRecordsFileFormatOption, unicode)
        self.assertIsInstance(NSExternalRecordsDirectoryOption, unicode)
        self.assertIsInstance(NSExternalRecordExtensionOption, unicode)
        self.assertIsInstance(NSEntityNameInPathKey, unicode)
        self.assertIsInstance(NSStoreUUIDInPathKey, unicode)
        self.assertIsInstance(NSStorePathKey, unicode)
        self.assertIsInstance(NSModelPathKey, unicode)
        self.assertIsInstance(NSObjectURIKey, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsOut(NSPersistentStoreCoordinator.importStoreWithIdentifier_fromExternalRecordsDirectory_toURL_options_withType_error_, 5)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertArgIsOut(NSPersistentStoreCoordinator.metadataForPersistentStoreOfType_URL_error_, 2)
        self.assertResultIsBOOL(NSPersistentStoreCoordinator.setMetadata_forPersistentStoreOfType_URL_error_)
        self.assertArgIsOut(NSPersistentStoreCoordinator.setMetadata_forPersistentStoreOfType_URL_error_, 3)
        self.assertResultIsBOOL(NSPersistentStoreCoordinator.setURL_forPersistentStore_)


    def testMethods(self):
        self.assertArgIsOut(NSPersistentStoreCoordinator.addPersistentStoreWithType_configuration_URL_options_error_, 4)
        self.assertResultIsBOOL(NSPersistentStoreCoordinator.removePersistentStore_error_)
        self.assertArgIsOut(NSPersistentStoreCoordinator.removePersistentStore_error_, 1)
        self.assertArgIsOut(NSPersistentStoreCoordinator.migratePersistentStore_toURL_options_withType_error_, 4)
        self.assertResultIsBOOL(NSPersistentStoreCoordinator.tryLock)
        self.assertArgIsOut(NSPersistentStoreCoordinator.metadataForPersistentStoreWithURL_error_, 1)





if __name__ == "__main__":
    main()
