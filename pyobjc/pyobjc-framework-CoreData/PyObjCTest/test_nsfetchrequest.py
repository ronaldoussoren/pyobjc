
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSFetchRequest (TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertEqual(NSManagedObjectResultType,  0x00)
        self.assertEqual(NSManagedObjectIDResultType,  0x01)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(NSFetchRequest.includesSubentities)
        self.assertArgIsBOOL(NSFetchRequest.setIncludesSubentities_, 0)

        self.assertResultIsBOOL(NSFetchRequest.includesPropertyValues)
        self.assertArgIsBOOL(NSFetchRequest.setIncludesPropertyValues_, 0)

        self.assertResultIsBOOL(NSFetchRequest.returnsObjectsAsFaults)
        self.assertArgIsBOOL(NSFetchRequest.setReturnsObjectsAsFaults_, 0)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(NSDictionaryResultType, 2)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSFetchRequest.includesPendingChanges)
        self.assertArgIsBOOL(NSFetchRequest.setIncludesPendingChanges_, 0)
        self.assertResultIsBOOL(NSFetchRequest.returnsDistinctResults)
        self.assertArgIsBOOL(NSFetchRequest.setReturnsDistinctResults_, 0)

if __name__ == "__main__":
    main()
