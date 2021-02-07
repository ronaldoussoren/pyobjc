import CoreFoundation
from PyObjCTools.TestSupport import TestCase
import objc


class TestCFBinaryHeap(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFBinaryHeapRef)

    def testCreation(self):
        heap = CoreFoundation.CFBinaryHeapCreate(None, 0)
        self.assertIsInstance(heap, CoreFoundation.CFBinaryHeapRef)

        CoreFoundation.CFBinaryHeapAddValue(heap, "hello")
        CoreFoundation.CFBinaryHeapAddValue(heap, "world")
        CoreFoundation.CFBinaryHeapAddValue(heap, "aapjes")

        self.assertTrue(CoreFoundation.CFBinaryHeapContainsValue(heap, "hello"))
        self.assertFalse(CoreFoundation.CFBinaryHeapContainsValue(heap, "niemand"))

    def testApply(self):
        def compare(a, b, info):
            if a < b:
                return -1
            elif b < a:
                return 1
            else:
                return 0

        heap = CoreFoundation.CFBinaryHeapCreate(None, 0)
        self.assertIsInstance(heap, CoreFoundation.CFBinaryHeapRef)

        CoreFoundation.CFBinaryHeapAddValue(heap, "hello")
        CoreFoundation.CFBinaryHeapAddValue(heap, "world")
        CoreFoundation.CFBinaryHeapAddValue(heap, "aapjes")

        items = []
        contexts = []

        def function(item, context):
            items.append(item * 2)
            contexts.append(context)

        CoreFoundation.CFBinaryHeapApplyFunction(heap, function, None)
        self.assertEqual(contexts, [None, None, None])
        self.assertEqual(items, ["aapjesaapjes", "hellohello", "worldworld"])

        ctx = [""]

        def function(item, context):
            context[0] += item

        CoreFoundation.CFBinaryHeapApplyFunction(heap, function, ctx)
        self.assertEqual(ctx[0], "aapjeshelloworld")

    def testTypeID(self):
        v = CoreFoundation.CFBinaryHeapGetTypeID()
        self.assertIsInstance(v, int)

    def testCopy(self):
        heap = CoreFoundation.CFBinaryHeapCreate(None, 0)
        self.assertIsInstance(heap, CoreFoundation.CFBinaryHeapRef)

        CoreFoundation.CFBinaryHeapAddValue(heap, "hello")
        CoreFoundation.CFBinaryHeapAddValue(heap, "world")
        CoreFoundation.CFBinaryHeapAddValue(heap, "aapjes")

        heap2 = CoreFoundation.CFBinaryHeapCreateCopy(None, 0, heap)
        self.assertIsInstance(heap2, CoreFoundation.CFBinaryHeapRef)

    def testInspect(self):
        heap = CoreFoundation.CFBinaryHeapCreate(None, 0)
        self.assertIsInstance(heap, CoreFoundation.CFBinaryHeapRef)

        CoreFoundation.CFBinaryHeapAddValue(heap, "hello")
        CoreFoundation.CFBinaryHeapAddValue(heap, "world")
        CoreFoundation.CFBinaryHeapAddValue(heap, "aapjes")

        # ok, min = CoreFoundation.CFBinaryHeapGetMinimumIfPresent(heap, None)
        # self.assertTrue(ok)
        # self.assertEqual(min, "aapjes")
        # self.fail()

        count = CoreFoundation.CFBinaryHeapGetCount(heap)
        self.assertEqual(count, 3)

        count = CoreFoundation.CFBinaryHeapGetCountOfValue(heap, "hello")
        self.assertEqual(count, 1)
        count = CoreFoundation.CFBinaryHeapGetCountOfValue(heap, "fobar")
        self.assertEqual(count, 0)

        self.assertTrue(CoreFoundation.CFBinaryHeapContainsValue(heap, "hello"))
        self.assertFalse(CoreFoundation.CFBinaryHeapContainsValue(heap, "foobar"))

        min_value = CoreFoundation.CFBinaryHeapGetMinimum(heap)
        self.assertEqual(min_value, "aapjes")

        count = CoreFoundation.CFBinaryHeapGetCount(heap)
        self.assertEqual(count, 3)

        values = CoreFoundation.CFBinaryHeapGetValues(heap)
        self.assertEqual(values, ("aapjes", "hello", "world"))

        CoreFoundation.CFBinaryHeapRemoveMinimumValue(heap)
        values = CoreFoundation.CFBinaryHeapGetValues(heap)
        self.assertEqual(values, ("hello", "world"))

        CoreFoundation.CFBinaryHeapRemoveAllValues(heap)
        values = CoreFoundation.CFBinaryHeapGetValues(heap)
        self.assertEqual(values, ())

    def testFunctions(self):
        self.assertArgHasType(CoreFoundation.CFBinaryHeapGetCountOfValue, 1, b"@")
        self.assertArgHasType(CoreFoundation.CFBinaryHeapContainsValue, 1, b"@")
        self.assertResultHasType(CoreFoundation.CFBinaryHeapGetMinimum, b"@")
        self.assertResultHasType(
            CoreFoundation.CFBinaryHeapGetMinimumIfPresent, objc._C_NSBOOL
        )
        self.assertArgHasType(CoreFoundation.CFBinaryHeapGetMinimumIfPresent, 1, b"o^@")
        self.assertArgIsFunction(
            CoreFoundation.CFBinaryHeapApplyFunction, 1, b"v@@", False
        )
        self.assertArgHasType(CoreFoundation.CFBinaryHeapApplyFunction, 2, b"@")
        self.assertArgHasType(CoreFoundation.CFBinaryHeapAddValue, 1, b"@")
