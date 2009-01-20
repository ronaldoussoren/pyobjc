
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSManagedObject (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSManagedObject.isInserted)
        self.failUnlessResultIsBOOL(NSManagedObject.isUpdated)
        self.failUnlessResultIsBOOL(NSManagedObject.isDeleted)
        self.failUnlessResultIsBOOL(NSManagedObject.isFault)

        self.failUnlessResultIsBOOL(NSManagedObject.validateValue_forKey_error_)
        self.failUnlessArgIsOut(NSManagedObject.validateValue_forKey_error_, 2)

        self.failUnlessResultIsBOOL(NSManagedObject.validateForDelete_)
        self.failUnlessArgIsOut(NSManagedObject.validateForDelete_, 0)

        self.failUnlessResultIsBOOL(NSManagedObject.validateForInsert_)
        self.failUnlessArgIsOut(NSManagedObject.validateForInsert_, 0)

        self.failUnlessResultIsBOOL(NSManagedObject.validateForUpdate_)
        self.failUnlessArgIsOut(NSManagedObject.validateForUpdate_, 0)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSManagedObject.hasFaultForRelationshipNamed_)

if __name__ == "__main__":
    main()
