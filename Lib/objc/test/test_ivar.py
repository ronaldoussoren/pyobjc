import unittest

import objc
import sys

NSObject = objc.lookUpClass('NSObject')

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
    idVar2 = objc.ivar('idVar2', '@')
    intVar = objc.ivar('intVar', objc._C_INT)
    doubleVar = objc.ivar('doubleVar', objc._C_DBL)

class TestInstanceVariables(unittest.TestCase):
    if not hasattr(unittest.TestCase, 'assertAlmostEquals'):
        def assertAlmostEquals(self, val1, val2):
            self.assert_(abs(val1 - val2) < 0.000001)

    def setUp(self):
        self.object = TestClass.alloc().init()

    def testID(self):
        # Check that we can set and query attributes of type 'id'
        self.assertEquals(self.object.idVar, None)
        self.assertEquals(self.object.idVar2, None)

        o = NSObject.alloc().init()

        self.object.idVar = o
        self.object.idVar2 = o

        self.failUnless(self.object.idVar is o)
        self.failUnless(self.object.idVar2 is o)

        self.object.idVar = "hello"
        self.assertEquals(self.object.idVar, "hello")

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
        self.assertRaises(ValueError, lambda x: setattr(self.object, 'doubleVar', x), "h")
        self.object.doubleVar = 42.0
        self.assertAlmostEquals(self.object.doubleVar, 42.0)

    def testLeak(self):
        # Check that plain python objects are correctly released when
        # they are no longer the value of an attribute
        self.deleted = 0
        self.object.idVar = Base(lambda : setattr(self, 'deleted', 1))
        self.object.idVar = None
        objc.recycleAutoreleasePool()
        self.assertEquals(self.deleted, 1)

    def testLeak2(self):
        self.deleted = 0
        self.object.idVar = Base(lambda : setattr(self, 'deleted', 1))
        del self.object
        objc.recycleAutoreleasePool()
        self.assertEquals(self.deleted, 1)

    def testOCLeak(self):
        # Check that Objective-C objects are correctly released when
        # they are no longer the value of an attribute
        self.deleted = 0
        self.object.idVar = OCBase.alloc().init_(lambda : setattr(self, 'deleted', 1))
        self.object.idVar = None
        objc.recycleAutoreleasePool()
        self.assertEquals(self.deleted, 1)

    def testOCLeak2(self):
        self.deleted = 0
        self.object.idVar = OCBase.alloc().init_(lambda : setattr(self, 'deleted', 1))
        del self.object
        objc.recycleAutoreleasePool()
        self.assertEquals(self.deleted, 1)

    def testDelete(self):
        self.assertRaises(TypeError, delattr, self.object.idVar)

if __name__ == '__main__':
    unittest.main()
