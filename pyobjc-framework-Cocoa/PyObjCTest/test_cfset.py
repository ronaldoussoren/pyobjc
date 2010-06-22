from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestSet (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFSetRef)

    def testTypeID(self):
        self.assertIsInstance(CFSetGetTypeID(), (int, long))
    def testCreation(self):
        st = CFSetCreate(None, [u"a", u"b", u"c"], 3, kCFTypeSetCallBacks)
        self.assertIsInstance(st, CFSetRef)
        self.assertIsInstance(st, objc.lookUpClass('NSSet'))
        st = CFSetCreate(None, [u"a", u"b", u"c"], 3, kCFTypeSetCallBacks)
        self.assertIsInstance(st, CFSetRef)
        st = CFSetCreateMutable(None, 0, kCFTypeSetCallBacks)
        self.assertIsInstance(st, CFSetRef)
        cp = CFSetCreateMutableCopy(None, 0, st)
        self.assertIsInstance(st, CFSetRef)
        cp = CFSetCreateCopy(None, st)
        self.assertIsInstance(st, CFSetRef)
    def testInspection(self):
        st = CFSetCreate(None, [u"a", u"b", u"c"], 3, kCFTypeSetCallBacks)
        self.assertIsInstance(st, CFSetRef)
        self.assertIsInstance(st, objc.lookUpClass('NSSet'))
        v = CFSetGetCount(st)
        self.assertEqual(v , 3)
        self.assertArgHasType(CFSetGetCountOfValue, 1, b'@')
        v = CFSetGetCountOfValue(st, u'd')
        self.assertEqual(v , 0)
        v = CFSetGetCountOfValue(st, u'b')
        self.assertEqual(v , 1)
        self.assertArgHasType(CFSetContainsValue, 1, b'@')
        v = CFSetContainsValue(st, u'd')
        self.assertIs(v, False)
        v = CFSetContainsValue(st, u'b')
        self.assertIs(v, True)
        self.assertResultHasType(CFSetGetValue, b'@')
        self.assertArgHasType(CFSetGetValue, 1, b'@')
        v = CFSetGetValue(st, u'd')
        self.assertIs(v, None)
        v = CFSetGetValue(st, u'b')
        self.assertEqual(v , u'b')
        self.assertResultIsBOOL(CFSetGetValueIfPresent)
        self.assertArgHasType(CFSetGetValueIfPresent, 1, b'@')
        self.assertArgHasType(CFSetGetValueIfPresent, 2, b'o^@')
        present, value = CFSetGetValueIfPresent(st, u'c', None)
        self.assertIs(present, True)
        self.assertEqual(value , u'c')
        values = CFSetGetValues(st, None)
        values = list(values)
        values.sort()
        self.assertEqual(values , [u'a', u'b', u'c'])
    def testApplying(self):
        st = CFSetCreate(None, [u"a", u"b", u"c"], 3, kCFTypeSetCallBacks)
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
        self.assertEqual(context , [u'a', u'b', u'c'])

    def testMutation(self):
        st = CFSetCreate(None, [u"a", u"b", u"c"], 3, kCFTypeSetCallBacks)
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
