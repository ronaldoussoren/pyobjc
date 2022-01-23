import objc
import gc
from PyObjCTools.TestSupport import TestCase

NSObject = objc.lookUpClass("NSObject")


class TestPythonMethod(TestCase):
    def test_creation(self):
        with self.assertRaisesRegex(
            TypeError,
            r"(function missing required argument 'callable' \(pos 1\))|(Required argument 'callable' \(pos 1\) not found)",
        ):
            objc.python_method()
        with self.assertRaisesRegex(
            TypeError, r"function takes at most 1 argument \(2 given\)"
        ):
            objc.python_method(1, 2)
        o = objc.python_method(1)
        self.assertEqual(o.callable, 1)

    def test_usage_basic(self):
        class MyClass:
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
        self.assertNotIsInstance(o.my_method, objc.selector)
        self.assertIsInstance(o.someSelector, objc.selector)

        self.assertEqual(o.my_method(4), 8)
        self.assertEqual(o.b, 2)

    def test_python_method_in_regular_class(self):
        class Foo:
            @objc.python_method
            def args(self, a, b):
                return (a, b)

        o = Foo()
        self.assertEqual(o.args(1, 2), (1, 2))

        o = Foo()
        self.assertEqual(o.args(b=1, a=2), (2, 1))

    def test_gc(self):
        deallocated = False

        class Cleanup:
            def __del__(self):
                nonlocal deallocated
                deallocated = True

        c = Cleanup()

        r = objc.python_method(c)
        c.r = r

        del c, r

        # XXX: This is a bit too specific for current
        #      CPython behaviour.
        self.assertFalse(deallocated)
        gc.collect(2)
        self.assertTrue(deallocated)

    # XXX: Need a way to create a python_method with
    #      a NULL callable (e.g. force a call to the
    #      tp_clear slot.

    # XXX: Need C helper that ensures that
    #      tp_call is used (instead of vectorcall),
    #      in particular when using keywords
