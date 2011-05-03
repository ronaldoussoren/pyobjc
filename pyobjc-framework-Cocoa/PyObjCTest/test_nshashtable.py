from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSHashTable (TestCase):
    def testConstants(self):
        self.assertEqual(NSHashTableStrongMemory, 0)
        self.assertEqual(NSHashTableZeroingWeakMemory, NSPointerFunctionsZeroingWeakMemory)
        self.assertEqual(NSHashTableCopyIn, NSPointerFunctionsCopyIn)
        self.assertEqual(NSHashTableObjectPointerPersonality, NSPointerFunctionsObjectPointerPersonality)

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
