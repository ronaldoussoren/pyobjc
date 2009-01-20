
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSManagedObjectModel (TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSManagedObjectModel.isConfiguration_compatibleWithStoreMetadata_)

if __name__ == "__main__":
    main()
