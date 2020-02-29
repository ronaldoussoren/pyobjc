from CoreData import *
from PyObjCTools.TestSupport import *


class TestNSAtomicStore(TestCase):
    def testConstants(self):
        self.assertEqual(NSPersistentHistoryChangeTypeInsert, 0)
        self.assertEqual(NSPersistentHistoryChangeTypeUpdate, 1)
        self.assertEqual(NSPersistentHistoryChangeTypeDelete, 2)


if __name__ == "__main__":
    main()
