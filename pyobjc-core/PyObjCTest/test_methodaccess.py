import objc
from objc import super  # noqa: A004
import gc
from .test_ivar import nilObject, NilHelper
from PyObjCTools.TestSupport import TestCase, expectedFailure

NSObject = objc.lookUpClass("NSObject")
# _NSZombie = objc.lookUpClass('_NSZombie')
NSProxy = objc.lookUpClass("NSProxy")


class OCTestWithAttributes(NSObject):
    class_attr = 1

    def init(self):
        self = super().init()
        if self is None:
            return None

        self.attr = 42
        return self

    # Attribute used in test_category_overides_attribute
    pyobjcTestMethod = 42


class MethodAccessTest(TestCase):
    def testObjCObject(self):
        # Trying to access the methods of objc.objc_object should not
        # crash the interpreter.
        with self.assertRaisesRegex(
            AttributeError, "<nil> doesn't have attribute func_code"
        ):
            objc.objc_object.pyobjc_classMethods.func_code

        with self.assertRaisesRegex(
            AttributeError, "<nil> doesn't have attribute func_code"
        ):
            objc.objc_object.pyobjc_instanceMethods.func_code,  # noqa: B018

        self.assertEqual(objc.objc_object.pyobjc_classMethods.__dict__, {})
        self.assertEqual(objc.objc_object.pyobjc_instanceMethods.__dict__, {})

        with self.assertRaisesRegex(
            AttributeError,
            "cannot access attribute 'pyobjc_instanceMethods' of NIL 'NilHelper' object",
        ):
            nilObject.pyobjc_instanceMethods.__dict__

        nil = NilHelper.alloc()
        instanceMethods = nil.pyobjc_instanceMethods
        nil.init()
        self.assertEqual(instanceMethods.__dict__, {})

    def testNSProxyStuff(self):
        # NSProxy is incompatitble with pyobjc_{class,instance}Methods, but
        # this should not crash the interpreter
        with self.assertRaisesRegex(AttributeError, "No selector foobar"):
            NSProxy.pyobjc_instanceMethods.foobar

        with self.assertRaisesRegex(AttributeError, "No selector foobar"):
            NSProxy.pyobjc_classMethods.foobar

        with self.assertRaisesRegex(AttributeError, "No attribute foobar"):
            NSProxy.foobar

    def testDir(self):
        o = NSObject.new()

        d = dir(o.pyobjc_instanceMethods)
        self.assertGreater(len(d), 10)
        self.assertIn("init", d)

        d = dir(NSObject.pyobjc_classMethods)
        self.assertGreater(len(d), 10)
        self.assertIn("alloc", d)

    def testDict(self):
        o = NSObject.new()

        with self.subTest("instance"):
            d = o.pyobjc_instanceMethods.__dict__.keys()
            self.assertGreater(len(d), 10)
            self.assertIn("init", d)

        with self.subTest("class"):
            d = NSObject.pyobjc_classMethods.__dict__.keys()
            self.assertGreater(len(d), 10)
            self.assertIn("alloc", d)

        with self.subTest("instance through class"):
            d = NSObject.pyobjc_instanceMethods.__dict__.keys()
            self.assertGreater(len(d), 10)
            self.assertIn("init", d)

        # d = o.pyobjc_classMethods.__dict__.keys()
        # self.assertGreater(len(d), 10)
        # self.assertIn("alloc", d)

    def testAttributes(self):
        o = NSObject.new()

        self.assertHasAttr(o.pyobjc_instanceMethods, "init")
        # self.assertHasAttr(o.pyobjc_classMethods, "alloc")

        self.assertHasAttr(NSObject.pyobjc_classMethods, "alloc")
        self.assertHasAttr(NSObject.pyobjc_instanceMethods, "init")

        self.assertNotHasAttr(NSObject.pyobjc_classMethods, "foothebar")
        self.assertNotHasAttr(NSObject.pyobjc_instanceMethods, "foothebar")

        o = OCTestWithAttributes.alloc().init()
        self.assertHasAttr(o, "attr")
        self.assertHasAttr(o, "class_attr")
        self.assertNotHasAttr(OCTestWithAttributes.pyobjc_classMethods, "attr")
        self.assertNotHasAttr(OCTestWithAttributes.pyobjc_instanceMethods, "attr")
        self.assertNotHasAttr(o.pyobjc_instanceMethods, "attr")
        self.assertNotHasAttr(OCTestWithAttributes.pyobjc_classMethods, "class_attr")
        self.assertNotHasAttr(OCTestWithAttributes.pyobjc_instanceMethods, "class_attr")
        self.assertNotHasAttr(o.pyobjc_instanceMethods, "class_attr")

        with self.assertRaisesRegex(AttributeError, "No such attribute: __members__"):
            o.pyobjc_instanceMethods.__members__

        with self.assertRaisesRegex(AttributeError, "No such attribute: __methods__"):
            o.pyobjc_instanceMethods.__methods__

    def test_repr(self):
        o = NSObject.alloc().init()
        self.assertRegex(
            repr(o.pyobjc_instanceMethods),
            "<instance method-accessor for <NSObject: 0x[a-f0-9]+>>",
        )
        self.assertRegex(
            repr(NSObject.pyobjc_instanceMethods),
            "<instance method-accessor for <objective-c class NSObject at 0x[0-9a-f]+>>",
        )
        self.assertRegex(
            repr(NSObject.pyobjc_classMethods),
            "<class method-accessor for <objective-c class NSObject at 0x[0-9a-f]+>>",
        )

    def test_python_category_override_attribute(self):
        # See also test_category_overides_attribute
        #
        # This testcase primarily checks the regular Python
        # behaviour to ensure that PyObjC's behaviour for
        # Cocoa subclasses is consistent with that.
        class BaseMeta(type):
            @property
            def meta(self):
                return f"meta {self.__name__}"

        class BaseClass(metaclass=BaseMeta):
            pass

        class SubClass(BaseClass):
            attribute = 42

        self.assertEqual(SubClass.meta, "meta SubClass")

        self.assertEqual(SubClass.attribute, 42)

        def attribute(self):
            return f"attribute {self.__name__}"

        BaseMeta.attribute = property(attribute)

        self.assertEqual(SubClass.meta, "meta SubClass")
        self.assertEqual(SubClass.attribute, "attribute SubClass")

    def test_category_overides_attribute(self):
        self.assertEqual(OCTestWithAttributes.pyobjcTestMethod, 42)

        # This import loads a category on NSObject that
        # defines '-[NSObject pyobjcTestMethod]'
        from . import nsobjectcategory  # noqa: F401

        # See 'test_python_category_override_attribute' above: objc.selector
        # is a descriptor with a ``__set__`` slot (that always raises), which
        # means the attribute resolution won't use "attribute" from the
        # SubClass ``__dict__`` but prefers the descriptor in the parent
        # class.
        # self.assertEqual(OCTestWithAttributes.pyobjcTestMethod, 42)

        self.assertIsInstance(OCTestWithAttributes.pyobjcTestMethod, objc.selector)
        self.assertIsInstance(
            OCTestWithAttributes.pyobjc_instanceMethods.pyobjcTestMethod, objc.selector
        )
        self.assertIsInstance(NSObject.pyobjcTestMethod, objc.selector)

    def test_access_in_unused_class(self):
        from .methodaccess import OC_UnusedClass

        self.assertIsInstance(
            OC_UnusedClass.pyobjc_instanceMethods.someInstanceMethod, objc.selector
        )
        self.assertIsInstance(
            OC_UnusedClass.pyobjc_classMethods.someClassMethod, objc.selector
        )

    @expectedFailure
    def test_cycle(self):
        cleared = False

        class DeallocHelper:
            def __del__(self):
                nonlocal cleared
                cleared = True

        class Bag:
            pass

        o = OCTestWithAttributes.alloc().init()
        o.helper = DeallocHelper()
        o.some = o.pyobjc_instanceMethods

        cleared = False
        del o
        self.assertFalse(cleared)
        gc.collect()

        # XXX: The object is not actually
        # collected, possibly because
        # objc.objc_object and objc.objc_class
        # don't have GC support
        self.assertTrue(cleared)


class Py_FirstGenSubClas(NSObject):
    pass


class ClassAndInstanceMethods(TestCase):
    # XXX: See https://github.com/ronaldoussoren/pyobjc/issues/452
    def testClassThroughInstance(self):
        # Class methods are not accessible through instances.
        with self.assertRaisesRegex(
            AttributeError, "'NSObject' object has no attribute 'alloc'"
        ):
            NSObject.new().alloc

    @expectedFailure
    def testClassThroughInstance2(self):
        # Class methods are not accessible through instances.
        with self.assertRaisesRegex(
            AttributeError, "'Py_FirstGenSubClas' object has no attribute 'alloc'"
        ):
            Py_FirstGenSubClas.new().alloc

    @expectedFailure
    def testPythonClassThroughInstance(self):
        # same as testClassThroughInstance, but without involving
        # PyObjC. This test uses properties instead of methods
        # because PyObjC's seletors are more like properties due
        # to having a ``__set__`` slot.

        class BaseMeta(type):
            @property
            def meta(self):
                return f"meta {self.__name__}"

        class BaseClass(metaclass=BaseMeta):
            pass

        # Defining "SubMeta" matches the PyObjC class structure,
        # but isn't necessary the  observe the unexpected behaviour
        class SubMeta(BaseMeta):
            pass

        class SubClass(BaseClass, metaclass=SubMeta):
            pass

        value = BaseClass()
        with self.assertRaisesRegex(
            AttributeError, "'BaseClass' object has no attribute 'meta'"
        ):
            value.meta

        value = SubMeta
        with self.assertRaisesRegex(
            AttributeError, "'SubClass' object has no attribute 'meta'"
        ):
            # ^^^^ This assertion fails, 'value.meta' returns the BaseMeta.meta property,
            #      *without* calling the ``__get__`` slot.
            value.meta


class TestReplacingMethods(TestCase):
    def test_replace_through_instane(self):
        o = NSObject.alloc().init()
        with self.assertRaisesRegex(
            AttributeError, "'NSObject' object attribute 'description' is read-only"
        ):
            o.description = 42

    def no_test_replace_through_class(self):
        # XXX: #479
        with self.assertRaisesRegex(
            AttributeError,
            "Cannot replace selector 'alloc' in 'NSObject' by non-selector",
        ):
            NSObject.alloc = 42
