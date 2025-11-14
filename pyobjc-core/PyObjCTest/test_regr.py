# XXX: This file needs to be refactored
import functools
import sys
import gc
import io
import warnings
import types
import struct
import fractions
import objc.simd

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
NSString = objc.lookUpClass("NSString")

# This metata will be ignored, overriding return value 'double'
# with a much smaller type ('char')
objc.registerMetaDataForSelector(
    b"OC_TestClass1", b"sumA:B:C:D:E:F:", {"retval": {"type": b"c"}}
)


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
    def test_sizeof_objc_object(self):
        array = NSArray.array()
        size = sys.getsizeof(array)
        self.assertIsInstance(size, int)
        self.assertGreater(size, sys.getsizeof(object()))

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

        self.assertTrue(len(w) == 0)

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

    def test_large_structs(self):

        # "Large" but simple APIs use a different code path, ensure
        # we're actually hitting that path.
        tp = structargs.StructArgClass.sumA_b_c_d_e_f_g_.__metadata__()["retval"][
            "type"
        ]
        self.assertGreater(objc._sizeOfType(tp) * 8, 256)

        inval = ((n,) * 6 for n in range(7))
        outval = structargs.StructArgClass.sumA_b_c_d_e_f_g_(*inval)
        self.assertEqual(outval, (sum(range(7)),) * 6)

    def test_empty_struct(self):
        o = structargs.StructArgClass.alloc().init()

        # libffi doesn't support calling functions with an empty struct
        # arguments (e.g. "struct empty {}", even if C compilers do.
        with self.assertRaisesRegex(
            objc.error, "Cannot create FFI CIF for i@:{empty=}: bad typedef"
        ):
            self.assertEqual(o.callWithEmpty_(()), 99)

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


class TestLargeSimpleMethod(TestCase):
    def test_large_but_simple_signature(self):
        o = OC_TestClass1.alloc().init()

        a = (1.0,) * 8
        b = (2.0,) * 8
        c = (3.0,) * 8
        d = (4.0,) * 8
        e = (5.0,) * 8
        f = (6.0,) * 8

        self.assertEqual(
            o.sumA_B_C_D_E_F_(a, b, c, d, e, f), 1.0 + 2.0 + 3.0 + 4.0 + 5.0 + 6.0
        )

        self.assertResultHasType(o.sumA_B_C_D_E_F_, objc._C_DBL)


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

        self.assertFalse(o.__pyobjc_magic_coookie__())

    def test_magic_normal(self):
        o = NSArray.alloc().init()

        self.assertFalse(o.__pyobjc_magic_coookie__())


class TestISA(TestCase):
    def test_base(self):
        o = NSArray()
        cls = o.pyobjc_ISA
        self.assertIsSubclass(cls, NSArray)

        o = NSArray.alloc()
        o.init()
        o.pyobjc_ISA


class DeallocRevives(NSObject):
    def __del__(self):
        global VALUE
        VALUE = self


class TestDelRevives(TestCase):
    def test_basic(self):
        global VALUE

        VALUE = None
        o = DeallocRevives()

        with warnings.catch_warnings():
            warnings.filterwarnings(
                "default", category=objc.RevivedObjectiveCObjectWarning
            )
            orig_stderr = sys.stderr
            try:
                sys.stderr = captured_stderr = io.StringIO()
                del o

            finally:
                sys.stderr = orig_stderr

        stderr_value = captured_stderr.getvalue()
        self.assertIn(
            "revived Objective-C object of type DeallocRevives. Object is zero-ed out.",
            stderr_value,
        )
        self.assertNotIn("Exception ignored in", stderr_value)

        self.assertEqual(repr(VALUE), "<null>")
        VALUE = None

    def test_basic_error(self):
        global VALUE

        VALUE = None
        o = DeallocRevives()

        with warnings.catch_warnings():
            warnings.filterwarnings(
                "error", category=objc.RevivedObjectiveCObjectWarning
            )
            orig_stderr = sys.stderr
            try:
                sys.stderr = captured_stderr = io.StringIO()
                del o

            finally:
                sys.stderr = orig_stderr

            stderr_value = captured_stderr.getvalue()
            self.assertIn(
                "revived Objective-C object of type DeallocRevives. Object is zero-ed out.",
                stderr_value,
            )
            self.assertIn("Exception ignored in", stderr_value)

            self.assertEqual(repr(VALUE), "<null>")
            VALUE = None


class TestMisCConversions(TestCase):
    def test_sel(self):
        # XXX: Fix me for PyObjC 12:
        self.assertEqual(objc.repythonify(b"hello", objc._C_SEL), "hello")
        self.assertEqual(objc.repythonify("hello", objc._C_SEL), "hello")
        self.assertEqual(
            objc.repythonify(NSArray.description, objc._C_SEL), "description"
        )
        self.assertEqual(objc.repythonify("hello", objc._C_SEL), "hello")
        self.assertEqual(objc.repythonify(bytearray(b"hello"), objc._C_SEL), "hello")

        self.assertEqual(objc.repythonify(b"", objc._C_SEL), None)
        self.assertEqual(objc.repythonify(bytearray(b""), objc._C_SEL), None)
        self.assertEqual(objc.repythonify("", objc._C_SEL), None)
        self.assertEqual(objc.repythonify(None, objc._C_SEL), None)

        with self.assertRaisesRegex(ValueError, "depythonifying 'SEL', got 'int'"):
            objc.repythonify(42, objc._C_SEL)

        with self.assertRaises(UnicodeEncodeError):
            objc.repythonify("hel\udffflo", objc._C_SEL)

    def test_class(self):
        self.assertEqual(objc.repythonify(None, objc._C_CLASS), None)
        self.assertEqual(objc.repythonify(NSArray, objc._C_CLASS), NSArray)
        self.assertEqual(objc.repythonify(type(NSArray), objc._C_CLASS), NSArray)

        with self.assertRaisesRegex(ValueError, "depythonifying 'Class', got 'object'"):
            objc.repythonify(object(), objc._C_CLASS)

        with self.assertRaisesRegex(ValueError, "depythonifying 'Class', got 'type'"):
            objc.repythonify(type, objc._C_CLASS)

    def test_union(self):
        inval = struct.pack("=i", 42)
        outval = objc.repythonify(inval, b"(p=if)")
        self.assertEqual(inval, outval)

        inval = struct.pack("=f", 42.5)
        outval = objc.repythonify(inval, b"(p=fi)")
        self.assertEqual(inval, outval)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'union' of size 4, got byte string of 3"
        ):
            objc.repythonify(inval[:-1], b"(p=fi)")

        with self.assertRaisesRegex(objc.error, "invalid union encoding"):
            objc.repythonify(inval, b"(p=fi")

    def test_vector(self):
        out = objc.repythonify((42,) * 4, b"<4i>")
        self.assertEqual(out, objc.simd.vector_int4(42, 42, 42, 42))

        with self.assertRaisesRegex(objc.error, "Unsupported SIMD encoding: <5i>"):
            objc.repythonify((42,) * 5, b"<5i>")

    def test_float(self):
        for encoding in (objc._C_FLT, objc._C_DBL, objc._C_LNG_DBL):
            with self.subTest(encoding=encoding):
                self.assertEqual(objc.repythonify(2.5, encoding), 2.5)

                f = fractions.Fraction(1, 2)
                self.assertEqual(float(f), 0.5)

                self.assertEqual(objc.repythonify(f, encoding), 0.5)

                with self.assertRaisesRegex(
                    ValueError, "depythonifying '[a-z ]*', got 'str'"
                ):
                    objc.repythonify("2.5", encoding)

                with self.assertRaisesRegex(
                    OverflowError, "int too large to convert to float"
                ):
                    objc.repythonify(2**10000, encoding)

                with self.assertRaisesRegex(
                    ValueError, "depythonifying '.*', got 'object'"
                ):
                    objc.repythonify(object(), encoding)


class TestConvertNegativeToUnsigedWarns(TestCase):
    def test_repythonify_negative_int(self):
        class Number:
            def __int__(self):
                return -28

        with warnings.catch_warnings():
            warnings.filterwarnings("error", category=DeprecationWarning)

            with self.assertRaisesRegex(
                DeprecationWarning, "converting negative value to unsigned integer"
            ):
                objc.repythonify(-40, b"I")

            with self.assertRaisesRegex(
                DeprecationWarning, "converting negative value to unsigned integer"
            ):
                objc.repythonify(Number(), b"I")


class TestKeywordArgumentsForSelect(TestCase):
    def test_kwargs_not_allowed(self):
        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            NSArray.arrayWithArray_(a=4)


class TestInvokingMethods(TestCase):
    def invokeDescriptionOf(self, value):
        signature = value.methodSignatureForSelector_(b"description")
        inv = NSInvocation.invocationWithMethodSignature_(signature)
        inv.setTarget_(value)
        inv.setSelector_(b"description")
        value.forwardInvocation_(inv)
        return inv.getReturnValue_(None)

    def test_nsobject(self):
        v = NSObject.alloc().init()
        with self.assertRaisesRegex(
            ValueError, "unrecognized selector sent to instance"
        ):
            self.invokeDescriptionOf(v)

    def test_pyobject(self):
        v = OCTestRegrWithGetItem.alloc().init()
        with self.assertRaisesRegex(
            ValueError, "unrecognized selector sent to instance"
        ):
            self.invokeDescriptionOf(v)

    def test_pyobject_with_descr(self):
        class OC_ObjectWithDescription(NSObject):
            def description(self):
                return "<an object>"

        v = OC_ObjectWithDescription.alloc().init()
        self.assertEqual(v.description(), "<an object>")
        self.assertEqual(self.invokeDescriptionOf(v), "<an object>")

    def test_forward_invalid(self):
        value = OCTestRegrWithGetItem.alloc().init()

        signature = value.methodSignatureForSelector_(b"description")
        inv = NSInvocation.invocationWithMethodSignature_(signature)
        inv.setTarget_(value)
        inv.setSelector_(b"descriptions")

        with self.assertRaisesRegex(
            ValueError, "unrecognized selector sent to instance"
        ):
            value.forwardInvocation_(inv)


class TestSelectorEdgeCases(TestCase):
    def test_sel_incomparable(self):
        def function(self):
            pass

        sel1 = objc.selector(function, selector=b"hello", signature=b"@@:")

        class Callable:
            def __call__(self):
                return 99

            def __eq__(self, other):
                raise RuntimeError("no comparison")

        sel2 = objc.selector(Callable(), selector=b"hello", signature=b"@@:")

        with self.assertRaisesRegex(RuntimeError, "no comparison"):
            sel1 == sel2  # noqa: B015

    def test_callable_with_name_issues(self):
        class Callable:
            def __call__(self):
                return 99

        func = Callable()
        with self.assertRaisesRegex(
            AttributeError, "'Callable' object has no attribute '__name__'"
        ):
            objc.selector(func)

        func.__name__ = "hello \udff0"
        with self.assertRaisesRegex(UnicodeEncodeError, "surrogates"):
            objc.selector(func)

        func.__name__ = 42
        with self.assertRaisesRegex(TypeError, "__name__ is not a string"):
            objc.selector(func)

    def test_calling_abstract(self):
        obj = NSObject.alloc().init()

        sel = objc.selector(None, selector=b"hello:", signature=b"@@:n^f")

        with self.assertRaisesRegex(
            TypeError, "Calling abstract methods with selector 'hello:'"
        ):
            sel(obj, None)

    def test_classmethod(self):
        @classmethod
        def func(cls):
            pass

        sel = objc.selector(func)
        self.assertEqual(sel.selector, b"func")
        self.assertTrue(sel.isClassMethod)

    def test_staticmethod(self):
        @staticmethod
        def func():
            pass

        with self.assertRaisesRegex(TypeError, "cannot use staticmethod"):
            objc.selector(func)


class TestStringSpecials(TestCase):
    def test_passing_string_as_self(self):
        strval = NSString.stringWithString_("hello")
        arrval = NSArray.alloc().init()
        self.assertEqual(arrval.count(), 0)

        m = arrval.count.definingClass.__dict__["count"]
        self.assertEqual(m(arrval), 0)

        with self.assertRaisesRegex(
            TypeError,
            "Expecting instance of .* as self, got one of objc.pyobjc_unicode",
        ):
            m(strval)

    def test_passing_non_string_as_self_simple(self):
        o = NSString.stringWithString_("hello")
        self.assertEqual(o.length(), 5)
        m = o.length.definingClass.__dict__["length"]

        self.assertEqual(m(o), 5)
        self.assertEqual(m(o.nsstring()), 5)
        with self.assertRaisesRegex(
            TypeError, "Expecting instance of .* as self, got one of str"
        ):
            m("Theo")

        with self.assertRaisesRegex(
            TypeError, "Expecting instance of .* as self, got one of int"
        ):
            m(42)

    def test_passing_non_string_as_self_complex(self):
        o = NSString.stringWithString_("hello")

        if not o.getCharacters_range_.__metadata__()["arguments"][2]["type"].startswith(
            b"o"
        ):
            objc.registerMetaDataForSelector(
                b"NSString",
                b"getCharacters:range:",
                {
                    "arguments": {
                        2
                        + 0: {
                            "type_modifier": b"o",
                            "c_array_length_in_arg": 2 + 1,
                            "type": b"^" + objc._C_UNICHAR,
                        }
                    }
                },
            )

        self.assertArgIsOut(o.getCharacters_range_, 0)
        self.assertArgSizeInArg(o.getCharacters_range_, 0, 1)

        self.assertEqual(o.getCharacters_range_(None, (0, 2)), "he")

        m = o.getCharacters_range_.definingClass.__dict__["getCharacters_range_"]

        self.assertEqual(m(o, None, (0, 3)), "hel")
        self.assertEqual(m(o.nsstring(), None, (0, 3)), "hel")

        with self.assertRaisesRegex(
            TypeError, "Expecting instance of .* as self, got one of str"
        ):
            m("Theo", None, (0, 3))

        with self.assertRaisesRegex(
            TypeError, "Expecting instance of .* as self, got one of int"
        ):
            m(42, None, (0, 3))


class TestClasses(TestCase):
    def test_setting_invalid_attribute(self):
        # XXX: This is a side effect of supporting KVO. Consider adding
        #      the same limitation to classes for consistency.
        name = "\udfffname"
        o = OCTestRegrWithGetItem.alloc().init()
        with self.assertRaisesRegex(UnicodeEncodeError, "surrogates not allowed"):
            setattr(o, name, 42)

    def test_attributes(self):
        o = OCTestRegrWithGetItem.alloc().init()
        o.key = 42
        self.assertEqual(o.key, 42)

        del o.key
        with self.assertRaises(AttributeError):
            del o.nosuchkey

    def test_class_comparisons(self):
        with self.assertRaisesRegex(
            TypeError, "not supported between instances of 'NSArray' and 'int'"
        ):
            NSArray < 42  # noqa: B015

        with self.assertRaisesRegex(
            TypeError, "not supported between instances of 'int' and 'NSObject'"
        ):
            42 < NSObject  # noqa: B015

    def test_compare_class_with_non_class(self):
        self.assertTrue(NSObject != 42)
        self.assertTrue(42 != NSObject)
        self.assertFalse(NSObject == 42)
        self.assertFalse(42 == NSObject)

    def test_compare_class_with_class(self):
        self.assertTrue(NSObject != objc.objc_object)
        self.assertFalse(NSObject == objc.objc_object)
        self.assertTrue(objc.objc_object != NSObject)
        self.assertFalse(objc.objc_object == NSObject)

        self.assertTrue(NSObject != NSString)
        self.assertFalse(NSObject == NSString)

        self.assertTrue(NSObject == NSObject)
        self.assertFalse(NSObject != NSObject)

        self.assertFalse(NSObject < NSObject)
        self.assertTrue(NSObject <= NSObject)
        self.assertFalse(NSObject > NSObject)
        self.assertTrue(NSObject >= NSObject)

        self.assertTrue(NSObject < NSString)
        self.assertTrue(NSObject <= NSString)
        self.assertFalse(NSObject > NSString)
        self.assertFalse(NSObject >= NSString)

        self.assertFalse(NSString < NSObject)
        self.assertFalse(NSString <= NSObject)
        self.assertTrue(NSString > NSObject)
        self.assertTrue(NSString >= NSObject)

        self.assertTrue(objc.objc_object < NSObject)
        self.assertTrue(objc.objc_object <= NSObject)
        self.assertFalse(objc.objc_object > NSObject)
        self.assertFalse(objc.objc_object >= NSObject)

        self.assertFalse(NSObject < objc.objc_object)
        self.assertFalse(NSObject <= objc.objc_object)
        self.assertTrue(NSObject > objc.objc_object)
        self.assertTrue(NSObject >= objc.objc_object)


class TestSelectorDetails(TestCase):
    def test_selector_unbound(self):
        o = NSString.alloc().initWithString_("hello")
        m = o.description.definingClass.__dict__["description"]
        r1 = m(o)
        r2 = m(o)
        self.assertEqual(r1, r2)
        self.assertIsInstance(r1, str)

        with self.assertRaisesRegex(TypeError, "Missing argument: self"):
            m()

        r3 = m(o.nsstring())
        self.assertEqual(r1, r3)

        m = o.getCharacters_range_.definingClass.__dict__["getCharacters_range_"]
        with self.assertRaisesRegex(TypeError, "Missing argument: self"):
            m()

        m = NSObject.alloc().init().description.definingClass.__dict__["description"]
        with self.assertRaisesRegex(
            TypeError,
            "Expecting instance of NSObject as self, got one of objc.pyobjc_unicode",
        ):
            m(o)
        with self.assertRaisesRegex(
            TypeError,
            "Expecting instance of NSObject as self, got one of objc.pyobjc_unicode",
        ):
            m(o)

    def test_selector_invalid_typestr(self):
        o = NSArray.array()
        m = o.reversedArray
        m.signature = b"X@:"
        with self.assertRaisesRegex(objc.error, "Unhandled type"):
            m()
        m.signature = b"@@:"

        NSArray.__dict__["reversedArray"].signature = b"X@:"
        with self.assertRaisesRegex(objc.error, "Unhandled type"):
            self.assertEqual(o.reversedArray.signature, b"X@:")
        NSArray.__dict__["reversedArray"].signature = b"@@:"
        self.assertEqual(o.reversedArray.signature, b"@@:")

    def test_selector_no_compare(self):
        class C:
            def __call__(self, a):
                pass

            def __eq__(self, b):
                raise RuntimeError("no compare")

        s = objc.selector(C(), selector=b"method:")
        t = objc.selector(lambda x, y: 42, selector=b"method:")

        with self.assertRaisesRegex(RuntimeError, "no compare"):
            s == t  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "no compare"):
            s != t  # noqa: B015

    def test_calling_abstract_selector(self):
        o = NSObject.alloc().init()
        s = objc.selector(None, selector=b"method:", signature=b"@@:@")
        with self.assertRaisesRegex(
            TypeError, "Calling abstract methods with selector 'method:'"
        ):
            s(o, 1)

    def test_calling_without_self(self):
        s = objc.selector(lambda s: 42, selector=b"method", signature=b"@@:")

        with self.assertRaisesRegex(TypeError, "need self argument"):
            s()

    def test_selector_classmethod(self):
        @classmethod
        def classMethod(cls):
            pass

        s = objc.selector(classMethod)
        self.assertTrue(s.isClassMethod)
        self.assertEqual(s.selector, b"classMethod")
        self.assertEqual(s.signature, b"v@:")

    def test_selector_staticmethod(self):
        @staticmethod
        def classMethod(cls):
            pass

        with self.assertRaisesRegex(
            TypeError, "cannot use staticmethod as the callable for a selector."
        ):
            objc.selector(classMethod)

    def test_descr_get_instance(self):
        @objc.selector
        def method(self):
            return 42

        bound = method.__get__(NSObject.alloc().init())

        class MyClass:
            method = bound

        self.assertIs(MyClass().method, bound)

    def test_descr_get_class(self):
        @objc.selector
        @classmethod
        def method(self):
            return 42

        with self.assertRaisesRegex(TypeError, "class is NULL"):
            # XXX: This doesn't match the behaviour of classmethod()
            method.__get__(NSObject)

    def test_invalid_signature(self):
        with self.assertRaisesRegex(ValueError, "invalid signature"):
            objc.selector(lambda x: 42, selector=b"method", signature=b"X@:")

        s = objc.selector(lambda x: 42, selector=b"method", signature=b"@@:")
        self.assertEqual(s.native_signature, b"@@:")
        s.signature = b"X@:"
        with self.assertRaisesRegex(objc.error, " Unhandled type"):
            s.signature

        with self.assertRaisesRegex(AttributeError, "not writable"):
            s.native_signature = b"X@:"
        self.assertEqual(s.native_signature, b"@@:")
        s.__get__(NSObject())
        with self.assertRaisesRegex(objc.error, " Unhandled type"):
            s.__metadata__()
