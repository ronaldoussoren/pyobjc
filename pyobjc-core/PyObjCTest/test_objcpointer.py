import warnings

import objc
from PyObjCTest.structpointer1 import OC_TestStructPointer
from PyObjCTools.TestSupport import TestCase, pyobjc_options

objc.registerMetaDataForSelector(
    b"OC_TestStructPointer",
    b"returnUnwrapped2",
    {"retval": {"type": b"^{UnwrappedStruct=iX}"}},
)


class TestObjCPointer(TestCase):
    def setUp(self):
        self._unknown_pointer_raises = objc.options.unknown_pointer_raises

    def tearDown(self):
        objc.options.unknown_pointer_raises = self._unknown_pointer_raises

    def test_default_option(self):
        self.assertEqual(objc.options.unknown_pointer_raises, False)

    def test_class_introspection(self):
        self.assertIn("pointerAsInteger", dir(objc.ObjCPointer))

    def test_objc_pointer_creation(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=objc.ObjCPointerWarning)

            with pyobjc_options(unknown_pointer_raises=False):
                v = OC_TestStructPointer.returnUnwrapped()
                self.assertIsInstance(v, objc.ObjCPointer)

                self.assertEqual(v.pointerAsInteger, 42)
                self.assertEqual(v.typestr, b"^{UnwrappedStruct=ii}")

                r = OC_TestStructPointer.unwrappedToInt_(v)
                self.assertEqual(r, 42)

                with self.assertRaisesRegex(
                    ValueError, "depythonifying 'pointer', got 'int'"
                ):
                    OC_TestStructPointer.unwrappedToInt_(44)

    def test_objc_pointer_raises(self):
        objc.options.unknown_pointer_raises = True
        with self.assertRaisesRegex(
            objc.UnknownPointerError, r"pointer of type \^{UnwrappedStruct=ii}@:"
        ):
            OC_TestStructPointer.returnUnwrapped()

    def test_warning_raises(self):
        with warnings.catch_warnings():
            warnings.simplefilter("error", category=objc.ObjCPointerWarning)
            with pyobjc_options(unknown_pointer_raises=False):
                with self.assertRaisesRegex(
                    objc.ObjCPointerWarning,
                    r"PyObjCPointer created: at 0x2a of type \^{UnwrappedStruct=ii}.*",
                ):
                    OC_TestStructPointer.returnUnwrapped()

    def test_objc_pointer_with_invalid_type(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=objc.ObjCPointerWarning)

            with pyobjc_options(unknown_pointer_raises=False):
                with self.assertRaisesRegex(
                    objc.internal_error, "Unhandled type '0x58' X}"
                ):
                    OC_TestStructPointer.returnUnwrapped2()
