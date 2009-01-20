
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSManagedObjectID (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSManagedObjectID.isTemporaryID)

if __name__ == "__main__":
    main()
