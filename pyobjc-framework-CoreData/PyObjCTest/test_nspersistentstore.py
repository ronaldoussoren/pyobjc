import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersistentStore(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertArgIsOut(
            CoreData.NSPersistentStore.metadataForPersistentStoreWithURL_error_, 1
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStore.setMetadata_forPersistentStoreWithURL_error_
        )
        self.assertArgIsOut(
            CoreData.NSPersistentStore.setMetadata_forPersistentStoreWithURL_error_, 2
        )
        self.assertResultIsBOOL(CoreData.NSPersistentStore.isReadOnly)
        self.assertArgIsBOOL(CoreData.NSPersistentStore.setReadOnly_, 0)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(CoreData.NSPersistentStore.loadMetadata_)
        self.assertArgIsOut(CoreData.NSPersistentStore.loadMetadata_, 0)
