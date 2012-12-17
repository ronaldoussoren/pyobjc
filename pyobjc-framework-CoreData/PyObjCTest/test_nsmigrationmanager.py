
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSMigrationManager (TestCase):

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(NSMigrationManager.migrateStoreFromURL_type_options_withMappingModel_toDestinationURL_destinationType_destinationOptions_error_)
        self.assertArgIsOut(NSMigrationManager.migrateStoreFromURL_type_options_withMappingModel_toDestinationURL_destinationType_destinationOptions_error_, 7)

    @min_os_level('10.6')
    def testMethods10_6(self):
        #self.assertArgIsOut(NSMigrationManager.loadMetadata_, 0)
        #self.assertResultIsBOOL(NSMigrationManager.loadMetadata_)
        pass

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBOOL(NSMigrationManager.setUsesStoreSpecificMigrationManager_, 0)
        self.assertResultIsBOOL(NSMigrationManager.usesStoreSpecificMigrationManager)

if __name__ == "__main__":
    main()
