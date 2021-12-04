import objc
import sys
from PyObjCTools.TestSupport import TestCase, skipUnless

NSObject = objc.lookUpClass("NSObject")
NSArray = objc.lookUpClass("NSArray")


class TestGenericClasses(TestCase):
    @skipUnless(sys.version_info[:2] >= (3, 9), "Feature requires python 3.9")
    def test_generic_classes(self):
        with self.subTest("NSObject"):
            int_object = NSObject[int]

            value = int_object.new()
            self.assertIsInstance(value, NSObject)
            with self.assertRaises(TypeError):
                isinstance(value, int_object)

            self.assertEqual(int_object.__args__, (int,))
            self.assertEqual(int_object.__origin__, NSObject)

        with self.subTest("NSArray"):
            int_array = NSArray[int]

            value = int_array.arrayWithArray_([1, 2, 3])
            self.assertIsInstance(value, NSArray)
            self.assertIn(1, value)
            self.assertNotIn(4, value)
            with self.assertRaises(TypeError):
                isinstance(value, int_array)

            self.assertEqual(int_array.__args__, (int,))
            self.assertEqual(int_array.__origin__, NSArray)
