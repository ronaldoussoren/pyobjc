import functools
import sys
import gc
import warnings
import types

import objc
from PyObjCTest import copying, structargs
from PyObjCTest import testbndl  # noqa: F401
from PyObjCTest.fnd import NSAutoreleasePool, NSObject
from PyObjCTest.testbndl import OC_TestClass1
from PyObjCTest.properties import OCPropertyDefinitions
from PyObjCTools.TestSupport import TestCase

rct = structargs.StructArgClass.someRect.__metadata__()["retval"]["type"]

NSInvocation = objc.lookUpClass("NSInvocation")
NSArray = objc.lookUpClass("NSArray")


class OCTestRegrWithGetItem(NSObject):
    def objectForKey_(self, k):
        return f"ofk: {k}"

    def __getitem__(self, k):
        return f"gi: {k}"


class OCTestRegrWithGetItem2(OCTestRegrWithGetItem):
    def objectForKey_(self, k):
        return f"ofk2: {k}"


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

        with self.assertRaisesRegex(
            TypeError, "Expecting instance of NSObject as self, got one of NoneType"
        ):
            NSObject.pyobjc_instanceMethods.description(None)
        with self.assertRaisesRegex(
            TypeError,
            "Expecting an Objective-C class or instance as self, got a NoneType",
        ):
            SelfIsNone.pyobjc_instanceMethods.f(None)

    def testOneArgumentTooMany(self):
        class ClsIsNone(NSObject):
            @classmethod
            def f(cls):
                pass

        anObject = NSObject.alloc().init()

        with self.assertRaisesRegex(TypeError, "Need 0 arguments, got 1"):
            anObject.description(None)
        with self.assertRaisesRegex(TypeError, "Need 0 arguments, got 1"):
            anObject.description("twelf")
        with self.assertRaisesRegex(TypeError, "Need 0 arguments, got 1"):
            NSObject.description(None)
        with self.assertRaisesRegex(
            TypeError, "takes 1 positional argument but 2 were given"
        ):
            ClsIsNone.f(None)

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


class TestNSIndexSetCreationIssue(TestCase):
    def test_issue625(self):
        cls = objc.lookUpClass("NSIndexSet")

        cls.alloc().initWithIndex_(0)


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


class TestReboundMethod(TestCase):
    # Issue #399
    def test_rebound(self):
        class Foo:
            alloc = NSObject.alloc

        f = Foo()
        f.alloc().init()


class TestReplaceMethod(TestCase):
    def test_replace_method(self):
        # GH #479
        NSAppleScript = objc.lookUpClass("NSAppleScript")
        o = NSAppleScript.alloc().initWithSource_("tell application Safari to quit")
        self.assertIsNot(o, None)

        v = o.source()
        self.assertIsInstance(v, str)

        # In some applications it is useful to replace an Objective-C method
        # by a property definition, like so:
        NSAppleScript.source = property(
            lambda self: self.pyobjc_instanceMethods.source()
        )

        v2 = o.source
        self.assertIsInstance(v, str)

        self.assertEqual(v, v2)


# This probably needs to be a seperate file:


NO_ATTR = object()


class PythonFunction:
    @property
    def __class__(self):
        return type(self._callable)

    def __init__(self, func):
        self._callable = func

    def __call__(self, *args, **kwds):
        return self._callable(*args, **kwds)

    def __get__(self, *args):
        return PythonFunction(self._callable.__get__(*args))

    def __getattr__(self, name):
        value = getattr(self._callable, name)
        if value is NO_ATTR:
            raise AttributeError(name)
        return value


class TestFunctionLikeObjects(TestCase):
    def test_helper(self):
        def func():
            return 42

        pfunc = PythonFunction(func)
        self.assertEqual(pfunc(), func())
        self.assertEqual(pfunc.__code__, func.__code__)

    def test_custom_func_in_class(self):
        values = []

        class Helper:
            @PythonFunction
            def bound1(self, oc_self):
                values.append("bound1")
                return 99

            @PythonFunction
            def bound2(self, oc_self):
                values.append("bound2")

        helper = Helper()

        class OC_ClassWithCustomFunc(NSObject):
            @PythonFunction
            def method1(self):
                values.append("method1")
                return 42

            @PythonFunction
            def method2(self):
                values.append("method2")

            def method3(self):
                values.append("method3")
                return 21

            def method4(self):
                values.append("method4")

            bound1 = helper.bound1
            bound2 = helper.bound2

        o = OC_ClassWithCustomFunc.alloc().init()
        self.assertEqual(o.method1.signature, b"@@:")
        self.assertEqual(o.method2.signature, b"v@:")
        self.assertEqual(o.method3.signature, b"@@:")
        self.assertEqual(o.method4.signature, b"v@:")
        self.assertEqual(o.bound1.signature, b"@@:")
        self.assertEqual(o.bound2.signature, b"v@:")

        # NOTE: Cannot try to access the return value
        # of methods whose signature says the return
        # value is ``void``, Cocoa will cause a crash
        # when calling ``getReturnValue`` for those.

        self.assertEqual(values, [])
        inv = NSInvocation.invocationWithMethodSignature_(
            o.methodSignatureForSelector_("method1")
        )
        inv.setSelector_("method1")
        inv.setTarget_(o)
        inv.invoke()
        v = inv.getReturnValue_(None)
        self.assertEqual(v, 42)
        self.assertEqual(values, ["method1"])
        del values[:]

        self.assertEqual(values, [])
        inv = NSInvocation.invocationWithMethodSignature_(
            o.methodSignatureForSelector_("method2")
        )
        inv.setSelector_("method2")
        inv.setTarget_(o)
        inv.invoke()
        self.assertEqual(values, ["method2"])
        del values[:]

        self.assertEqual(values, [])
        inv = NSInvocation.invocationWithMethodSignature_(
            o.methodSignatureForSelector_("method3")
        )
        inv.setSelector_("method3")
        inv.setTarget_(o)
        inv.invoke()
        v = inv.getReturnValue_(None)
        self.assertEqual(v, 21)
        self.assertEqual(values, ["method3"])
        del values[:]

        self.assertEqual(values, [])
        inv = NSInvocation.invocationWithMethodSignature_(
            o.methodSignatureForSelector_("method4")
        )
        inv.setSelector_("method4")
        inv.setTarget_(o)
        inv.invoke()

        self.assertEqual(values, ["method4"])
        del values[:]

        self.assertEqual(values, [])
        inv = NSInvocation.invocationWithMethodSignature_(
            o.methodSignatureForSelector_("bound1")
        )
        inv.setSelector_("bound1")
        inv.setTarget_(o)
        inv.invoke()
        v = inv.getReturnValue_(None)
        self.assertEqual(v, 99)
        self.assertEqual(values, ["bound1"])
        del values[:]

        self.assertEqual(values, [])
        inv = NSInvocation.invocationWithMethodSignature_(
            o.methodSignatureForSelector_("bound2")
        )
        inv.setSelector_("bound2")
        inv.setTarget_(o)
        inv.invoke()
        del values[:]

    def test_custom_func_with_no_code(self):
        with self.assertRaisesRegex(
            ValueError, " does not have a valid '__code__' attribute"
        ):

            class OC_ClassWithCustomFunc2a(NSObject):
                @PythonFunction
                def methodx(self):
                    return 42

                methodx.__code__ = 42

        with self.assertRaisesRegex(
            ValueError, " does not have a valid '__code__' attribute"
        ):

            class OC_ClassWithCustomFunc2b(NSObject):
                @PythonFunction
                def methodx(self):
                    return 42

                methodx.__code__ = NO_ATTR

    def no_test_callable_edge_cases(self):
        @PythonFunction
        def func1(a, b=4):
            pass

        @PythonFunction
        def func2(a, *, b=4):
            pass

        s = objc.selector(func1)
        self.assertEqual(s.signature, b"@@:")

        objc.selector(func2)
        self.assertEqual(s.signature, b"@@:")

        func1.__code__ = None
        bound = func1.__get__(NSObject, 42)
        self.assertIsInstance(bound, types.MethodType)
        objc.selector(bound)


class TestReplacingDir(TestCase):
    def test_replace_dir(self):
        class OC_TestReplacingDir(NSObject):
            pass

        value = OC_TestReplacingDir.new()
        self.assertIsInstance(value.__dir__, types.BuiltinFunctionType)

        def __dir__(self):
            return ["hello"]

        OC_TestReplacingDir.__dir__ = __dir__

        self.assertEqual(value.__dir__(), ["hello"])
        self.assertIsInstance(value.__dir__, types.MethodType)

    def test_basic_dir(self):
        class OC_TestBasicDir(NSObject):
            pass

        o = OC_TestBasicDir.alloc().init()
        self.assertNotIn("key", dir(o))
        self.assertIn("init", dir(o))

        o.key = 42
        self.assertIn("key", dir(o))
        self.assertIn("init", dir(o))


class TestMethodsWithVarargs(TestCase):
    def test_method_with_varargs(self):
        class OC_MethodWithVarargs1(NSObject):
            def method_(self, *args):
                pass

    def test_method_with_varargs_2(self):
        class OC_MethodWithVarargs2(NSObject):
            def method_(self, value, *args):
                pass

    def test_method_with_varargs_3(self):
        with self.assertRaises(objc.BadPrototypeError):

            class OC_MethodWithVarargs3(NSObject):
                def method_(self, value, value2, *args):
                    pass

    def test_method_with_varargs_4(self):
        class OC_MethodWithVarargs4(NSObject):
            def method_(self, value, other=9, *args):
                pass


class TestSuperClassAttr(TestCase):
    def test_class_of_builtin_super(self):
        self.assertIs(super(object, object()).__class__, super)

    def test_class_of_objc_super(self):
        self.assertIs(objc.super(NSObject, NSObject.new()).__class__, objc.super)

    def test_single_arg_super(self):
        v = objc.super(NSInvocation)
        v.__new__

        with self.assertRaisesRegex(TypeError, "attribute name must be string"):
            getattr(v, 42)

    def test_super_attr_name(self):
        with self.assertRaisesRegex(TypeError, "attribute name must be string"):
            getattr(objc.super(NSObject, NSObject.new()), 42)


class TestSuperDealloc(TestCase):
    def test_super_dealloc(self):
        deleted = False

        class D:
            def __del__(self):
                nonlocal deleted
                deleted = True

        s = super(D, D())
        del s
        assert deleted


class TestMagic(TestCase):
    def test_magic_nil(self):
        o = NSArray.alloc()
        o.init()

        with self.assertRaisesRegex(
            AttributeError, "cannot access attribute '__pyobjc_magic_coookie__' of NIL"
        ):
            o.__pyobjc_magic_coookie__()

    def test_magic_normal(self):
        o = NSArray.alloc().init()

        self.assertFalse(o.__pyobjc_magic_coookie__())
