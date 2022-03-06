import objc
from .test_ivar import nilObject
from PyObjCTools.TestSupport import TestCase

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
            objc.objc_object.pyobjc_instanceMethods.func_code,

        self.assertEqual(objc.objc_object.pyobjc_classMethods.__dict__, {})
        self.assertEqual(objc.objc_object.pyobjc_instanceMethods.__dict__, {})

        with self.assertRaisesRegex(
            AttributeError,
            "cannot access attribute 'pyobjc_instanceMethods' of NIL 'NilHelper' object",
        ):
            nilObject.pyobjc_instanceMethods.__dict__

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

        d = o.pyobjc_instanceMethods.__dict__.keys()
        self.assertGreater(len(d), 10)
        self.assertIn("init", d)

        d = NSObject.pyobjc_classMethods.__dict__.keys()
        self.assertGreater(len(d), 10)
        self.assertIn("alloc", d)

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


class ClassAndInstanceMethods(TestCase):
    def testClassThroughInstance(self):
        # Class methods are not accessible through instances.
        with self.assertRaisesRegex(
            AttributeError, "'NSObject' object has no attribute 'alloc'"
        ):
            NSObject.new().alloc
