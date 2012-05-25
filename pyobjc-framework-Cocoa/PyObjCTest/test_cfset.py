from PyObjCTools.TestSupport import *
from CoreFoundation import *


try:
    long
except NameError:
    long = int


class TestSet (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFSetRef)

    def testTypeID(self):
        self.assertIsInstance(CFSetGetTypeID(), (int, long))

    def testCreation(self):
        st = CFSetCreate(None, [b"a".decode('ascii'), b"b".decode('ascii'), b"c".decode('ascii')], 3, kCFTypeSetCallBacks)
        self.assertIsInstance(st, CFSetRef)
        self.assertIsInstance(st, objc.lookUpClass('NSSet'))
        st = CFSetCreate(None, [b"a".decode('ascii'), b"b".decode('ascii'), b"c".decode('ascii')], 3, kCFTypeSetCallBacks)
        self.assertIsInstance(st, CFSetRef)
        st = CFSetCreateMutable(None, 0, kCFTypeSetCallBacks)
        self.assertIsInstance(st, CFSetRef)
        cp = CFSetCreateMutableCopy(None, 0, st)
        self.assertIsInstance(st, CFSetRef)
        cp = CFSetCreateCopy(None, st)
        self.assertIsInstance(st, CFSetRef)

    def testInspection(self):
        st = CFSetCreate(None, [b"a".decode('ascii'), b"b".decode('ascii'), b"c".decode('ascii')], 3, kCFTypeSetCallBacks)
        self.assertIsInstance(st, CFSetRef)
        self.assertIsInstance(st, objc.lookUpClass('NSSet'))
        v = CFSetGetCount(st)
        self.assertEqual(v , 3)
        self.assertArgHasType(CFSetGetCountOfValue, 1, b'@')
        v = CFSetGetCountOfValue(st, b'd'.decode('ascii'))
        self.assertEqual(v , 0)
        v = CFSetGetCountOfValue(st, b'b'.decode('ascii'))
        self.assertEqual(v , 1)
        self.assertArgHasType(CFSetContainsValue, 1, b'@')
        v = CFSetContainsValue(st, b'd'.decode('ascii'))
        self.assertIs(v, False)
        v = CFSetContainsValue(st, b'b'.decode('ascii'))
        self.assertIs(v, True)
        self.assertResultHasType(CFSetGetValue, b'@')
        self.assertArgHasType(CFSetGetValue, 1, b'@')
        v = CFSetGetValue(st, b'd'.decode('ascii'))
        self.assertIs(v, None)
        v = CFSetGetValue(st, b'b'.decode('ascii'))
        self.assertEqual(v , b'b'.decode('ascii'))
        self.assertResultIsBOOL(CFSetGetValueIfPresent)
        self.assertArgHasType(CFSetGetValueIfPresent, 1, b'@')
        self.assertArgHasType(CFSetGetValueIfPresent, 2, b'o^@')
        present, value = CFSetGetValueIfPresent(st, b'c'.decode('ascii'), None)
        self.assertIs(present, True)
        self.assertEqual(value , b'c'.decode('ascii'))
        values = CFSetGetValues(st, None)
        values = list(values)
        values.sort()
        self.assertEqual(values , [b'a'.decode('ascii'), b'b'.decode('ascii'), b'c'.decode('ascii')])

    def testApplying(self):
        st = CFSetCreate(None, [b"a".decode('ascii'), b"b".decode('ascii'), b"c".decode('ascii')], 3, kCFTypeSetCallBacks)
        self.assertIsInstance(st, CFSetRef)
        self.assertIsInstance(st, objc.lookUpClass('NSSet'))
        context = []
        def callback(value, context):
            context.append(value)

        self.assertArgIsFunction(CFSetApplyFunction, 1, b'v@@', False)
        self.assertArgHasType(CFSetApplyFunction, 2, b'@')
        CFSetApplyFunction(st, callback, context)
        self.assertEqual(len(context) , 3)
        context.sort()
        self.assertEqual(context , [b'a'.decode('ascii'), b'b'.decode('ascii'), b'c'.decode('ascii')])

    def testMutation(self):
        st = CFSetCreate(None, [b"a".decode('ascii'), b"b".decode('ascii'), b"c".decode('ascii')], 3, kCFTypeSetCallBacks)
        self.assertIsInstance(st, CFSetRef)
        self.assertIsInstance(st, objc.lookUpClass('NSSet'))
        st = CFSetCreateMutableCopy(None, 0, st)
        self.assertIsInstance(st, CFSetRef)
        self.assertEqual(CFSetGetCount(st) , 3)
        self.assertArgHasType(CFSetSetValue, 1, b'@')
        CFSetSetValue(st, 'c')
        self.assertEqual(CFSetGetCount(st) , 3)
        CFSetSetValue(st, 'd')
        self.assertEqual(CFSetGetCount(st) , 4)
        self.assertArgHasType(CFSetRemoveValue, 1, b'@')
        CFSetRemoveValue(st, 'c')
        self.assertEqual(CFSetGetCount(st) , 3)
        CFSetRemoveAllValues(st)
        self.assertEqual(CFSetGetCount(st) , 0)
        self.assertArgHasType(CFSetAddValue, 1, b'@')
        CFSetAddValue(st, 'd')

        self.assertArgHasType(CFSetReplaceValue, 1, b'@')
        CFSetReplaceValue(st, 'd')

if __name__ == "__main__":
    main()
