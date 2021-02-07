import CoreFoundation
import objc
from PyObjCTools.TestSupport import TestCase


class TestSet(TestCase):
    def testTypes(self):
        try:
            if objc.lookUpClass("NSSet") is CoreFoundation.CFSetRef:
                return
        except objc.error:
            pass
        self.assertIsCFType(CoreFoundation.CFSetRef)

    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFSetGetTypeID(), int)

    def testCreation(self):
        st = CoreFoundation.CFSetCreate(
            None, ["a", "b", "c"], 3, CoreFoundation.kCFTypeSetCallBacks
        )
        self.assertIsInstance(st, CoreFoundation.CFSetRef)
        self.assertIsInstance(st, objc.lookUpClass("NSSet"))
        st = CoreFoundation.CFSetCreate(
            None, ["a", "b", "c"], 3, CoreFoundation.kCFTypeSetCallBacks
        )
        self.assertIsInstance(st, CoreFoundation.CFSetRef)
        st = CoreFoundation.CFSetCreateMutable(
            None, 0, CoreFoundation.kCFTypeSetCallBacks
        )
        self.assertIsInstance(st, CoreFoundation.CFSetRef)
        cp = CoreFoundation.CFSetCreateMutableCopy(None, 0, st)
        self.assertIsInstance(cp, CoreFoundation.CFSetRef)
        cp = CoreFoundation.CFSetCreateCopy(None, st)
        self.assertIsInstance(cp, CoreFoundation.CFSetRef)

    def testInspection(self):
        st = CoreFoundation.CFSetCreate(
            None, ["a", "b", "c"], 3, CoreFoundation.kCFTypeSetCallBacks
        )
        self.assertIsInstance(st, CoreFoundation.CFSetRef)
        self.assertIsInstance(st, objc.lookUpClass("NSSet"))
        v = CoreFoundation.CFSetGetCount(st)
        self.assertEqual(v, 3)
        self.assertArgHasType(CoreFoundation.CFSetGetCountOfValue, 1, b"@")
        v = CoreFoundation.CFSetGetCountOfValue(st, "d")
        self.assertEqual(v, 0)
        v = CoreFoundation.CFSetGetCountOfValue(st, "b")
        self.assertEqual(v, 1)
        self.assertArgHasType(CoreFoundation.CFSetContainsValue, 1, b"@")
        v = CoreFoundation.CFSetContainsValue(st, "d")
        self.assertIs(v, False)
        v = CoreFoundation.CFSetContainsValue(st, "b")
        self.assertIs(v, True)
        self.assertResultHasType(CoreFoundation.CFSetGetValue, b"@")
        self.assertArgHasType(CoreFoundation.CFSetGetValue, 1, b"@")
        v = CoreFoundation.CFSetGetValue(st, "d")
        self.assertIs(v, None)
        v = CoreFoundation.CFSetGetValue(st, "b")
        self.assertEqual(v, "b")
        self.assertResultIsBOOL(CoreFoundation.CFSetGetValueIfPresent)
        self.assertArgHasType(CoreFoundation.CFSetGetValueIfPresent, 1, b"@")
        self.assertArgHasType(CoreFoundation.CFSetGetValueIfPresent, 2, b"o^@")
        present, value = CoreFoundation.CFSetGetValueIfPresent(st, "c", None)
        self.assertIs(present, True)
        self.assertEqual(value, "c")
        values = CoreFoundation.CFSetGetValues(st, None)
        values = list(values)
        values.sort()
        self.assertEqual(values, ["a", "b", "c"])

    def testApplying(self):
        st = CoreFoundation.CFSetCreate(
            None, ["a", "b", "c"], 3, CoreFoundation.kCFTypeSetCallBacks
        )
        self.assertIsInstance(st, CoreFoundation.CFSetRef)
        self.assertIsInstance(st, objc.lookUpClass("NSSet"))
        context = []

        def callback(value, context):
            context.append(value)

        self.assertArgIsFunction(CoreFoundation.CFSetApplyFunction, 1, b"v@@", False)
        self.assertArgHasType(CoreFoundation.CFSetApplyFunction, 2, b"@")
        CoreFoundation.CFSetApplyFunction(st, callback, context)
        self.assertEqual(len(context), 3)
        context.sort()
        self.assertEqual(context, ["a", "b", "c"])

    def testMutation(self):
        st = CoreFoundation.CFSetCreate(
            None, ["a", "b", "c"], 3, CoreFoundation.kCFTypeSetCallBacks
        )
        self.assertIsInstance(st, CoreFoundation.CFSetRef)
        self.assertIsInstance(st, objc.lookUpClass("NSSet"))
        st = CoreFoundation.CFSetCreateMutableCopy(None, 0, st)
        self.assertIsInstance(st, CoreFoundation.CFSetRef)
        self.assertEqual(CoreFoundation.CFSetGetCount(st), 3)
        self.assertArgHasType(CoreFoundation.CFSetSetValue, 1, b"@")
        CoreFoundation.CFSetSetValue(st, "c")
        self.assertEqual(CoreFoundation.CFSetGetCount(st), 3)
        CoreFoundation.CFSetSetValue(st, "d")
        self.assertEqual(CoreFoundation.CFSetGetCount(st), 4)
        self.assertArgHasType(CoreFoundation.CFSetRemoveValue, 1, b"@")
        CoreFoundation.CFSetRemoveValue(st, "c")
        self.assertEqual(CoreFoundation.CFSetGetCount(st), 3)
        CoreFoundation.CFSetRemoveAllValues(st)
        self.assertEqual(CoreFoundation.CFSetGetCount(st), 0)
        self.assertArgHasType(CoreFoundation.CFSetAddValue, 1, b"@")
        CoreFoundation.CFSetAddValue(st, "d")

        self.assertArgHasType(CoreFoundation.CFSetReplaceValue, 1, b"@")
        CoreFoundation.CFSetReplaceValue(st, "d")
