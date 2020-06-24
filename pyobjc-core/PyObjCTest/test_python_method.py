import objc
from PyObjCTools.TestSupport import TestCase

NSObject = objc.lookUpClass("NSObject")


class TestPythonMethod(TestCase):
    def test_creation(self):
        self.assertRaises(TypeError, objc.python_method)
        self.assertRaises(TypeError, objc.python_method, 1, 2)
        o = objc.python_method(1)
        self.assertEqual(o.callable, 1)

    def test_usage_basic(self):
        class MyClass(object):
            @objc.python_method
            def my_method(self, a):
                return a * 2

            b = objc.python_method(1)

            @objc.python_method
            @classmethod
            def my_class(cls):
                return str(cls)

        o = MyClass()
        self.assertEqual(o.my_method(4), 8)
        self.assertEqual(o.b, 1)

        self.assertEqual(MyClass.my_class(), str(MyClass))

    def test_usage_objc(self):
        class OC_PythonMethod_Class(NSObject):
            @objc.python_method
            def my_method(self, a):
                return a * 2

            def someSelector(self):
                pass

            b = objc.python_method(2)

        o = OC_PythonMethod_Class.alloc().init()
        self.assertIsNotInstance(o.my_method, objc.selector)
        self.assertIsInstance(o.someSelector, objc.selector)

        self.assertEqual(o.my_method(4), 8)
        self.assertEqual(o.b, 2)
