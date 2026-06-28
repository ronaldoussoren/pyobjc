import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSPersistentStore(TestCase):
    def test_methods(self):
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

        self.assertResultIsBOOL(CoreData.NSPersistentStore.loadMetadata_)
        self.assertArgIsOut(CoreData.NSPersistentStore.loadMetadata_, 0)
