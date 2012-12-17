from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSPointerFunctions (TestCase):

    def testConstants(self):
        self.assertEqual(NSPointerFunctionsStrongMemory, (0 << 0))
        self.assertEqual(NSPointerFunctionsZeroingWeakMemory, (1 << 0))
        self.assertEqual(NSPointerFunctionsOpaqueMemory, (2 << 0))
        self.assertEqual(NSPointerFunctionsMallocMemory, (3 << 0))
        self.assertEqual(NSPointerFunctionsMachVirtualMemory, (4 << 0))
        self.assertEqual(NSPointerFunctionsObjectPersonality, (0 << 8))
        self.assertEqual(NSPointerFunctionsOpaquePersonality, (1 << 8))
        self.assertEqual(NSPointerFunctionsObjectPointerPersonality, (2 << 8))
        self.assertEqual(NSPointerFunctionsCStringPersonality, (3 << 8))
        self.assertEqual(NSPointerFunctionsStructPersonality, (4 << 8))
        self.assertEqual(NSPointerFunctionsIntegerPersonality, (5 << 8))

        self.assertEqual(NSPointerFunctionsCopyIn, (1 << 16))

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(NSPointerFunctionsWeakMemory, 5<<0)

    def testPropType(self):
        o = NSPointerFunctions.alloc().initWithOptions_(0)

        v = o.usesStrongWriteBarrier()
        self.assertTrue((v is True) or (v is False) )

        self.assertArgIsBOOL(o.setUsesStrongWriteBarrier_, 0)
        self.assertArgIsBOOL(o.setUsesWeakReadAndWriteBarriers_, 0)

        v = o.usesWeakReadAndWriteBarriers()
        self.assertTrue((v is True) or (v is False) )

if __name__ == "__main__":
    main()
