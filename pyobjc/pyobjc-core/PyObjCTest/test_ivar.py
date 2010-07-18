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
        self.assertEquals(self.object.idVar, None)
        self.assertEquals(self.object.idVar2, None)

        o = NSObject.alloc().init()

        self.object.idVar = o
        self.object.idVar2 = o

        self.assertIs(self.object.idVar, o)
        self.assertIs(self.object.idVar2, o)

        self.object.idVar = u"hello"
        self.assertEquals(self.object.idVar, u"hello")

    def testInt(self):
        # Check that we can set and query attributes of type 'int'
        self.assertEquals(self.object.intVar, 0)

        self.assertRaises(ValueError, lambda x: setattr(self.object, 'intVar', x), "h")

        self.object.intVar = 42
        self.assertEquals(self.object.intVar, 42)

    def testDouble(self):
        # Check that we can set and query attributes of type 'double'

        # Can't rely on this for doubles...
        #self.assertEquals(self.object.doubleVar, 0.0)
        self.assertRaises(ValueError, lambda x: setattr(self.object, 'doubleVar', x), u"h")
        self.object.doubleVar = 42.0
        self.assertAlmostEquals(self.object.doubleVar, 42.0)

    def testLeak(self):
        # Check that plain python objects are correctly released when
        # they are no longer the value of an attribute
        pool = NSAutoreleasePool.alloc().init()
        self.deleted = 0
        self.object.idVar = Base(lambda : setattr(self, 'deleted', 1))
        self.object.idVar = None
        del pool
        self.assertEquals(self.deleted, 1)

    def testLeak2(self):

        self.deleted = 0

        pool = NSAutoreleasePool.alloc().init()

        self.object.idVar = Base(lambda : setattr(self, 'deleted', 1))
        del self.object
        del pool
        self.assertEquals(self.deleted, 1)

    def testOCLeak(self):
        # Check that Objective-C objects are correctly released when
        # they are no longer the value of an attribute
        pool = NSAutoreleasePool.alloc().init()
        self.deleted = 0
        self.object.idVar = OCBase.alloc().init_(lambda : setattr(self, 'deleted', 1))
        self.object.idVar = None
        del pool
        self.assertEquals(self.deleted, 1)

    def testOCLeak2(self):
        pool = NSAutoreleasePool.alloc().init()
        self.deleted = 0
        self.object.idVar = OCBase.alloc().init_(lambda : setattr(self, 'deleted', 1))
        del self.object
        del pool
        self.assertEquals(self.deleted, 1)

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

        self.assertEquals(getter(obj, 'intValue'), 42)
        self.assertIsInstance(getter(obj, 'intValue'), int)

        self.assertEquals(getter(obj, 'floatValue'), -10.055)
        self.assertIsInstance(getter(obj, 'floatValue'), float)

        self.assertEquals(getter(obj, 'charValue'), ord('a'))
        self.assertIsInstance(getter(obj, 'charValue'), int)

        self.assertEquals(getter(obj, 'strValue'), b"hello world")
        self.assertIsInstance(getter(obj, 'strValue'), bytes)

        self.assertIsInstance(getter(obj, 'objValue'), NSObject)

        self.assertIsNone(getter(obj, 'nilValue'))

        self.assertEquals(getter(obj, 'pyValue'), slice(1, 10, 4))
        self.assertIsInstance(getter(obj, 'pyValue'), slice)

        self.assertEquals(getter(obj, 'rectValue'), ((1, 2), (3, 4)))

        self.assertRaises(AttributeError, getter, obj, "noSuchMember")

    def testWriting(self):
        obj = ClassWithVariables.alloc().init()

        getter = objc.getInstanceVariable
        setter = objc.setInstanceVariable

        self.assertEquals(getter(obj, 'intValue'), 42)
        setter(obj, 'intValue', 99)
        self.assertEquals(getter(obj, 'intValue'), 99)

        self.assertEquals(getter(obj, 'floatValue'), -10.055)
        setter(obj, 'floatValue', 0.5)
        self.assertEquals(getter(obj, 'floatValue'), 0.5)

        self.assertEquals(getter(obj, 'charValue'), ord('a'))
        setter(obj, 'charValue', b'b')
        self.assertEquals(getter(obj, 'charValue'), ord('b'))
        setter(obj, 'charValue', 10)
        self.assertEquals(getter(obj, 'charValue'), 10)

        self.assertEquals(getter(obj, 'strValue'), b"hello world")
        setter(obj, 'strValue', b"foo bar")
        self.assertEquals(getter(obj, 'strValue'), b"foo bar")
        setter(obj, 'strValue', None)
        self.assertEquals(getter(obj, 'strValue'), None)

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

        self.assertEquals(getter(obj, 'pyValue'), slice(1, 10, 4))
        setter(obj, 'pyValue', [1,2,3])
        self.assertEquals(getter(obj, 'pyValue'), [1,2,3])

        self.assertEquals(getter(obj, 'rectValue'), ((1, 2), (3, 4)))
        setter(obj, 'rectValue', ((-4, -8), (2, 7)))
        self.assertEquals(getter(obj, 'rectValue'), ((-4, -8), (2, 7)))

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

        o = AnonIvarClass.alloc().init()
        o.var = NSObject.alloc().init()

        self.assertIsInstance(o.var, NSObject)
    
        o.var2 = 4
        self.assertIsInstance(o.var2, float)
    

if __name__ == '__main__':
    main()
