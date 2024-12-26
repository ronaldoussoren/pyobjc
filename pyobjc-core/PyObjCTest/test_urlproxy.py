import objc
import os
import pathlib
from PyObjCTools.TestSupport import TestCase

NSMutableArray = objc.lookUpClass("NSMutableArray")
NSURL = objc.lookUpClass("NSURL")


class TestURLProxy(TestCase):
    def test_basic_construction(self):
        a = NSMutableArray.array()
        p = pathlib.Path(__file__)
        a.addObject_(p)

        self.assertIn(p, a)

        del p

        (valueClass,) = a.valueForKeyPath_("@unionOfObjects.class")
        self.assertEqual(valueClass.__name__, "OC_PythonURL")

        (description,) = a.valueForKeyPath_("@unionOfObjects.description")
        self.assertEqual(description, "file://" + __file__)

        x = a.firstObject()
        self.assertIsInstance(x, pathlib.Path)
        del x

    def test_invalid_values(self):
        a = NSMutableArray.array()
        p = pathlib.Path(__file__ + "\0therest")
        with self.assertRaisesRegex(ValueError, "result has embedded NULs"):
            a.addObject_(p)

        class MyPath(pathlib.PosixPath):
            def __fspath__(self):
                raise RuntimeError("cannot fspath me")

        p = MyPath(__file__)
        with self.assertRaisesRegex(RuntimeError, "cannot fspath me"):
            os.fspath(p)

        with self.assertRaisesRegex(RuntimeError, "cannot fspath me"):
            a.addObject_(p)

        class MyPath(pathlib.PosixPath):
            def __fspath__(self):
                return super().__fspath__().encode()

        p = MyPath(__file__)
        with self.assertRaisesRegex(ValueError, "did not return a string"):
            a.addObject_(p)

    def test_no_path(self):
        # Test with an empty return value from __fspath__,
        # which isn't a valid system path and returns in a
        # 'nil' return value when constructing an NSURL.
        class MyPath(pathlib.PosixPath):
            def __fspath__(self):
                return ""

        a = NSMutableArray.array()
        p = MyPath(__file__)

        with self.assertRaisesRegex(objc.error, "Cannot convert path-like to URL"):
            a.addObject_(p)
