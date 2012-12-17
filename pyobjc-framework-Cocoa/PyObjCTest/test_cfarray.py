from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import NSArray, NSMutableArray

import sys

try:
    long
except NameError:
    long = int

if sys.version_info[0] == 3:
    def cmp(a, b):
        if a < b:
            return -1
        elif b < a:
            return 1
        return 0


class TestCFArray (TestCase):
    def testCFArrayIsNSArray(self):
        self.assertTrue(issubclass(CFArrayRef, NSArray))
        self.assertTrue(issubclass(CFMutableArrayRef, NSMutableArray))

    def testCFArrayCreate(self):
        array = CFArrayCreate(None, [1,2,3,4], 4, kCFTypeArrayCallBacks)
        self.assertEqual(array, [1,2,3,4])
        self.assertIsInstance(array, NSArray)

        array = CFArrayCreateMutable(None, 0, kCFTypeArrayCallBacks)
        CFArrayAppendValue(array, 42)
        CFArrayAppendValue(array, 43)
        CFArrayAppendValue(array, 44)
        self.assertEqual(array, [42, 43, 44])
        self.assertIsInstance(array, CFMutableArrayRef)

    def testCFArrayApplyFunction(self):
        array = CFArrayCreate(None, [1,2,3,4], 4, kCFTypeArrayCallBacks)

        self.assertArgIsFunction(CFArrayApplyFunction, 2, b'v@@', False)
        self.assertArgHasType(CFArrayApplyFunction, 3, b'@')

        items = []
        infos = []

        def applier(item, info):
            items.append(item * item)
            infos.append(info)

        CFArrayApplyFunction(array, (0, 4), applier, 42)
        self.assertEqual(items, [1,4,9,16])
        self.assertEqual(infos, [42,42,42,42])

        items = []
        infos = []
        CFArrayApplyFunction(array, (1, 2), applier, 42)
        self.assertEqual(items, [4,9])
        self.assertEqual(infos, [42,42])

    def testBSearchValues(self):
        # This method causes a hard crash, reason unclear.
        array = CFArrayCreate(None, range(20), 20, kCFTypeArrayCallBacks)

        self.assertArgHasType(CFArrayBSearchValues, 2, b'@')
        self.assertArgIsFunction(CFArrayBSearchValues, 3, b'l@@@', False)
        self.assertArgHasType(CFArrayBSearchValues, 4, b'@')

        def compare(l, r, context):
            return cmp(l, r)

        r = CFArrayBSearchValues(array, (0, 20), 10, compare, None)
        self.assertEqual(r, 10)

        r = CFArrayBSearchValues(array, (0, 20), 9.5, compare, None)
        self.assertEqual(r, 10)

        r = CFArrayBSearchValues(array, (0, 20), 99, compare, None)
        self.assertTrue(r >= 20)

        r = CFArrayBSearchValues(array, (0, 20), -1, compare, None)
        self.assertEqual(r, 0)

    def testSortValues(self):
        array = NSMutableArray.arrayWithArray_([4,2,1,3,0,5])

        self.assertArgIsFunction(CFArraySortValues, 2, b'l@@@', False)
        self.assertArgHasType(CFArraySortValues, 3, b'@')

        def compare(l, r, context):
            return cmp(l, r)
        CFArraySortValues(array, (0, 6), compare, None)

        self.assertEqual(array, [0, 1, 2, 3, 4, 5])

    def testTypeID(self):
        v = CFArrayGetTypeID()
        self.assertIsInstance(v, (int, long))

    def testCopy(self):
        array = CFArrayCreate(None, [1,2,3,4], 4, kCFTypeArrayCallBacks)
        self.assertEqual(array, [1,2,3,4])
        self.assertIsInstance(array, NSArray)

        cpy = CFArrayCreateCopy(None, array)
        self.assertEqual(cpy, [1,2,3,4])
        self.assertIsInstance(cpy, NSArray)

        cpy = CFArrayCreateMutableCopy(None, 0, array)
        self.assertEqual(cpy, [1,2,3,4])
        self.assertIsInstance(cpy, CFMutableArrayRef)
        self.assertIsNot(cpy, array )

    def testCounts(self):
        array = CFArrayCreate(None, [1,2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEqual(array, [1,2,3,4,4,2])
        self.assertIsInstance(array, NSArray)

        self.assertEqual(CFArrayGetCount(array) , 6 )
        self.assertEqual(CFArrayGetCountOfValue(array, (0,6), 4) , 2 )
        self.assertEqual(CFArrayGetCountOfValue(array, (0,6), 2) , 2 )
        self.assertEqual(CFArrayGetCountOfValue(array, (0,6), 3) , 1 )

    def testContains(self):
        array = CFArrayCreate(None, [b"a".decode('latin1'),2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEqual(array, [b"a".decode('latin1'),2,3,4,4,2])
        self.assertIsInstance(array, NSArray)

        self.assertFalse( CFArrayContainsValue(array, (0, 6), b"hello".decode('latin1')) )
        self.assertTrue( CFArrayContainsValue(array, (0, 6), 4) )
        self.assertFalse( CFArrayContainsValue(array, (0, 2), 4) )

        self.assertEqual(CFArrayGetFirstIndexOfValue(array, (0, 6), 3) , 2 )
        self.assertEqual(CFArrayGetFirstIndexOfValue(array, (0, 6), 2) , 1 )
        self.assertEqual(CFArrayGetFirstIndexOfValue(array, (0, 6), b"hello".decode('latin1')) , kCFNotFound )
        self.assertEqual(CFArrayGetLastIndexOfValue(array, (0, 6), 3) , 2 )
        self.assertEqual(CFArrayGetLastIndexOfValue(array, (0, 6), 2) , 5 )
        self.assertEqual(CFArrayGetLastIndexOfValue(array, (0, 6), b"hello".decode('latin1')) , kCFNotFound )
        self.assertArgHasType(CFArrayGetFirstIndexOfValue, 2, b'@')
        self.assertArgHasType(CFArrayGetLastIndexOfValue, 2, b'@')

    def testGetting(self):
        array = CFArrayCreate(None, [b"a".decode('latin1'),2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEqual(array, [b"a".decode('latin1'),2,3,4,4,2])
        self.assertIsInstance(array, NSArray)

        self.assertEqual(CFArrayGetValueAtIndex(array, 0) , b"a".decode('latin1')  )
        self.assertEqual(CFArrayGetValueAtIndex(array, 1) , 2  )
        self.assertArgHasType(CFArrayGetValues, 2, b'o^@')
        self.assertArgSizeInArg(CFArrayGetValues, 2, 1)

        vals = CFArrayGetValues(array, (0, 3), None)
        self.assertIsInstance(vals, tuple)
        self.assertEqual(vals , (b"a".decode('latin1'), 2, 3) )

    def testUpdating(self):
        array = CFArrayCreate(None, [b"a".decode('latin1'),2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEqual(array, [b"a".decode('latin1'),2,3,4,4,2])
        self.assertIsInstance(array, NSArray)
        array = CFArrayCreateMutableCopy(None, 0, array)

        self.assertArgHasType(CFArrayAppendValue, 1, b'@')
        self.assertArgHasType(CFArrayInsertValueAtIndex, 2, b'@')
        self.assertArgHasType(CFArraySetValueAtIndex, 2, b'@')

        CFArrayAppendValue(array, b"foo".decode('latin1'))
        self.assertEqual(array, [b"a".decode('latin1'),2,3,4,4,2,b"foo".decode('latin1')])

        CFArrayInsertValueAtIndex(array, 1, 4)
        self.assertEqual(array, [b"a".decode('latin1'),4, 2,3,4,4,2,b"foo".decode('latin1')])

        CFArrayRemoveValueAtIndex(array, 2)
        self.assertEqual(array, [b"a".decode('latin1'),4, 3,4,4,2,b"foo".decode('latin1')])

        CFArraySetValueAtIndex(array, 2, b"two".decode('latin1'))
        self.assertEqual(array, [b"a".decode('latin1'),4, b"two".decode('latin1'),4,4,2,b"foo".decode('latin1')])

        CFArrayExchangeValuesAtIndices(array, 1,2)
        self.assertEqual(array, [b"a".decode('latin1'),b"two".decode('latin1'),4,4,4,2,b"foo".decode('latin1')])

        self.assertArgHasType(CFArrayReplaceValues, 2, b'n^@')
        self.assertArgSizeInArg(CFArrayReplaceValues, 2, 3)
        CFArrayReplaceValues(array, (2,3), (b'a'.decode('latin1'), b'b'.decode('latin1'), b'c'.decode('latin1'), b'd'.decode('latin1'), b'e'.decode('latin1'), b'f'.decode('latin1')), 6)
        self.assertEqual(array, [b"a".decode('latin1'),b"two".decode('latin1'),b'a'.decode('latin1'), b'b'.decode('latin1'), b'c'.decode('latin1'), b'd'.decode('latin1'), b'e'.decode('latin1'), b'f'.decode('latin1'), 2, b'foo'.decode('latin1')])

        array2 = CFArrayCreate(None, [b'hello'.decode('latin1'), b'earth'.decode('latin1')], 2, kCFTypeArrayCallBacks)
        CFArrayAppendArray(array, array2, (0,2))
        self.assertEqual(array, [
            b"a".decode('latin1') ,b"two".decode('latin1') ,b'a'.decode('latin1') , b'b'.decode('latin1') , b'c'.decode('latin1') , b'd'.decode('latin1') , b'e'.decode('latin1') , b'f'.decode('latin1') , 2, b'foo'.decode('latin1') , b'hello'.decode('latin1') , b'earth'.decode('latin1') ])

        CFArrayRemoveAllValues(array)
        self.assertEqual(array, [])


if __name__ == "__main__":
    main()
