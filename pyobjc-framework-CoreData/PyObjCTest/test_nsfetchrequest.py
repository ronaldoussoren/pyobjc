import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFetchRequest(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertEqual(CoreData.NSManagedObjectResultType, 0x00)
        self.assertEqual(CoreData.NSManagedObjectIDResultType, 0x01)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(CoreData.NSFetchRequest.includesSubentities)
        self.assertArgIsBOOL(CoreData.NSFetchRequest.setIncludesSubentities_, 0)

        self.assertResultIsBOOL(CoreData.NSFetchRequest.includesPropertyValues)
        self.assertArgIsBOOL(CoreData.NSFetchRequest.setIncludesPropertyValues_, 0)

        self.assertResultIsBOOL(CoreData.NSFetchRequest.returnsObjectsAsFaults)
        self.assertArgIsBOOL(CoreData.NSFetchRequest.setReturnsObjectsAsFaults_, 0)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreData.NSDictionaryResultType, 2)
        self.assertEqual(CoreData.NSCountResultType, 4)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(CoreData.NSFetchRequest.includesPendingChanges)
        self.assertArgIsBOOL(CoreData.NSFetchRequest.setIncludesPendingChanges_, 0)
        self.assertResultIsBOOL(CoreData.NSFetchRequest.returnsDistinctResults)
        self.assertArgIsBOOL(CoreData.NSFetchRequest.setReturnsDistinctResults_, 0)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(CoreData.NSFetchRequest.shouldRefreshRefetchedObjects)
        self.assertArgIsBOOL(
            CoreData.NSFetchRequest.setShouldRefreshRefetchedObjects_, 0
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsOut(CoreData.NSFetchRequest.execute_, 0)
