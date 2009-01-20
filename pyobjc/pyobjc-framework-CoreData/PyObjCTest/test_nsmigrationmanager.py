
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSMigrationManager (TestCase):

    @min_os_level("10.5")
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSMigrationManager.migrateStoreFromURL_type_options_withMappingModel_toDestinationURL_destinationType_destinationOptions_error_)
        self.failUnlessArgIsOut(NSMigrationManager.migrateStoreFromURL_type_options_withMappingModel_toDestinationURL_destinationType_destinationOptions_error_, 7)

if __name__ == "__main__":
    main()
