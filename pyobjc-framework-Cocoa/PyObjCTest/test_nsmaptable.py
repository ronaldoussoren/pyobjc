import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestNSMapTable(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSMapTableStrongMemory, 0)
        self.assertEqual(
            Foundation.NSMapTableZeroingWeakMemory,
            Foundation.NSPointerFunctionsZeroingWeakMemory,
        )
        self.assertEqual(
            Foundation.NSMapTableCopyIn, Foundation.NSPointerFunctionsCopyIn
        )
        self.assertEqual(
            Foundation.NSMapTableObjectPointerPersonality,
            Foundation.NSPointerFunctionsObjectPointerPersonality,
        )

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(
            Foundation.NSMapTableWeakMemory, Foundation.NSPointerFunctionsWeakMemory
        )

    @expectedFailure
    def testFunctions(self):
        self.fail("NSMapTable C-API is untested")
