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

        self.assertEqual(NSPersistentHistoryResultTypeStatusOnly, 0x0)
        self.assertEqual(NSPersistentHistoryResultTypeObjectIDs, 0x1,)
        self.assertEqual(NSPersistentHistoryResultTypeCount, 0x2)
        self.assertEqual(NSPersistentHistoryResultTypeTransactionsOnly, 0x3)
        self.assertEqual(NSPersistentHistoryResultTypeChangesOnly, 0x4)
        self.assertEqual(NSPersistentHistoryResultTypeTransactionsAndChanges, 0x5)

if __name__ == "__main__":
    main()
