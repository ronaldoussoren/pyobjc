import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSAtomicStore(TestCase):
    def testConstants(self):
        self.assertEqual(CoreData.NSPersistentHistoryChangeTypeInsert, 0)
        self.assertEqual(CoreData.NSPersistentHistoryChangeTypeUpdate, 1)
        self.assertEqual(CoreData.NSPersistentHistoryChangeTypeDelete, 2)
