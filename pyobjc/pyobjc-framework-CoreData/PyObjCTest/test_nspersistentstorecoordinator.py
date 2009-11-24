
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPersistentStoreCoordinator (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSSQLiteStoreType, unicode)
        self.failUnlessIsInstance(NSXMLStoreType, unicode)
        self.failUnlessIsInstance(NSBinaryStoreType, unicode)
        self.failUnlessIsInstance(NSInMemoryStoreType, unicode)
        self.failUnlessIsInstance(NSStoreTypeKey, unicode)
        self.failUnlessIsInstance(NSStoreUUIDKey, unicode)
        self.failUnlessIsInstance(NSPersistentStoreCoordinatorStoresDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSAddedPersistentStoresKey, unicode)
        self.failUnlessIsInstance(NSRemovedPersistentStoresKey, unicode)
        self.failUnlessIsInstance(NSUUIDChangedPersistentStoresKey, unicode)
        self.failUnlessIsInstance(NSReadOnlyPersistentStoreOption, unicode)
        self.failUnlessIsInstance(NSValidateXMLStoreOption, unicode)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessIsInstance(NSPersistentStoreTimeoutOption, unicode)
        self.failUnlessIsInstance(NSSQLitePragmasOption, unicode)
        self.failUnlessIsInstance(NSIgnorePersistentStoreVersioningOption, unicode)
        self.failUnlessIsInstance(NSMigratePersistentStoresAutomaticallyOption, unicode)
        self.failUnlessIsInstance(NSStoreModelVersionHashesKey, unicode)
        self.failUnlessIsInstance(NSStoreModelVersionIdentifiersKey, unicode)
        self.failUnlessIsInstance(NSPersistentStoreOSCompatibility, unicode)

        self.failUnlessIsInstance(NSPersistentStoreCoordinatorWillRemoveStoreNotification, unicode)
        self.failUnlessIsInstance(NSSQLiteAnalyzeOption, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(NSSQLiteManualVacuumOption, unicode)
        self.failUnlessIsInstance(NSInferMappingModelAutomaticallyOption, unicode)
        self.failUnlessIsInstance(NSXMLExternalRecordType, unicode)
        self.failUnlessIsInstance(NSBinaryExternalRecordType, unicode)
        self.failUnlessIsInstance(NSExternalRecordsFileFormatOption, unicode)
        self.failUnlessIsInstance(NSExternalRecordsDirectoryOption, unicode)
        self.failUnlessIsInstance(NSExternalRecordExtensionOption, unicode)
        self.failUnlessIsInstance(NSEntityNameInPathKey, unicode)
        self.failUnlessIsInstance(NSStoreUUIDInPathKey, unicode)
        self.failUnlessIsInstance(NSStorePathKey, unicode)
        self.failUnlessIsInstance(NSModelPathKey, unicode)
        self.failUnlessIsInstance(NSObjectURIKey, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsOut(NSPersistentStoreCoordinator.importStoreWithIdentifier_fromExternalRecordsDirectory_toURL_options_withType_error_, 5)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessArgIsOut(NSPersistentStoreCoordinator.metadataForPersistentStoreOfType_URL_error_, 2)
        self.failUnlessResultIsBOOL(NSPersistentStoreCoordinator.setMetadata_forPersistentStoreOfType_URL_error_)
        self.failUnlessArgIsOut(NSPersistentStoreCoordinator.setMetadata_forPersistentStoreOfType_URL_error_, 3)
        self.failUnlessResultIsBOOL(NSPersistentStoreCoordinator.setURL_forPersistentStore_)


    def testMethods(self):
        self.failUnlessArgIsOut(NSPersistentStoreCoordinator.addPersistentStoreWithType_configuration_URL_options_error_, 4)
        self.failUnlessResultIsBOOL(NSPersistentStoreCoordinator.removePersistentStore_error_)
        self.failUnlessArgIsOut(NSPersistentStoreCoordinator.removePersistentStore_error_, 1)
        self.failUnlessArgIsOut(NSPersistentStoreCoordinator.migratePersistentStore_toURL_options_withType_error_, 4)
        self.failUnlessResultIsBOOL(NSPersistentStoreCoordinator.tryLock)
        self.failUnlessArgIsOut(NSPersistentStoreCoordinator.metadataForPersistentStoreWithURL_error_, 1)





if __name__ == "__main__":
    main()
