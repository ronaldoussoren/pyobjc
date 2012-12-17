from PyObjCTools.TestSupport import *
from CoreFoundation import *

try:
    long
except NameError:
    long = int


class TestCFBag (TestCase):

    def testCreation(self):
        bag = CFBagCreate(None, [1,1,2,3,4], 5)
        self.assert_(isinstance(bag, CFBagRef))
        self.assertEqual(CFBagGetCountOfValue(bag, 1), 2)
        self.assertEqual(CFBagGetCountOfValue(bag, 3), 1)

        bag = CFBagCreateMutable(None, 0)
        self.assert_(isinstance(bag, CFBagRef))
        CFBagAddValue(bag, 9)
        CFBagAddValue(bag, 8)
        CFBagAddValue(bag, 9)
        self.assertEqual(CFBagGetCountOfValue(bag, 9), 2)
        self.assertEqual(CFBagGetCountOfValue(bag, 8), 1)

    def testApplyFunction(self):
        items = []
        contexts = []

        bag = CFBagCreate(None, [1,1,2,3,4], 5)

        def func(item, context):
            items.append(item*item)
            contexts.append(context)

        CFBagApplyFunction(bag, func, 99)
        items.sort()
        self.assertEqual(items, [1,1,4,9,16])
        self.assertEqual(contexts, [99,99,99,99,99])

    def testTypeID(self):
        v = CFBagGetTypeID()
        self.assertIsInstance(v, (int, long))

    def testCopy(self):
        bag = CFBagCreate(None, [1,1,2,3,4], 5)
        self.assertIsInstance(bag, CFBagRef)
        bag2 = CFBagCreateCopy(None, bag)
        self.assertIsInstance(bag2, CFBagRef)
        bag3 = CFBagCreateMutableCopy(None, 0, bag)
        self.assertIsInstance(bag3, CFBagRef)
        self.assertIsNot(bag3, bag )

    def testInspect(self):
        bag = CFBagCreate(None, [b"Hello".decode('ascii'), 42, b"World".decode('ascii'), 42, b"a".decode('ascii'), b"a".decode('ascii'), b"a".decode('ascii')], 7)
        self.assertIsInstance(bag, CFBagRef)
        self.assertEqual(CFBagGetCount(bag) , 7)
        self.assertEqual(CFBagGetCountOfValue(bag, b"Hello".decode('ascii')) , 1)
        self.assertEqual(CFBagGetCountOfValue(bag, 42) , 2)
        self.assertEqual(CFBagGetCountOfValue(bag, b"a".decode('ascii')) , 3)
        self.assertTrue(CFBagContainsValue(bag, b"a".decode('ascii')) )
        self.assertFalse(CFBagContainsValue(bag, b"b".decode('ascii')) )

        v = CFBagGetValue(bag, b"b".decode('ascii'))
        self.assertIs(v, None)
        v = CFBagGetValue(bag, b"a".decode('ascii'))
        self.assertEqual(v , b"a".decode('ascii'))
        exists, value = CFBagGetValueIfPresent(bag, b"a".decode('ascii'), None)
        self.assertTrue( exists )
        self.assertEqual(value , b"a".decode('ascii') )
        exists, value = CFBagGetValueIfPresent(bag, b"b".decode('ascii'), None)
        self.assertFalse( exists )
        self.assertIs(value, None )
        values = set(CFBagGetValues(bag))
        l = set([b"Hello".decode('ascii'), 42, b"World".decode('ascii'), 42, b"a".decode('ascii'), b"a".decode('ascii'), b"a".decode('ascii')])
        self.assertEqual(values , l )

    def testMutation(self):
        bag = CFBagCreateMutable(None, 0)
        self.assertEqual(CFBagGetCount(bag) , 0)
        CFBagAddValue(bag, b"hello".decode('ascii'))
        self.assertEqual(CFBagGetCount(bag) , 1)
        CFBagAddValue(bag, b"hello".decode('ascii'))
        self.assertEqual(CFBagGetCount(bag) , 2)
        CFBagReplaceValue(bag, b"hello".decode('ascii'))
        self.assertEqual(CFBagGetCount(bag) , 2)
        CFBagReplaceValue(bag, b"world".decode('ascii'))
        self.assertEqual(CFBagGetCount(bag) , 2)
        CFBagSetValue(bag, b"world".decode('ascii'))
        self.assertEqual(CFBagGetCount(bag) , 3)
        CFBagSetValue(bag, b"world".decode('ascii'))
        self.assertEqual(CFBagGetCount(bag) , 3)
        CFBagRemoveValue(bag, b"hello".decode('ascii'))
        self.assertEqual(CFBagGetCount(bag) , 2)
        CFBagRemoveValue(bag, b"hello".decode('ascii'))
        self.assertEqual(CFBagGetCount(bag) , 1)
        CFBagRemoveAllValues(bag)
        self.assertEqual(CFBagGetCount(bag) , 0)

    def testFunctions(self):
        self.assertArgHasType(CFBagGetCountOfValue, 1, b'@')
        self.assertArgHasType(CFBagContainsValue, 1, b'@')
        self.assertArgHasType(CFBagGetValue, 1, b'@')
        self.assertResultHasType(CFBagGetValue, b'@')
        self.assertArgHasType(CFBagGetValueIfPresent, 1, b'@')
        self.assertArgHasType(CFBagGetValueIfPresent, 2, b'o^@')
        self.assertResultHasType(CFBagGetValueIfPresent, objc._C_NSBOOL)
        self.assertArgIsFunction(CFBagApplyFunction, 1, b'v@@', False)
        self.assertArgHasType(CFBagApplyFunction, 2, b'@')
        self.assertArgHasType(CFBagAddValue, 1, b'@')
        self.assertArgHasType(CFBagReplaceValue, 1, b'@')
        self.assertArgHasType(CFBagSetValue, 1, b'@')
        self.assertArgHasType(CFBagRemoveValue, 1, b'@')

if __name__ == "__main__":
    main()
