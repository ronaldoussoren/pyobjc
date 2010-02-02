from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSPersistentDocument (TestCase):

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_modelConfiguration_storeOptions_error_)
        self.assertArgIsOut(NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_modelConfiguration_storeOptions_error_, 4)
        
    def testMethods(self):
        self.assertResultIsBOOL(NSPersistentDocument.writeToURL_ofType_forSaveOperation_originalContentsURL_error_)
        self.assertArgIsOut(NSPersistentDocument.writeToURL_ofType_forSaveOperation_originalContentsURL_error_, 4)

        self.assertResultIsBOOL(NSPersistentDocument.readFromURL_ofType_error_)
        self.assertArgIsOut(NSPersistentDocument.readFromURL_ofType_error_, 2)

        self.assertResultIsBOOL(NSPersistentDocument.revertToContentsOfURL_ofType_error_)
        self.assertArgIsOut(NSPersistentDocument.revertToContentsOfURL_ofType_error_, 2)

        self.assertResultIsBOOL(NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_error_)
        self.assertArgIsOut(NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_error_, 2)

if __name__ == "__main__":
    main()
