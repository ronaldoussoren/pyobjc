from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSMapTable (TestCase):
    def testConstants(self):
        self.assertEqual(NSMapTableStrongMemory, 0)
        self.assertEqual(NSMapTableZeroingWeakMemory, NSPointerFunctionsZeroingWeakMemory)
        self.assertEqual(NSMapTableCopyIn, NSPointerFunctionsCopyIn)
        self.assertEqual(NSMapTableObjectPointerPersonality, NSPointerFunctionsObjectPointerPersonality)

    @expectedFailure
    def testFunctions(self):
        self.fail("NSMapTable C-API is untested")

if __name__ == "__main__":
    main()
