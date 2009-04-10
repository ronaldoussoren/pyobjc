from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestSet (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFSetRef)

    def testTypeID(self):
        self.failUnless(isinstance(CFSetGetTypeID(), (int, long)))

    def testCreation(self):
        st = CFSetCreate(None, [u"a", u"b", u"c"], 3, kCFTypeSetCallBacks)
        self.failUnless(isinstance(st, CFSetRef))
        self.failUnless(isinstance(st, objc.lookUpClass('NSSet')))

        st = CFSetCreate(None, [u"a", u"b", u"c"], 3, kCFTypeSetCallBacks)
        self.failUnless(isinstance(st, CFSetRef))

        st = CFSetCreateMutable(None, 0, kCFTypeSetCallBacks)
        self.failUnless(isinstance(st, CFSetRef))

        cp = CFSetCreateMutableCopy(None, 0, st)
        self.failUnless(isinstance(st, CFSetRef))

        cp = CFSetCreateCopy(None, st)
        self.failUnless(isinstance(st, CFSetRef))

    def testInspection(self):
        st = CFSetCreate(None, [u"a", u"b", u"c"], 3, kCFTypeSetCallBacks)
        self.failUnless(isinstance(st, CFSetRef))
        self.failUnless(isinstance(st, objc.lookUpClass('NSSet')))

        v = CFSetGetCount(st)
        self.failUnless(v == 3)

        self.failUnlessArgHasType(CFSetGetCountOfValue, 1, '@')
        v = CFSetGetCountOfValue(st, u'd')
        self.failUnless(v == 0)
        v = CFSetGetCountOfValue(st, u'b')
        self.failUnless(v == 1)

        self.failUnlessArgHasType(CFSetContainsValue, 1, '@')
        v = CFSetContainsValue(st, u'd')
        self.failUnless(v is False)
        v = CFSetContainsValue(st, u'b')
        self.failUnless(v is True)

        self.failUnlessResultHasType(CFSetGetValue, '@')
        self.failUnlessArgHasType(CFSetGetValue, 1, '@')
        v = CFSetGetValue(st, u'd')
        self.failUnless(v is None)

        v = CFSetGetValue(st, u'b')
        self.failUnless(v == u'b')

        self.failUnlessResultIsBOOL(CFSetGetValueIfPresent)
        self.failUnlessArgHasType(CFSetGetValueIfPresent, 1, '@')
        self.failUnlessArgHasType(CFSetGetValueIfPresent, 2, 'o^@')
        present, value = CFSetGetValueIfPresent(st, u'c', None)
        self.failUnless(present is True)
        self.failUnless(value == u'c')

        values = CFSetGetValues(st, None)
        values = list(values)
        values.sort()
        self.failUnless(values == [u'a', u'b', u'c'])

    def testApplying(self):
        st = CFSetCreate(None, [u"a", u"b", u"c"], 3, kCFTypeSetCallBacks)
        self.failUnless(isinstance(st, CFSetRef))
        self.failUnless(isinstance(st, objc.lookUpClass('NSSet')))

        context = []
        def callback(value, context):
            context.append(value)

        self.failUnlessArgIsFunction(CFSetApplyFunction, 1, 'v@@', False)
        self.failUnlessArgHasType(CFSetApplyFunction, 2, '@')
        CFSetApplyFunction(st, callback, context)
        self.failUnless(len(context) == 3)
        context.sort()
        self.failUnless(context == [u'a', u'b', u'c'])

    def testMutation(self):
        st = CFSetCreate(None, [u"a", u"b", u"c"], 3, kCFTypeSetCallBacks)
        self.failUnless(isinstance(st, CFSetRef))
        self.failUnless(isinstance(st, objc.lookUpClass('NSSet')))
        st = CFSetCreateMutableCopy(None, 0, st)
        self.failUnless(isinstance(st, CFSetRef))

        self.failUnless(CFSetGetCount(st) == 3)
        self.failUnlessArgHasType(CFSetSetValue, 1, '@')
        CFSetSetValue(st, 'c')
        self.failUnless(CFSetGetCount(st) == 3)
        CFSetSetValue(st, 'd')
        self.failUnless(CFSetGetCount(st) == 4)

        self.failUnlessArgHasType(CFSetRemoveValue, 1, '@')
        CFSetRemoveValue(st, 'c')
        self.failUnless(CFSetGetCount(st) == 3)

        CFSetRemoveAllValues(st)
        self.failUnless(CFSetGetCount(st) == 0)

        self.failUnlessArgHasType(CFSetAddValue, 1, '@')
        CFSetAddValue(st, 'd')

        self.failUnlessArgHasType(CFSetReplaceValue, 1, '@')
        CFSetReplaceValue(st, 'd')


if __name__ == "__main__":
    main()
