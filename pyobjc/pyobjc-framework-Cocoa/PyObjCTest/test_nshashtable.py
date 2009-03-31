from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSHashTable (TestCase):
    def testConstants(self):
        self.assertEquals(NSHashTableStrongMemory, 0)
        self.assertEquals(NSHashTableZeroingWeakMemory, NSPointerFunctionsZeroingWeakMemory)
        self.assertEquals(NSHashTableCopyIn, NSPointerFunctionsCopyIn)
        self.assertEquals(NSHashTableObjectPointerPersonality, NSPointerFunctionsObjectPointerPersonality)

    @expectedFailure
    def testFunctions(self):
        self.fail("NSHasTable functions")


    def testMethods(self):
        self.failUnlessResultIsBOOL(NSHashTable.containsObject_)
        self.failUnlessResultIsBOOL(NSHashTable.intersectsHashTable_)
        self.failUnlessResultIsBOOL(NSHashTable.isEqualToHashTable_)
        self.failUnlessResultIsBOOL(NSHashTable.isSubsetOfHashTable_)

if __name__ == "__main__":
    main()
