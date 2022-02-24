import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersistentStoreRequest(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreData.NSPersistentStoreRequestType)

    def testConstants(self):
        self.assertEqual(CoreData.NSFetchRequestType, 1)
        self.assertEqual(CoreData.NSSaveRequestType, 2)
        self.assertEqual(CoreData.NSBatchInsertRequestType, 5)
        self.assertEqual(CoreData.NSBatchUpdateRequestType, 6)
        self.assertEqual(CoreData.NSBatchDeleteRequestType, 7)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            CoreData.NSAsynchronousFetchRequest.initWithFetchRequest_completionBlock_,
            1,
            b"v@",
        )
        self.assertResultIsBlock(
            CoreData.NSAsynchronousFetchRequest.completionBlock, b"v@"
        )
