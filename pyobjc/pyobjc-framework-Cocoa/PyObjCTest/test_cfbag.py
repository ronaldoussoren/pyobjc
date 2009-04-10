from PyObjCTools.TestSupport import *
from CoreFoundation import *

class TestCFBag (TestCase):

    def testCreation(self):
        bag = CFBagCreate(None, [1,1,2,3,4], 5)
        self.assert_(isinstance(bag, CFBagRef))
        self.assertEquals(CFBagGetCountOfValue(bag, 1), 2)
        self.assertEquals(CFBagGetCountOfValue(bag, 3), 1)

        bag = CFBagCreateMutable(None, 0)
        self.assert_(isinstance(bag, CFBagRef))
        CFBagAddValue(bag, 9)
        CFBagAddValue(bag, 8)
        CFBagAddValue(bag, 9)
        self.assertEquals(CFBagGetCountOfValue(bag, 9), 2)
        self.assertEquals(CFBagGetCountOfValue(bag, 8), 1)
    
    def testApplyFunction(self):
        items = []
        contexts = []

        bag = CFBagCreate(None, [1,1,2,3,4], 5)

        def func(item, context):
            items.append(item*item)
            contexts.append(context)

        CFBagApplyFunction(bag, func, 99)
        items.sort()
        self.assertEquals(items, [1,1,4,9,16])
        self.assertEquals(contexts, [99,99,99,99,99])

    def testTypeID(self):
        v = CFBagGetTypeID()
        self.failUnless(  isinstance(v, (int, long))  )

    def testCopy(self):
        bag = CFBagCreate(None, [1,1,2,3,4], 5)
        self.failUnless( isinstance(bag, CFBagRef) )

        bag2 = CFBagCreateCopy(None, bag)
        self.failUnless( isinstance(bag2, CFBagRef) )

        bag3 = CFBagCreateMutableCopy(None, 0, bag)
        self.failUnless( isinstance(bag3, CFBagRef) )
        self.failIf( bag3 is bag )

    def testInspect(self):
        bag = CFBagCreate(None, [u"Hello", 42, u"World", 42, u"a", u"a", u"a"], 7)
        self.failUnless( isinstance(bag, CFBagRef) )

        self.failUnless( CFBagGetCount(bag) == 7)
        self.failUnless( CFBagGetCountOfValue(bag, u"Hello") == 1)
        self.failUnless( CFBagGetCountOfValue(bag, 42) == 2)
        self.failUnless( CFBagGetCountOfValue(bag, u"a") == 3)

        self.failUnless( CFBagContainsValue(bag, u"a") )
        self.failIf( CFBagContainsValue(bag, u"b") )

        v = CFBagGetValue(bag, u"b")
        self.failUnless( v is None)

        v = CFBagGetValue(bag, u"a")
        self.failUnless( v == u"a")

        exists, value = CFBagGetValueIfPresent(bag, u"a", None)
        self.failUnless( exists )
        self.failUnless( value == u"a" )

        exists, value = CFBagGetValueIfPresent(bag, u"b", None)
        self.failIf( exists )
        self.failUnless( value is None )

        values = list(CFBagGetValues(bag))
        values.sort()
        l = [u"Hello", 42, u"World", 42, u"a", u"a", u"a"]
        l.sort()
        self.failUnless( values == l )


    def testMutation(self):
        bag = CFBagCreateMutable(None, 0)
        self.failUnless( CFBagGetCount(bag) == 0)

        CFBagAddValue(bag, u"hello")
        self.failUnless( CFBagGetCount(bag) == 1)
        CFBagAddValue(bag, u"hello")
        self.failUnless( CFBagGetCount(bag) == 2)

        CFBagReplaceValue(bag, u"hello")
        self.failUnless( CFBagGetCount(bag) == 2)

        CFBagReplaceValue(bag, u"world")
        self.failUnless( CFBagGetCount(bag) == 2)

        CFBagSetValue(bag, u"world")
        self.failUnless( CFBagGetCount(bag) == 3)

        CFBagSetValue(bag, u"world")
        self.failUnless( CFBagGetCount(bag) == 3)

        CFBagRemoveValue(bag, u"hello")
        self.failUnless( CFBagGetCount(bag) == 2)
        CFBagRemoveValue(bag, u"hello")
        self.failUnless( CFBagGetCount(bag) == 1)

        CFBagRemoveAllValues(bag)
        self.failUnless( CFBagGetCount(bag) == 0)

    def testFunctions(self):
        self.failUnlessArgHasType(CFBagGetCountOfValue, 1, '@')
        self.failUnlessArgHasType(CFBagContainsValue, 1, '@')
        self.failUnlessArgHasType(CFBagGetValue, 1, '@')
        self.failUnlessResultHasType(CFBagGetValue, '@')
        self.failUnlessArgHasType(CFBagGetValueIfPresent, 1, '@')
        self.failUnlessArgHasType(CFBagGetValueIfPresent, 2, 'o^@')
        self.failUnlessResultHasType(CFBagGetValueIfPresent, objc._C_NSBOOL)
        self.failUnlessArgIsFunction(CFBagApplyFunction, 1, 'v@@', False)
        self.failUnlessArgHasType(CFBagApplyFunction, 2, '@')
        self.failUnlessArgHasType(CFBagAddValue, 1, '@')
        self.failUnlessArgHasType(CFBagReplaceValue, 1, '@')
        self.failUnlessArgHasType(CFBagSetValue, 1, '@')
        self.failUnlessArgHasType(CFBagRemoveValue, 1, '@')


if __name__ == "__main__":
    main()
