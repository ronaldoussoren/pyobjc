import objc
from PyObjCTest.methodlookup import PyObjC_MethodLookup1, PyObjC_MethodLookup2
from PyObjCTools.TestSupport import TestCase


class TestSuperObject(TestCase):
    def test_super_type(self):
        self.assertIsSubclass(objc.super, super)
        self.assertIsNot(objc.super, super)


class TestMethodResolution(TestCase):
    #
    # These are fairly minimal tests of the lazy method resolution mechanism
    # introduced in PyObjC 3.x.

    def test_instance_dir(self):
        o = PyObjC_MethodLookup1.alloc().init()
        self.assertNotIn("instance2", PyObjC_MethodLookup1.__dict__)
        self.assertIn("instance2", dir(o))
        self.assertIn("instance2", dir(PyObjC_MethodLookup1))
        self.assertNotIn("instance2", dir(type(PyObjC_MethodLookup1)))

    def test_class_dir(self):
        o = PyObjC_MethodLookup1
        self.assertNotIn("clsmeth2", PyObjC_MethodLookup1.__dict__)
        self.assertNotIn("clsmeth2", type(PyObjC_MethodLookup1).__dict__)
        self.assertNotIn("clsmeth2", dir(o))
        self.assertNotIn("clsmeth2", dir(PyObjC_MethodLookup1))
        self.assertIn("clsmeth2", dir(type(PyObjC_MethodLookup1)))

    def test_instance_method_caching(self):
        o = PyObjC_MethodLookup1.alloc().init()
        self.assertNotIn("instance", PyObjC_MethodLookup1.__dict__)
        self.assertIsInstance(o.instance, objc.selector)
        self.assertIn("instance", PyObjC_MethodLookup1.__dict__)
        self.assertIsInstance(o.instance, objc.selector)

        # Check that the version from __dict__ is actually used:
        orig = PyObjC_MethodLookup1.__dict__["instance"].signature
        try:
            PyObjC_MethodLookup1.__dict__["instance"].signature = b"d@:"
            self.assertEqual(o.instance.signature, b"d@:")

        finally:
            PyObjC_MethodLookup1.__dict__["instance"].signature = orig

    def test_class_method_caching(self):
        o = PyObjC_MethodLookup1
        self.assertNotIn("clsmeth", type(PyObjC_MethodLookup1).__dict__)
        self.assertIsInstance(o.clsmeth, objc.selector)
        self.assertIn("clsmeth", type(PyObjC_MethodLookup1).__dict__)
        self.assertIsInstance(o.clsmeth, objc.selector)

        # Check that the version from __dict__ is actually used:
        orig = type(PyObjC_MethodLookup1).__dict__["clsmeth"].signature
        try:
            type(PyObjC_MethodLookup1).__dict__["clsmeth"].signature = b"d@:"
            self.assertEqual(o.clsmeth.signature, b"d@:")

        finally:
            type(PyObjC_MethodLookup1).__dict__["clsmeth"].signature = orig

    def test_instance_overloading(self):
        s1 = PyObjC_MethodLookup1.instance3
        s2 = PyObjC_MethodLookup1.instance4

        # Overridden in subclass:
        self.assertNotEqual(PyObjC_MethodLookup2.instance3, s1)

        # Not overriden in subclass:
        self.assertEqual(PyObjC_MethodLookup2.instance4, s2)

        self.assertEqual(PyObjC_MethodLookup2.instance3.selector, s1.selector)
        self.assertEqual(PyObjC_MethodLookup2.instance4.selector, s2.selector)

    def test_class_overloading(self):
        s1 = PyObjC_MethodLookup1.clsmeth3
        s2 = PyObjC_MethodLookup1.clsmeth4

        self.assertIn("clsmeth3", type(PyObjC_MethodLookup1).__dict__)
        self.assertIn("clsmeth4", type(PyObjC_MethodLookup1).__dict__)

        # Overridden in subclass:
        self.assertEqual(
            PyObjC_MethodLookup2.clsmeth3.definingClass, PyObjC_MethodLookup2
        )
        self.assertIn("clsmeth3", type(PyObjC_MethodLookup2).__dict__)

        # Not overriden in subclass:
        self.assertEqual(
            PyObjC_MethodLookup2.clsmeth4.definingClass, PyObjC_MethodLookup1
        )

        self.assertEqual(PyObjC_MethodLookup2.clsmeth3.selector, s1.selector)
        self.assertEqual(PyObjC_MethodLookup2.clsmeth4.selector, s2.selector)

    def test_instance_specials(self):
        # Harder cases to get right: selectors with an embedded underscore
        #  (which means the default translation from Python to ObjC names
        #   won't work)
        o = PyObjC_MethodLookup1.alloc().init()

        self.assertEqual(o.OC_description(), "method description")
        self.assertEqual(o.OC_description.selector, b"OC_description")

        self.assertEqual(o.pyobjc__instanceCount(), 42)
        self.assertEqual(o.pyobjc__instanceCount.selector, b"pyobjc__instanceCount")

        self.assertEqual(o.pyobjc_setObject_forKey_(1, 2), [1, 2])
        self.assertEqual(
            o.pyobjc_setObject_forKey_.selector, b"pyobjc_setObject:forKey:"
        )

    def test_class_specials(self):
        # Harder cases to get right: selectors with an embedded underscore
        #  (which means the default translation from Python to ObjC names
        #   won't work)
        o = PyObjC_MethodLookup1

        self.assertEqual(o.OC_description(), "class description")
        self.assertEqual(o.OC_description.selector, b"OC_description")

        self.assertEqual(o.pyobjc__classCount(), 99)
        self.assertEqual(o.pyobjc__classCount.selector, b"pyobjc__classCount")

        self.assertEqual(o.pyobjc_setObject_forKey_(1, 2), [2, 1])
        self.assertEqual(
            o.pyobjc_setObject_forKey_.selector, b"pyobjc_setObject:forKey:"
        )

    def test_explicit_choice(self):
        s = PyObjC_MethodLookup1.pyobjc_classMethods.both
        self.assertTrue(s.isClassMethod)

        with self.assertRaisesRegex(AttributeError, "No selector instance5"):
            PyObjC_MethodLookup1.pyobjc_classMethods.instance5

        s = PyObjC_MethodLookup1.pyobjc_instanceMethods.both
        self.assertFalse(s.isClassMethod)
        with self.assertRaisesRegex(AttributeError, "No selector clsmeth5"):
            PyObjC_MethodLookup1.pyobjc_instanceMethods.clsmeth5
