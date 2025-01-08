import objc
from PyObjCTest.instanceVariables import ClassWithVariables
from PyObjCTools.TestSupport import TestCase


NSObject = objc.lookUpClass("NSObject")
NSAutoreleasePool = objc.lookUpClass("NSAutoreleasePool")
NSArray = objc.lookUpClass("NSArray")


# XXX: This type and instance should be in a  helper module
class NilHelper(NSObject):
    def init(self):
        self.release()
        return None


nilObject = NilHelper.alloc()
nilObject.init()


class Base:
    def __init__(self, ondel):
        self.ondel = ondel

    def __del__(self):
        self.ondel()


class OCBase(NSObject):
    def init_(self, ondel):
        self.ondel = ondel

    def __del__(self):
        self.ondel()


class TestClass(NSObject):
    idVar = objc.ivar("idVar")
    idVar2 = objc.ivar("idVar2", b"@")
    intVar = objc.ivar("intVar", objc._C_INT)
    doubleVar = objc.ivar("doubleVar", objc._C_DBL)
    outlet = objc.ivar("outlet", isOutlet=True)
    unnamed = objc.ivar()
    shortVar = objc.ivar.short("shortVar2")


class TestInstanceVariables(TestCase):
    def setUp(self):
        self.object = TestClass.alloc().init()

    def test_class_setup(self):
        v = objc.ivar()
        with self.assertRaisesRegex(TypeError, "required argument "):
            v.__pyobjc_class_setup__()

        class_dict = {}
        ilist = set()
        clist = set()

        v.__pyobjc_class_setup__("myname", class_dict, ilist, clist)
        self.assertEqual(v.__name__, "myname")
        self.assertEqual(class_dict, {})
        self.assertEqual(ilist, set())
        self.assertEqual(clist, set())

    def test_ivar_misusage(self):
        iv = objc.ivar("iv")

        with self.assertRaisesRegex(
            TypeError, "Cannot access Objective-C instance-variables through class"
        ):
            iv.__get__(objc.lookUpClass("NSObject"))

        o = NSArray.alloc()
        o.init()

        with self.assertRaisesRegex(
            TypeError, "Cannot access Objective-C instance-variables of 'nil'"
        ):
            iv.__get__(o)

        with self.assertRaisesRegex(ValueError, "Invalid type encoding"):
            objc.ivar("iv", b"X")

    def test_ivar_equality(self):
        # Check that ivar equality tests are correct,
        # and that equal values have equal hashes.
        ivar_a = objc.ivar("a")
        ivar_a2 = objc.ivar("a")
        ivar_a3 = objc.ivar("a", objc._C_FLT)
        ivar_b = objc.ivar("b")
        ivar_b2 = objc.ivar("b", isSlot=True)
        ivar_b3 = objc.ivar("b", isOutlet=True)
        ivar_nameless = objc.ivar()
        ivar_nameless2 = objc.ivar()

        self.assertFalse(ivar_b.__isSlot__)
        self.assertFalse(ivar_b.__isOutlet__)
        self.assertTrue(ivar_b2.__isSlot__)
        self.assertTrue(ivar_b3.__isOutlet__)

        self.assertTrue(ivar_a == ivar_a2)
        self.assertFalse(ivar_a == ivar_a3)
        self.assertFalse(ivar_a == ivar_b)
        self.assertFalse(ivar_b == ivar_b2)
        self.assertFalse(ivar_b == ivar_b3)
        self.assertFalse(ivar_b2 == ivar_b3)
        self.assertTrue(ivar_nameless == ivar_nameless2)
        self.assertFalse(ivar_nameless == ivar_a)
        self.assertFalse(ivar_a == ivar_nameless)
        self.assertFalse(ivar_a == 42)

        self.assertFalse(ivar_a != ivar_a2)
        self.assertTrue(ivar_a != ivar_a3)
        self.assertTrue(ivar_a != ivar_b)
        self.assertTrue(ivar_b != ivar_b2)
        self.assertTrue(ivar_b != ivar_b3)
        self.assertTrue(ivar_b2 != ivar_b3)
        self.assertFalse(ivar_nameless != ivar_nameless2)
        self.assertTrue(ivar_nameless != ivar_a)
        self.assertTrue(ivar_a != ivar_nameless)
        self.assertTrue(ivar_a != 42)

        with self.assertRaisesRegex(TypeError, "'<' not supported"):
            ivar_a < ivar_b  # noqa: B015

        self.assertEqual(hash(ivar_nameless), hash(ivar_nameless2))
        self.assertEqual(hash(ivar_a), hash(ivar_a2))
        self.assertNotEqual(hash(ivar_b), hash(ivar_b2))
        self.assertNotEqual(hash(ivar_b), hash(ivar_b3))

    def test_ivars_with_same_name(self):
        with self.assertRaises(objc.error):

            class WithSameName(NSObject):
                a = objc.ivar("a")
                b = objc.ivar("a")

    def test_repr(self):
        self.assertEqual(repr(TestClass.idVar), "<instance-variable idVar>")
        self.assertEqual(repr(TestClass.outlet), "<IBOutlet outlet>")
        self.assertEqual(repr(TestClass.unnamed), "<instance-variable unnamed>")

        v = objc.ivar()
        self.assertEqual(repr(v), "<instance-variable>")

        v = objc.ivar(isOutlet=True)
        self.assertEqual(repr(v), "<IBOutlet>")

    def test_ivar_in_python_class(self):
        class MyObject:
            idVar = objc.ivar("idVar")

        instance = MyObject()

        with self.assertRaisesRegex(
            TypeError, "objc.ivar descriptor on a plain Python object"
        ):
            instance.idVar

        with self.assertRaisesRegex(
            TypeError, "objc.ivar descriptor on a plain Python object"
        ):
            instance.idVar = 4

    # def test_ivar_of_null(self):
    # XXX: Arange for an objc_object that refers to NULL

    def test_non_existing_ivar(self):
        instance = NSObject.alloc().init()
        iv = objc.ivar("nosuchname")

        with self.assertRaisesRegex(
            RuntimeError, "objc.ivar descriptor for non-existing instance variable.*"
        ):
            iv.__get__(instance, NSObject)

        with self.assertRaisesRegex(
            RuntimeError, "objc.ivar descriptor for non-existing instance variable.*"
        ):
            iv.__set__(instance, 42)

        iv = objc.ivar()  # No name
        with self.assertRaisesRegex(TypeError, "Using unnamed instance variable"):
            iv.__get__(instance, NSObject)

        with self.assertRaisesRegex(TypeError, "Using unnamed instance variable"):
            iv.__set__(instance, 42)

    def testID(self):
        # Check that we can set and query attributes of type 'id'
        self.assertEqual(self.object.idVar, None)
        self.assertEqual(self.object.idVar2, None)

        o = NSObject.alloc().init()

        self.object.idVar = o
        self.object.idVar2 = o

        self.assertIs(self.object.idVar, o)
        self.assertIs(self.object.idVar2, o)

        self.object.idVar = "hello"
        self.assertEqual(self.object.idVar, "hello")

    def testInt(self):
        # Check that we can set and query attributes of type 'int'
        self.assertEqual(self.object.intVar, 0)

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str' of 1"):
            self.object.intVar = "h"

        self.object.intVar = 42
        self.assertEqual(self.object.intVar, 42)

    def testShort(self):
        self.assertEqual(self.object.shortVar, 0)

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str' of 1"):
            self.object.intVar = "h"

        self.object.shortVar = 42
        self.assertEqual(self.object.shortVar, 42)
        self.assertEqual(TestClass.shortVar.__name__, "shortVar2")

    def testDouble(self):
        # Check that we can set and query attributes of type 'double'

        # Can't rely on this for doubles...
        # self.assertEqual(self.object.doubleVar, 0.0)
        with self.assertRaisesRegex(ValueError, "depythonifying 'double', got 'str'"):
            self.object.doubleVar = "h"
        self.object.doubleVar = 42.0
        self.assertAlmostEqual(self.object.doubleVar, 42.0)

    def testLeak(self):
        # Check that plain python objects are correctly released when
        # they are no longer the value of an attribute
        pool = NSAutoreleasePool.alloc().init()
        self.deleted = 0
        self.object.idVar = Base(lambda: setattr(self, "deleted", 1))  # noqa: B010
        self.object.idVar = None
        del pool
        self.assertEqual(self.deleted, 1)

    def testLeak2(self):
        self.deleted = 0

        pool = NSAutoreleasePool.alloc().init()

        self.object.idVar = Base(lambda: setattr(self, "deleted", 1))  # noqa: B010
        del self.object
        del pool
        self.assertEqual(self.deleted, 1)

    def testOCLeak(self):
        # Check that Objective-C objects are correctly released when
        # they are no longer the value of an attribute
        pool = NSAutoreleasePool.alloc().init()
        self.deleted = 0
        self.object.idVar = OCBase.alloc().init_(
            lambda: setattr(self, "deleted", 1)  # noqa: B010
        )
        self.object.idVar = None
        del pool
        self.assertEqual(self.deleted, 1)

    def testOCLeak2(self):
        pool = NSAutoreleasePool.alloc().init()
        self.deleted = 0
        self.object.idVar = OCBase.alloc().init_(
            lambda: setattr(self, "deleted", 1)  # noqa: B010
        )
        del self.object
        del pool
        self.assertEqual(self.deleted, 1)

    def testDelete(self):
        with self.assertRaisesRegex(
            TypeError, "Cannot delete Objective-C instance variables"
        ):
            del self.object.idVar


class TestAllInstanceVariables(TestCase):
    # Some tests for accessing any instance variable, even those not
    # declared in python.

    def testReading(self):
        obj = ClassWithVariables.alloc().init()

        getter = objc.getInstanceVariable

        cls = getter(obj, "isa")
        self.assertIs(cls, type(obj))

        self.assertEqual(getter(obj, "intValue"), 42)
        self.assertIsInstance(getter(obj, "intValue"), int)

        self.assertEqual(getter(obj, "floatValue"), -10.055)
        self.assertIsInstance(getter(obj, "floatValue"), float)

        self.assertEqual(getter(obj, "charValue"), ord("a"))
        self.assertIsInstance(getter(obj, "charValue"), int)

        self.assertEqual(getter(obj, "strValue"), b"hello world")
        self.assertIsInstance(getter(obj, "strValue"), bytes)

        self.assertIsInstance(getter(obj, "objValue"), NSObject)

        self.assertIsNone(getter(obj, "nilValue"))

        self.assertEqual(getter(obj, "pyValue"), slice(1, 10, 4))
        self.assertIsInstance(getter(obj, "pyValue"), slice)

        self.assertEqual(getter(obj, "rectValue"), ((1, 2), (3, 4)))

        with self.assertRaisesRegex(AttributeError, "noSuchMember"):
            getter(obj, "noSuchMember")

        with self.assertRaisesRegex(
            TypeError, "Expecting an Objective-C object, got instance of str"
        ):
            getter("value", "upper")

        with self.assertRaisesRegex(
            TypeError, r"function takes at most 2 arguments \(3 given\)"
        ):
            getter(obj, "value", 42)

        with self.assertRaisesRegex(TypeError, "argument 2 must be str, not int"):
            getter(obj, 42)

        with self.assertRaisesRegex(
            ValueError, "Getting instance variable of a nil object"
        ):
            getter(nilObject, "isa")

    def testWriting(self):
        obj = ClassWithVariables.alloc().init()

        getter = objc.getInstanceVariable
        setter = objc.setInstanceVariable

        self.assertEqual(getter(obj, "intValue"), 42)
        setter(obj, "intValue", 99)
        self.assertEqual(getter(obj, "intValue"), 99)

        self.assertEqual(getter(obj, "floatValue"), -10.055)
        setter(obj, "floatValue", 0.5)
        self.assertEqual(getter(obj, "floatValue"), 0.5)

        self.assertEqual(getter(obj, "charValue"), ord("a"))
        setter(obj, "charValue", b"b")
        self.assertEqual(getter(obj, "charValue"), ord("b"))
        setter(obj, "charValue", 10)
        self.assertEqual(getter(obj, "charValue"), 10)

        self.assertEqual(getter(obj, "strValue"), b"hello world")
        setter(obj, "strValue", b"foo bar")
        self.assertEqual(getter(obj, "strValue"), b"foo bar")
        setter(obj, "strValue", None)
        self.assertEqual(getter(obj, "strValue"), None)

        o = NSObject.new()
        self.assertIsNot(getter(obj, "objValue"), o)
        with self.assertRaisesRegex(
            TypeError,
            "Instance variable is an object, updateRefCounts argument is required",
        ):
            setter(obj, "objValue", o)

        self.assertIsNot(getter(obj, "objValue"), o)
        setter(obj, "objValue", o, True)
        self.assertIs(getter(obj, "objValue"), o)

        o2 = NSObject.new()
        o2.retain()
        self.assertIsNot(getter(obj, "objValue"), o2)
        setter(obj, "objValue", o2, False)
        self.assertIs(getter(obj, "objValue"), o2)

        class Fake:
            @property
            def __pyobjc_object__(self):
                raise TypeError("Cannot proxy")

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            setter(obj, "objValue", Fake(), True)
        self.assertIs(getter(obj, "objValue"), o2)

        self.assertEqual(getter(obj, "pyValue"), slice(1, 10, 4))
        setter(obj, "pyValue", [1, 2, 3])
        self.assertEqual(getter(obj, "pyValue"), [1, 2, 3])

        self.assertEqual(getter(obj, "rectValue"), ((1, 2), (3, 4)))
        setter(obj, "rectValue", ((-4, -8), (2, 7)))
        self.assertEqual(getter(obj, "rectValue"), ((-4, -8), (2, 7)))

        with self.assertRaisesRegex(AttributeError, "noSuchMember"):
            setter(obj, "noSuchMember", "foo")

        with self.assertRaisesRegex(
            TypeError, "Expecting an Objective-C object, got instance of str"
        ):
            setter("value", "upper", 1)

        with self.assertRaisesRegex(ValueError, "depythonifying 'Class', got 'int'"):
            setter(obj, "isa", 42)

        with self.assertRaisesRegex(
            TypeError, "depythonifying struct, got no sequence"
        ):
            setter(obj, "rectValue", 42)

        with self.assertRaisesRegex(
            TypeError,
            r"(function missing required argument 'name' \(pos 2\))|(Required argument 'name' \(pos 2\) not found)",
        ):
            setter(obj)

        with self.assertRaisesRegex(
            ValueError, "Setting instance variable of a nil object"
        ):
            setter(nilObject, "isa", NSObject)

    def testClassMod(self):
        # It's scary as hell, but updating the class of an object does "work"
        # (for some perverted interpretation of the word)

        class DummyClass(NSObject):
            __slots__ = ()

        o = NSObject.alloc().init()
        self.assertIsInstance(o, NSObject)
        self.assertNotIsInstance(o, DummyClass)

        objc.setInstanceVariable(o, "isa", DummyClass)
        self.assertIsInstance(o, DummyClass)

    def testDir(self):
        obj = ClassWithVariables.alloc().init()

        # Note: cannot check the exact contents of dir(), who knows
        # what NSObject defines...
        v = objc.listInstanceVariables(obj)
        self.assertIn(("charValue", objc._C_CHR), v)
        self.assertIn(("intValue", objc._C_INT), v)
        self.assertIn(("isa", objc._C_CLASS), v)

        with self.assertRaisesRegex(TypeError, "not an Objective-C class or object"):
            v = objc.listInstanceVariables(self)

        v = objc.listInstanceVariables(NSObject.alloc().init())
        self.assertIn(("isa", objc._C_CLASS), v)

        v = objc.listInstanceVariables(NSObject)
        self.assertIn(("isa", objc._C_CLASS), v)

        class PythonClassWithVariables(ClassWithVariables):
            extra = objc.ivar("extra", objc._C_FLT)

        obj = PythonClassWithVariables.alloc().init()
        v = objc.listInstanceVariables(obj)
        self.assertIn(("charValue", objc._C_CHR), v)
        self.assertIn(("intValue", objc._C_INT), v)
        self.assertIn(("extra", objc._C_FLT), v)
        self.assertIn(("isa", objc._C_CLASS), v)

    def testAnonymousIvar(self):
        class AnonIvarClass(NSObject):
            var = objc.ivar()
            var2 = objc.ivar(type=objc._C_DBL)

            outlet = objc.IBOutlet()
            self.assertTrue(outlet.__isOutlet__)
            self.assertFalse(outlet.__isSlot__)

        o = AnonIvarClass.alloc().init()
        o.var = NSObject.alloc().init()

        self.assertIsInstance(o.var, NSObject)

        o.var2 = 4
        self.assertIsInstance(o.var2, float)

    def testNamedOutlet(self):
        class NamedOutlet(NSObject):
            outlet1 = objc.IBOutlet()
            outlet2 = objc.IBOutlet("my_outlet")

        all_outlets = {}

        for name, tp in objc.listInstanceVariables(NamedOutlet):
            all_outlets[name] = tp

        self.assertEqual(all_outlets["outlet1"], objc._C_ID)
        self.assertEqual(all_outlets["my_outlet"], objc._C_ID)

        o = NamedOutlet.alloc().init()
        self.assertTrue(hasattr(o, "outlet1"))
        self.assertTrue(hasattr(o, "outlet2"))


class TestStructConvenience(TestCase):
    def test_using_convenience(self):
        for name, typestr in [
            ("bool", objc._C_BOOL),
            ("char", objc._C_CHR),
            ("int", objc._C_INT),
            ("short", objc._C_SHT),
            ("long", objc._C_LNG),
            ("long_long", objc._C_LNG_LNG),
            ("unsigned_char", objc._C_UCHR),
            ("unsigned_int", objc._C_UINT),
            ("unsigned_short", objc._C_USHT),
            ("unsigned_long", objc._C_ULNG),
            ("unsigned_long_long", objc._C_ULNG_LNG),
            ("float", objc._C_FLT),
            ("double", objc._C_DBL),
            ("BOOL", objc._C_NSBOOL),
            ("UniChar", objc._C_UNICHAR),
            ("char_text", objc._C_CHAR_AS_TEXT),
            ("char_int", objc._C_CHAR_AS_INT),
        ]:
            with self.subTest(name):
                self.assertHasAttr(objc.ivar, name)
                try:
                    v = getattr(objc.ivar, name)()
                except TypeError as exc:
                    print("XXX", exc, name, getattr(objc.ivar, name))
                    continue
                self.assertIsInstance(v, objc.ivar)
                self.assertEqual(v.__typestr__, typestr)
                self.assertEqual(v.__name__, None)
                self.assertFalse(v.__isOutlet__)
                self.assertFalse(v.__isSlot__)

                v = getattr(objc.ivar, name)("my_var")
                self.assertIsInstance(v, objc.ivar)
                self.assertEqual(v.__typestr__, typestr)
                self.assertEqual(v.__name__, "my_var")
                self.assertFalse(v.__isOutlet__)
                self.assertFalse(v.__isSlot__)
