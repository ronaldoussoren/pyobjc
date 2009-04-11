
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSManagedObject (TestCase):
    def testMethods(self):
        o = NSManagedObject.alloc().init()
        self.failUnlessResultIsBOOL(o.isInserted)
        self.failUnlessResultIsBOOL(o.isUpdated)
        self.failUnlessResultIsBOOL(o.isDeleted)
        self.failUnlessResultIsBOOL(o.isFault)

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
