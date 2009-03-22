from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSPersistentDocument (TestCase):

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_modelConfiguration_storeOptions_error_)
        self.failUnlessArgIsOut(NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_modelConfiguration_storeOptions_error_, 4)
        
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPersistentDocument.writeToURL_ofType_forSaveOperation_originalContentsURL_error_)
        self.failUnlessArgIsOut(NSPersistentDocument.writeToURL_ofType_forSaveOperation_originalContentsURL_error_, 4)

        self.failUnlessResultIsBOOL(NSPersistentDocument.readFromURL_ofType_error_)
        self.failUnlessArgIsOut(NSPersistentDocument.readFromURL_ofType_error_, 2)

        self.failUnlessResultIsBOOL(NSPersistentDocument.revertToContentsOfURL_ofType_error_)
        self.failUnlessArgIsOut(NSPersistentDocument.revertToContentsOfURL_ofType_error_, 2)

        self.failUnlessResultIsBOOL(NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_error_)
        self.failUnlessArgIsOut(NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_error_, 2)

if __name__ == "__main__":
    main()
