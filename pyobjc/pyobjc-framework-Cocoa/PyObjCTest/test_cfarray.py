import unittest
from CoreFoundation import *
from Foundation import NSArray, NSMutableArray

class TestCFArray (unittest.TestCase):
    def testCFArrayIsNSArray(self):
        self.assert_(issubclass(CFArrayRef, NSArray))
        self.assert_(issubclass(CFMutableArrayRef, NSMutableArray))

    def testCFArrayCreate(self):
        array = CFArrayCreate(None, [1,2,3,4], 4)
        self.assertEquals(array, [1,2,3,4])
        self.assert_(isinstance(array, CFArrayRef))

        array = CFArrayCreateMutable(None, 0)
        CFArrayAppendValue(array, 42)
        CFArrayAppendValue(array, 43)
        CFArrayAppendValue(array, 44)
        self.assertEquals(array, [42, 43, 44])
        self.assert_(isinstance(array, CFMutableArrayRef))

    def testCFArrayApplyFunction(self):
        array = CFArrayCreate(None, [1,2,3,4], 4)
        
        items = []
        infos = []

        def applier(item, info):
            items.append(item * item)
            infos.append(info)

        CFArrayApplyFunction(array, (0, 4), applier, 42)
        self.assertEquals(items, [1,4,9,16])
        self.assertEquals(infos, [42,42,42,42])

        items = []
        infos = []
        CFArrayApplyFunction(array, (1, 2), applier, 42)
        self.assertEquals(items, [4,9])
        self.assertEquals(infos, [42,42])

    def testBSearchValues(self):
        # This method causes a hard crash, reason unclear.
        array = CFArrayCreate(None, range(20), 20)

        def compare(l, r, context):
            return cmp(l, r)

        r = CFArrayBSearchValues(array, (0, 20), 10, compare, None)
        self.assertEquals(r, 10)

        r = CFArrayBSearchValues(array, (0, 20), 9.5, compare, None)
        self.assertEquals(r, 10)

        r = CFArrayBSearchValues(array, (0, 20), 99, compare, None)
        self.assert_(r >= 20)

        r = CFArrayBSearchValues(array, (0, 20), -1, compare, None)
        self.assertEquals(r, 0)

    def testSortValues(self):
        array = NSMutableArray.arrayWithArray_([4,2,1,3,0,5])

        def compare(l, r, context):
            return cmp(l, r)
        CFArraySortValues(array, (0, 6), compare, None)

        self.assertEquals(array, [0, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
