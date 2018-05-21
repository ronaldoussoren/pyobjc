from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSHashTable (TestCase):
    def testConvenience(self):
        v = NSHashTable.hashTableWithOptions_(NSPointerFunctionsObjectPersonality)
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
        self.assertIn(v.pop(), {1,2,3})
        self.assertIn(v.pop(), {1,2,3})
        self.assertIn(v.pop(), {1,2,3})
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
        self.assertEqual(NSHashTableStrongMemory, 0)
        self.assertEqual(NSHashTableZeroingWeakMemory, NSPointerFunctionsZeroingWeakMemory)
        self.assertEqual(NSHashTableCopyIn, NSPointerFunctionsCopyIn)
        self.assertEqual(NSHashTableObjectPointerPersonality, NSPointerFunctionsObjectPointerPersonality)

    @min_os_level('10.8')
    def testConstants(self):
        self.assertEqual(NSHashTableWeakMemory, NSPointerFunctionsWeakMemory)

    @expectedFailure
    def testFunctions(self):
        self.fail("NSHasTable functions")


    def testMethods(self):
        self.assertResultIsBOOL(NSHashTable.containsObject_)
        self.assertResultIsBOOL(NSHashTable.intersectsHashTable_)
        self.assertResultIsBOOL(NSHashTable.isEqualToHashTable_)
        self.assertResultIsBOOL(NSHashTable.isSubsetOfHashTable_)

if __name__ == "__main__":
    main()
