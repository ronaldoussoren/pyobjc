from CoreData import *
from PyObjCTools.TestSupport import *


class TestNSManagedObjectID(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSManagedObjectID.isTemporaryID)


if __name__ == "__main__":
    main()
