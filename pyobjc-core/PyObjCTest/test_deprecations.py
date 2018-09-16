from PyObjCTools.TestSupport import *
import objc
import warnings
import contextlib

from PyObjCTest.deprecations import *

objc.registerMetaDataForSelector(b"OCTestDeprecations", b"method1", dict());
objc.registerMetaDataForSelector(b"OCTestDeprecations", b"method2", dict(deprecated=1004));
objc.registerMetaDataForSelector(b"OCTestDeprecations", b"method3", dict(deprecated=1004));
objc.registerMetaDataForSelector(b"OCTestDeprecations", b"method4", dict(deprecated=1005));
objc.registerMetaDataForSelector(b"OCTestDeprecations", b"method5", dict(deprecated=1005));
objc.registerMetaDataForSelector(b"OCTestDeprecations", b"method6", dict(deprecated=1006));
objc.registerMetaDataForSelector(b"OCTestDeprecations", b"method7", dict(deprecated=1006));
objc.registerMetaDataForSelector(b"OCTestDeprecations", b"method8", dict(deprecated=1010));
objc.registerMetaDataForSelector(b"OCTestDeprecations", b"method9", dict(deprecated=1010));

_FunctionTable = [
    ("func1", b'i', '', dict()),
    ("func2", b'i', '', dict(deprecated=1004)),
    ("func3", b'i', '', dict(deprecated=1004)),
    ("func4", b'i', '', dict(deprecated=1005)),
    ("func5", b'i', '', dict(deprecated=1005)),
    ("func6", b'i', '', dict(deprecated=1006)),
    ("func7", b'i', '', dict(deprecated=1006)),
    ("func8", b'i', '', dict(deprecated=1010)),
    ("func9", b'i', '', dict(deprecated=1010)),
]

objc.loadFunctionList(function_list, globals(),  _FunctionTable, False)

@contextlib.contextmanager
def deprecation_warnings(level):
    orig = objc.options.deprecation_warnings
    try:
        objc.options.deprecation_warnings = level
        yield
    finally:
        objc.options.deprecation_warnings = orig


class TestDeprecationWarnings (TestCase):
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

    def test_warning(self):
        self.assertTrue(issubclass(objc.ApiDeprecationWarning, DeprecationWarning))

    def test_disabled_warnings(self):
        o = OCTestDeprecations.alloc().init()
        with deprecation_warnings(0):
            self.assertNoDeprecationWarning(o.method1)
            self.assertNoDeprecationWarning(o.method2)
            self.assertNoDeprecationWarning(func1)
            self.assertNoDeprecationWarning(func2)

    def test_enabled_warnings(self):
        o = OCTestDeprecations.alloc().init()

        with deprecation_warnings(1006):
            self.assertNoDeprecationWarning(o.method1)
            self.assertDeprecationWarning(o.method2)
            self.assertDeprecationWarning(o.method4)
            self.assertDeprecationWarning(o.method6)
            self.assertNoDeprecationWarning(o.method8)

            self.assertNoDeprecationWarning(func1)
            self.assertDeprecationWarning(func2)
            self.assertDeprecationWarning(func4)
            self.assertDeprecationWarning(func6)
            self.assertNoDeprecationWarning(func8)

if __name__ == "__main__":
    main()
