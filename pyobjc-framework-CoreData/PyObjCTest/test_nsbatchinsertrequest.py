import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSBatchInsertRequest(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBlock(CoreData.NSBatchInsertRequest.dictionaryHandler, b"Z@")
        self.assertArgIsBlock(
            CoreData.NSBatchInsertRequest.setDictionaryHandler_, 0, b"Z@"
        )
        self.assertResultIsBlock(
            CoreData.NSBatchInsertRequest.managedObjectHandler, b"Z@"
        )
        self.assertArgIsBlock(
            CoreData.NSBatchInsertRequest.setManagedObjectHandler_, 0, b"Z@"
        )

        self.assertArgIsBlock(
            CoreData.NSBatchInsertRequest.batchInsertRequestWithEntityName_dictionaryHandler_,
            1,
            b"Z@",
        )
        self.assertArgIsBlock(
            CoreData.NSBatchInsertRequest.batchInsertRequestWithEntityName_managedObjectHandler_,
            1,
            b"Z@",
        )

        self.assertArgIsBlock(
            CoreData.NSBatchInsertRequest.initWithEntity_dictionaryHandler_, 1, b"Z@"
        )
        self.assertArgIsBlock(
            CoreData.NSBatchInsertRequest.initWithEntity_managedObjectHandler_, 1, b"Z@"
        )

        self.assertArgIsBlock(
            CoreData.NSBatchInsertRequest.initWithEntityName_dictionaryHandler_,
            1,
            b"Z@",
        )
        self.assertArgIsBlock(
            CoreData.NSBatchInsertRequest.initWithEntityName_managedObjectHandler_,
            1,
            b"Z@",
        )
