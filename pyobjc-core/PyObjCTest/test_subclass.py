import objc
import sys
import io
import types
import warnings
import builtins
from PyObjCTest.testbndl import PyObjC_TestClass3
from PyObjCTools.TestSupport import TestCase
from .objectint import OC_ObjectInt
from objc import super  # noqa: A004

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass("NSObject")
NSArray = objc.lookUpClass("NSArray")
NSData = objc.lookUpClass("NSData")
NSAutoreleasePool = objc.lookUpClass("NSAutoreleasePool")


class TestSubclassing(TestCase):
    def test_dont_inherit_from_objc_root(self):
        with self.assertRaises(TypeError):

            class DirectObjectObject(objc.objc_object):
                pass

    # XXX: Likewise for objc.objc_class?
    #      This currently does not raise, not sure
    #      if subclassing would ever be valid or useful.

    def testMethodRaise(self):
        # Defining a method whose name is a keyword followed by two underscores
        # should define the method name without underscores in the runtime,
        # and this method should be accesible both with and without the
        # underscores.

        class RaiseClass(NSObject):
            def raise__(self):
                pass

        self.assertHasAttr(RaiseClass, "raise__")
        self.assertHasAttr(RaiseClass, "raise")
        self.assertEqual(RaiseClass.raise__.selector, b"raise")
        self.assertEqual(getattr(RaiseClass, "raise").selector, b"raise")

        raiseInstance = RaiseClass.alloc().init()
        self.assertHasAttr(raiseInstance, "raise__")
        self.assertHasAttr(raiseInstance, "raise")
        self.assertEqual(RaiseClass.raise__.selector, b"raise")
        self.assertEqual(getattr(RaiseClass, "raise").selector, b"raise")

    def testMIObjC(self):
        try:

            class MIClass1(NSObject, NSArray):
                pass

            self.fail("Can multiple inherit from two objc classes")
        except TypeError:
            pass

    def testSubclassOfSubclass(self):
        class Level1Class(NSObject):
            def hello(self):
                return "level1"

        class Level2Class(Level1Class):
            def hello(self):
                return "level2"

            def superHello(self):
                return objc.super(Level2Class, self).hello()

            def description(self):
                return objc.super(Level2Class, self).description()

            @objc.objc_method(signature=b"f@:d")
            def roundValue_(self, value):
                return value / 2

            @objc.python_method
            def world(self):
                return "world"

        obj = Level1Class.alloc().init()
        v = obj.hello()
        self.assertEqual(v, "level1")

        obj = Level2Class.alloc().init()
        v = obj.hello()
        self.assertEqual(v, "level2")

        v = obj.superHello()
        self.assertEqual(v, "level1")

        v = obj.description()
        # this may be a bit hardwired for comfort
        self.assertEqual(v.find("<Level2Class"), 0)

        self.assertTrue(OC_ObjectInt.respondsToSelector_of_(b"hello", obj))
        self.assertFalse(OC_ObjectInt.respondsToSelector_of_(b"world", obj))

        m = OC_ObjectInt.methodSignatureForSelector_of_(b"hello", obj)
        self.assertEqual(m.numberOfArguments(), 2)
        self.assertEqual(m.methodReturnType(), b"@")

        m = OC_ObjectInt.methodSignatureForSelector_of_(b"roundValue:", obj)
        self.assertEqual(m.numberOfArguments(), 3)
        self.assertEqual(m.methodReturnType(), b"f")
        self.assertEqual(m.getArgumentTypeAtIndex_(2), b"d")

        NSInvocation = objc.lookUpClass("NSInvocation")
        inv = NSInvocation.invocationWithMethodSignature_(m)
        inv.setTarget_(obj)
        inv.setSelector_(b"roundValue:")
        inv.setArgument_atIndex_(31.0, 2)
        inv.invoke()
        self.assertEqual(inv.getReturnValue_(None), 15.5)

    def testMethodSignature(self):
        class Signature(NSObject):
            def test_x_(self, arg, x):
                pass

            test_x_ = objc.selector(test_x_, signature=b"v@:@i")

        v = Signature.new()

        self.assertIsInstance(v, Signature)

        self.assertEqual(v.methodSignatureForSelector_("foo:"), None)

        x = v.methodSignatureForSelector_("test:x:")
        self.assertIsNotNone(x)

        self.assertEqual(x.methodReturnType(), b"v")
        self.assertEqual(x.numberOfArguments(), 4)
        self.assertEqual(x.getArgumentTypeAtIndex_(0), b"@")
        self.assertEqual(x.getArgumentTypeAtIndex_(1), b":")
        self.assertEqual(x.getArgumentTypeAtIndex_(2), b"@")
        self.assertEqual(x.getArgumentTypeAtIndex_(3), b"i")

    def test_subclassMethodSignatureError(self):
        class OC_SubClassingMethodSignatureBase(NSObject):
            def method(self):
                return 1

        self.assertResultHasType(OC_SubClassingMethodSignatureBase.method, objc._C_ID)

        with self.assertRaisesRegex(
            objc.BadPrototypeError,
            "signature that is not compatible with super-class: @@: != d@:",
        ):

            class OC_SubClassingMethodSignatureChild(OC_SubClassingMethodSignatureBase):
                @objc.objc_method(signature=b"d@:")
                def method(self):
                    pass


class TestSelectors(TestCase):
    def testSelectorRepr(self):
        class SelectorRepr(NSObject):
            def foo(self):
                pass

        self.assertStartswith(
            repr(SelectorRepr.foo), "<unbound selector foo of SelectorRepr at"
        )

        self.assertRegex(
            repr(SelectorRepr.new().foo), "<selector foo of <SelectorRepr:.*>"
        )

        @objc.selector
        def someSel_arg_(self, a, b):
            pass

        self.assertStartswith(repr(someSel_arg_), "<unbound selector someSel:arg: at")


class TestCopying(TestCase):
    def testCopy(self):
        class MyCopyClass(NSObject):
            def copyWithZone_(self, zone):
                # NSObject doesn't implement the copying protocol
                # o = super(MyCopyClass, self).copyWithZone_(zone)
                o = self.__class__.alloc().init()
                o.foobar = 2
                return o

            copyWithZone_ = objc.selector(
                copyWithZone_,
                signature=NSObject.copyWithZone_.signature,
                isClassMethod=0,
            )

        # Make sure the runtime correctly marked our copyWithZone_
        # implementation.
        o = MyCopyClass.alloc().init()

        self.assertFalse(o.copyWithZone_.__metadata__()["classmethod"])
        self.assertTrue(o.copyWithZone_.__metadata__()["retval"]["already_retained"])
        # self.assertEqual(
        #    o.copyWithZone_.callable,
        #    MyCopyClass.__dict__['copyWithZone_'].callable
        # )

        o = MyCopyClass.alloc().init()
        o.foobar = 1

        self.assertEqual(o.foobar, 1)

        # Make a copy from ObjC (see testbundle.m)
        c = PyObjC_TestClass3.copyValue_(o)

        self.assertIsInstance(c, MyCopyClass)
        self.assertEqual(c.foobar, 2)

    def testMultipleInheritance1(self):
        # New-style class mixin
        class MixinClass1:
            def mixinMethod(self):
                return "foo"

        class MITestClass1(NSObject, MixinClass1):
            def init(self):
                return NSObject.pyobjc_instanceMethods.init(self)

        self.assertHasAttr(MITestClass1, "mixinMethod")

        o = MITestClass1.alloc().init()
        self.assertEqual(o.mixinMethod(), "foo")

    def testMultipleInheritance2(self):
        # old-style class mixin
        class MixinClass2:
            def mixinMethod(self):
                return "foo"

        class MITestClass2(NSObject, MixinClass2):
            def init(self):
                return NSObject.pyobjc_instanceMethods.init(self)

        self.assertHasAttr(MITestClass2, "mixinMethod")

        o = MITestClass2.alloc().init()
        self.assertEqual(o.mixinMethod(), "foo")

    def testMultipleInheritance3(self):
        # New-style class mixin
        class MixinClass3:
            def mixinMethod(self):
                return "foo"

        class MITestClass3(NSObject, MixinClass3):
            def init(self):
                return super().init()

        self.assertHasAttr(MITestClass3, "mixinMethod")

        o = MITestClass3.alloc().init()
        self.assertEqual(o.mixinMethod(), "foo")


class TestClassMethods(TestCase):
    def testClassMethod(self):
        """check that classmethod()-s are converted to selectors"""

        class ClassMethodTest(NSObject):
            def clsMeth(self):
                return "hello"

            clsMeth = classmethod(clsMeth)

        self.assertIsInstance(ClassMethodTest.clsMeth, objc.selector)
        self.assertTrue(ClassMethodTest.clsMeth.isClassMethod)

    def testStaticMethod(self):
        """check that staticmethod()-s are not converted to selectors"""

        class StaticMethodTest(NSObject):
            def stMeth(self):
                return "hello"

            stMeth = staticmethod(stMeth)

        def func():
            pass

        self.assertIsInstance(StaticMethodTest.stMeth, type(func))


class TestOverridingSpecials(TestCase):
    def testOverrideSpecialMethods_alloc(self):
        aList = [0]

        class ClassWithAlloc(NSObject):
            def alloc(cls):
                aList[0] += 1
                return objc.super(ClassWithAlloc, cls).alloc()

        self.assertEqual(aList[0], 0)
        o = ClassWithAlloc.alloc().init()
        self.assertEqual(aList[0], 1)
        self.assertIsInstance(o, NSObject)
        del o

    def testOverrideSpecialMethods_retain_release(self):
        aList = []

        class ClassWithRetaining(NSObject):
            def retain(self):
                aList.append("retain")
                v = objc.super(ClassWithRetaining, self).retain()
                return v

            def release(self):
                aList.append("release")
                return objc.super(ClassWithRetaining, self).release()

            def __del__(self):
                aList.append("__del__")

        o = ClassWithRetaining.alloc().init()
        v = o.retainCount()
        o.retain()
        self.assertEqual(aList, ["retain"])
        self.assertEqual(o.retainCount(), v + 1)
        o.release()
        self.assertEqual(aList, ["retain", "release"])
        self.assertEqual(o.retainCount(), v)
        del o

        self.assertEqual(aList, ["retain", "release", "release", "__del__"])

        # Test again, now remove all python references and create one
        # again.
        del aList[:]
        pool = NSAutoreleasePool.alloc().init()
        o = ClassWithRetaining.alloc().init()
        v = NSArray.arrayWithArray_([o])
        del o
        self.assertEqual(aList, ["retain"])
        o = v[0]
        self.assertEqual(aList, ["retain"])
        del v
        del o
        del pool

        self.assertEqual(aList, ["retain", "release", "release", "__del__"])

    def testOverrideSpecialMethods_retainCount(self):
        aList = []

        class ClassWithRetainCount(NSObject):
            def retainCount(self):
                aList.append("retainCount")
                return objc.super(ClassWithRetainCount, self).retainCount()

        o = ClassWithRetainCount.alloc().init()
        self.assertEqual(aList, [])
        v = o.retainCount()
        self.assertIsInstance(v, int)
        self.assertEqual(aList, ["retainCount"])
        del o

    def testOverrideDealloc(self):
        aList = []

        class Dummy:
            def __del__(self):
                aList.append("__del__")

        self.assertEqual(aList, [])
        Dummy()
        self.assertEqual(aList, ["__del__"])

        class ClassWithDealloc(NSObject):
            def init(self):
                self = objc.super(ClassWithDealloc, self).init()
                if self is not None:
                    self.obj = Dummy()
                return self

            def dealloc(self):
                aList.append("dealloc")
                return objc.super(ClassWithDealloc, self).dealloc()

        del aList[:]
        o = ClassWithDealloc.alloc().init()
        self.assertEqual(aList, [])
        del o
        self.assertEqual(len(aList), 2)
        self.assertIn("dealloc", aList)
        self.assertIn("__del__", aList)

        class SubClassWithDealloc(ClassWithDealloc):
            def dealloc(self):
                aList.append("dealloc.dealloc")
                return objc.super(SubClassWithDealloc, self).dealloc()

        del aList[:]
        o = SubClassWithDealloc.alloc().init()
        self.assertEqual(aList, [])
        del o
        self.assertEqual(len(aList), 3)
        self.assertIn("dealloc.dealloc", aList)
        self.assertIn("dealloc", aList)
        self.assertIn("__del__", aList)

        class ClassWithDeallocAndDel(NSObject):
            def init(self):
                self = objc.super(ClassWithDeallocAndDel, self).init()
                if self is not None:
                    self.obj = Dummy()
                return self

            def dealloc(self):
                aList.append("dealloc")
                return objc.super(ClassWithDeallocAndDel, self).dealloc()

            def __del__(self):
                aList.append("mydel")

        del aList[:]
        o = ClassWithDeallocAndDel.alloc().init()
        self.assertEqual(aList, [])
        del o
        self.assertEqual(len(aList), 3)
        self.assertIn("mydel", aList)
        self.assertIn("dealloc", aList)
        self.assertIn("__del__", aList)

    def testMethodNames(self):
        class MethodNamesClass(NSObject):
            def someName_andArg_(self, name, arg):
                pass

            def _someName_andArg_(self, name, arg):
                pass

            def raise__(self):
                pass

            def froobnicate__(self, a, b):
                pass

        self.assertEqual(
            MethodNamesClass.someName_andArg_.selector, b"someName:andArg:"
        )
        self.assertEqual(
            MethodNamesClass._someName_andArg_.selector, b"_someName:andArg:"
        )
        self.assertEqual(MethodNamesClass.raise__.selector, b"raise")

        # This must be a selector due to having selectors with unnamed parts
        # in Objective-C.
        self.assertIsInstance(MethodNamesClass.froobnicate__, objc.selector)

    def testOverrideRespondsToSelector(self):
        class OC_RespondsClass(NSObject):
            def initWithList_(self, lst):
                objc.super(OC_RespondsClass, self).init()
                self.lst = lst
                return self

            def respondsToSelector_(self, selector):
                self.lst.append(selector)
                return objc.super(OC_RespondsClass, self).respondsToSelector_(selector)

        lst = []
        o = OC_RespondsClass.alloc().initWithList_(lst)

        self.assertEqual(lst, [])

        b = o.respondsToSelector_("init")
        self.assertTrue(b)
        self.assertEqual(lst, ["init"])

        b = o.respondsToSelector_("alloc")
        self.assertFalse(b)
        self.assertEqual(lst, ["init", "alloc"])

    def testOverrideInstancesRespondToSelector(self):
        lst = []

        class OC_InstancesRespondClass(NSObject):
            @classmethod
            def instancesRespondToSelector_(cls, selector):
                lst.append(selector)
                return objc.super(
                    OC_InstancesRespondClass, cls
                ).instancesRespondToSelector_(selector)

        self.assertEqual(lst, [])

        b = OC_InstancesRespondClass.instancesRespondToSelector_("init")
        self.assertTrue(b)
        self.assertEqual(lst, ["init"])

        b = OC_InstancesRespondClass.instancesRespondToSelector_("alloc")
        self.assertFalse(b)
        self.assertEqual(lst, ["init", "alloc"])

    def testImplementingSetValueForKey(self):
        values = {}

        class CrashTest(NSObject):
            def setValue_forKey_(self, v, k):
                values[k] = v

        o = CrashTest.alloc().init()
        o.setValue_forKey_(42, "key")

        self.assertEqual(values, {"key": 42})

    def test_invalid_slots(self):
        with self.assertRaisesRegex(TypeError, "not iterable"):

            class ClassWithIntegerSlots(NSObject):
                __slots__ = 42

        with self.assertRaisesRegex(TypeError, "be str, not int"):

            class ClassWithIntegerInSlots(NSObject):
                __slots__ = (
                    "a",
                    42,
                )

        with self.assertRaisesRegex(UnicodeEncodeError, r".*surrogates not allowed"):

            class ClassWithInvalidNamedSlot(NSObject):
                __slots__ = "\uDC00"

    def test_dict_as_slots(self):
        # When __slots__ is a dict pydoc can use the
        # values to document slots.

        class ClassWithDictSlots(NSObject):
            __slots__ = {"a": "some a", "b": "some b"}

        self.assertIsInstance(ClassWithDictSlots.__slots__, dict)
        self.assertEqual(ClassWithDictSlots.__slots__, {"a": "some a", "b": "some b"})

    def test_override_name(self):
        objc.lookUpClass("NSAttributedString")

        with self.assertRaisesRegex(
            objc.error, "NSAttributedString is overriding existing Objective-C class"
        ):

            class NSAttributedString(NSObject):
                pass

    def test_name_with_invalid_characters(self):
        with self.assertRaisesRegex(
            objc.error, "'MyClass!' not a valid Objective-C class name"
        ):
            type("MyClass!", (NSObject,), {})

    def test_mutate_dict_during_setup(self):
        class Helper:
            def __pyobjc_class_setup__(
                self, key, class_dict, instance_methods, class_methods
            ):
                for k in ("attr1", "attr2"):
                    try:
                        del class_dict[k]
                    except KeyError:
                        pass

    def test_class_dict_contains_int(self):
        class NoCompare:
            def __eq__(self, other):
                raise RuntimeError("Cannot compare")

            def __hash__(self):
                return 42

        @objc.typedSelector(b"i@:")
        def someSelector(self):
            return 42

        with self.assertRaisesRegex(RuntimeError, "Cannot compare"):
            type("ClassWithIntInDict", (NSObject,), {NoCompare(): someSelector})

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)

            cls = type("ClassWithIntInDict", (NSObject,), {42: someSelector})

        self.assertIsInstance(cls.someSelector, objc.selector)
        self.assertIsInstance(cls.__dict__[42], objc.selector)

    def test_reuse_selector(self):
        class ClassWithOriginalSelector(NSObject):
            def mySelector(self):
                return "hello there"

        class ClassWithCopiedSelector(NSObject):
            mySelector = ClassWithOriginalSelector.mySelector

        value = ClassWithOriginalSelector.alloc().init()
        self.assertEqual(value.mySelector(), "hello there")

        value = ClassWithCopiedSelector.alloc().init()
        self.assertEqual(value.mySelector(), "hello there")

        self.assertEqual(
            ClassWithOriginalSelector.mySelector.__objclass__, ClassWithOriginalSelector
        )
        self.assertEqual(
            ClassWithCopiedSelector.mySelector.__objclass__, ClassWithCopiedSelector
        )

    def test_method_with_nonascii_name(self):
        with self.assertRaisesRegex(
            UnicodeEncodeError,
            r"'ascii' codec can't encode character '\\xf6' in position 6: ordinal not in range\(128\)",
        ):

            class ClassWithNonASCIIMethod(NSObject):
                def myMethöd(self):
                    pass

    def test_method_with_integer_name(self):
        def myMethod(self):
            return "gone"

        with self.assertRaisesRegex(
            TypeError, "method name is of type int, not a string"
        ):
            type("ClassWithNumberMethod", (NSObject,), {42: myMethod})

    def test_special_methods(self):
        class ClassWithEq(NSObject):
            def __eq__(self, other):
                return True

        self.assertNotIsInstance(ClassWithEq.__eq__, objc.selector)

    def test_del_raises(self):
        class ClassWithDel(NSObject):
            def __del__(self):
                raise ValueError("huh?")

        o = ClassWithDel.alloc().init()

        orig_stderr = sys.stderr
        try:
            sys.stderr = captured_stderr = io.StringIO()

            del o

        finally:
            sys.stderr = orig_stderr

        self.assertIn("ValueError: huh", captured_stderr.getvalue())
        self.assertIn("Exception ignored", captured_stderr.getvalue())

    def test_uninit_warn_as_error(self):
        o = NSObject.alloc()

        with warnings.catch_warnings():
            warnings.simplefilter("error", category=objc.UninitializedDeallocWarning)

            orig_stderr = sys.stderr
            try:
                sys.stderr = captured_stderr = io.StringIO()

                del o

            finally:
                sys.stderr = orig_stderr

        self.assertIn(
            "leaking an uninitialized object of type NSObject",
            captured_stderr.getvalue(),
        )
        self.assertIn("Exception ignored", captured_stderr.getvalue())


class TestSelectorAttributes(TestCase):
    # XXX: These should be moved to a different file and
    #      test all attributes...

    def test_selector_hash(self):
        @objc.selector
        def mySelector(self):
            return 1

        self.assertIsInstance(hash(mySelector), int)

        class ClassForTestingHash(NSObject):
            def aSelector(self):
                pass

        self.assertIsInstance(hash(ClassForTestingHash.aSelector), int)
        self.assertIsInstance(hash(ClassForTestingHash.alloc().init().aSelector), int)

    def test_selector_self(self):
        @objc.selector
        def mySelector(self):
            return 1

        self.assertIs(mySelector.self, None)

        obj = NSObject.alloc().init()
        v = mySelector.__get__(obj, NSObject)
        self.assertIs(v.self, obj)

    def test_selector_class(self):
        @objc.selector
        def mySelector(self):
            return 1

        self.assertIs(mySelector.definingClass, None)

        obj = NSObject.alloc().init()
        v = mySelector.__get__(obj, NSObject)
        self.assertIs(v.definingClass, None)

        # XXX: See also test_methodlookiup.py

    def test_seleoctor_required(self):
        @objc.selector
        def mySelector(self):
            pass

        self.assertIs(mySelector.isRequired, True)

        def mySelector(self):
            pass

        mySelector = objc.selector(mySelector, isRequired=0)
        self.assertIs(mySelector.isRequired, False)

    def test_selector_metadata(self):
        @objc.selector
        def mySelector(self):
            return 1

        self.assertIsInstance(mySelector.__metadata__(), dict)
        self.assertIs(mySelector.__metadata__()["classmethod"], False)

        # XXX: Tests for the detailed contents

    def test_selector_native_signature(self):
        @objc.selector
        def mySelector(self):
            return 1

        self.assertEqual(mySelector.native_signature, b"@@:")

    # XXX: selector.signature is tested in test_signature.py
    # XXX: selector.isHidden is tested in test_hidden_selector.py

    def test_selector_selector(self):
        @objc.selector
        def mySelector(self):
            return 1

        @objc.selector
        def mySelector_arg_(self):
            return 1

        self.assertEqual(mySelector.selector, b"mySelector")
        self.assertEqual(mySelector_arg_.selector, b"mySelector:arg:")

    def test_selector_name(self):
        @objc.selector
        def mySelector(self):
            return 1

        @objc.selector
        def mySelector_arg_(self):
            return 1

        self.assertEqual(mySelector.__name__, "mySelector")
        self.assertEqual(mySelector_arg_.__name__, "mySelector_arg_")

    def test_native_repr(self):
        obj = NSObject.alloc().init()
        obj.description()

        s = NSObject.__dict__["description"]
        self.assertEqual(repr(s), "<unbound native-selector description in NSObject>")

        self.assertRegex(
            repr(obj.description),
            r"^<native-selector description of <NSObject: 0x[0-9a-f]+>>$",
        )

    def test_python_compare(self):
        class ClassForTestingCompare1(NSObject):
            def meth1(self):
                pass

            def meth2(self):
                pass

        class ClassForTestingCompare2(NSObject):
            def meth1(self):
                pass

        obj = ClassForTestingCompare1.alloc().init()
        obj2 = ClassForTestingCompare2.alloc().init()

        meth1 = obj.meth1
        meth2 = obj.meth2
        meth3 = obj2.meth1

        self.assertTrue(meth1 == meth1)
        self.assertFalse(meth1 != meth1)

        self.assertTrue(meth1 != meth2)
        self.assertFalse(meth1 == meth2)

        self.assertTrue(meth1 != meth3)
        self.assertFalse(meth1 == meth3)

        self.assertTrue(meth1 != dir)

        self.assertTrue(meth1 != dir)
        self.assertFalse(meth1 == dir)

        # XXX: Ordering between selector instances
        #      is not very usefull, but the code
        #      has been here for ages.
        #
        #      Consider deprecating
        self.assertFalse(meth1 < meth1)
        self.assertTrue(meth1 < meth2)
        self.assertTrue(meth1 <= meth1)
        self.assertFalse(meth1 > meth1)
        self.assertTrue(meth2 > meth1)
        self.assertTrue(meth1 >= meth1)

        with self.assertRaisesRegex(
            TypeError,
            "'<' not supported between instances of 'objc.python_selector' and 'int'",
        ):
            meth1 < 42  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'<' not supported between instances of 'int' and 'objc.python_selector'",
        ):
            42 < meth1  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'<=' not supported between instances of 'objc.python_selector' and 'int'",
        ):
            meth1 <= 42  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'<=' not supported between instances of 'int' and 'objc.python_selector'",
        ):
            42 <= meth1  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'>' not supported between instances of 'objc.python_selector' and 'int'",
        ):
            meth1 > 42  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'>' not supported between instances of 'int' and 'objc.python_selector'",
        ):
            42 > meth1  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'>=' not supported between instances of 'objc.python_selector' and 'int'",
        ):
            meth1 >= 42  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'>=' not supported between instances of 'int' and 'objc.python_selector'",
        ):
            42 >= meth1  # noqa: B015

    def test_native_compare(self):
        # XXX: Same tests but with python selectors
        # XXX: Also comparision between native and python selector
        obj = NSObject.alloc().init()
        obj2 = NSObject.alloc().init()

        meth1 = obj.description
        meth2 = obj.respondsToSelector_
        meth3 = obj2.description

        self.assertTrue(meth1 == meth1)
        self.assertFalse(meth1 != meth1)

        self.assertTrue(meth1 != meth2)
        self.assertFalse(meth1 == meth2)

        self.assertTrue(meth1 != meth3)
        self.assertFalse(meth1 == meth3)

        self.assertTrue(meth1 != dir)

        self.assertTrue(meth1 != dir)
        self.assertFalse(meth1 == dir)

        # XXX: Ordering between selector instances
        #      is not very usefull, but the code
        #      has been here for ages.
        #
        #      Consider deprecating
        self.assertFalse(meth1 < meth1)
        self.assertTrue(meth1 < meth2)
        self.assertTrue(meth1 <= meth1)
        self.assertFalse(meth1 > meth1)
        self.assertTrue(meth2 > meth1)
        self.assertTrue(meth1 >= meth1)

        with self.assertRaisesRegex(
            TypeError,
            "'<' not supported between instances of 'objc.native_selector' and 'int'",
        ):
            meth1 < 42  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'<' not supported between instances of 'int' and 'objc.native_selector'",
        ):
            42 < meth1  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'<=' not supported between instances of 'objc.native_selector' and 'int'",
        ):
            meth1 <= 42  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'<=' not supported between instances of 'int' and 'objc.native_selector'",
        ):
            42 <= meth1  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'>' not supported between instances of 'objc.native_selector' and 'int'",
        ):
            meth1 > 42  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'>' not supported between instances of 'int' and 'objc.native_selector'",
        ):
            42 > meth1  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'>=' not supported between instances of 'objc.native_selector' and 'int'",
        ):
            meth1 >= 42  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'>=' not supported between instances of 'int' and 'objc.native_selector'",
        ):
            42 >= meth1  # noqa: B015


class TestSelectorEdgeCases(TestCase):
    # XXX: These should be moved to a different file
    #
    # Note: all these tests have two variant: one for the "simple" caller
    #       and one for the regular caller.

    def test_no_keywords(self):
        with self.assertRaisesRegex(
            TypeError,
            "(does not accept keyword arguments)|(keyword arguments not supported)",
        ):
            NSArray.alloc().init().copyWithZone_(zone=None)

        with self.assertRaisesRegex(
            TypeError,
            "(does not accept keyword arguments)|(keyword arguments not supported)",
        ):
            NSData.dataWithBytes_length_(data=b"hello", length=3)

        with self.assertRaisesRegex(
            TypeError,
            "(does not accept keyword arguments)|(keyword arguments not supported)",
        ):
            NSArray.alloc(cls=NSArray)

    def test_call_on_wrong_self(self):
        obj = NSObject.alloc().init()

        # Resolve methods:
        NSArray.new().description()
        NSData.alloc().initWithBytes_length_(b"hello", 3)

        meth1 = NSArray.__dict__["description"]
        self.assertIs(meth1.self, None)

        meth2 = NSData.__dict__["initWithBytes_length_"]
        self.assertIs(meth2.self, None)

        with self.assertRaisesRegex(
            TypeError, "Expecting instance of NSArray as self, got one of NSObject"
        ):
            meth1(obj)

        with self.assertRaisesRegex(
            TypeError, "Expecting instance of NSData as self, got one of NSObject"
        ):
            meth2(obj)

    def test_didEnd(self):
        # Some magic in selector.__new__ to automaticly set the correct signature
        # for methods like this.
        @objc.selector
        def somethingDidEnd_returnCode_contextInfo_(self, a, b, c):
            pass

        self.assertEqual(somethingDidEnd_returnCode_contextInfo_.signature, b"v@:@i^v")

    def test_selector_from_selector(self):
        @objc.selector
        def someSelector(self):
            pass

        value = objc.selector(someSelector)
        self.assertIs(value.callable, someSelector.callable)

    def test_void_selector_returns_value(self):
        class OC_TestVoidSelectorReturnsValue(NSObject):
            @objc.objc_method(signature=b"v@:")
            def method(self):
                return 42

        self.assertResultHasType(OC_TestVoidSelectorReturnsValue.method, b"v")
        o = OC_TestVoidSelectorReturnsValue()

        with self.assertRaisesRegex(
            ValueError, "method: did not return None, expecting void return value"
        ):
            OC_ObjectInt.invokeSelector_of_(b"method", o)

    def test_selector_from_bound_method(self):
        class Helper:
            def method(self, ocSelf):
                return f"helper {ocSelf}"

        class ClassWithBoundMethodForSelector(NSObject):
            method = objc.selector(Helper().method, selector=b"method")

        self.assertEqual(ClassWithBoundMethodForSelector.method.signature, b"@@:")

        obj = ClassWithBoundMethodForSelector.new()
        self.assertRegex(
            obj.method(), "helper <ClassWithBoundMethodForSelector: 0x[0-9a-f]+>"
        )

    def test_selector_from_callable_object(self):
        class Helper:
            def __call__(self, ocSelf):
                return f"helper {ocSelf}"

        class ClassWithCallableForSelector(NSObject):
            method = objc.selector(Helper(), selector=b"method")

        self.assertEqual(ClassWithCallableForSelector.method.signature, b"@@:")

        obj = ClassWithCallableForSelector.new()
        self.assertRegex(
            obj.method(), "helper <ClassWithCallableForSelector: 0x[0-9a-f]+>"
        )

    def test_selector_from_c_func(self):
        class ClassWithDirAsSelectorFail(NSObject):
            method = objc.selector(dir, selector=b"method")

        self.assertEqual(ClassWithDirAsSelectorFail.method.signature, b"@@:")

        class ClassWithDirAsSelector(NSObject):
            method = objc.selector(dir, selector=b"method", signature=b"@@:")

        self.assertEqual(ClassWithDirAsSelector.method.signature, b"@@:")

        obj = ClassWithDirAsSelector.alloc().init()
        self.assertEqual(obj.method(), dir(obj))


class TestMixin(TestCase):
    def test_basic(self):
        class Mixin:
            pass

        class MixinBase1(NSObject, Mixin):
            pass

        class MixinUser1(MixinBase1):
            def method(self):
                pass

    def test_ignore_selectors_in_mix(self):
        class Mixin:
            def method(self):
                return 42

            method = objc.selector(method, signature=b"d@:")

        class MixinBase2(NSObject, Mixin):
            pass

        class MixinUser2(MixinBase2):
            def method(self):
                return 1

        self.assertResultHasType(MixinUser2.method, b"@")


class TestSuperUsage(TestCase):
    def setUp(self):
        self.unbound = object()
        self.globals = globals()
        self.orig_super = self.globals.get("super", self.unbound)

    def tearDown(self):
        if self.orig_super is not self.unbound:
            self.globals["super"] = self.orig_super
        elif "super" in self.globals:
            del self.globals["super"]

    def test_bound_super(self):
        self.globals["super"] = objc.super

        with warnings.catch_warnings():
            warnings.simplefilter("error", category=objc.ObjCSuperWarning)

            class OC_TestSuperUsage1(NSObject):
                def init(self):
                    self = super().init()
                    return self

    def test_unbound_super(self):
        if "super" in self.globals:
            del self.globals["super"]

        with warnings.catch_warnings():
            with self.assertRaises(objc.ObjCSuperWarning):
                warnings.simplefilter("error", category=objc.ObjCSuperWarning)

                class OC_TestSuperUsage2(NSObject):
                    def init(self):
                        self = super().init()
                        return self

    def test_wrong_super(self):
        self.globals["super"] = builtins.super

        with warnings.catch_warnings():
            with self.assertRaises(objc.ObjCSuperWarning):
                warnings.simplefilter("error", category=objc.ObjCSuperWarning)

                class OC_TestSuperUsage3(NSObject):
                    def init(self):
                        self = super().init()
                        return self


class OC_DunderInitBase(NSObject):
    # Helper for ``TestUsingDunderInit``
    def __new__(cls, *args, **kwds):
        return cls.alloc().init()


class TestUsingDunderInit(TestCase):
    # Some users have an intermediate class
    # which implements ``__new__`` to be able
    # to create Cocoa sublcasses using a similar
    # interface as normal Python subclasses, e.g.
    # with ``__init__`` for initializing the instance.
    #
    # This should continue to work.

    def test_using_dunder_init(self):
        class OC_DunderInitSub1(OC_DunderInitBase):
            def __init__(self, x, y=2):
                self.x = x
                self.y = y

        o = OC_DunderInitSub1(x=1)
        self.assertIsInstance(o, OC_DunderInitSub1)
        self.assertEqual(o.x, 1)
        self.assertEqual(o.y, 2)

        with self.assertRaises(TypeError):
            OC_DunderInitSub1()

        with self.assertRaises(TypeError):
            OC_DunderInitSub1(9, z=4)

    def test_multipe_generations(self):
        class OC_DunderInitSub2(OC_DunderInitBase):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        class OC_DunderInitSub3(OC_DunderInitSub2):
            def __init__(self, x, y, z):
                super().__init__(x, y)
                self.z = z

        o = OC_DunderInitSub3(1, 2, 3)
        self.assertIsInstance(o, OC_DunderInitSub3)
        self.assertEqual(o.x, 1)
        self.assertEqual(o.y, 2)
        self.assertEqual(o.z, 3)


class TestSubclassOptions(TestCase):
    def test_without_attribute_transform(self):
        orig = objc.options._transformAttribute
        try:
            objc.options._transformAttribute = None

            class OC_SubClassOptions1(NSObject):
                def method(self):
                    pass

            self.assertIsInstance(OC_SubClassOptions1.method, objc.selector)

            def method2(self):
                pass

            OC_SubClassOptions1.method2 = method2
            self.assertIsInstance(OC_SubClassOptions1.method2, types.FunctionType)

            def raiser(*args, **kwds):
                raise RuntimeError

            objc.options._transformAttribute = raiser

            def method3(self):
                pass

            with self.assertRaises(RuntimeError):
                OC_SubClassOptions1.method3 = method3

        finally:
            objc.options._transformAttribute = orig

    def test_without_classdict_processor(self):
        orig = objc.options._processClassDict
        try:
            objc.options._processClassDict = None

            with self.assertRaisesRegex(
                objc.error,
                "Cannot create class because 'objc.options._processClassDict' is not set",
            ):

                class OC_SubClassOptions2(NSObject):
                    def method(self):
                        pass

            def raiser(*args, **kwds):
                raise RuntimeError

            objc.options._processClassDict = raiser

            with self.assertRaises(RuntimeError):

                class OC_SubClassOptions3(NSObject):
                    def method(self):
                        pass

        finally:
            objc.options._processClassDict = orig
