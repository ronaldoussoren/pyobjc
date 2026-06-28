import Foundation
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestNSMapTable(TestCase):
    def test_constants(self):
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

        self.assertEqual(
            Foundation.NSMapTableWeakMemory, Foundation.NSPointerFunctionsWeakMemory
        )

    @expectedFailure
    def test_functions(self):
        self.fail("NSMapTable C-API is untested")
