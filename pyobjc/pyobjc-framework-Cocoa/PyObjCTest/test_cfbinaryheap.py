from CoreFoundation import *

from PyObjCTools.TestSupport import *

class TestCFBinaryHeap (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFBinaryHeapRef)

    def testCreation(self):
        heap = CFBinaryHeapCreate(
                None, 0)
        self.assert_(isinstance(heap, CFBinaryHeapRef))

        CFBinaryHeapAddValue(heap, "hello")
        CFBinaryHeapAddValue(heap, "world")
        CFBinaryHeapAddValue(heap, "aapjes")

        self.failUnless(CFBinaryHeapContainsValue(heap, "hello"))
        self.failIf(CFBinaryHeapContainsValue(heap, "niemand"))

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
        self.assertEquals(contexts, [None, None, None])
        self.assertEquals(items, ["aapjesaapjes", "hellohello", "worldworld"])

        ctx = ['']
        def function(item, context):
            context[0] += item
        CFBinaryHeapApplyFunction(heap, function, ctx)
        self.assertEquals(ctx[0], 'aapjeshelloworld')


    def testTypeID(self):
        v = CFBinaryHeapGetTypeID()
        self.failUnless(  isinstance(v, (int, long))  )

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
        #self.failUnless(ok)
        #self.failUnlessEqual(min, "aapjes")
        #self.fail()

        count = CFBinaryHeapGetCount(heap)
        self.failUnlessEqual(count, 3)

        count = CFBinaryHeapGetCountOfValue(heap, "hello")
        self.failUnlessEqual(count, 1)
        count = CFBinaryHeapGetCountOfValue(heap, "fobar")
        self.failUnlessEqual(count, 0)

        self.failUnless(CFBinaryHeapContainsValue(heap, "hello"))
        self.failIf(CFBinaryHeapContainsValue(heap, "foobar"))

        min = CFBinaryHeapGetMinimum(heap)
        self.failUnlessEqual(min, "aapjes")

        count = CFBinaryHeapGetCount(heap)
        self.failUnlessEqual(count, 3)

        #ok, min = CFBinaryHeapGetMinimumIfPresent(heap, None)
        #self.failUnless(ok)
        #self.failUnlessEqual(min, "aapjes")
        #self.fail()

        values = CFBinaryHeapGetValues(heap)
        self.failUnlessEqual(values, ("aapjes", "hello", "world"))

        CFBinaryHeapRemoveMinimumValue(heap)
        values = CFBinaryHeapGetValues(heap)
        self.failUnlessEqual(values, ("hello", "world"))

        CFBinaryHeapRemoveAllValues(heap)
        values = CFBinaryHeapGetValues(heap)
        self.failUnlessEqual(values, ())

    def testFunctions(self):
        self.failUnlessArgHasType(CFBinaryHeapGetCountOfValue, 1, '@')
        self.failUnlessArgHasType(CFBinaryHeapContainsValue, 1, '@')
        self.failUnlessResultHasType(CFBinaryHeapGetMinimum, '@')
        self.failUnlessResultHasType(CFBinaryHeapGetMinimumIfPresent, objc._C_NSBOOL)
        self.failUnlessArgHasType(CFBinaryHeapGetMinimumIfPresent, 1, 'o^@')
        self.failUnlessArgIsFunction(CFBinaryHeapApplyFunction, 1, 'v@@', False)
        self.failUnlessArgHasType(CFBinaryHeapApplyFunction, 2, '@')
        self.failUnlessArgHasType(CFBinaryHeapAddValue, 1, '@')

if __name__ == "__main__":
    main()
