from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import NSArray, NSMutableArray

class TestCFArray (TestCase):
    def testCFArrayIsNSArray(self):
        self.assert_(issubclass(CFArrayRef, NSArray))
        self.assert_(issubclass(CFMutableArrayRef, NSMutableArray))

    def testCFArrayCreate(self):
        array = CFArrayCreate(None, [1,2,3,4], 4, kCFTypeArrayCallBacks)
        self.assertEquals(array, [1,2,3,4])
        self.assert_(isinstance(array, CFArrayRef))

        array = CFArrayCreateMutable(None, 0, kCFTypeArrayCallBacks)
        CFArrayAppendValue(array, 42)
        CFArrayAppendValue(array, 43)
        CFArrayAppendValue(array, 44)
        self.assertEquals(array, [42, 43, 44])
        self.assert_(isinstance(array, CFMutableArrayRef))

    def testCFArrayApplyFunction(self):
        array = CFArrayCreate(None, [1,2,3,4], 4, kCFTypeArrayCallBacks)

        self.failUnlessArgIsFunction(CFArrayApplyFunction, 2, 'v@@', False)
        self.failUnlessArgHasType(CFArrayApplyFunction, 3, '@')
        
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
        array = CFArrayCreate(None, range(20), 20, kCFTypeArrayCallBacks)

        self.failUnlessArgHasType(CFArrayBSearchValues, 2, '@')
        self.failUnlessArgIsFunction(CFArrayBSearchValues, 3, 'l@@@', False)
        self.failUnlessArgHasType(CFArrayBSearchValues, 4, '@')

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

        self.failUnlessArgIsFunction(CFArraySortValues, 2, 'l@@@', False)
        self.failUnlessArgHasType(CFArraySortValues, 3, '@')

        def compare(l, r, context):
            return cmp(l, r)
        CFArraySortValues(array, (0, 6), compare, None)

        self.assertEquals(array, [0, 1, 2, 3, 4, 5])

    def testTypeID(self):
        v = CFArrayGetTypeID()
        self.failUnless( isinstance(v, (int, long)) )

    def testCopy(self):
        array = CFArrayCreate(None, [1,2,3,4], 4, kCFTypeArrayCallBacks)
        self.assertEquals(array, [1,2,3,4])
        self.assert_(isinstance(array, CFArrayRef))

        cpy = CFArrayCreateCopy(None, array)
        self.assertEquals(cpy, [1,2,3,4])
        self.assert_(isinstance(cpy, CFArrayRef))

        cpy = CFArrayCreateMutableCopy(None, 0, array)
        self.assertEquals(cpy, [1,2,3,4])
        self.assert_(isinstance(cpy, CFMutableArrayRef))
        self.failIf( cpy is array )


    def testCounts(self):
        array = CFArrayCreate(None, [1,2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEquals(array, [1,2,3,4,4,2])
        self.assert_(isinstance(array, CFArrayRef))

        self.failUnless(  CFArrayGetCount(array) == 6 )
        self.failUnless(  CFArrayGetCountOfValue(array, (0,6), 4) == 2 )
        self.failUnless(  CFArrayGetCountOfValue(array, (0,6), 2) == 2 )
        self.failUnless(  CFArrayGetCountOfValue(array, (0,6), 3) == 1 )

    def testContains(self):
        array = CFArrayCreate(None, [u"a",2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEquals(array, [u"a",2,3,4,4,2])
        self.assert_(isinstance(array, CFArrayRef))

        self.failIf( CFArrayContainsValue(array, (0, 6), u"hello") )
        self.failUnless( CFArrayContainsValue(array, (0, 6), 4) )
        self.failIf( CFArrayContainsValue(array, (0, 2), 4) )

        self.failUnless( CFArrayGetFirstIndexOfValue(array, (0, 6), 3) == 2 )
        self.failUnless( CFArrayGetFirstIndexOfValue(array, (0, 6), 2) == 1 )
        self.failUnless( CFArrayGetFirstIndexOfValue(array, (0, 6), u"hello") == kCFNotFound )

        self.failUnless( CFArrayGetLastIndexOfValue(array, (0, 6), 3) == 2 )
        self.failUnless( CFArrayGetLastIndexOfValue(array, (0, 6), 2) == 5 )
        self.failUnless( CFArrayGetLastIndexOfValue(array, (0, 6), u"hello") == kCFNotFound )

        self.failUnlessArgHasType(CFArrayGetFirstIndexOfValue, 2, '@')
        self.failUnlessArgHasType(CFArrayGetLastIndexOfValue, 2, '@')


    def testGetting(self):
        array = CFArrayCreate(None, [u"a",2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEquals(array, [u"a",2,3,4,4,2])
        self.assert_(isinstance(array, CFArrayRef))

        self.failUnless(   CFArrayGetValueAtIndex(array, 0) == u"a"  )
        self.failUnless(   CFArrayGetValueAtIndex(array, 1) == 2  )


        self.failUnlessArgHasType(CFArrayGetValues, 2, 'o^@')
        self.failUnlessArgSizeInArg(CFArrayGetValues, 2, 1)

        vals = CFArrayGetValues(array, (0, 3), None)
        self.failUnless( isinstance(vals, tuple) )
        self.failUnless( vals == (u"a", 2, 3) )
        

    def testUpdating(self):
        array = CFArrayCreate(None, [u"a",2,3,4,4,2], 6, kCFTypeArrayCallBacks)
        self.assertEquals(array, [u"a",2,3,4,4,2])
        self.assert_(isinstance(array, CFArrayRef))
        array = CFArrayCreateMutableCopy(None, 0, array)


        self.failUnlessArgHasType(CFArrayAppendValue, 1, '@')
        self.failUnlessArgHasType(CFArrayInsertValueAtIndex, 2, '@')
        self.failUnlessArgHasType(CFArraySetValueAtIndex, 2, '@')

        CFArrayAppendValue(array, u"foo")
        self.assertEquals(array, [u"a",2,3,4,4,2,u"foo"])

        CFArrayInsertValueAtIndex(array, 1, 4)
        self.assertEquals(array, [u"a",4, 2,3,4,4,2,u"foo"])

        CFArrayRemoveValueAtIndex(array, 2)
        self.assertEquals(array, [u"a",4, 3,4,4,2,u"foo"])

        CFArraySetValueAtIndex(array, 2, u"two")
        self.assertEquals(array, [u"a",4, u"two",4,4,2,u"foo"])


        CFArrayExchangeValuesAtIndices(array, 1,2)
        self.assertEquals(array, [u"a",u"two",4,4,4,2,u"foo"])

        self.failUnlessArgHasType(CFArrayReplaceValues, 2, 'n^@')
        self.failUnlessArgSizeInArg(CFArrayReplaceValues, 2, 3)
        CFArrayReplaceValues(array, (2,3), (u'a', u'b', u'c', u'd', u'e', u'f'), 6)
        self.assertEquals(array, [u"a",u"two",u'a', u'b', u'c', u'd', u'e', u'f', 2, u'foo'])

        array2 = CFArrayCreate(None, [u'hello', u'earth'], 2, kCFTypeArrayCallBacks)
        CFArrayAppendArray(array, array2, (0,2))
        self.assertEquals(array, [u"a",u"two",u'a', u'b', u'c', u'd', u'e', u'f', 2, u'foo', u'hello', u'earth'])

        CFArrayRemoveAllValues(array)
        self.assertEquals(array, [])


if __name__ == "__main__":
    main()
