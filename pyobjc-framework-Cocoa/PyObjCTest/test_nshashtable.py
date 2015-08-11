from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSHashTable (TestCase):
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
