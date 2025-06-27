import objc
from objc import super  # noqa: A004
import gc
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

    def method(self):
        return 21

    @classmethod
    def clsmethod(cls):
        return 99


OCTestWithAttributes.method = -21
type(OCTestWithAttributes).clsmethod = -99


class MethodAccessTest(TestCase):
    def test_circular(self):
        with objc.autorelease_pool():
            o = OCTestWithAttributes.alloc().init()
            methods = o.pyobjc_instanceMethods

            o.attr = methods

            del o
            del methods

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

    def test_access_replaced_method(self):
        o = OCTestWithAttributes.alloc().init()
        self.assertEqual(o.method, -21)

        self.assertEqual(o.pyobjc_instanceMethods.method(), 21)

    def test_access_replaced_method_through_class(self):
        self.assertEqual(OCTestWithAttributes.clsmethod, -99)
        self.assertEqual(OCTestWithAttributes.pyobjc_classMethods.clsmethod(), 99)

        # XXX: This test fails, but shouldn't.
        o = OCTestWithAttributes.alloc().init()
        self.assertEqual(OCTestWithAttributes.pyobjc_instanceMethods.method(o), 21)

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

        OC_UnusedClass.someOtherInstanceMethod = 42

        self.assertIsInstance(
            OC_UnusedClass.pyobjc_instanceMethods.someOtherInstanceMethod, objc.selector
        )

        class helper:
            def __get__(self, instance, instance_type=None):
                raise RuntimeError("no getting")

            def __set__(self, instance, new_value):
                raise RuntimeError("no setting")

        OC_UnusedClass.yetAnotherInstanceMethod = helper()

        self.assertIsInstance(
            OC_UnusedClass.pyobjc_instanceMethods.yetAnotherInstanceMethod,
            objc.selector,
        )

        #
        # Actually use the class to validate  that the changes to
        # 'someOtherInstanceMethod' and 'yetAnotherInstanceMethod' were
        # effective.
        #

        o = OC_UnusedClass.alloc().init()
        self.assertEqual(o.someOtherInstanceMethod, 42)

        with self.assertRaisesRegex(RuntimeError, "no getting"):
            o.yetAnotherInstanceMethod

        with self.assertRaisesRegex(RuntimeError, "no setting"):
            o.yetAnotherInstanceMethod = 21

        #
        # Revalidate resolving through method accessor
        #
        self.assertIsInstance(
            OC_UnusedClass.pyobjc_instanceMethods.someOtherInstanceMethod, objc.selector
        )
        self.assertIsInstance(
            OC_UnusedClass.pyobjc_instanceMethods.yetAnotherInstanceMethod,
            objc.selector,
        )

        # Check in __dict__
        d = OC_UnusedClass.pyobjc_instanceMethods.__dict__
        self.assertIn("someOtherInstanceMethod", d)
        self.assertIn("yetAnotherInstanceMethod", d)
        self.assertIsInstance(d["someOtherInstanceMethod"], objc.selector)
        self.assertIsInstance(d["yetAnotherInstanceMethod"], objc.selector)

    def test_various_methods(self):
        value = OCTestWithAttributes.alloc().init()
        NSObject.alloca = objc.python_method(OCTestWithAttributes.alloc)
        for cls in type(value).__mro__:
            try:
                cls.__dict__["alloca"]
            except KeyError:
                pass
        with self.assertRaisesRegex(AttributeError, "alloca"):
            value.pyobjc_instanceMethods.alloca

        # XXX: 'del' won't work, hence accept that this
        #      pollutes the test environment a little.
        # del NSObject.alloca

        class OCTestWithGetAttr(NSObject):
            def __getattr__(self, key):
                raise AttributeError(f"no -- {key} --")

        value = OCTestWithGetAttr.alloc().init()
        with self.assertRaisesRegex(AttributeError, "no -- method --"):
            value.method

        with self.assertRaisesRegex(AttributeError, "No selector method"):
            value.pyobjc_instanceMethods.method

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
