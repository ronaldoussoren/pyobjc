from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSMapTable (TestCase):
    def testConstants(self):
        self.assertEqual(NSMapTableStrongMemory, 0)
        self.assertEqual(NSMapTableZeroingWeakMemory, NSPointerFunctionsZeroingWeakMemory)
        self.assertEqual(NSMapTableCopyIn, NSPointerFunctionsCopyIn)
        self.assertEqual(NSMapTableObjectPointerPersonality, NSPointerFunctionsObjectPointerPersonality)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(NSMapTableWeakMemory, NSPointerFunctionsWeakMemory)

    @expectedFailure
    def testFunctions(self):
        self.fail("NSMapTable C-API is untested")

if __name__ == "__main__":
    main()
