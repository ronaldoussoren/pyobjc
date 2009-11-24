
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSFetchRequest (TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.failUnlessEqual(NSManagedObjectResultType,  0x00)
        self.failUnlessEqual(NSManagedObjectIDResultType,  0x01)

    @min_os_level("10.5")
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSFetchRequest.includesSubentities)
        self.failUnlessArgIsBOOL(NSFetchRequest.setIncludesSubentities_, 0)

        self.failUnlessResultIsBOOL(NSFetchRequest.includesPropertyValues)
        self.failUnlessArgIsBOOL(NSFetchRequest.setIncludesPropertyValues_, 0)

        self.failUnlessResultIsBOOL(NSFetchRequest.returnsObjectsAsFaults)
        self.failUnlessArgIsBOOL(NSFetchRequest.setReturnsObjectsAsFaults_, 0)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.failUnlessEqual(NSDictionaryResultType, 2)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(NSFetchRequest.includesPendingChanges)
        self.failUnlessArgIsBOOL(NSFetchRequest.setIncludesPendingChanges_, 0)
        self.failUnlessResultIsBOOL(NSFetchRequest.returnsDistinctResults)
        self.failUnlessArgIsBOOL(NSFetchRequest.setReturnsDistinctResults_, 0)

if __name__ == "__main__":
    main()
