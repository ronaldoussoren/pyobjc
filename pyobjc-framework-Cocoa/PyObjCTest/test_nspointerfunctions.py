import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestNSPointerFunctions(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSPointerFunctionsOptions)

    def testConstants(self):
        self.assertEqual(Foundation.NSPointerFunctionsStrongMemory, (0 << 0))
        self.assertEqual(Foundation.NSPointerFunctionsZeroingWeakMemory, (1 << 0))
        self.assertEqual(Foundation.NSPointerFunctionsOpaqueMemory, (2 << 0))
        self.assertEqual(Foundation.NSPointerFunctionsMallocMemory, (3 << 0))
        self.assertEqual(Foundation.NSPointerFunctionsMachVirtualMemory, (4 << 0))
        self.assertEqual(Foundation.NSPointerFunctionsObjectPersonality, (0 << 8))
        self.assertEqual(Foundation.NSPointerFunctionsOpaquePersonality, (1 << 8))
        self.assertEqual(
            Foundation.NSPointerFunctionsObjectPointerPersonality, (2 << 8)
        )
        self.assertEqual(Foundation.NSPointerFunctionsCStringPersonality, (3 << 8))
        self.assertEqual(Foundation.NSPointerFunctionsStructPersonality, (4 << 8))
        self.assertEqual(Foundation.NSPointerFunctionsIntegerPersonality, (5 << 8))

        self.assertEqual(Foundation.NSPointerFunctionsCopyIn, (1 << 16))

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(Foundation.NSPointerFunctionsWeakMemory, 5 << 0)

    def testPropType(self):
        o = Foundation.NSPointerFunctions.alloc().initWithOptions_(0)

        v = o.usesStrongWriteBarrier()
        self.assertTrue((v is True) or (v is False))

        self.assertArgIsBOOL(o.setUsesStrongWriteBarrier_, 0)
        self.assertArgIsBOOL(o.setUsesWeakReadAndWriteBarriers_, 0)

        v = o.usesWeakReadAndWriteBarriers()
        self.assertTrue((v is True) or (v is False))

    @expectedFailure
    def testCallbacks(self):
        self.fail("pointer personality functions")
