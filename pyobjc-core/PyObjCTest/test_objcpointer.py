import warnings

import objc
from PyObjCTest.structpointer1 import OC_TestStructPointer
from PyObjCTools.TestSupport import TestCase


class TestObjCPointer(TestCase):
    def setUp(self):
        self._unknown_pointer_raises = objc.options.unknown_pointer_raises

    def tearDown(self):
        objc.options.unknown_pointer_raises = self._unknown_pointer_raises

    def test_default_option(self):
        self.assertEqual(objc.options.unknown_pointer_raises, False)

    def test_class_introspection(self):
        self.assertIn("type", dir(objc.ObjCPointer))
        self.assertIn("pointerAsInteger", dir(objc.ObjCPointer))

    def test_objc_pointer_creation(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=objc.ObjCPointerWarning)

            objc.options.unknown_pointer_raises = False

            v = OC_TestStructPointer.returnUnwrapped()
            self.assertIsInstance(v, objc.ObjCPointer)

            self.assertEqual(v.pointerAsInteger, 42)
            self.assertEqual(v.type, b"^{UnwrappedStruct=ii}")

    def test_objc_pointer_raises(self):
        objc.options.unknown_pointer_raises = True
        self.assertRaises(
            objc.UnknownPointerError, OC_TestStructPointer.returnUnwrapped
        )
