from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSMapTable (TestCase):
    def testConstants(self):
        self.assertEquals(NSMapTableStrongMemory, 0)
        self.assertEquals(NSMapTableZeroingWeakMemory, NSPointerFunctionsZeroingWeakMemory)
        self.assertEquals(NSMapTableCopyIn, NSPointerFunctionsCopyIn)
        self.assertEquals(NSMapTableObjectPointerPersonality, NSPointerFunctionsObjectPointerPersonality)

    @expectedFailure
    def testFunctions(self):
        self.fail("NSMapTable C-API is untested")

if __name__ == "__main__":
    main()
