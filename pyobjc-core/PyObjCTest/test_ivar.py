from __future__ import unicode_literals
from PyObjCTools.TestSupport import *

import objc
import sys
from PyObjCTest.instanceVariables import ClassWithVariables

NSObject = objc.lookUpClass('NSObject')
NSAutoreleasePool = objc.lookUpClass('NSAutoreleasePool')

class Base (object):
    def __init__(self, ondel):
        self.ondel = ondel

    def __del__ (self):
        self.ondel()

class OCBase (NSObject):
    def init_(self, ondel):
        self.ondel = ondel

    def __del__ (self):
        self.ondel()

class TestClass (NSObject):
    idVar = objc.ivar('idVar')
    idVar2 = objc.ivar('idVar2', b'@')
    intVar = objc.ivar('intVar', objc._C_INT)
    doubleVar = objc.ivar('doubleVar', objc._C_DBL)


class TestInstanceVariables(TestCase):
    def setUp(self):
        self.object = TestClass.alloc().init()

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

        self.assertRaises(ValueError, lambda x: setattr(self.object, 'intVar', x), "h")

        self.object.intVar = 42
        self.assertEqual(self.object.intVar, 42)

    def testDouble(self):
        # Check that we can set and query attributes of type 'double'

        # Can't rely on this for doubles...
        #self.assertEqual(self.object.doubleVar, 0.0)
        self.assertRaises(ValueError, lambda x: setattr(self.object, 'doubleVar', x), "h")
        self.object.doubleVar = 42.0
        self.assertAlmostEqual(self.object.doubleVar, 42.0)

    def testLeak(self):
        # Check that plain python objects are correctly released when
        # they are no longer the value of an attribute
        pool = NSAutoreleasePool.alloc().init()
        self.deleted = 0
        self.object.idVar = Base(lambda : setattr(self, 'deleted', 1))
        self.object.idVar = None
        del pool
        self.assertEqual(self.deleted, 1)

    def testLeak2(self):

        self.deleted = 0

        pool = NSAutoreleasePool.alloc().init()

        self.object.idVar = Base(lambda : setattr(self, 'deleted', 1))
        del self.object
        del pool
        self.assertEqual(self.deleted, 1)

    def testOCLeak(self):
        # Check that Objective-C objects are correctly released when
        # they are no longer the value of an attribute
        pool = NSAutoreleasePool.alloc().init()
        self.deleted = 0
        self.object.idVar = OCBase.alloc().init_(lambda : setattr(self, 'deleted', 1))
        self.object.idVar = None
        del pool
        self.assertEqual(self.deleted, 1)

    def testOCLeak2(self):
        pool = NSAutoreleasePool.alloc().init()
        self.deleted = 0
        self.object.idVar = OCBase.alloc().init_(lambda : setattr(self, 'deleted', 1))
        del self.object
        del pool
        self.assertEqual(self.deleted, 1)

    def testDelete(self):
        self.assertRaises(TypeError, delattr, self.object.idVar)


class TestAllInstanceVariables (TestCase):
    # Some tests for accessing any instance variable, even those not
    # declared in python.

    def testReading(self):
        obj = ClassWithVariables.alloc().init()

        getter = objc.getInstanceVariable

        cls = getter(obj, 'isa')
        self.assertIs(cls, type(obj))

        self.assertEqual(getter(obj, 'intValue'), 42)
        self.assertIsInstance(getter(obj, 'intValue'), int)

        self.assertEqual(getter(obj, 'floatValue'), -10.055)
        self.assertIsInstance(getter(obj, 'floatValue'), float)

        self.assertEqual(getter(obj, 'charValue'), ord('a'))
        self.assertIsInstance(getter(obj, 'charValue'), int)

        self.assertEqual(getter(obj, 'strValue'), b"hello world")
        self.assertIsInstance(getter(obj, 'strValue'), bytes)

        self.assertIsInstance(getter(obj, 'objValue'), NSObject)

        self.assertIsNone(getter(obj, 'nilValue'))

        self.assertEqual(getter(obj, 'pyValue'), slice(1, 10, 4))
        self.assertIsInstance(getter(obj, 'pyValue'), slice)

        self.assertEqual(getter(obj, 'rectValue'), ((1, 2), (3, 4)))

        self.assertRaises(AttributeError, getter, obj, "noSuchMember")

    def testWriting(self):
        obj = ClassWithVariables.alloc().init()

        getter = objc.getInstanceVariable
        setter = objc.setInstanceVariable

        self.assertEqual(getter(obj, 'intValue'), 42)
        setter(obj, 'intValue', 99)
        self.assertEqual(getter(obj, 'intValue'), 99)

        self.assertEqual(getter(obj, 'floatValue'), -10.055)
        setter(obj, 'floatValue', 0.5)
        self.assertEqual(getter(obj, 'floatValue'), 0.5)

        self.assertEqual(getter(obj, 'charValue'), ord('a'))
        setter(obj, 'charValue', b'b')
        self.assertEqual(getter(obj, 'charValue'), ord('b'))
        setter(obj, 'charValue', 10)
        self.assertEqual(getter(obj, 'charValue'), 10)

        self.assertEqual(getter(obj, 'strValue'), b"hello world")
        setter(obj, 'strValue', b"foo bar")
        self.assertEqual(getter(obj, 'strValue'), b"foo bar")
        setter(obj, 'strValue', None)
        self.assertEqual(getter(obj, 'strValue'), None)

        o = NSObject.new()
        self.assertIsNot(getter(obj, 'objValue'), o)
        self.assertRaises(TypeError, setter, 'objValue', o)
        self.assertIsNot(getter(obj, 'objValue'), o)
        setter(obj, 'objValue', o, True)
        self.assertIs(getter(obj, 'objValue'), o)

        o2 = NSObject.new()
        o2.retain()
        self.assertIsNot(getter(obj, 'objValue'), o2)
        setter(obj, 'objValue', o2, False)
        self.assertIs(getter(obj, 'objValue'), o2)

        self.assertEqual(getter(obj, 'pyValue'), slice(1, 10, 4))
        setter(obj, 'pyValue', [1,2,3])
        self.assertEqual(getter(obj, 'pyValue'), [1,2,3])

        self.assertEqual(getter(obj, 'rectValue'), ((1, 2), (3, 4)))
        setter(obj, 'rectValue', ((-4, -8), (2, 7)))
        self.assertEqual(getter(obj, 'rectValue'), ((-4, -8), (2, 7)))

        self.assertRaises(AttributeError, setter, obj, "noSuchMember", 'foo')

    def testClassMod(self):
        # It's scary as hell, but updating the class of an object does "work"
        # (for some perverted interpretation of the word)

        class DummyClass (NSObject):
            __slots__ = ()

        o = NSObject.alloc().init()
        self.assertIsInstance(o, NSObject)
        self.assertIsNotInstance(o, DummyClass)

        objc.setInstanceVariable(o, "isa", DummyClass)
        self.assertIsInstance(o, DummyClass)

    def testDir(self):
        obj = ClassWithVariables.alloc().init()

        # Note: cannot check the exact contents of dir(), who knows
        # what NSObject defines...
        v = objc.listInstanceVariables(obj)
        self.assertIn(('charValue', objc._C_CHR), v)
        self.assertIn(('intValue', objc._C_INT), v)
        self.assertIn(('isa', objc._C_CLASS), v)


    def testAnonymousIvar(self):

        class AnonIvarClass (NSObject):

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
        class NamedOutlet (NSObject):
            outlet1 = objc.IBOutlet()
            outlet2 = objc.IBOutlet("my_outlet")

        all_outlets = {}

        for name, tp in objc.listInstanceVariables(NamedOutlet):
            all_outlets[name] = tp

        self.assertEqual(all_outlets['outlet1'], objc._C_ID)
        self.assertEqual(all_outlets['my_outlet'], objc._C_ID)

        o = NamedOutlet.alloc().init()
        self.assertTrue(hasattr(o, 'outlet1'))
        self.assertTrue(hasattr(o, 'outlet2'))

class TestStructConvenience (TestCase):
    def test_using_convenience(self):
        for name, typestr in [
                ('bool', objc._C_BOOL),
                ('char', objc._C_CHR),
                ('int', objc._C_INT),
                ('short', objc._C_SHT),
                ('long', objc._C_LNG),
                ('long_long', objc._C_LNG_LNG),
                ('unsigned_char', objc._C_UCHR),
                ('unsigned_int', objc._C_UINT),
                ('unsigned_short', objc._C_USHT),
                ('unsigned_long', objc._C_ULNG),
                ('unsigned_long_long', objc._C_ULNG_LNG),
                ('float', objc._C_FLT),
                ('double', objc._C_DBL),
                ('BOOL', objc._C_NSBOOL),
                ('UniChar', objc._C_UNICHAR),
                ('char_text', objc._C_CHAR_AS_TEXT),
                ('char_int', objc._C_CHAR_AS_INT),
            ]:
            self.assertHasAttr(objc.ivar, name)
            v = getattr(objc.ivar, name)()
            self.assertIsInstance(v, objc.ivar)
            self.assertEqual(v.__typestr__, typestr)
            self.assertEqual(v.__name__, None)
            self.assertFalse(v.__isOutlet__)
            self.assertFalse(v.__isSlot__)

            v = getattr(objc.ivar, name)('my_var')
            self.assertIsInstance(v, objc.ivar)
            self.assertEqual(v.__typestr__, typestr)
            self.assertEqual(v.__name__, 'my_var')
            self.assertFalse(v.__isOutlet__)
            self.assertFalse(v.__isSlot__)

if __name__ == '__main__':
    main()
