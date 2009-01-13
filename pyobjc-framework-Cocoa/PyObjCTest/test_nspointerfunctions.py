from PyObjCTools.TestSupport import * 

from Foundation import *


class TestNSPointerFunctions (TestCase):

    def testConstants(self):
        self.assertEquals(NSPointerFunctionsStrongMemory, (0 << 0))
        self.assertEquals(NSPointerFunctionsZeroingWeakMemory, (1 << 0))
        self.assertEquals(NSPointerFunctionsOpaqueMemory, (2 << 0))
        self.assertEquals(NSPointerFunctionsMallocMemory, (3 << 0))
        self.assertEquals(NSPointerFunctionsMachVirtualMemory, (4 << 0))
        self.assertEquals(NSPointerFunctionsObjectPersonality, (0 << 8))
        self.assertEquals(NSPointerFunctionsOpaquePersonality, (1 << 8))
        self.assertEquals(NSPointerFunctionsObjectPointerPersonality, (2 << 8))
        self.assertEquals(NSPointerFunctionsCStringPersonality, (3 << 8))
        self.assertEquals(NSPointerFunctionsStructPersonality, (4 << 8))
        self.assertEquals(NSPointerFunctionsIntegerPersonality, (5 << 8))

        self.assertEquals(NSPointerFunctionsCopyIn, (1 << 16))

    def testPropType(self):
        o = NSPointerFunctions.alloc().initWithOptions_(0)

        v = o.usesStrongWriteBarrier()
        self.failUnless( (v is True) or (v is False) )

        v = o.usesWeakReadAndWriteBarriers()
        self.failUnless( (v is True) or (v is False) )

if __name__ == "__main__":
    main()
