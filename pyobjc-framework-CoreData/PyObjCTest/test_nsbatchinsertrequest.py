import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSBatchInsertRequest(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBlock(CoreData.dictionaryHandler, b"Z@")
        self.assertArgIsBlock(CoreData.setDictionaryHandler_, 0, b"Z@")
        self.assertResultIsBlock(CoreData.managedObjectHandler, b"Z@")
        self.assertArgIsBlock(CoreData.setManagedObjectHandler_, 0, b"Z@")

        self.assertArgIsBlock(
            CoreData.batchInsertRequestWithEntityName_dictionaryHandler_, 1, b"Z@"
        )
        self.assertArgIsBlock(
            CoreData.batchInsertRequestWithEntityName_managedObjectHandler_, 1, b"Z@"
        )

        self.assertArgIsBlock(CoreData.initWithEntity_dictionaryHandler_, 1, b"Z@")
        self.assertArgIsBlock(CoreData.initWithEntity_managedObjectHandler_, 1, b"Z@")
