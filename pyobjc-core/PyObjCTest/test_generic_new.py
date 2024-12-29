import objc
from PyObjCTools.TestSupport import TestCase
from objc import super  # noqa: A004
import objc._new as new_mod
from .genericnew import (
    OC_GenericNew,
    OC_GenericNewChild,
    OC_GenericNewChild2,
    OC_GenericNewChild3,
)
import textwrap

NSObject = objc.lookUpClass("NSObject")

objc.registerNewKeywordsFromSelector("OC_GenericNew", b"initWithValue:")
objc.registerNewKeywordsFromSelector("OC_GenericNew", b"initWithURL:")
objc.registerNewKeywordsFromSelector("OC_GenericNew", b"initWithFirst:second:")
objc.registerNewKeywordsFromSelector("OC_GenericNewChild", b"initWithX:y:")
objc.registerNewKeywordsFromSelector("OC_GenericNewChild2", b"initWithX:y:z:")
objc.registerUnavailableMethod("OC_GenericNewChild2", b"initWithX:y:")
objc.registerUnavailableMethod("OC_GenericNewChild2", b"init")
objc.registerNewKeywords("OC_GenericNewChild3", ("a", "b"), "valueWithA_b_")


class TestDefaultNewForPythonClass(TestCase):
    def test_nsobject(self):
        v = NSObject()
        self.assertIsInstance(v, NSObject)

        self.assertEqual(new_mod.NEW_MAP["NSObject"], {(): "init"})

        with self.assertRaisesRegex(
            TypeError, r"NSObject\(\) does not support keyword arguments 'y', 'x'"
        ):
            NSObject(y=3, x=4)

        doc = NSObject.__new__.__doc__
        self.assertIsInstance(doc, str)
        self.assertEqual(
            doc,
            textwrap.dedent(
                """\
            NSObject():
               returns cls.alloc().init()

            The order of keyword arguments is significant
        """
            ),
        )

        self.assertIsInstance(NSObject.__new__, new_mod.function_wrapper)
        NSObject.__new__.foo = 42
        self.assertEqual(NSObject.__new__._function.foo, 42)
        del NSObject.__new__._function.foo

    def test_basic(self):
        class OCPyNew1(NSObject):
            def initWithX_y_(self, x_val, y_val):
                self = super().init()
                self.x = x_val
                self.y = y_val
                return self

            def initPoint_(self, p):
                self = super().init()
                self.x, self.y = p
                return self

            def initializeZ_(self, z):
                self.z = 0

            # Not a method, should be used
            initA_b_ = 42

        v = OCPyNew1(x=1, y=2)
        self.assertIsInstance(v, OCPyNew1)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)

        v = OCPyNew1(point=(3, 4))
        self.assertIsInstance(v, OCPyNew1)
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 4)

        v = OCPyNew1()
        self.assertIsInstance(v, OCPyNew1)

        with self.assertRaisesRegex(
            TypeError, "does not support keyword arguments 'a', 'b'"
        ):
            OCPyNew1(a=1, b=2)

        with self.assertRaisesRegex(
            TypeError, r"OCPyNew1\(\) does not support keyword arguments 'y', 'x'"
        ):
            OCPyNew1(y=3, x=4)

        with self.assertRaisesRegex(
            TypeError, r"OCPyNew1\(\) does not support keyword arguments 'z'"
        ):
            OCPyNew1(z=4)

        with self.assertRaisesRegex(TypeError, "does not accept positional arguments"):
            OCPyNew1(1, 2)

        doc = OCPyNew1.__new__.__doc__
        self.assertIsInstance(doc, str)
        self.assertEqual(
            doc,
            textwrap.dedent(
                """\
                OCPyNew1():
                   returns cls.alloc().init()

                OCPyNew1(*, point):
                   returns cls.alloc().initPoint_(point)

                OCPyNew1(*, x, y):
                   returns cls.alloc().initWithX_y_(x, y)

                The order of keyword arguments is significant
            """
            ),
        )

    def test_no_new_in_options(self):
        orig = objc.options._setDunderNew
        try:

            def raiser(*args, **kwds):
                raise RuntimeError

            objc.options._setDunderNew = raiser

            with self.assertRaises(RuntimeError):

                class OCPyNew6a(NSObject):
                    pass

            objc.options._setDunderNew = None

            class OCPyNew6b(NSObject):
                pass

            self.assertIs(
                OCPyNew6b.__new__,
                objc.lookUpClass("_PyObjCIntermediate_NSObject").__new__,
            )

        finally:
            objc.options._setDunderNew = orig

    def test_explicit_new(self):
        # Test that an explicit __new__ overrides the default
        # implementation.
        class OCPyNew2(NSObject):
            def __new__(self, *, z):
                return self.alloc().initWithValue_(z)

            def initWithValue_(self, value):
                self = super().init()
                self.value = value
                return self

        v = OCPyNew2(z=4)
        self.assertEqual(v.value, 4)

        with self.assertRaisesRegex(TypeError, "got an unexpected keyword argument"):
            OCPyNew2(value=9)

    def test_dunder_init(self):
        class OCPyNew3(NSObject):
            def initWithValue_(self, v):
                self = super().init()
                self.value = v
                return self

            def __init__(self, **kwds):
                # __init__ is never called automaticly for
                # Cocoa classes.
                self.value += 1

        v = OCPyNew3.alloc().initWithValue_(3)
        self.assertEqual(v.value, 3)

        v = OCPyNew3(value=4)
        self.assertEqual(v.value, 4)

    def test_dunder_init_with_error(self):
        class OCPyNew4(NSObject):
            def initWithValue_error_(self, v, error):
                self = super().init()
                self.value = v
                return self, None

            def __init__(self, **kwds):
                # __init__ is never called automaticly for
                # Cocoa classes.
                self.value += 1

        v, e = OCPyNew4.alloc().initWithValue_error_(3, None)
        self.assertEqual(v.value, 3)
        self.assertIs(e, None)

        v, e = OCPyNew4(value=4, error=None)
        self.assertEqual(v.value, 4)
        self.assertIs(e, None)

    def test_init_is_none(self):
        class OCPyNew5(NSObject):
            init = None

            def initWithValue_(self, new_value):
                self = super().init()
                self.value = new_value
                return self

        with self.assertRaisesRegex(
            TypeError, r"OCPyNew5\(\) requires keyword arguments"
        ):
            OCPyNew5()

        v = OCPyNew5(value=3)
        self.assertIsInstance(v, OCPyNew5)
        self.assertEqual(v.value, 3)


class TestDefaultNewForObjectiveCClass(TestCase):
    # 1. Class with init methods
    # 2. Subclass with more init methods
    # 3. Sublcass with unavailable init methods
    def test_base(self):
        v = OC_GenericNew()
        self.assertEqual(v.value(), None)

        v = OC_GenericNew(value=42)
        self.assertEqual(v.value(), 42)

        v = OC_GenericNew(URL=99)
        self.assertEqual(v.value(), 99)

        v = OC_GenericNew(first=1, second=2)
        self.assertEqual(v.value(), ["first-second", 1, 2])

        with self.assertRaisesRegex(
            TypeError, r"OC_GenericNew\(\) does not support keyword arguments 'x', 'y'"
        ):
            OC_GenericNew(x=1, y=2)

    def test_extended_base(self):
        v = OC_GenericNewChild()
        self.assertEqual(v.value(), None)

        v = OC_GenericNewChild(value=42)
        self.assertEqual(v.value(), 42)

        v = OC_GenericNewChild(first=1, second=2)
        self.assertEqual(v.value(), ["first-second", 1, 2])

        v = OC_GenericNewChild(x=1, y=2)
        self.assertEqual(v.value(), ["x-y", 1, 2])

    def test_removed_init(self):

        with self.assertRaisesRegex(
            TypeError, r"OC_GenericNewChild2\(\) requires keyword arguments"
        ):
            v = OC_GenericNewChild2()

        v = OC_GenericNewChild2(value=42)
        self.assertEqual(v.value(), 42)

        v = OC_GenericNewChild2(first=1, second=2)
        self.assertEqual(v.value(), ["first-second", 1, 2])

        with self.assertRaisesRegex(
            TypeError,
            r"OC_GenericNewChild2\(\) does not support keyword arguments 'x', 'y'",
        ):
            OC_GenericNewChild2(x=1, y=2)

        v = OC_GenericNewChild2(x=1, y=2, z=3)
        self.assertEqual(v.value(), ["x-y-z", 1, 2, 3])

        self.assertEqual(
            OC_GenericNewChild2.__new__.__doc__,
            textwrap.dedent(
                """\
            OC_GenericNewChild2(*, URL):
               returns cls.alloc().initWithURL_(URL)

            OC_GenericNewChild2(*, first, second):
               returns cls.alloc().initWithFirst_second_(first, second)

            OC_GenericNewChild2(*, value):
               returns cls.alloc().initWithValue_(value)

            OC_GenericNewChild2(*, x, y, z):
               returns cls.alloc().initWithX_y_z_(x, y, z)

            The order of keyword arguments is significant
        """
            ),
        )

    def test_class_factory(self):
        v = OC_GenericNewChild3(a=9, b=10)
        self.assertEqual(v.value(), ["A-B", 9, 10])

        self.assertEqual(
            OC_GenericNewChild3.__new__.__doc__,
            textwrap.dedent(
                """\
            OC_GenericNewChild3():
               returns cls.alloc().init()

            OC_GenericNewChild3(*, URL):
               returns cls.alloc().initWithURL_(URL)

            OC_GenericNewChild3(*, a, b):
               returns cls.valueWithA_b_(a, b)

            OC_GenericNewChild3(*, first, second):
               returns cls.alloc().initWithFirst_second_(first, second)

            OC_GenericNewChild3(*, value):
               returns cls.alloc().initWithValue_(value)

            The order of keyword arguments is significant
            """
            ),
        )
