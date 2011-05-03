
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPersistentStore (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertArgIsOut(NSPersistentStore.metadataForPersistentStoreWithURL_error_, 1)
        self.assertResultIsBOOL(NSPersistentStore.setMetadata_forPersistentStoreWithURL_error_)
        self.assertArgIsOut(NSPersistentStore.setMetadata_forPersistentStoreWithURL_error_, 2)
        self.assertResultIsBOOL(NSPersistentStore.isReadOnly)
        self.assertArgIsBOOL(NSPersistentStore.setReadOnly_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSPersistentStore.loadMetadata_)
        self.assertArgIsOut(NSPersistentStore.loadMetadata_, 0)


if __name__ == "__main__":
    main()
