from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPersistentStoreResult (TestCase):
    def testConstants(self):
        self.assertEqual(NSStatusOnlyResultType, 0)
        self.assertEqual(NSUpdatedObjectIDsResultType, 1)
        self.assertEqual(NSUpdatedObjectsCountResultType, 2)

        self.assertEqual(NSBatchDeleteResultTypeStatusOnly, 0)
        self.assertEqual(NSBatchDeleteResultTypeObjectIDs, 1)
        self.assertEqual(NSBatchDeleteResultTypeCount, 2)

if __name__ == "__main__":
    main()
