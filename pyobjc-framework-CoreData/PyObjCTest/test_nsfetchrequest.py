import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFetchRequest(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreData.NSFetchRequestResultType)
        self.assertEqual(CoreData.NSManagedObjectResultType, 0x00)
        self.assertEqual(CoreData.NSManagedObjectIDResultType, 0x01)
        self.assertEqual(CoreData.NSDictionaryResultType, 2)
        self.assertEqual(CoreData.NSCountResultType, 4)

    def test_methods(self):
        self.assertResultIsBOOL(CoreData.NSFetchRequest.includesSubentities)
        self.assertArgIsBOOL(CoreData.NSFetchRequest.setIncludesSubentities_, 0)

        self.assertResultIsBOOL(CoreData.NSFetchRequest.includesPropertyValues)
        self.assertArgIsBOOL(CoreData.NSFetchRequest.setIncludesPropertyValues_, 0)

        self.assertResultIsBOOL(CoreData.NSFetchRequest.returnsObjectsAsFaults)
        self.assertArgIsBOOL(CoreData.NSFetchRequest.setReturnsObjectsAsFaults_, 0)

        self.assertResultIsBOOL(CoreData.NSFetchRequest.includesPendingChanges)
        self.assertArgIsBOOL(CoreData.NSFetchRequest.setIncludesPendingChanges_, 0)
        self.assertResultIsBOOL(CoreData.NSFetchRequest.returnsDistinctResults)
        self.assertArgIsBOOL(CoreData.NSFetchRequest.setReturnsDistinctResults_, 0)

        self.assertResultIsBOOL(CoreData.NSFetchRequest.shouldRefreshRefetchedObjects)
        self.assertArgIsBOOL(
            CoreData.NSFetchRequest.setShouldRefreshRefetchedObjects_, 0
        )

    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertArgIsOut(CoreData.NSFetchRequest.execute_, 0)
