from PyObjCTools.TestSupport import TestCase

import objc
from objc import _transform
import types
import inspect
import functools
import sys

from .test_vector_proxy import OC_Vector
from . import test_protocol  # noqa: F401
from . import test_vectorcall  # noqa: F401

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
    transformer = staticmethod(_transform.transformCallable)

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
            self.assertIs(out, value.callable)

        with self.subTest("@python_method(classmethod())"):
            value = objc.python_method(classmethod(lambda x: None))
            self.assertIsInstance(value, objc.python_method)

            out = self.transformer("value", value, NSObject, [])
            self.assertIs(out, value.callable)

        with self.subTest("@classmethod(python_method())"):
            value = classmethod(objc.python_method(lambda x: None))

            out = self.transformer("value", value, NSObject, [])
            self.assertIsInstance(out, classmethod)
            self.assertIs(out.__wrapped__, value.__wrapped__.callable)

    def test_dont_transform_dunder_method(self):
        def __dir__(self):
            return []

        out = self.transformer("__dir__", __dir__, NSObject, [])
        self.assertIs(out, __dir__)

    def test_dont_transform_selector(self):
        with self.subTest("python selector"):
            value = objc.selector(lambda x: None, b"value", b"@@:")
            self.assertIsInstance(value, objc.selector)

            out = self.transformer("value", value, NSObject, [])
            self.assertIs(out, value)

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
        def value(self):
            yield 1

        out = self.transformer("value", value, NSObject, [])
        self.assertIs(out, value)

        value = value(1)
        out = self.transformer("value", value, NSObject, [])
        self.assertIs(out, value)

    def test_dont_convert_async_function(self):
        async def value(self):
            pass

        out = self.transformer("value", value, NSObject, [])
        self.assertIs(out, value)

        # XXX: Should arange to "await" value(1) to avoid
        # runtime error in tests
        value = value(1)
        out = self.transformer("value", value, NSObject, [])
        self.assertIs(out, value)

    def test_dont_convert_if_methodname_does_not_match(self):
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
            self.assertEqual(out.signature, b"@@:")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("function returning value [2]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self):
                if sys.version_info[0] == 0:
                    return
                return 1

            out = self.transformer("pyvalue", pyvalue, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.selector, b"pyvalue")
            self.assertEqual(out.signature, b"@@:")
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
            self.assertEqual(out.signature, b"@@:@")
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
            self.assertEqual(out.signature, b"v@:")
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
            self.assertEqual(out.signature, b"v@:")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("too many positional arguments [1]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a):
                pass

            with self.assertRaisesRegex(
                ValueError,
                "'pyvalue' expects 0 arguments, .* has 1 positional arguments",
            ):
                self.transformer("pyvalue", pyvalue, NSObject, [])

        with self.subTest("too many positional arguments [2]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a, b):
                pass

            with self.assertRaisesRegex(
                ValueError,
                "'pyvalue:' expects 1 arguments, .* has 2 positional arguments",
            ):
                self.transformer("pyvalue:", pyvalue, NSObject, [])

        with self.subTest("too many positional arguments [3]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, a, b, c=4, d=5):
                pass

            with self.assertRaisesRegex(
                ValueError,
                "'pyvalue:' expects 1 arguments, .* has between 2 and 4 positional arguments",
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
            self.assertEqual(out.signature, b"v@:")
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
            self.assertEqual(out.signature, b"v@:@")
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
            self.assertEqual(out.signature, b"v@:@")
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
            self.assertEqual(out.signature, b"v@:@")
            self.assertEqual(out.isClassMethod, wrap_classmethod)

        with self.subTest("too few positional arguments [1]"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self):
                pass

            with self.assertRaisesRegex(
                ValueError,
                "'pyvalue:' expects 1 arguments, .* has 0 positional arguments",
            ):
                self.transformer("pyvalue:", pyvalue, NSObject, [])

        with self.subTest("keyword only"):

            @outer_wrap
            @wrap
            @inner_wrap
            def pyvalue(self, *, kw):
                pass

            with self.assertRaisesRegex(
                ValueError, "has 1 keyword-only arguments without a default"
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
            self.assertEqual(out.signature, b"@@:")
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
            self.assertEqual(out.signature, b"@@:")
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
            self.assertEqual(out.signature, b"v@:@")
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
            self.assertEqual(out.signature, b"v@:")
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
        self.assertEqual(out.signature, b"v@:")
        self.assertIs(out.isClassMethod, False)

        with self.assertRaisesRegex(
            ValueError, "'pyvalue:' expects 1 arguments, .* has 0 positional arguments"
        ):
            self.transformer("pyvalue:", pyvalue, NSObject, [])

        pyvalue = Helper().method2
        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        pyvalue = Helper.classhelper
        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertEqual(out.signature, b"v@:")
        self.assertIs(out.isClassMethod, False)

    def test_objc_method_to_selector(self):
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
        self.assertEqual(out.signature, b"v@:")
        self.assertIs(out.isClassMethod, True)

        @_transform.objc_method(signature=b"f@:")
        def pyvalue(self):
            return 1

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertEqual(out.signature, b"f@:")
        self.assertIs(out.isClassMethod, False)

        @_transform.objc_method(selector=b"other")
        def pyvalue(self):
            return 1

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"other")
        self.assertEqual(out.signature, b"@@:")
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
        self.assertEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        with self.assertRaisesRegex(
            ValueError, "'pyvalue:' expects 1 arguments, .* has 0 positional arguments"
        ):
            self.transformer("pyvalue:", pyvalue, NSObject, [])

    def test_callable_with_signature_to_selector(self):
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
        self.assertEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        with self.assertRaisesRegex(
            ValueError, "'pyvalue:' expects 1 arguments, .* has 0 positional arguments"
        ):
            self.transformer("pyvalue:", pyvalue, NSObject, [])

    def test_callable_without_signature_to_selector(self):
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
        self.assertEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        out = self.transformer("pyvalue:", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue:")
        self.assertEqual(out.signature, b"@@:@")
        self.assertIs(out.isClassMethod, False)

    def test_builtin_to_selector(self):
        pyvalue = dir
        with self.assertRaises((ValueError, TypeError)):
            inspect.signature(pyvalue)

        out = self.transformer("pyvalue", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue")
        self.assertEqual(out.signature, b"@@:")
        self.assertIs(out.isClassMethod, False)

        out = self.transformer("pyvalue:", pyvalue, NSObject, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.selector, b"pyvalue:")
        self.assertEqual(out.signature, b"@@:@")
        self.assertIs(out.isClassMethod, False)

    def test_inherit_signature(self):
        def method(self):
            return 1

        out = self.transformer("count", method, NSMutableArray, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.signature, objc._C_NSUInteger + b"@:")

        out = self.transformer("alloc", method, NSMutableArray, [])
        self.assertIsInstance(out, objc.selector)
        self.assertTrue(out.isClassMethod)
        self.assertEqual(out.signature, b"@@:")

    def test_inherit_selector(self):
        class Fake:
            def method(self, a):
                return 1

            method = objc.selector(method, selector=b"other:", signature=b"d@:@")

        def method(self, a):
            return 1

        out = self.transformer("method", method, Fake, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.signature, b"d@:@")
        self.assertEqual(out.selector, b"other:")

    def test_overridden_full_signature(self):
        # Use OC_Vector... method to check that
        # an override signature gets used.
        def getVectorFloat3(self):
            return 1

        out = self.transformer("getVectorFloat3", getVectorFloat3, OC_Vector, [])
        self.assertIsInstance(out, objc.selector)
        self.assertEqual(out.signature, b"<3f>@:")

    def test_overriden_metadata(self):
        # Check that defing a method that has custom
        # metadata though objc.register* but isn't
        # in the parent class gets the updated signature

        # This method has custom metadata in test_vectorcall

        with self.subTest("full_signature override"):

            def v2d(self):
                pass

            out = self.transformer("v2d", v2d, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.signature, b"<2d>@:")

        with self.subTest("return value override in metadata"):
            # Make sure the return value has a different size
            # than 'id' to ensure that this is not determined
            # post-constuction.
            self.fail()

    def test_protocol_method(self):
        self.fail()

    def test_informal_protocol_method(self):
        # Defined MyProto3 from test_protocols
        def testMethod(self):
            return 1

        with self.subTest("basic case"):
            out = self.transformer("testMethod", testMethod, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.signature, b"I@:")

        #
        # Informal protocol should only affect methods that have
        # better information (inherited, classmethod or objc_method)
        #

        with self.subTest("objc_method sets sigature"):
            m = _transform.objc_method(signature=b"d@:")(testMethod)
            out = self.transformer("testMethod", m, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertEqual(out.signature, b"d@:")

        with self.subTest("objc_method sets isclass to True"):
            m = _transform.objc_method(isclass=True)(testMethod)
            out = self.transformer("testMethod", m, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertTrue(out.isClassMethod)
            self.assertEqual(out.signature, b"@@:")

        with self.subTest("explicit class method"):
            m = classmethod(testMethod)
            out = self.transformer("testMethod", m, NSObject, [])
            self.assertIsInstance(out, objc.selector)
            self.assertTrue(out.isClassMethod)
            self.assertEqual(out.signature, b"@@:")

        class Fake:
            def testMethod(self):
                return 1

            testMethod = objc.selector(
                testMethod, selector=b"testMethod", signature=b"f@:"
            )

        with self.subTest("inherited method"):
            self.assertIsInstance(testMethod, types.FunctionType)
            out = self.transformer("testMethod", testMethod, Fake, [])
            self.assertIsInstance(out, objc.selector)
            self.assertFalse(out.isClassMethod)
            self.assertEqual(out.signature, b"f@:")


class TestCTransformer(TestCase):
    # Subclass from TestTransformer and repace the transformer argument
    pass
