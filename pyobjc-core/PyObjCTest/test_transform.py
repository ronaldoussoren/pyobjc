from PyObjCTools.TestSupport import TestCase, SkipTest

import objc
from objc import _transform
import types
import inspect
import functools
import sys

from .test_vector_proxy import OC_Vector
from . import test_protocol  # noqa: F401
from . import test_vectorcall  # noqa: F401
from .protocol import OC_TestProtocol, OC_TestProtocolT1
from .test_protocol import MyProtocol

NSObject = objc.lookUpClass("NSObject")
NSMutableArray = objc.lookUpClass("NSMutableArray")


class TestObjCMethod(TestCase):
    def test_exposed(self):
        self.assertIs(objc.objc_method, _transform.objc_method)

    def test_no_parens(self):
        @_transform.objc_method
        def my_method(self):
            pass

        self.assertIsInstance(my_method, _transform.objc_method)
        self.assertIsInstance(my_method.__wrapped__, types.FunctionType)
        self.assertIs(my_method.selector, None)
        self.assertIs(my_method.signature, None)
        self.assertIs(my_method.isclass, None)

        with self.assertRaisesRegex(TypeError, "is not a callable"):
            _transform.objc_method(42)

    def test_parens_no_args(self):
        @_transform.objc_method()
        def my_method(self):
            pass

        self.assertIsInstance(my_method, _transform.objc_method)
        self.assertIsInstance(my_method.__wrapped__, types.FunctionType)
        self.assertIs(my_method.selector, None)
        self.assertIs(my_method.signature, None)
        self.assertIs(my_method.isclass, None)

        with self.assertRaisesRegex(TypeError, "is not a callable"):
            _transform.objc_method()(42)

        with self.assertRaisesRegex(TypeError, "Expecting exactly 1 argument"):
            _transform.objc_method()(lambda self: None, 42)

        with self.assertRaisesRegex(TypeError, "Unexpected keyword arguments"):
            _transform.objc_method()(lambda self: None, no_arg=42)

    def test_parens_kwds(self):
        @_transform.objc_method(selector=b"foo", signature=b"bar", isclass=False)
        def my_method(self):
            pass

        self.assertIsInstance(my_method, _transform.objc_method)
        self.assertIsInstance(my_method.__wrapped__, types.FunctionType)
        self.assertEqual(my_method.selector, b"foo")
        self.assertEqual(my_method.signature, b"bar")
        self.assertIs(my_method.isclass, False)

        with self.assertRaisesRegex(TypeError, "is not a callable"):
            _transform.objc_method(selector=b"hello")(42)

        with self.assertRaisesRegex(
            TypeError, "got an unexpected keyword argument 'no_arg'"
        ):

            @_transform.objc_method(no_arg=b"hello")
            def my_method(self):
                pass

    def test_wrapped_classmethod(self):
        @_transform.objc_method(selector=b"foo", signature=b"bar", isclass=False)
        @classmethod
        def my_method(self):
            pass

        self.assertIsInstance(my_method, _transform.objc_method)
        self.assertIsInstance(my_method.__wrapped__, classmethod)
        self.assertEqual(my_method.selector, b"foo")
        self.assertEqual(my_method.signature, b"bar")
        self.assertIs(my_method.isclass, False)

    def test_is_callable(self):
        @_transform.objc_method(selector=b"foo", signature=b"bar", isclass=False)
        def my_method(self):
            return 42

        o = my_method(4)
        self.assertEqual(o, 42)


class TestPythonMethod(TestCase):
    def test_exposed(self):
        self.assertIs(objc.python_method, _transform.python_method)

    def test_no_parens(self):
        @_transform.python_method
        def my_method(self):
            pass

        self.assertIsInstance(my_method, _transform.python_method)
        self.assertIsInstance(my_method.__wrapped__, types.FunctionType)
        self.assertNotHasAttr(my_method, "selector")
        self.assertNotHasAttr(my_method, "signature")
        self.assertNotHasAttr(my_method, "isclass")

        with self.assertRaisesRegex(TypeError, "is not a callable"):
            _transform.python_method(42)

    def test_parens_no_args(self):
        @_transform.python_method()
        def my_method(self):
            pass

        self.assertIsInstance(my_method, _transform.python_method)
        self.assertIsInstance(my_method.__wrapped__, types.FunctionType)
        self.assertNotHasAttr(my_method, "selector")
        self.assertNotHasAttr(my_method, "signature")
        self.assertNotHasAttr(my_method, "isclass")

        @_transform.python_method()
        @classmethod
        def my_method(self):
            pass

        self.assertIsInstance(my_method, _transform.python_method)
        self.assertIsInstance(my_method.__wrapped__, classmethod)
        self.assertNotHasAttr(my_method, "selector")
        self.assertNotHasAttr(my_method, "signature")
        self.assertNotHasAttr(my_method, "isclass")

        with self.assertRaisesRegex(TypeError, "is not a callable"):
            _transform.python_method()(42)

        with self.assertRaisesRegex(TypeError, "Expecting exactly 1 argument"):
            _transform.python_method()(lambda self: None, 42)

        with self.assertRaisesRegex(TypeError, "Unexpected keyword arguments"):
            _transform.python_method()(lambda self: None, no_arg=42)

    def test_wrapped_classmethod(self):
        @_transform.python_method
        @classmethod
        def my_method(self):
            pass

        self.assertIsInstance(my_method, _transform.python_method)
        self.assertIsInstance(my_method.__wrapped__, classmethod)

    def test_is_callable(self):
        @_transform.python_method()
        def my_method(self):
            return 42

        o = my_method(4)
        self.assertEqual(o, 42)


class TestTransformer(TestCase):
    transformer = staticmethod(_transform.transformAttribute)

    def assertSignaturesEqual(self, a, b):
        # This assertion ignores numeric junk in signatures, currently
        # only present with the C implementation for transformer.
        self.assertEqual(
            b"".join(objc.splitSignature(a)), b"".join(objc.splitSignature(b))
        )

    def test_dont_transform_values(self):
        for value in ([], (), {}, set(), 0, 54.5, True):
            with self.subTest(value=value):
                out = self.transformer("value", value, NSObject, [])
                self.assertIs(out, value)

    def test_dont_transform_types(self):
        for value in (int, NSObject):
            with self.subTest(value=value):
                out = self.transformer("value", value, NSObject, [])
                self.assertIs(out, value)

    def test_dont_transform_staticmethod(self):
        value = staticmethod(lambda x: None)
        self.assertIsInstance(value, staticmethod)

        out = self.transformer("value", value, NSObject, [])
        self.assertIs(out, value)

    def test_dont_transform_python_method(self):
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("new functionality in the Python version")

        with self.subTest("@python_method(func)"):
            value = _transform.python_method(lambda x: None)
            self.assertIsInstance(value, _transform.python_method)

            out = self.transformer("value", value, NSObject, [])
            self.assertIs(out, value.__wrapped__)

        with self.subTest("@python_method(classmethod())"):
            value = _transform.python_method(classmethod(lambda x: None))
            self.assertIsInstance(value, _transform.python_method)

            out = self.transformer("value", value, NSObject, [])
            self.assertIs(out, value.__wrapped__)

        with self.subTest("@classmethod(python_method())"):
            value = classmethod(_transform.python_method(lambda x: None))

            out = self.transformer("value", value, NSObject, [])
            self.assertIsInstance(out, classmethod)
            self.assertIs(out.__wrapped__, value.__wrapped__.__wrapped__)

    def test_dont_transform_legacy_python_method(self):
        with self.subTest("@python_method(func)"):
            value = objc.python_method(lambda x: None)
            self.assertIsInstance(value, objc.python_method)

            out = self.transformer("value", value, NSObject, [])
            if type(self).__name__ == "TestCTransformer":
                # The C implementation unwraps python_method
                # later in the process.
                self.assertIs(out, value)
            else:
                self.assertIs(out, value.callable)

        with self.subTest("@python_method(classmethod())"):
            value = objc.python_method(classmethod(lambda x: None))
            self.assertIsInstance(value, objc.python_method)

            out = self.transformer("value", value, NSObject, [])

            if type(self).__name__ == "TestCTransformer":
                # The C implementation unwraps python_method
                # later in the process.
                self.assertIs(out, value)
            else:
                self.assertIs(out, value.callable)

        with self.subTest("@classmethod(python_method())"):
            value = classmethod(objc.python_method(lambda x: None))

            out = self.transformer("value", value, NSObject, [])
            self.assertIsInstance(out, classmethod)
            if type(self).__name__ == "TestCTransformer":
                # The C implementation unwraps python_method
                # later in the process.
                self.assertIs(out.__wrapped__, value.__wrapped__)
            else:
                self.assertIs(out.__wrapped__, value.__wrapped__.callable)

    def test_dont_transform_dunder_method(self):
        def __dir__(self):
            return []

        out = self.transformer("__dir__", __dir__, NSObject, [])
        self.assertIs(out, __dir__)

    def test_copy_python_selector(self):
        value = objc.selector(lambda x: None, b"value", b"@@:")
        self.assertIsInstance(value, objc.selector)

        out = self.transformer("value", value, NSObject, [])
        self.assertIsNot(out, value)
        self.assertIs(out.callable, value.callable)
        self.assertEqual(out.selector, value.selector)
        self.assertEqual(out.signature, value.signature)
        self.assertEqual(out.isClassMethod, value.isClassMethod)
        self.assertEqual(out.isRequired, value.isRequired)

        value = objc.selector(None, b"value", b"@@:")
        self.assertIsInstance(value, objc.selector)
        self.assertIs(value.callable, None)

        with self.assertRaisesRegex(ValueError, "selector object without callable"):
            out = self.transformer("value", value, NSObject, [])

    def test_dont_transform_selector(self):

        with self.subTest("native class selector"):
            value = NSObject.description
            self.assertIsInstance(value, objc.selector)

            out = self.transformer("value", value, NSObject, [])
            self.assertIs(out, value)

        o = NSObject.alloc().init()
        with self.subTest("native instance selector"):
            value = o.description
            self.assertIsInstance(value, objc.selector)

            out = self.transformer("value", value, NSObject, [])
            self.assertIs(out, value)

        with self.subTest("native unbound instance selector"):
            value = o.pyobjc_instanceMethods.description
            self.assertIsInstance(value, objc.selector)

            out = self.transformer("value", value, NSObject, [])
            self.assertIs(out, value)

    def test_dont_convert_generators(self):
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("new functionality in the Python version")

        def value(self):
            yield 1

        out = self.transformer("value", value, NSObject, [])
        self.assertIs(out, value)

        value = value(1)
        out = self.transformer("value", value, NSObject, [])
        self.assertIs(out, value)

    def test_dont_convert_async_function(self):
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("new functionality in the Python version")

        async def value(self):
            pass

        out = self.transformer("value", value, NSObject, [])
        self.assertIs(out, value)

        # XXX: Should arange to "await" value(1) to avoid
        # runtime error in tests
        value = value(1)

        def await_value():
            try:
                value.send(None)
            except StopIteration:
                pass

        self.addCleanup(await_value)
        out = self.transformer("value", value, NSObject, [])
        self.assertIs(out, value)

    def test_dont_convert_if_methodname_does_not_match(self):
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("new functionality in the Python version")

        # When the method name does not match the pattern
        # of a selector name don't convert to a selector.

        def method_name(self, a, b):
            pass

        out = self.transformer("method_name", method_name, NSObject, [])
        self.assertIs(out, method_name)

        out = self.transformer("method_name", classmethod(method_name), NSObject, [])
        self.assertIsInstance(out, classmethod)
        self.assertIs(out.__wrapped__, method_name)

        def other__method__name(self, a):
            pass

        out = self.transformer("other__method__name", other__method__name, NSObject, [])
        self.assertIs(out, other__method__name)

        out = self.transformer(
            "other__method__name", classmethod(other__method__name), NSObject, []
        )
        self.assertIsInstance(out, classmethod)
        self.assertIs(out.__wrapped__, other__method__name)

    def check_function_conversion(
        self, *, wrap_classmethod, inner_wrap=lambda x: x, outer_wrap=lambda x: x
    ):
        if wrap_classmethod:
            wrap = classmethod
        else:

            def wrap(x):
                return x

        with self.subTest("function returning value [1]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self):
                return 1

            out = self.transformer("pyvalue", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue")
            self.assertSignaturesEqual(out.signature, b"@@:")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("function returning value [2]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self):
                if sys.version_info[0] == 0:
                    return
                return sys.modules

            out = self.transformer("pyvalue", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue")
            self.assertSignaturesEqual(out.signature, b"@@:")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("function returning value [2]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a):
                return 1

            out = self.transformer("pyvalue:", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue:")
            self.assertSignaturesEqual(out.signature, b"@@:@")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("function returning nothing [1]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self):
                return

            out = self.transformer("pyvalue", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue")
            self.assertSignaturesEqual(out.signature, b"v@:")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("function returning nothing [2]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self):
                pass

            out = self.transformer("pyvalue", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue")
            self.assertSignaturesEqual(out.signature, b"v@:")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("too many positional arguments [1]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a):
                pass

            with self.assertRaisesRegex(
                objc.BadPrototypeError,
                "expects 0 arguments, .* has 1 positional arguments",
            ):
                self.transformer("pyvalue", pyvalue, NSObject, [])

        with self.subTest("too many positional arguments [2]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a, b):
                pass

            with self.assertRaisesRegex(
                objc.BadPrototypeError,
                "expects 1 arguments, .* has 2 positional arguments",
            ):
                self.transformer("pyvalue:", pyvalue, NSObject, [])

        with self.subTest("too many positional arguments [3]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a, b, c=4, d=5):
                pass

            with self.assertRaisesRegex(
                objc.BadPrototypeError,
                "expects 1 arguments, .* has between 2 and 4 positional arguments",
            ):
                self.transformer("pyvalue:", pyvalue, NSObject, [])

        with self.subTest("positional optional arguments [1]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a=1):
                pass

            out = self.transformer("pyvalue", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue")
            self.assertSignaturesEqual(out.signature, b"v@:")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("positional optional arguments [2]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a=1):
                pass

            out = self.transformer("pyvalue:", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue:")
            self.assertSignaturesEqual(out.signature, b"v@:@")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("positional optional arguments [3]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a, b=1):
                pass

            out = self.transformer("pyvalue:", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue:")
            self.assertSignaturesEqual(out.signature, b"v@:@")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("positional optional arguments [4]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a=1, b=1):
                pass

            out = self.transformer("pyvalue:", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue:")
            self.assertSignaturesEqual(out.signature, b"v@:@")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("too few positional arguments [1]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self):
                pass

            with self.assertRaisesRegex(
                objc.BadPrototypeError,
                "expects 1 arguments, .* has 0 positional arguments",
            ):
                self.transformer("pyvalue:", pyvalue, NSObject, [])

        with self.subTest("keyword only"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, *, kw):
                pass

            with self.assertRaisesRegex(
                objc.BadPrototypeError, "keyword-only arguments"
            ):
                self.transformer("pyvalue", pyvalue, NSObject, [])

        with self.subTest("keyword only with default"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, *, kw=1):
                return 1

            out = self.transformer("pyvalue", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue")
            self.assertSignaturesEqual(out.signature, b"@@:")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("check selector source"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self):
                return 1

            out = self.transformer("aSelector", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"aSelector")
            self.assertSignaturesEqual(out.signature, b"@@:")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("method with varargs"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, *args):
                pass

            out = self.transformer("aSelector:", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"aSelector:")
            self.assertSignaturesEqual(out.signature, b"v@:@")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("method with kwargs"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, **kwds):
                pass

            out = self.transformer("aSelector", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"aSelector")
            self.assertSignaturesEqual(out.signature, b"v@:")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

    def test_function_to_selector(self):
        self.check_function_conversion(wrap_classmethod=False)

    def test_classmethod_to_selector(self):
        self.check_function_conversion(wrap_classmethod=True)

    def test_bound_method_to_selector(self):
        class Helper:
            def method(self, a):
                pass

            def method2(self, a):
                return 42

            @classmethod
            def classhelper(self, a):
                pass

        pyvalue = Helper().method
        try:
            inspect.signature(pyvalue)
        except (ValueError, TypeError):
            self.fail("Cannot create inspect.Signature for Helper")

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertSignaturesEqual(out.signature, b"v@:")
        self.assertIs(out.isClassMethod, False)

        with self.assertRaisesRegex(
            objc.BadPrototypeError, "expects 1 arguments, .* has 0 positional arguments"
        ):
            self.transformer("pyvalue:", pyvalue, NSObject, [])

        pyvalue = Helper().method2
        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertSignaturesEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        pyvalue = Helper.classhelper
        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertSignaturesEqual(out.signature, b"v@:")
        self.assertIs(out.isClassMethod, False)

    def test_objc_method_to_selector(self):
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("new functionality in the Python version")

        self.check_function_conversion(
            wrap_classmethod=False, inner_wrap=_transform.objc_method
        )
        self.check_function_conversion(
            wrap_classmethod=True, inner_wrap=_transform.objc_method
        )
        self.check_function_conversion(
            wrap_classmethod=True, outer_wrap=_transform.objc_method
        )

        @_transform.objc_method(isclass=True)
        def pyvalue(self):
            pass

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertSignaturesEqual(out.signature, b"v@:")
        self.assertIs(out.isClassMethod, True)

        @_transform.objc_method(signature=b"f@:")
        def pyvalue(self):
            return 1

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertSignaturesEqual(out.signature, b"f@:")
        self.assertIs(out.isClassMethod, False)

        @_transform.objc_method(selector=b"other")
        def pyvalue(self):
            return 1

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"other")
        self.assertSignaturesEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        @_transform.objc_method(isclass=True)
        @classmethod
        def pyvalue(self):
            return 1

        with self.assertRaisesRegex(
            ValueError,
            "'pyvalue' is objc_method with isclass specified wraps classmethod",
        ):
            self.transformer("pyvalue", pyvalue, NSObject, [])

        @_transform.objc_method(isclass=False)
        @classmethod
        def pyvalue(self):
            return 1

        with self.assertRaisesRegex(
            ValueError,
            "'pyvalue' is objc_method with isclass specified wraps classmethod",
        ):
            self.transformer("pyvalue", pyvalue, NSObject, [])

        @_transform.objc_method(isclass=False)
        @classmethod
        def method_name(self):
            return 1

        with self.assertRaisesRegex(
            ValueError,
            "'method_name' is an objc_method instance, but cannot determine Objective-C selector",
        ):
            self.transformer("method_name", method_name, NSObject, [])

    def test_partial_to_selector(self):
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("new functionality in the Python version")

        def base(a, b):
            pass

        pyvalue = functools.partial(base, 42)

        try:
            inspect.signature(pyvalue)
        except (ValueError, TypeError):
            self.fail("Cannot create inspect.Signature for partial")

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertSignaturesEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        with self.assertRaisesRegex(
            objc.BadPrototypeError, "expects 1 arguments, .* has 0 positional arguments"
        ):
            self.transformer("pyvalue:", pyvalue, NSObject, [])

    def test_callable_with_signature_to_selector(self):
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("new functionality in the Python version")

        class Callable:
            def __call__(self, a):
                pass

        pyvalue = Callable()
        try:
            inspect.signature(pyvalue)
        except (ValueError, TypeError):
            self.fail("Cannot create inspect.Signature for Callable")

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertSignaturesEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        with self.assertRaisesRegex(
            objc.BadPrototypeError, "expects 1 arguments, .* has 0 positional arguments"
        ):
            self.transformer("pyvalue:", pyvalue, NSObject, [])

    def test_callable_without_signature_to_selector(self):
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("new functionality in the Python version")

        class Callable:
            def __call__(self, a):
                pass

            @property
            def __signature__(self):
                raise TypeError("no signature")

        pyvalue = Callable()
        with self.assertRaises((ValueError, TypeError)):
            inspect.signature(pyvalue)

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertSignaturesEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        out = self.transformer("pyvalue:", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue:")
        self.assertSignaturesEqual(out.signature, b"@@:@")
        self.assertIs(out.isClassMethod, False)

    def test_builtin_to_selector(self):
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("new functionality in the Python version")

        pyvalue = dir
        with self.assertRaises((ValueError, TypeError)):
            inspect.signature(pyvalue)

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertSignaturesEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        out = self.transformer("pyvalue:", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue:")
        self.assertSignaturesEqual(out.signature, b"@@:@")
        self.assertIs(out.isClassMethod, False)

    def test_inherit_signature(self):
        def method(self):
            return 1

        with self.subTest("count"):
            out = self.transformer("count", method, NSMutableArray, [])
            self.assertIsInstance(out, objc.selector)
            self.assertSignaturesEqual(out.signature, objc._C_NSUInteger + b"@:")
            self.assertFalse(out.isClassMethod)

        with self.subTest("alloc"):
            out = self.transformer("alloc", method, NSMutableArray, [])
            self.assertIsInstance(out, objc.selector)
            self.assertTrue(out.isClassMethod)
            self.assertSignaturesEqual(out.signature, b"@@:")

    def test_inherit_selector(self):
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("new functionality in the Python version")

        def method(self, a):
            return 1

        method = objc.selector(method, selector=b"other:", signature=b"d@:@")

        class_name = "Fake" + type(self).__name__
        Fake = type(class_name, (NSObject,), {"method": method})

        def method(self, a):
            return 1

        out = self.transformer("method", method, Fake, [])
        self.assertIsInstance(out, objc.selector)
        self.assertSignaturesEqual(out.signature, b"d@:@")
        self.assertEqual(out.selector, b"other:")

    def test_prefer_inherit_instance(self):
        # Check that if a method name can refer to a class
        # and instance method in the parent (e.g. the NSObject
        # protocol methods) the transformer uses the instance
        # method when transforming.
        def description(self):
            return "x"

        out = self.transformer("description", description, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertSignaturesEqual(out.signature, b"@@:")
        self.assertEqual(out.selector, b"description")
        self.assertFalse(out.isClassMethod)

    def test_overridden_full_signature(self):
        # Use OC_Vector... method to check that
        # an override signature gets used.
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("handled differently in the C version")

        def getVectorFloat3(self):
            return 1

        out = self.transformer("getVectorFloat3", getVectorFloat3, OC_Vector, [])
        self.assertIsInstance(out, objc.selector)
        self.assertSignaturesEqual(out.signature, b"<3f>@:")

    def test_overriden_metadata(self):
        # Check that defing a method that has custom
        # metadata though objc.register* but isn't
        # in the parent class gets the updated signature

        # This method has custom metadata in test_vectorcall
        if type(self).__name__ == "TestCTransformer":
            raise SkipTest("handled differently in the C version")

        with self.subTest("full_signature override"):

            def v2d(self):
                pass

            out = self.transformer("v2d", v2d, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertSignaturesEqual(out.signature, b"<2d>@:")

        with self.subTest("return value override in metadata"):
            # Make sure the return value has a different size
            # than 'id' to ensure that this is not determined
            # post-constuction.
            objc.registerMetaDataForSelector(
                b"NSObject",
                b"octransformreturningshort:withFloat:",
                {
                    "retval": {"type": objc._C_SHT},
                    "arguments": {2 + 1: {"type": objc._C_FLT}},
                },
            )

            def octransformreturningshort_(self, a, b):
                return 1

            out = self.transformer(
                "octransformreturningshort:withFloat:",
                octransformreturningshort_,
                NSObject,
                [],
            )
            self.assertIsInstance(out, objc.selector)
            self.assertSignaturesEqual(out.signature, b"s@:@f")

    def test_protocol_method(self):
        with self.subTest("ObjC protocol, instance method match"):

            def method1(self):
                return 4

            out = self.transformer("method1", method1, NSObject, [OC_TestProtocol])
            self.assertIsInstance(out, objc.selector)
            self.assertFalse(out.isClassMethod)
            self.assertSignaturesEqual(out.signature, b"i@:")

        with self.subTest(
            "ObjC protocol, class method where protocl defines instance method"
        ):

            @classmethod
            def method1(self):
                return 4

            out = self.transformer("method1", method1, NSObject, [OC_TestProtocol])
            self.assertIsInstance(out, objc.selector)
            self.assertTrue(out.isClassMethod)
            self.assertSignaturesEqual(out.signature, b"@@:")

        with self.subTest(
            "ObjC protocol, instance method where protocol defines class method"
        ):

            def classMethod1(self):
                return 4

            out = self.transformer(
                "classMethod1", classMethod1, NSObject, [OC_TestProtocolT1]
            )
            self.assertIsInstance(out, objc.selector)
            self.assertFalse(out.isClassMethod)
            self.assertSignaturesEqual(out.signature, b"@@:")

        with self.subTest("ObjC protocol, class method match"):

            @classmethod
            def classMethod1(self):
                return 4

            out = self.transformer(
                "classMethod1", classMethod1, NSObject, [OC_TestProtocolT1]
            )
            self.assertIsInstance(out, objc.selector)
            self.assertTrue(out.isClassMethod)
            self.assertSignaturesEqual(out.signature, b"i@:")

        with self.subTest("Python protocol, instance method match"):

            def protoMethod(self):
                return 4

            out = self.transformer(
                "protoMethod", protoMethod, NSObject, [OC_TestProtocolT1, MyProtocol]
            )
            self.assertIsInstance(out, objc.selector)
            self.assertFalse(out.isClassMethod)
            self.assertSignaturesEqual(out.signature, b"I@:")

        with self.subTest("No protocol match, default signature"):

            def foomethod(self):
                return 4

            out = self.transformer(
                "foomethod", foomethod, NSObject, [OC_TestProtocolT1, MyProtocol]
            )
            self.assertIsInstance(out, objc.selector)
            self.assertFalse(out.isClassMethod)
            self.assertSignaturesEqual(out.signature, b"@@:")

    def test_informal_protocol_method(self):
        # Defined MyProto3 from test_protocols
        def testMethod(self):
            return 1

        with self.subTest("basic case"):
            out = self.transformer("testMethod", testMethod, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertSignaturesEqual(out.signature, b"I@:")

        #
        # Informal protocol should only affect methods that have
        # better information (inherited, classmethod or objc_method)
        #

        if type(self).__name__ != "TestCTransformer":
            with self.subTest("objc_method sets sigature"):
                m = _transform.objc_method(signature=b"d@:")(testMethod)
                out = self.transformer("testMethod", m, NSObject, [])
                self.assertIsInstance(out, objc.selector)
                self.assertSignaturesEqual(out.signature, b"d@:")

            if type(self).__name__ != "TestCTransformer":
                with self.subTest("objc_method sets isclass to True"):
                    m = _transform.objc_method(isclass=True)(testMethod)
                    out = self.transformer("testMethod", m, NSObject, [])
                    self.assertIsInstance(out, objc.selector)
                    self.assertTrue(out.isClassMethod)
                    self.assertSignaturesEqual(out.signature, b"@@:")

        with self.subTest("explicit class method"):
            m = classmethod(testMethod)
            out = self.transformer("testMethod", m, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertTrue(out.isClassMethod)
            self.assertSignaturesEqual(out.signature, b"@@:")

        class_name = "Fake2" + type(self).__name__

        def testMethod(self):
            return 1

        testMethod = objc.selector(testMethod, selector=b"testMethod", signature=b"f@:")
        Fake2 = type(class_name, (NSObject,), {"testMethod": testMethod})

        def testMethod(self):
            return 1

        with self.subTest("inherited method"):
            self.assertIsInstance(testMethod, types.FunctionType)
            out = self.transformer("testMethod", testMethod, Fake2, [])
            self.assertIsInstance(out, objc.selector)
            self.assertFalse(out.isClassMethod)
            self.assertSignaturesEqual(out.signature, b"f@:")


class OC_TestTransformerHelper(NSObject):
    pass


class TestCTransformer(TestTransformer):
    # Subclass from TestTransformer and repace the transformer argument
    # XXX: TestTransformer needs some tweaks to deal with differences
    #      between the ObjC and Python implementation!
    @staticmethod
    def transformer(name, value, class_object, protocols):
        if name.startswith("__"):
            # XXX: This is implemented in class-method.m/objc-class.m, not in PyObjCSelector_FromFunction
            return value

        try:
            result = objc._callableToSelector(name, value, class_object, protocols)
            if isinstance(result, objc.selector):
                # A number of checks performed by the Python implementation are
                # performed at a different point in the C implementation, adjust for
                # that
                #
                # XXX: Still need to check that the two implementations match!
                assert isinstance(result.selector, bytes)
                assert isinstance(result.signature, bytes)
                assert isinstance(result.isClassMethod, bool)
                if result.selector != b"alloc":
                    # XXX: The 'alloc' case in test_inherit_signature causes
                    # a hard crash here, in a way that confuses LLDB
                    setattr(
                        OC_TestTransformerHelper,
                        name,
                        objc.selector(
                            result.callable,
                            selector=result.selector,
                            signature=result.signature,
                            isClassMethod=result.isClassMethod,
                        ),
                    )
                pass

            return result

        except TypeError as exc:
            if str(exc) == "expecting function, method or classmethod":
                return value


class OC_TransformWithoutDict(NSObject):
    __slots__ = ()


class OC_TransformWithDict(NSObject):
    pass


class OC_TransformWithIvar(NSObject):
    __slots__ = ()
    iv = objc.ivar()


class OC_TransformWitIvarA(NSObject):
    __slots__ = ()
    a = objc.ivar()


class OC_TransformWithSlot(NSObject):
    __slots__ = ("iv",)


class TestClassDictProcessor(TestCase):
    # XXX: To be determined if/how this can be verified against
    # the C implementation (e.g. TestCTransformer)
    processor = staticmethod(_transform.processClassDict)

    def assertValidResult(self, rval):
        # Sanity check of the return value of the processor
        self.assertIsInstance(rval, tuple)
        self.assertEqual(len(rval), 4)
        self.assertIsInstance(rval[0], bool)
        self.assertIsInstance(rval[1], tuple)
        self.assertIsInstance(rval[2], tuple)
        self.assertIsInstance(rval[3], tuple)

        for item in rval[1]:
            self.assertIsInstance(item, objc.ivar)

        for item in rval[2]:
            self.assertIsInstance(item, objc.selector)
            self.assertNotIsInstance(item, objc.native_selector)
            self.assertFalse(item.isClassMethod)

        for item in rval[3]:
            self.assertIsInstance(item, objc.selector)
            self.assertNotIsInstance(item, objc.native_selector)
            self.assertTrue(item.isClassMethod)

    def test_empty_dict(self):
        class_dict = {}
        meta_dict = {}
        rval = self.processor(class_dict, meta_dict, NSObject, [])
        self.assertValidResult(rval)
        self.assertEqual(
            rval,
            (
                False,
                (objc.ivar("__dict__", objc._C_PythonObject, isSlot=True),),
                (),
                (),
            ),
        )
        self.assertTrue(class_dict["__objc_python_subclass__"])
        self.assertEqual(meta_dict, {})

    def test_slots(self):
        with self.subTest("no __slots__"):
            class_dict = {}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertEqual(
                rval,
                (
                    False,
                    (objc.ivar("__dict__", objc._C_PythonObject, isSlot=True),),
                    (),
                    (),
                ),
            )
            self.assertEqual(class_dict["__slots__"], ())
            self.assertEqual(meta_dict, {})

        with self.subTest("empty __slots__"):
            class_dict = {"__slots__": ()}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertEqual(rval, (False, (), (), ()))
            self.assertEqual(class_dict["__slots__"], ())
            self.assertEqual(meta_dict, {})

        with self.subTest("some __slots__ in a tuple"):
            class_dict = {"__slots__": ("a", "b")}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertEqual(
                rval,
                (
                    False,
                    tuple(
                        objc.ivar(nm, objc._C_PythonObject, isSlot=True)
                        for nm in ("a", "b")
                    ),
                    (),
                    (),
                ),
            )
            self.assertEqual(class_dict["__slots__"], ())
            self.assertEqual(meta_dict, {})

        with self.subTest("some __slots__ in a list"):
            class_dict = {"__slots__": ["a", "b"]}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertEqual(
                rval,
                (
                    False,
                    tuple(
                        objc.ivar(nm, objc._C_PythonObject, isSlot=True)
                        for nm in ("a", "b")
                    ),
                    (),
                    (),
                ),
            )
            self.assertEqual(class_dict["__slots__"], ())
            self.assertEqual(meta_dict, {})

        with self.subTest("one __slots__ as astring"):
            class_dict = {"__slots__": "ab"}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertEqual(
                rval,
                (False, (objc.ivar("ab", objc._C_PythonObject, isSlot=True),), (), ()),
            )
            self.assertEqual(class_dict["__slots__"], ())
            self.assertEqual(meta_dict, {})

        with self.subTest("some __slots__ in a dict"):
            class_dict = {"__slots__": {"a": "doc a", "b": "doc b"}}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertEqual(
                rval,
                (
                    False,
                    tuple(
                        objc.ivar(nm, objc._C_PythonObject, isSlot=True)
                        for nm in ("a", "b")
                    ),
                    (),
                    (),
                ),
            )
            self.assertEqual(class_dict["__slots__"], ())
            self.assertEqual(meta_dict, {})

        with self.subTest("invalid __slots__ as int"):
            class_dict = {"__slots__": 42}
            meta_dict = {}
            with self.assertRaisesRegex(TypeError, "not iterable"):
                self.processor(class_dict, meta_dict, NSObject, [])

            self.assertEqual(class_dict["__slots__"], 42)
            self.assertEqual(meta_dict, {})

        with self.subTest("invalid __slots__ as tuple of string and int"):
            class_dict = {"__slots__": ("a", 42)}
            meta_dict = {}
            with self.assertRaisesRegex(TypeError, r"must be str, not int"):
                self.processor(class_dict, meta_dict, NSObject, [])

            self.assertIn("a", class_dict)
            self.assertEqual(class_dict["__slots__"], ("a", 42))
            self.assertEqual(meta_dict, {})

        with self.subTest("inherit from __dict__, without slots"):
            class_dict = {}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, OC_TransformWithDict, [])
            self.assertValidResult(rval)
            self.assertEqual(rval, (False, (), (), ()))
            self.assertEqual(class_dict["__slots__"], ())
            self.assertEqual(meta_dict, {})

        with self.subTest("inherit from __dict__, with slots"):
            class_dict = {"__slots__": ["a", "b"]}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, OC_TransformWithDict, [])
            self.assertValidResult(rval)
            self.assertEqual(
                rval,
                (
                    False,
                    tuple(
                        objc.ivar(nm, objc._C_PythonObject, isSlot=True)
                        for nm in ("a", "b")
                    ),
                    (),
                    (),
                ),
            )
            self.assertEqual(class_dict["__slots__"], ())
            self.assertEqual(meta_dict, {})

        with self.subTest("inherit from dict-less, without slots"):
            class_dict = {}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, OC_TransformWithoutDict, [])
            self.assertValidResult(rval)
            self.assertEqual(
                rval,
                (
                    False,
                    (objc.ivar("__dict__", objc._C_PythonObject, isSlot=True),),
                    (),
                    (),
                ),
            )
            self.assertEqual(class_dict["__slots__"], ())
            self.assertEqual(meta_dict, {})

        with self.subTest("inherit from dict-less, with slots"):
            class_dict = {"__slots__": ["a", "b"]}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, OC_TransformWithoutDict, [])
            self.assertValidResult(rval)
            self.assertEqual(
                rval,
                (
                    False,
                    tuple(
                        objc.ivar(nm, objc._C_PythonObject, isSlot=True)
                        for nm in ("a", "b")
                    ),
                    (),
                    (),
                ),
            )
            self.assertEqual(class_dict["__slots__"], ())
            self.assertEqual(meta_dict, {})

        if type(self).__name__ != "TestCClassDictProcessor":
            with self.subTest("slot overrides parent class"):

                class_dict = {"__slots__": ("a",)}
                meta_dict = {}
                with self.assertRaisesRegex(
                    objc.error,
                    "objc.ivar 'a' overrides instance variable in super class",
                ):
                    self.processor(class_dict, meta_dict, OC_TransformWitIvarA, [])
                self.assertEqual(meta_dict, {})

    def test_ivars(self):
        with self.subTest("unnamed ivar"):
            ivar = objc.ivar(type=objc._C_FLT)
            class_dict = {"var": ivar, "__slots__": ()}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertEqual(rval, (False, (ivar,), (), ()))
            self.assertEqual(ivar.__name__, "var")
            self.assertIs(ivar, class_dict["var"])
            self.assertIs(ivar, rval[1][0])
            self.assertEqual(meta_dict, {})

        with self.subTest("named ivar, name matches"):
            ivar = objc.ivar(name="var", type=objc._C_FLT)
            class_dict = {"var": ivar, "__slots__": ()}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertEqual(rval, (False, (ivar,), (), ()))
            self.assertEqual(ivar.__name__, "var")
            self.assertIs(ivar, class_dict["var"])
            self.assertIs(ivar, rval[1][0])
            self.assertEqual(meta_dict, {})

        with self.subTest("named ivar, name does not match"):
            ivar = objc.ivar(name="varname", type=objc._C_FLT)
            class_dict = {"var": ivar, "__slots__": ()}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertEqual(rval, (False, (ivar,), (), ()))
            self.assertEqual(ivar.__name__, "varname")
            self.assertIs(ivar, class_dict["var"])
            self.assertIs(ivar, rval[1][0])
            self.assertEqual(meta_dict, {})

        if type(self).__name__ == "TestCClassDictProcessor":
            return

        with self.subTest("two ivars with same C name"):
            ivar_a = objc.ivar()
            ivar_b = objc.ivar(name="a")
            class_dict = {"a": ivar_a, "b": ivar_b}
            meta_dict = {}
            with self.assertRaisesRegex(objc.error, "'b' reimplements objc.ivar 'a'"):
                self.processor(class_dict, meta_dict, NSObject, [])
            self.assertEqual(meta_dict, {})

        with self.subTest("ivar mismatch with slot"):
            ivar_a = objc.ivar()
            class_dict = {"a": ivar_a, "__slots__": ("a",)}
            meta_dict = {}
            with self.assertRaisesRegex(objc.error, "'a' redefines <"):
                self.processor(class_dict, meta_dict, NSObject, [])
            self.assertEqual(meta_dict, {})

        with self.subTest("ivar overrides parent class"):

            ivar = objc.ivar()
            class_dict = {"iv": ivar, "__slots__": ()}
            meta_dict = {}
            with self.assertRaisesRegex(
                objc.error, "objc.ivar 'iv' overrides instance variable in super class"
            ):
                self.processor(class_dict, meta_dict, OC_TransformWithIvar, [])
            self.assertEqual(meta_dict, {})

        with self.subTest("ivar overrides parent class"):
            ivar = objc.ivar()
            class_dict = {"iv": ivar, "__slots__": ()}
            meta_dict = {}
            with self.assertRaisesRegex(
                objc.error, "objc.ivar 'iv' overrides instance variable in super class"
            ):
                self.processor(class_dict, meta_dict, OC_TransformWithSlot, [])
            self.assertEqual(meta_dict, {})

    def check_selectors(self, *, wrap_classmethod):
        if wrap_classmethod:
            wrap = classmethod
        else:

            def wrap(func):
                return func

        with self.subTest("basic method"):

            @wrap
            def method_(self, arg):
                pass

            class_dict = {"method_": method_, "__slots__": ()}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertFalse(rval[0])
            self.assertEqual(rval[1], ())
            if wrap_classmethod:
                self.assertEqual(rval[2], ())
                check = rval[3]
                self.assertIn("method_", meta_dict)
                self.assertNotIn("method_", class_dict)

            else:
                self.assertEqual(rval[3], ())
                check = rval[2]
                self.assertNotIn("method_", meta_dict)
                self.assertIn("method_", class_dict)

            self.assertEqual(len(check), 1)
            self.assertEqual(check[0].selector, b"method:")
            self.assertEqual(check[0].isClassMethod, wrap_classmethod)

        with self.subTest("hidden method"):

            def method_(self, value):
                pass

            method_ = objc.selector(
                method_,
                selector=b"method:",
                isHidden=True,
                isClassMethod=wrap_classmethod,
            )

            class_dict = {"method_": method_, "__slots__": ()}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertFalse(rval[0])
            self.assertEqual(rval[1], ())

            if wrap_classmethod:
                self.assertEqual(rval[2], ())
                check = rval[3]

            else:
                self.assertEqual(rval[3], ())
                check = rval[2]

            self.assertNotIn("method_", meta_dict)
            self.assertNotIn("method_", class_dict)

            self.assertEqual(len(check), 1)
            self.assertEqual(check[0].selector, method_.selector)
            self.assertEqual(check[0].signature, method_.signature)
            self.assertEqual(check[0].callable, method_.callable)

        with self.subTest("method name doesn't match selector"):

            # @objc.objc_method(selector=b"sendValue:", isclass=wrap_classmethod)
            def method(self, a):
                pass

            method = objc.selector(
                method, selector=b"sendValue:", isClassMethod=wrap_classmethod
            )

            class_dict = {"method": method, "__slots__": ()}
            meta_dict = {}
            rval = self.processor(class_dict, meta_dict, NSObject, [])
            self.assertValidResult(rval)
            self.assertFalse(rval[0])
            self.assertEqual(rval[1], ())

            if wrap_classmethod:
                self.assertEqual(rval[2], ())
                check = rval[3]
                check_dict = meta_dict

            else:
                self.assertEqual(rval[3], ())
                check = rval[2]
                check_dict = class_dict

            self.assertEqual(len(check), 1)
            self.assertEqual(check[0].selector, b"sendValue:")

            self.assertIn("method", check_dict)
            self.assertIn("sendValue_", check_dict)
            self.assertIs(check_dict["method"], check_dict["sendValue_"])

        # XXX: Test there key in dict does not match selector

    def test_instance_methods(self):
        self.check_selectors(wrap_classmethod=False)

    def test_class_methods(self):
        self.check_selectors(wrap_classmethod=False)

    def test_methods_needing_intermediate(self):
        # XXX: Might need to keep this logic in C for two reasons:
        #  1. DRY w.r.t. method names
        #  2. This directly affects correctness of the bridge itself.

        for selector in (b"dealloc",):
            with self.subTest(selector=selector):

                @objc.objc_method(selector=selector)
                def method(self):
                    pass

                class_dict = {selector.decode(): method}
                meta_dict = {}
                rval = self.processor(class_dict, meta_dict, NSObject, [])
                self.assertValidResult(rval)
                self.assertTrue(rval[0])

            with self.subTest(selector=selector, second_gen=True):

                @objc.objc_method(selector=selector)
                def method(self):
                    pass

                class_dict = {selector.decode(): method}
                meta_dict = {}
                rval = self.processor(
                    class_dict, meta_dict, OC_TransformWithoutDict, []
                )
                self.assertValidResult(rval)
                self.assertFalse(rval[0])

        for selector in (
            b"storedValueForKey:",
            b"valueForKey:",
            b"forwardInvocation:",
            b"methodSignatureForSelector:",
            b"respondsToSelector:",
            b"copyWithZone:",
            b"mutableCopyWithZone:",
        ):
            with self.subTest(selector=selector):

                @objc.objc_method(selector=selector)
                def method(self, arg):
                    pass

                class_dict = {selector.decode().replace(":", "_"): method}
                meta_dict = {}
                rval = self.processor(class_dict, meta_dict, NSObject, [])
                self.assertValidResult(rval)
                self.assertTrue(rval[0])

        for selector in (
            b"takeStoredValue:forKey:",
            b"takeValue:forKey:",
            b"setValue:forKey:",
        ):
            with self.subTest(selector=selector, match_name=True):

                @objc.objc_method(selector=selector)
                def method(self, arg1, arg2):
                    pass

                class_dict = {selector.decode().replace(":", "_"): method}
                meta_dict = {}
                rval = self.processor(class_dict, meta_dict, NSObject, [])
                self.assertValidResult(rval)
                self.assertTrue(rval[0])

            if type(self).__name__ != "TestCClassDictProcessor":
                with self.subTest(selector=selector, match_name=False):

                    @objc.objc_method(selector=selector)
                    def method(self, arg1, arg2):
                        pass

                    class_dict = {"method": method}
                    meta_dict = {}
                    rval = self.processor(class_dict, meta_dict, NSObject, [])
                    self.assertValidResult(rval)
                    self.assertTrue(rval[0])

    def test_python_methods(self):
        if type(self).__name__ == "TestCClassDictProcessor":
            raise SkipTest("Known difference between C and Python implementation")

        def method(self):
            pass

        class_dict = {"method": objc.python_method(method), "__slots__": ()}
        meta_dict = {}
        rval = self.processor(class_dict, meta_dict, NSObject, [])
        self.assertValidResult(rval)
        self.assertEqual(rval, (False, (), (), ()))
        self.assertIs(class_dict["method"], method)
        self.assertEqual(meta_dict, {})

    def test_mocked_transformer(self):
        # Check that the transformer is called as expected for all attributes,
        # mostly to avoid complicating the method tests.
        if type(self).__name__ == "TestCClassDictProcessor":
            raise SkipTest("Not relevant for C implementation")

        self.fail()

    def test_class_setup_changes_dict(self):
        class SideEffectingSetup:
            def __pyobjc_class_setup__(
                self, name, class_dict, instance_methods, class_methods
            ):
                class_dict[name + "getter"] = lambda self: 42

        class_dict = {"attr": SideEffectingSetup()}
        meta_dict = {}
        rval = self.processor(class_dict, meta_dict, NSObject, [])
        self.assertValidResult(rval)
        self.assertIn("attrgetter", class_dict)
        self.assertIsInstance(class_dict["attrgetter"], objc.selector)
        self.assertEqual(len(rval[2]), 1)
        self.assertIs(rval[2][0], class_dict["attrgetter"])

    # - Check class_dict is updated when values are transformed
    #   (Done implicitly in selector tests)
    #
    # - "hidden" selectors (possibly needs new API), in particular inheriting them
    # - Protocol validation
    # - test using objc.object_property because that has a non-trivial class_setup method


class TestCClassDictProcessor(TestClassDictProcessor):
    @staticmethod
    def processor(class_dict, meta_dict, class_object, protocols):
        (
            needs_intermediate,
            instance_variables,
            instance_methods,
            class_methods,
        ) = objc._transformClassDict(class_dict, meta_dict, class_object, protocols)

        instance_variables = tuple(sorted(instance_variables, key=lambda x: x.__name__))
        instance_methods = tuple(sorted(instance_methods, key=lambda x: x.selector))
        class_methods = tuple(sorted(class_methods, key=lambda x: x.selector))

        return (needs_intermediate, instance_variables, instance_methods, class_methods)
