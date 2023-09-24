import objc
import inspect
import textwrap
import warnings
import sys
from PyObjCTools.TestSupport import TestCase

from PyObjCTest.test_metadata_function import (
    getDoubleFunc,
    getOldDoubleFunc,
    raiseFunc,
    raiseFunc2,
    oldDoubleFunc,
    getGetter,
    get2ndGetter,
)
from PyObjCTest.test_deprecations import deprecation_warnings


bundle = objc.lookUpClass("NSBundle").bundleWithPath_(
    "/System/Library/Frameworks/AppKit.framework"
)

objc.loadBundleFunctions(
    bundle,
    globals(),
    [
        (
            "NSRectClipList",
            b"v^{CGRect={CGPoint=dd}{CGSize=dd}}q",
            "",
            {"arguments": {0: {"c_array_length_in_arg": 1, "type_modifier": b"n"}}},
        ),
        (
            "NSClassFromString",
            b"#@",
            "NSClassFromString doc",
            {
                "deprecated": 1005,
            },
        ),
        (
            "NSCountFrames",
            b"Q",
            "",
            {
                "suggestion": "Don't use this function",
            },
        ),
    ],
    False,
)

doubleFunc = getDoubleFunc()


class TestFunctions(TestCase):
    def test_repr(self):
        self.assertIsInstance(NSRectClipList, objc.function)  # noqa: F821

        self.assertRegex(
            repr(NSRectClipList),  # noqa: F821
            r"<objc.function 'NSRectClipList' at 0x[0-9a-f]+>",  # noqa: F821
        )
        self.assertRegex(repr(doubleFunc), r"<objc.function at 0x[0-9a-f]+>")

        self.assertIsInstance(NSRectClipList.__metadata__(), dict)  # noqa: F821
        self.assertEqual(
            NSRectClipList.__metadata__(),  # noqa: F821
            {
                "full_signature": b"v^{CGRect={CGPoint=dd}{CGSize=dd}}q",
                "arguments": (
                    {
                        "c_array_length_in_arg": 1,
                        "null_accepted": True,
                        "type": b"n^{CGRect={CGPoint=dd}{CGSize=dd}}",
                    },
                    {"_template": True, "type": b"q"},
                ),
                "retval": {"_template": True, "type": b"v"},
            },
        )
        self.assertEqual(
            inspect.signature(NSRectClipList),  # noqa: F821
            inspect.Signature(
                [
                    inspect.Parameter(p, inspect.Parameter.POSITIONAL_ONLY)
                    for p in ("arg0", "arg1")
                ]
            ),
        )

        if "Foundation" in sys.modules:
            recttype = "CoreFoundation.CGRect"
        else:
            recttype = "CGRect"

        self.assertEqual(
            NSRectClipList.__doc__,  # noqa: F821
            textwrap.dedent(
                f"""\
            void NSRectClipList(in {recttype}* arg0, long long arg1);

            arg0: array with length in arg1"""
            ),
        )

        self.assertEqual(
            NSClassFromString.__metadata__()["__doc__"],  # noqa: F821
            "NSClassFromString doc",  # noqa: F821
        )
        self.assertIn("NSClassFromString doc", NSClassFromString.__doc__)  # noqa: F821

    def test_no_instantation(self):
        with self.assertRaisesRegex(
            TypeError, "cannot create 'objc.function' instances"
        ):
            objc.function()

    def test_no_keywords(self):
        with self.assertRaisesRegex(
            TypeError,
            "(<objc.function 'NSRectClipList' at 0x[0-9a-f]+> does not accept keyword arguments)|(keyword arguments not supported)",
        ):
            NSRectClipList(list=[], size=0)  # noqa: F821

        with self.assertRaisesRegex(
            TypeError,
            r"(<objc.function 'oldDoubleFunc' at 0x[0-9a-f]+> does not accept keyword arguments)|(keyword arguments not supported)",
        ):
            oldDoubleFunc(list=[], size=0)

        with self.assertRaisesRegex(
            TypeError,
            r"(<objc.function at 0x[0-9a-f]+> does not accept keyword arguments)|(keyword arguments not supported)",
        ):
            doubleFunc(orig=1)

    def test_func_in_class(self):
        class Foo:
            func = NSRectClipList  # noqa: F821

        o = Foo()
        self.assertIs(o.func, NSRectClipList)  # noqa: F821
        self.assertIs(Foo.func, NSRectClipList)  # noqa: F821

    def test_invalid_typestr(self):
        with self.assertRaisesRegex(
            objc.internal_error, r"Incomplete type signature: '\^'"
        ):
            m = {}
            objc.loadBundleFunctions(
                bundle,
                m,
                [
                    (
                        "NSGetWindowServerMemory",
                        b"qq^q^q^",
                        "NSGetWindowServerMemory docs",
                        {
                            "arguments": {
                                "1": {"type_modifier": b"o"},
                                "2": {"type_modifier": b"o"},
                                "3": {"type_modifier": b"o"},
                            }
                        },
                    ),
                ],
                False,
            )

    def test_invalid_metadata(self):
        with self.assertRaisesRegex(
            TypeError, "Metadata dictionary is of type 'int' instead of 'dict'"
        ):
            m = {}
            objc.loadBundleFunctions(
                bundle,
                m,
                [
                    (
                        "NSGetWindowServerMemory",
                        b"qq^q^q^q",
                        "NSGetWindowServerMemory docs",
                        42,
                    ),
                ],
                False,
            )

    def test_too_many_arguments(self):
        with self.assertRaisesRegex(
            objc.error, "Callable metadata with too many arguments"
        ):
            m = {}
            objc.loadBundleFunctions(
                bundle,
                m,
                [
                    (
                        "NSGetWindowServerMemory",
                        b"qq",
                        "",
                        {
                            "arguments": {
                                0: {
                                    "callable": {
                                        "retval": {"type": b"i"},
                                        "arguments": {
                                            i: {"type": b"i"} for i in range(200)
                                        },
                                    }
                                },
                            }
                        },
                    ),
                ],
                False,
            )

    def assertDeprecationWarning(self, func):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            func()

        self.assertEqual(len(w), 1)
        self.assertTrue(issubclass(w[-1].category, objc.ApiDeprecationWarning))

    def assertNoDeprecationWarning(self, func):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            func()

        if w:
            print([(x.category, x.message) for x in w])
            print(func.__metadata__())
        self.assertEqual(len(w), 0)

    def test_disabled_function(self):
        with self.assertRaisesRegex(TypeError, "Don't use this function"):
            NSCountFrames()  # noqa: F821

    def test_deprecations(self):
        NSClassFromString("NSObject")  # noqa: F821

        self.assertEqual(
            NSClassFromString.__metadata__()["deprecated"], 1005  # noqa: F821
        )

        with deprecation_warnings("10.4"):
            self.assertNoDeprecationWarning(
                lambda: NSClassFromString("NSObject")  # noqa: F821
            )

        with deprecation_warnings("10.5"):
            self.assertDeprecationWarning(
                lambda: NSClassFromString("NSObject")  # noqa: F821
            )

        with deprecation_warnings("10.8"):
            self.assertDeprecationWarning(
                lambda: NSClassFromString("NSObject")  # noqa: F821
            )

        with warnings.catch_warnings():
            warnings.simplefilter("error")
            with deprecation_warnings("10.8"):
                with self.assertRaisesRegex(
                    objc.ApiDeprecationWarning,
                    r"NSClassFromString\(\) is a deprecated API \(macOS 10.5\)",
                ):
                    NSClassFromString("NSObject")  # noqa: F821

        func = getOldDoubleFunc()
        with deprecation_warnings("10.4"):
            self.assertNoDeprecationWarning(lambda: func(2))

        with deprecation_warnings("10.5"):
            self.assertDeprecationWarning(lambda: func(2))

        with deprecation_warnings("10.8"):
            self.assertDeprecationWarning(lambda: func(2))

        with warnings.catch_warnings():
            warnings.simplefilter("error")
            with deprecation_warnings("10.8"):
                with self.assertRaisesRegex(
                    objc.ApiDeprecationWarning,
                    r"objc.function instance\(\) is a deprecated API \(macOS 10.5\)",
                ):
                    func(2)

        func = getGetter()
        with deprecation_warnings("10.4"):
            self.assertNoDeprecationWarning(lambda: func(None, None))

        with deprecation_warnings("10.5"):
            self.assertDeprecationWarning(lambda: func(None, None))

        with deprecation_warnings("10.8"):
            self.assertDeprecationWarning(lambda: func(None, None))

        with warnings.catch_warnings():
            warnings.simplefilter("error")
            with deprecation_warnings("10.8"):
                with self.assertRaisesRegex(
                    objc.ApiDeprecationWarning,
                    r"objc.function instance\(\) is a deprecated API \(macOS 10.5\)",
                ):
                    func(None, None)

        with deprecation_warnings("10.4"):
            self.assertNoDeprecationWarning(lambda: oldDoubleFunc(2))

        with deprecation_warnings("10.5"):
            self.assertDeprecationWarning(lambda: oldDoubleFunc(2))

        with deprecation_warnings("10.8"):
            self.assertDeprecationWarning(lambda: oldDoubleFunc(2))

    def test_function_raises(self):
        with self.assertRaisesRegex(objc.error, "ExceptionName - No Reason"):
            raiseFunc()

        with self.assertRaisesRegex(objc.error, "ExceptionName - No Reason"):
            raiseFunc2(1)

    def test_too_many_native_arguments(self):
        func = get2ndGetter()
        with self.assertRaisesRegex(
            objc.error,
            "wrapping a function with 63 arguments, at most 62 are supported",
        ):
            func(None, None)

    def test_wrong_argcount(self):
        with self.assertRaisesRegex(TypeError, "Need 1 arguments, got 2"):
            NSClassFromString("NSObject", "extra")  # noqa: F821

        with self.assertRaisesRegex(TypeError, "Need 1 arguments, got 0"):
            NSClassFromString()  # noqa: F821

        with self.assertRaisesRegex(TypeError, "Need 1 arguments, got 2"):
            doubleFunc(1, 2)

        with self.assertRaisesRegex(TypeError, "Need 1 arguments, got 0"):
            doubleFunc()

        with self.assertRaisesRegex(TypeError, "Need 0 arguments, got 2"):
            getGetter(1, 2)
