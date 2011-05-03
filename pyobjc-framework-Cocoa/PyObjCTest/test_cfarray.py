from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import NSArray, NSMutableArray

import sys
if sys.version_info[0] == 3:
    def cmp(a, b):
        if a < b:
            return -1
        elif b < a:
            return 1
        return 0


class TestCFArray (TestCase):
    def testCFArrayIsNSArray(self):
        self.assert_(issubclass(CFArrayRef, NSArray))
        self.assert_(issubclass(CFMutableArrayRef, NSMutableArray))

    def testCFArrayCreate(self):
        array = CFArrayCreate(None, [1,2,3,4], 4, kCFTypeArrayCallBacks)
        self.assertEqual(array, [1,2,3,4])
        self.assert_(isinstance(array, CFArrayRef))

        array = CFArrayCreateMutable(None, 0, kCFTypeArrayCallBacks)
        CFArrayAppendValue(array, 42)
        CFArrayAppendValue(array, 43)
        CFArrayAppendValue(array, 44)
        self.assertEqual(array, [42, 43, 44])
        self.assert_(isinstance(array, CFMutableArrayRef))

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
        self.assert_(r >= 20)

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
        self.assert_(isinstance(array, CFArrayRef))

        cpy = CFArrayCreateCopy(None, array)
        self.assertEqual(cpy, [1,2,3,4])
        self.assert_(isinstance(cpy, CFArrayRef))

        cpy = CFArrayCreateMutableCopy(None, 0, array)
        self.assertEqual(cpy, [1,2,3,4])
        self.assert_(isinstance(cpy, CFMutableArrayRef))
        self.assertIsNot(cpy, array )
    def testCounts(self):
        array = CFArrayCreate(None, [1,2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEqual(array, [1,2,3,4,4,2])
        self.assert_(isinstance(array, CFArrayRef))

        self.assertEqual(CFArrayGetCount(array) , 6 )
        self.assertEqual(CFArrayGetCountOfValue(array, (0,6), 4) , 2 )
        self.assertEqual(CFArrayGetCountOfValue(array, (0,6), 2) , 2 )
        self.assertEqual(CFArrayGetCountOfValue(array, (0,6), 3) , 1 )
    def testContains(self):
        array = CFArrayCreate(None, [u"a",2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEqual(array, [u"a",2,3,4,4,2])
        self.assert_(isinstance(array, CFArrayRef))

        self.assertFalse( CFArrayContainsValue(array, (0, 6), u"hello") )
        self.assertTrue( CFArrayContainsValue(array, (0, 6), 4) )
        self.assertFalse( CFArrayContainsValue(array, (0, 2), 4) )

        self.assertEqual(CFArrayGetFirstIndexOfValue(array, (0, 6), 3) , 2 )
        self.assertEqual(CFArrayGetFirstIndexOfValue(array, (0, 6), 2) , 1 )
        self.assertEqual(CFArrayGetFirstIndexOfValue(array, (0, 6), u"hello") , kCFNotFound )
        self.assertEqual(CFArrayGetLastIndexOfValue(array, (0, 6), 3) , 2 )
        self.assertEqual(CFArrayGetLastIndexOfValue(array, (0, 6), 2) , 5 )
        self.assertEqual(CFArrayGetLastIndexOfValue(array, (0, 6), u"hello") , kCFNotFound )
        self.assertArgHasType(CFArrayGetFirstIndexOfValue, 2, b'@')
        self.assertArgHasType(CFArrayGetLastIndexOfValue, 2, b'@')


    def testGetting(self):
        array = CFArrayCreate(None, [u"a",2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEqual(array, [u"a",2,3,4,4,2])
        self.assert_(isinstance(array, CFArrayRef))

        self.assertEqual(CFArrayGetValueAtIndex(array, 0) , u"a"  )
        self.assertEqual(CFArrayGetValueAtIndex(array, 1) , 2  )
        self.assertArgHasType(CFArrayGetValues, 2, b'o^@')
        self.assertArgSizeInArg(CFArrayGetValues, 2, 1)

        vals = CFArrayGetValues(array, (0, 3), None)
        self.assertIsInstance(vals, tuple)
        self.assertEqual(vals , (u"a", 2, 3) )
    def testUpdating(self):
        array = CFArrayCreate(None, [u"a",2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEqual(array, [u"a",2,3,4,4,2])
        self.assert_(isinstance(array, CFArrayRef))
        array = CFArrayCreateMutableCopy(None, 0, array)


        self.assertArgHasType(CFArrayAppendValue, 1, b'@')
        self.assertArgHasType(CFArrayInsertValueAtIndex, 2, b'@')
        self.assertArgHasType(CFArraySetValueAtIndex, 2, b'@')

        CFArrayAppendValue(array, u"foo")
        self.assertEqual(array, [u"a",2,3,4,4,2,u"foo"])

        CFArrayInsertValueAtIndex(array, 1, 4)
        self.assertEqual(array, [u"a",4, 2,3,4,4,2,u"foo"])

        CFArrayRemoveValueAtIndex(array, 2)
        self.assertEqual(array, [u"a",4, 3,4,4,2,u"foo"])

        CFArraySetValueAtIndex(array, 2, u"two")
        self.assertEqual(array, [u"a",4, u"two",4,4,2,u"foo"])


        CFArrayExchangeValuesAtIndices(array, 1,2)
        self.assertEqual(array, [u"a",u"two",4,4,4,2,u"foo"])

        self.assertArgHasType(CFArrayReplaceValues, 2, b'n^@')
        self.assertArgSizeInArg(CFArrayReplaceValues, 2, 3)
        CFArrayReplaceValues(array, (2,3), (u'a', u'b', u'c', u'd', u'e', u'f'), 6)
        self.assertEqual(array, [u"a",u"two",u'a', u'b', u'c', u'd', u'e', u'f', 2, u'foo'])

        array2 = CFArrayCreate(None, [u'hello', u'earth'], 2, kCFTypeArrayCallBacks)
        CFArrayAppendArray(array, array2, (0,2))
        self.assertEqual(array, [u"a",u"two",u'a', u'b', u'c', u'd', u'e', u'f', 2, u'foo', u'hello', u'earth'])

        CFArrayRemoveAllValues(array)
        self.assertEqual(array, [])


if __name__ == "__main__":
    main()
