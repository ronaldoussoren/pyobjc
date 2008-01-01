from CoreFoundation import *

import unittest

class TestCFBinaryHeap (unittest.TestCase):
    def dont_testCreation(self):
        def compare(l, r, info):
            return cmp(l, r)

        heap = CFBinaryHeapCreate(
                None, 0, 
                kCFStringBinaryHeapCallBacks,
                None)
        self.assert_(isinstance(heap, CFBinaryHeapRef))

        CFBinaryHeapAddValue(heap, "hello")
        CFBinaryHeapAddValue(heap, "world")
        CFBinaryHeapAddValue(heap, "aapjes")

        self.failUnless(CFBinaryHeapContainsValue("hello"))
        self.failIf(CFBinaryHeapContainsValue("niemand"))

    def dont_testApply(self):
        def compare(l, r, info):
            return cmp(l, r)

        heap = CFBinaryHeapCreate(
                None, 0, 
                kCFStringBinaryHeapCallBacks,
                None)
        self.assert_(isinstance(heap, CFBinaryHeapRef))

        CFBinaryHeapAddValue(heap, "hello")
        CFBinaryHeapAddValue(heap, "world")
        CFBinaryHeapAddValue(heap, "aapjes")

        items = []
        contexts = []

        def function(item, context):
            items.append(item * 2)
            context.append(context)

        CFBinaryHeapApplyFunction(heap, function, None)
        self.assertEquals(contexts, [None, None, None])
        #items.sort()
        self.assertEquals(items, ["aapjesaapjes", "hellohello", "worldworld"])

if __name__ == "__main__":
    unittest.main()
