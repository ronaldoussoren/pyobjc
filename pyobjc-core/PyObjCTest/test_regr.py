import functools
import sys
import gc
import warnings

import objc
from PyObjCTest import copying, structargs
from PyObjCTest import testbndl  # noqa: F401
from PyObjCTest.fnd import NSAutoreleasePool, NSObject
from PyObjCTest.testbndl import OC_TestClass1
from PyObjCTest.properties import OCPropertyDefinitions
from PyObjCTools.TestSupport import TestCase

rct = structargs.StructArgClass.someRect.__metadata__()["retval"]["type"]


class OCTestRegrWithGetItem(NSObject):
    def objectForKey_(self, k):
        return "ofk: %s" % (k,)

    def __getitem__(self, k):
        return "gi: %s" % (k,)


class OCTestRegrWithGetItem2(OCTestRegrWithGetItem):
    def objectForKey_(self, k):
        return "ofk2: %s" % (k,)


class ReturnAStruct(NSObject):
    def someRectWithRect_(self, aRect):
        ((x, y), (h, w)) = aRect
        return ((x, y), (h, w))

    someRectWithRect_ = objc.selector(someRectWithRect_, signature=rct + b"@:" + rct)


class TestRegressions(TestCase):
    def testSetCompare(self):
        oc = objc.lookUpClass("NSSet").setWithArray_([None])
        oc2 = objc.lookUpClass("NSMutableSet").setWithArray_([None])
        py = {None}

        self.assertEqual(list(oc.allObjects()), [None])
        for o in oc.allObjects():
            self.assertIn(o, py)
        self.assertEqual(oc, oc2)
        self.assertIsNot(oc, oc2)
        self.assertEqual(oc, py)

        self.assertEqual(py, oc)

    def testNSObjectPerforming(self):
        o = NSObject.performSelector_("new")
        self.assertIsInstance(o, NSObject)

        v = o.performSelector_("description")
        self.assertEqual(v, o.description())

    def testNSObjectRespondsToCommonMethods(self):
        self.assertTrue(NSObject.pyobjc_classMethods.respondsToSelector_("alloc"))
        self.assertTrue(NSObject.instancesRespondToSelector_("init"))
        self.assertFalse(NSObject.instancesRespondToSelector_("frodel"))

    def testDeallocUninit(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=objc.UninitializedDeallocWarning)

            for clsName in ["NSURL", "NSObject", "NSArray"]:
                d = objc.lookUpClass(clsName).alloc()
                del d

        # Check that we generate a warning for unitialized objects that
        # get deallocated

        with warnings.catch_warnings(record=True) as w:
            warnings.filterwarnings("always")
            d = NSObject.alloc()
            del d

            # Expliclty for garbage collection, without this
            # there are sporadic test failures when using
            # coverage.py
            gc.collect()

        self.assertTrue(len(w) == 1)
        self.assertEqual(w[0].category, objc.UninitializedDeallocWarning)

    def testOneWayMethods(self):
        # This one should be in test_methods*.py
        from PyObjCTest.initialize import OC_TestInitialize

        o = OC_TestInitialize.alloc().init()
        self.assertEqual(
            objc.splitSignature(o.onewayVoidMethod.signature),
            (objc._C_ONEWAY + objc._C_VOID, objc._C_ID, objc._C_SEL),
        )

        # Make sure we can call the method
        o.onewayVoidMethod()
        self.assertEqual(o.isInitialized(), -1)

    def testNoneAsSelf(self):
        class SelfIsNone(NSObject):
            def f(x):
                pass

        self.assertRaises(TypeError, NSObject.pyobjc_instanceMethods.description, None)
        self.assertRaises(TypeError, SelfIsNone.pyobjc_instanceMethods.f, None)

    def testOneArgumentTooMany(self):
        class ClsIsNone(NSObject):
            @classmethod
            def f(cls):
                pass

        anObject = NSObject.alloc().init()

        self.assertRaises(TypeError, anObject.description, None)
        self.assertRaises(TypeError, anObject.description, "twelf")
        self.assertRaises(TypeError, NSObject.description, None)
        self.assertRaises(TypeError, ClsIsNone.f, None)

    def testBufferArg(self):
        data = objc.lookUpClass("NSData")

        o = structargs.StructArgClass.alloc().init()

        s = (b"foobar", 4)

        d = o.dataFromBuffer_(s)
        self.assertIsInstance(d, data)
        self.assertEqual(d.length(), 4)
        self.assertEqual(d.bytes(), b"foob")

        s = (bytearray(b"FOOBAR"), 3)

        d = o.dataFromBuffer_(s)
        self.assertIsInstance(d, data)
        self.assertEqual(d.length(), 3)
        self.assertEqual(d.bytes(), b"FOO")

    def testStructArgs(self):
        # Like AppKit.test.test_nsimage.TestNSImage.test_compositePoint
        # unlike that this one doesn't crash on darwin/x86, makeing it less
        # likely that libffi is at fault

        o = structargs.StructArgClass.alloc().init()
        v = o.compP_aRect_anOp_((1, 2), ((3, 4), (5, 6)), 7)
        self.assertEqual(v, "aP:{1, 2} aR:{{3, 4}, {5, 6}} anO:7")

    def testInitialize(self):
        calls = []
        self.assertEqual(len(calls), 0)

        class InitializeTestClass(NSObject):
            @classmethod
            def initialize(cls):
                calls.append(repr(cls))

        InitializeTestClass.new()
        self.assertEqual(len(calls), 1)
        InitializeTestClass.new()
        self.assertEqual(len(calls), 1)

    def testStructReturnPy(self):
        o = ReturnAStruct.alloc().init()
        p = structargs.StructArgClass.alloc().init()

        v = p.someRectWithObject_X_Y_H_W_(o, 1, 2, 3, 4)
        self.assertEqual(v, ((1, 2), (3, 4)))

    def testStructReturn(self):
        o = structargs.StructArgClass.alloc().init()
        v = o.someRect()
        self.assertEqual(v, ((1, 2), (3, 4)))


if sys.byteorder == "little":
    # i386 has specific stack alignment requirements.

    class AlignmentTestClass(NSObject):
        def testWithObject_(self, obj):
            return obj.stackPtr()

    def testStackPtr(self):
        o = structargs.StructArgClass.alloc().init()

        p = self.AlignmentTestClass.alloc().init()
        self.assertEqual(p.testWithObject_(o) % 16, o.stackPtr() % 16)


#
# Regression in retainCount management when a Python object
# is created from Objective-C. This only happened when the
# Python class has an implementation of the designated initializer.
#
# Mentioned by Dirk Stoop on the Pyobjc-dev mailing-list.
#

gDeallocCounter = 0


class OC_LeakTest_20090704_init(NSObject):
    def init(self):
        # self = super(OC_LeakTest_20090704_init, self).init()
        return self

    def dealloc(self):
        global gDeallocCounter
        gDeallocCounter += 1


class OC_LeakTest_20090704_noinit(NSObject):
    def dealloc(self):
        global gDeallocCounter
        gDeallocCounter += 1


class TestInitMemoryLeak(TestCase):
    def testNoPythonInit(self):
        # This test is basicly a self-test of the test-case, the
        # test even passed before the regression was fixed.

        global gDeallocCounter

        pool = NSAutoreleasePool.alloc().init()
        try:
            v = copying.OC_CopyHelper.newObjectOfClass_(OC_LeakTest_20090704_noinit)
            self.assertIsInstance(v, OC_LeakTest_20090704_noinit)

            gDeallocCounter = 0
            del v

        finally:
            del pool

        self.assertNotEqual(gDeallocCounter, 0)

    def testWithPythonInit(self):
        global gDeallocCounter

        pool = NSAutoreleasePool.alloc().init()
        try:
            v = copying.OC_CopyHelper.newObjectOfClass_(OC_LeakTest_20090704_init)
            self.assertIsInstance(v, OC_LeakTest_20090704_init)

            gDeallocCounter = 0
            del v

        finally:
            del pool

        self.assertNotEqual(gDeallocCounter, 0)

    def testInitFailureLeaks(self):
        NSData = objc.lookUpClass("NSData")

        with warnings.catch_warnings(record=True) as w:
            v = NSData.alloc().initWithContentsOfFile_("/etc/no-such-file.txt")
            self.assertFalse(v is not None)
            del v

        self.assertEqual(w, [])

    def testExplicitGetItem(self):
        v = OCTestRegrWithGetItem.alloc().init()

        self.assertEqual(v.objectForKey_("foo"), "ofk: foo")
        self.assertEqual(v["foo"], "gi: foo")

        v = OCTestRegrWithGetItem2.alloc().init()
        self.assertEqual(v.objectForKey_("foo"), "ofk2: foo")
        self.assertEqual(v["foo"], "gi: foo")

    def testAllowDecorators(self):
        def decorator(function):
            @functools.wraps(function)
            def wrapper(*args, **kwds):
                return function(*args, **kwds) * 2

            return wrapper

        class OCTestRegrWithWrapped(NSObject):
            @decorator
            def someMethod(self):
                return 42

        o = OCTestRegrWithWrapped.alloc().init()
        v = o.someMethod()
        self.assertEqual(v, 84)

    def testDefaultSignatures(self):
        def meth():
            pass

        s = objc.selector(meth)
        self.assertEqual(s.selector, b"meth")
        self.assertEqual(s.signature, b"v@:")

        def meth__():
            pass

        s = objc.selector(meth__)
        self.assertEqual(s.selector, b"meth::")
        self.assertEqual(s.signature, b"v@:@@")

        def meth():
            return 1

        s = objc.selector(meth)
        self.assertEqual(s.selector, b"meth")
        self.assertEqual(s.signature, b"@@:")

        def meth__():
            return 1

        s = objc.selector(meth__)
        self.assertEqual(s.selector, b"meth::")
        self.assertEqual(s.signature, b"@@:@@")


class TestNSInvocationBug(TestCase):
    def testNSInvocationOveride(self):
        class HelperNSInvocationTest(NSObject):
            def forwardInvocation_(self, inv):
                pass


class TestDocTestProblem(TestCase):
    def test_doctest(self):
        import doctest

        class DocTestHelper(NSObject):
            pass

        f = doctest.DocTestFinder(verbose=False)
        f.find(DocTestHelper)


class TestNSDataCreationIssue(TestCase):
    def test_issue271(self):
        cls = objc.lookUpClass("NSData")

        cls.alloc().initWithData_(b"hello")


class TestTypedefedClass(TestCase):
    # Issue #298, see description in Modules/objc/module.m
    def test_typedefed(self):
        v = OC_TestClass1.alloc().init()

        o = v.returnObjectValue_(1)
        self.assertIsInstance(o, objc.lookUpClass("NSObject"))

        o = v.returnObjectValue_(2)
        self.assertIsInstance(o, objc.lookUpClass("NSArray"))

        o = v.returnObjectValue_(3)
        self.assertIsInstance(o, objc.lookUpClass("NSDictionary"))

    def test_property(self):
        v = OCPropertyDefinitions.alloc().init()

        o = v.parent()
        self.assertIsInstance(o, objc.lookUpClass("NSArray"))
