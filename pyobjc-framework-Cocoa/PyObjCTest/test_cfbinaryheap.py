from CoreFoundation import *

from PyObjCTools.TestSupport import *

class TestCFBinaryHeap (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFBinaryHeapRef)

    def testCreation(self):
        heap = CFBinaryHeapCreate(
                None, 0)
        self.assert_(isinstance(heap, CFBinaryHeapRef))

        CFBinaryHeapAddValue(heap, "hello")
        CFBinaryHeapAddValue(heap, "world")
        CFBinaryHeapAddValue(heap, "aapjes")

        self.assertTrue(CFBinaryHeapContainsValue(heap, "hello"))
        self.assertFalse(CFBinaryHeapContainsValue(heap, "niemand"))

    def testApply(self):
        def compare(l, r, info):
            return cmp(l, r)

        heap = CFBinaryHeapCreate(
                None, 0)
        self.assert_(isinstance(heap, CFBinaryHeapRef))

        CFBinaryHeapAddValue(heap, "hello")
        CFBinaryHeapAddValue(heap, "world")
        CFBinaryHeapAddValue(heap, "aapjes")

        items = []
        contexts = []

        def function(item, context):
            items.append(item * 2)
            contexts.append(context)

        CFBinaryHeapApplyFunction(heap, function, None)
        self.assertEqual(contexts, [None, None, None])
        self.assertEqual(items, ["aapjesaapjes", "hellohello", "worldworld"])

        ctx = ['']
        def function(item, context):
            context[0] += item
        CFBinaryHeapApplyFunction(heap, function, ctx)
        self.assertEqual(ctx[0], 'aapjeshelloworld')


    def testTypeID(self):
        v = CFBinaryHeapGetTypeID()
        self.assertIsInstance(v, (int, long))
    def testCopy(self):
        heap = CFBinaryHeapCreate(
                None, 0)
        self.assert_(isinstance(heap, CFBinaryHeapRef))

        CFBinaryHeapAddValue(heap, "hello")
        CFBinaryHeapAddValue(heap, "world")
        CFBinaryHeapAddValue(heap, "aapjes")

        heap2 = CFBinaryHeapCreateCopy(None, 0, heap)
        self.assert_(isinstance(heap2, CFBinaryHeapRef))

    def testInspect(self):
        from Foundation import NSString, NSLog
        heap = CFBinaryHeapCreate(
                None, 0)
        self.assert_(isinstance(heap, CFBinaryHeapRef))


        CFBinaryHeapAddValue(heap, "hello")
        CFBinaryHeapAddValue(heap, "world")
        CFBinaryHeapAddValue(heap, "aapjes")

        #ok, min = CFBinaryHeapGetMinimumIfPresent(heap, None)
        #self.assertTrue(ok)
        #self.assertEqual(min, "aapjes")
        #self.fail()

        count = CFBinaryHeapGetCount(heap)
        self.assertEqual(count, 3)

        count = CFBinaryHeapGetCountOfValue(heap, "hello")
        self.assertEqual(count, 1)
        count = CFBinaryHeapGetCountOfValue(heap, "fobar")
        self.assertEqual(count, 0)

        self.assertTrue(CFBinaryHeapContainsValue(heap, "hello"))
        self.assertFalse(CFBinaryHeapContainsValue(heap, "foobar"))

        min = CFBinaryHeapGetMinimum(heap)
        self.assertEqual(min, "aapjes")

        count = CFBinaryHeapGetCount(heap)
        self.assertEqual(count, 3)

        #ok, min = CFBinaryHeapGetMinimumIfPresent(heap, None)
        #self.assertTrue(ok)
        #self.assertEqual(min, "aapjes")
        #self.fail()

        values = CFBinaryHeapGetValues(heap)
        self.assertEqual(values, ("aapjes", "hello", "world"))

        CFBinaryHeapRemoveMinimumValue(heap)
        values = CFBinaryHeapGetValues(heap)
        self.assertEqual(values, ("hello", "world"))

        CFBinaryHeapRemoveAllValues(heap)
        values = CFBinaryHeapGetValues(heap)
        self.assertEqual(values, ())

    def testFunctions(self):
        self.assertArgHasType(CFBinaryHeapGetCountOfValue, 1, b'@')
        self.assertArgHasType(CFBinaryHeapContainsValue, 1, b'@')
        self.assertResultHasType(CFBinaryHeapGetMinimum, b'@')
        self.assertResultHasType(CFBinaryHeapGetMinimumIfPresent, objc._C_NSBOOL)
        self.assertArgHasType(CFBinaryHeapGetMinimumIfPresent, 1, b'o^@')
        self.assertArgIsFunction(CFBinaryHeapApplyFunction, 1, b'v@@', False)
        self.assertArgHasType(CFBinaryHeapApplyFunction, 2, b'@')
        self.assertArgHasType(CFBinaryHeapAddValue, 1, b'@')

if __name__ == "__main__":
    main()
