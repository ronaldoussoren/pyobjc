from PyObjCTools.TestSupport import TestCase
from .transient import OC_Transient
import objc

NSNull = objc.lookUpClass("NSNull")
NSArray = objc.lookUpClass("NSArray")


class TestTransient(TestCase):
    def test_basic_functionality(self):
        with objc.autorelease_pool():
            o = OC_Transient.alloc().init()
            del o

    def test_basic_python_subclass(self):
        class Py_Transient1(OC_Transient):
            pass

        with objc.autorelease_pool():
            o = Py_Transient1.alloc().init()
            del o

    def test_python_method(self):
        cleared = False

        class Py_Transient2(OC_Transient):
            def beforeDealloc(self):
                nonlocal cleared
                cleared = True

        with objc.autorelease_pool():
            o = Py_Transient2.alloc().init()
            self.assertFalse(cleared)
            del o

        self.assertTrue(cleared)

    def test_array_of_values(self):
        cleared = False
        stored = None

        class PyTransient3(OC_Transient):
            def method(self):
                nonlocal stored
                stored = self

            def beforeDealloc(self):
                nonlocal cleared
                cleared = True

        with objc.autorelease_pool():
            o = PyTransient3.alloc().init()
            a = NSArray.alloc().initWithObject_(o)
            del o

        self.assertFalse(cleared)

        with objc.autorelease_pool():
            stored = None
            a.makeObjectsPerformSelector_(b"method")
            self.assertFalse(cleared)
            self.assertIsInstance(stored, PyTransient3)
            stored2 = stored

            self.assertFalse(stored.__flags__ & 0x8, "should not release flag set")

            stored = None
            a.makeObjectsPerformSelector_(b"method")
            self.assertIs(stored2, stored)

            del stored, stored2
            del a

        self.assertTrue(cleared)
