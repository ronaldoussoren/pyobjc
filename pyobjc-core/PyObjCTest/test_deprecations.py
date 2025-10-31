# XXX: Add variants for tests using the regular caller, these
#      all use the "simple" caller.
import contextlib
import warnings

import objc
from PyObjCTest.deprecations import OCTestDeprecations, function_list
from PyObjCTools.TestSupport import TestCase

objc.registerMetaDataForSelector(b"OCTestDeprecations", b"method1", {})
objc.registerMetaDataForSelector(
    b"OCTestDeprecations", b"method2", {"deprecated": 1004}
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations", b"method3", {"deprecated": 1004}
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations", b"method4", {"deprecated": 1005}
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations", b"method5", {"deprecated": 1005}
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations", b"method6", {"deprecated": 1006}
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations", b"method7", {"deprecated": 1006}
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations", b"method8", {"deprecated": 1010}
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations", b"method9", {"deprecated": 1010}
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations",
    b"method1:",
    {
        "arguments": {2: {"type_modifier": "n"}},
    },
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations",
    b"method2:",
    {"arguments": {2: {"type_modifier": "n"}}, "deprecated": 1004},
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations",
    b"method3:",
    {"arguments": {2: {"type_modifier": "n"}}, "deprecated": 1004},
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations",
    b"method4:",
    {"arguments": {2: {"type_modifier": "n"}}, "deprecated": 1005},
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations",
    b"method5:",
    {"arguments": {2: {"type_modifier": "n"}}, "deprecated": 1005},
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations",
    b"method6:",
    {"arguments": {2: {"type_modifier": "n"}}, "deprecated": 1006},
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations",
    b"method7:",
    {"arguments": {2: {"type_modifier": "n"}}, "deprecated": 1006},
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations",
    b"method8:",
    {"arguments": {2: {"type_modifier": "n"}}, "deprecated": 1010},
)
objc.registerMetaDataForSelector(
    b"OCTestDeprecations",
    b"method9:",
    {"arguments": {2: {"type_modifier": "n"}}, "deprecated": 1010},
)

_FunctionTable = [
    ("func1", b"i", "", {}),
    ("func2", b"i", "", {"deprecated": 1004}),
    ("func3", b"i", "", {"deprecated": 1004}),
    ("func4", b"i", "", {"deprecated": 1005}),
    ("func5", b"i", "", {"deprecated": 1005}),
    ("func6", b"i", "", {"deprecated": 1006}),
    ("func7", b"i", "", {"deprecated": 1006}),
    ("func8", b"i", "", {"deprecated": 1010}),
    ("func9", b"i", "", {"deprecated": 1010}),
]

objc.loadFunctionList(function_list, globals(), _FunctionTable, False)


@contextlib.contextmanager
def deprecation_warnings(level):
    orig = objc.options.deprecation_warnings
    try:
        objc.options.deprecation_warnings = level
        yield
    finally:
        objc.options.deprecation_warnings = orig


class TestDeprecationWarnings(TestCase):
    def assertDeprecationWarning(self, func, *args):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            func(*args)

        self.assertEqual(len(w), 1)
        self.assertTrue(issubclass(w[-1].category, objc.ApiDeprecationWarning))

        with self.assertRaises(objc.ApiDeprecationWarning):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("error")
                func(*args)

    def assertNoDeprecationWarning(self, func, *args):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            func(*args)

        if w:
            print([(x.category, x.message) for x in w])
            print(func.__metadata__())
        self.assertEqual(len(w), 0)

    def test_warning(self):
        self.assertTrue(issubclass(objc.ApiDeprecationWarning, DeprecationWarning))

    def test_disabled_warnings(self):
        o = OCTestDeprecations.alloc().init()
        with deprecation_warnings(None):
            self.assertNoDeprecationWarning(o.method1)
            self.assertNoDeprecationWarning(o.method2)
            self.assertNoDeprecationWarning(o.method1_, 0)
            self.assertNoDeprecationWarning(o.method2_, 0)
            self.assertNoDeprecationWarning(func1)  # noqa: F821
            self.assertNoDeprecationWarning(func2)  # noqa: F821

    def test_enabled_warnings(self):
        o = OCTestDeprecations.alloc().init()

        with deprecation_warnings("10.6"):
            self.assertNoDeprecationWarning(o.method1)
            self.assertDeprecationWarning(o.method2)
            self.assertDeprecationWarning(o.method4)
            self.assertDeprecationWarning(o.method6)
            self.assertNoDeprecationWarning(o.method8)
            self.assertNoDeprecationWarning(o.method1_, 0)
            self.assertDeprecationWarning(o.method2_, 0)
            self.assertDeprecationWarning(o.method4_, 0)
            self.assertDeprecationWarning(o.method6_, 0)
            self.assertNoDeprecationWarning(o.method8_, 0)

            self.assertNoDeprecationWarning(func1)  # noqa: F821
            self.assertDeprecationWarning(func2)  # noqa: F821
            self.assertDeprecationWarning(func4)  # noqa: F821
            self.assertDeprecationWarning(func6)  # noqa: F821
            self.assertNoDeprecationWarning(func8)  # noqa: F821

    def test_deprecation_error(self):
        o = OCTestDeprecations.alloc().init()

        with warnings.catch_warnings():
            warnings.simplefilter("error")

            with deprecation_warnings("10.6"):
                with self.assertRaisesRegex(
                    objc.ApiDeprecationWarning,
                    r"-\[OCTestDeprecations method2\] is a deprecated API \(macOS 10\.4\)",
                ):
                    o.method2()

                with self.assertRaisesRegex(
                    objc.ApiDeprecationWarning,
                    r"-\[OCTestDeprecations method2:\] is a deprecated API \(macOS 10\.4\)",
                ):
                    o.method2_(0)
