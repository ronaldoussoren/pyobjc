
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPersistentStore (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessArgIsOut(NSPersistentStore.metadataForPersistentStoreWithURL_error_, 1)
        self.failUnlessResultIsBOOL(NSPersistentStore.setMetadata_forPersistentStoreWithURL_error_)
        self.failUnlessArgIsOut(NSPersistentStore.setMetadata_forPersistentStoreWithURL_error_, 2)
        self.failUnlessResultIsBOOL(NSPersistentStore.isReadOnly)
        self.failUnlessArgIsBOOL(NSPersistentStore.setReadOnly_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(NSPersistentStore.loadMetadata_)
        self.failUnlessArgIsOut(NSPersistentStore.loadMetadata_, 0)


if __name__ == "__main__":
    main()
