import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestNSHashTable(TestCase):
    def testConvenience(self):
        v = Foundation.NSHashTable.hashTableWithOptions_(
            Foundation.NSPointerFunctionsObjectPersonality
        )
        self.assertEqual(len(v), 0)

        v.add(32)
        v.add(2)

        self.assertIn(32, v)
        self.assertNotIn(42, v)

        self.assertNotIn(1, v)
        self.assertIn(2, v)
        v.remove(2)
        v.remove(1)
        self.assertNotIn(1, v)
        self.assertNotIn(2, v)

        v.clear()
        self.assertEqual(len(v), 0)

        v.add(1)
        v.add(2)
        v.add(3)

        self.assertEqual(len(v), 3)
        self.assertIn(v.pop(), {1, 2, 3})
        self.assertIn(v.pop(), {1, 2, 3})
        self.assertIn(v.pop(), {1, 2, 3})
        self.assertEqual(len(v), 0)

        v.add(None)
        self.assertEqual(len(v), 1)
        self.assertIn(None, v)
        v.remove(None)
        self.assertEqual(len(v), 0)

        v.add(None)
        o = v.pop()
        self.assertEqual(o, None)
        self.assertEqual(len(v), 0)

    def testConstants(self):
        self.assertEqual(Foundation.NSHashTableStrongMemory, 0)
        self.assertEqual(
            Foundation.NSHashTableZeroingWeakMemory,
            Foundation.NSPointerFunctionsZeroingWeakMemory,
        )
        self.assertEqual(
            Foundation.NSHashTableCopyIn, Foundation.NSPointerFunctionsCopyIn
        )
        self.assertEqual(
            Foundation.NSHashTableObjectPointerPersonality,
            Foundation.NSPointerFunctionsObjectPointerPersonality,
        )

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(
            Foundation.NSHashTableWeakMemory, Foundation.NSPointerFunctionsWeakMemory
        )

    @expectedFailure
    def testFunctions(self):
        self.fail("NSHasTable functions")

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSHashTable.containsObject_)
        self.assertResultIsBOOL(Foundation.NSHashTable.intersectsHashTable_)
        self.assertResultIsBOOL(Foundation.NSHashTable.isEqualToHashTable_)
        self.assertResultIsBOOL(Foundation.NSHashTable.isSubsetOfHashTable_)
