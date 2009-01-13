from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSHashTable (TestCase):
    def testConstants(self):
        self.assertEquals(NSHashTableStrongMemory, 0)
        self.assertEquals(NSHashTableZeroingWeakMemory, NSPointerFunctionsZeroingWeakMemory)
        self.assertEquals(NSHashTableCopyIn, NSPointerFunctionsCopyIn)
        self.assertEquals(NSHashTableObjectPointerPersonality, NSPointerFunctionsObjectPointerPersonality)

    def testFunctions(self):
        self.fail("NSHasTable functions")

if __name__ == "__main__":
    main()
