"""
Test lowlevel message passing details (Python -> ObjC)

Note: See also testbndl.m, the implementation there must be synchronized with
this file.

Done:
- Return simple values

Todo:
- Return structs
- Pass in basic types
- Pass in struct types
- Pass by reference of basic types (in, out, inout)
- Pass by reference of struct types (in, out, inout)
- 0, 1, 4 arguments

Also Todo: Passing from Objective-C to python
- Using NSInvocation '[obj forwardInvocation:inv]'
- Using normal calls
"""
import unittest
import objc

# This should be an extension module (basicly an empty module that happens
# to define objective-C classes), that should allow for using distutils to
# build the extension module and removes the need for an absolute path.
from objc.test.testbndl import *

print OC_TestClass1.new().dummyFunc()

class TestSimpleReturns(unittest.TestCase):
    #
    # Test returns of basic types from instance and classs methods
    #
    def testClsLongLong(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.longlongClsFunc(), -(1L << 60))
        self.assertEquals(OC_TestClass1.longlongClsFunc(), -42)
        self.assertEquals(OC_TestClass1.longlongClsFunc(), 0)
        self.assertEquals(OC_TestClass1.longlongClsFunc(), 42)
        self.assertEquals(OC_TestClass1.longlongClsFunc(), (1L << 60))

    def testClsULongLong(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.ulonglongClsFunc(), 0)
        self.assertEquals(OC_TestClass1.ulonglongClsFunc(), 42)
        self.assertEquals(OC_TestClass1.ulonglongClsFunc(), (1L << 63))

    def testClsLong(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.longClsFunc(), -(1 << 30))
        self.assertEquals(OC_TestClass1.longClsFunc(), -42)
        self.assertEquals(OC_TestClass1.longClsFunc(), 0)
        self.assertEquals(OC_TestClass1.longClsFunc(), 42)
        self.assertEquals(OC_TestClass1.longClsFunc(), (1 << 30))

    def testClsULong(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.ulongClsFunc(), 0)
        self.assertEquals(OC_TestClass1.ulongClsFunc(), 42)
        self.assertEquals(OC_TestClass1.ulongClsFunc(), (1 << 30))

    def testClsInt(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.intClsFunc(), -(1 << 30))
        self.assertEquals(OC_TestClass1.intClsFunc(), -42)
        self.assertEquals(OC_TestClass1.intClsFunc(), 0)
        self.assertEquals(OC_TestClass1.intClsFunc(), 42)
        self.assertEquals(OC_TestClass1.intClsFunc(), (1 << 30))

    def testClsUInt(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.uintClsFunc(), 0)
        self.assertEquals(OC_TestClass1.uintClsFunc(), 42)
        self.assertEquals(OC_TestClass1.uintClsFunc(), (1 << 30))

    def testClsShort(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.shortClsFunc(), -(1 << 14))
        self.assertEquals(OC_TestClass1.shortClsFunc(), -42)
        self.assertEquals(OC_TestClass1.shortClsFunc(), 0)
        self.assertEquals(OC_TestClass1.shortClsFunc(), 42)
        self.assertEquals(OC_TestClass1.shortClsFunc(), (1 << 14))

    def testClsUShort(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.ushortClsFunc(), 0)
        self.assertEquals(OC_TestClass1.ushortClsFunc(), 42)
        self.assertEquals(OC_TestClass1.ushortClsFunc(), (1 << 14))

    def testClsChar(self):
        # Fails with libffi due to the way we treat 'char' at the moment
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.charClsFunc(), '\x10')
        self.assertEquals(OC_TestClass1.charClsFunc(), '\x00')
        self.assertEquals(OC_TestClass1.charClsFunc(), '\xef')

    def testClsUChar(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.ucharClsFunc(), 0)
        self.assertEquals(OC_TestClass1.ucharClsFunc(), 128)
        self.assertEquals(OC_TestClass1.ucharClsFunc(), 255)

    def testClsFloat(self):
        # Fails, possibly rounding error
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.floatClsFunc(), 0.128)
        self.assertEquals(OC_TestClass1.floatClsFunc(), 1.0)
        self.assertEquals(OC_TestClass1.floatClsFunc(), 42.0)
        self.assertEquals(OC_TestClass1.floatClsFunc(), 1e10)

    def testClsDouble(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.doubleClsFunc(), 0.128)
        self.assertEquals(OC_TestClass1.doubleClsFunc(), 1.0)
        self.assertEquals(OC_TestClass1.doubleClsFunc(), 42.0)
        self.assertEquals(OC_TestClass1.doubleClsFunc(), 1e10)

    def testLongLong(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.longlongFunc(), -(1L << 60))
        self.assertEquals(obj.longlongFunc(), -42)
        self.assertEquals(obj.longlongFunc(), 0)
        self.assertEquals(obj.longlongFunc(), 42)
        self.assertEquals(obj.longlongFunc(), (1L << 60))

    def testULongLong(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.ulonglongFunc(), 0)
        self.assertEquals(obj.ulonglongFunc(), 42)
        self.assertEquals(obj.ulonglongFunc(), (1L << 63))

    def testLong(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.longFunc(), -(1 << 30))
        self.assertEquals(obj.longFunc(), -42)
        self.assertEquals(obj.longFunc(), 0)
        self.assertEquals(obj.longFunc(), 42)
        self.assertEquals(obj.longFunc(), (1 << 30))

    def testULong(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.ulongFunc(), 0)
        self.assertEquals(obj.ulongFunc(), 42)
        self.assertEquals(obj.ulongFunc(), (1 << 30))

    def testInt(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.intFunc(), -(1 << 30))
        self.assertEquals(obj.intFunc(), -42)
        self.assertEquals(obj.intFunc(), 0)
        self.assertEquals(obj.intFunc(), 42)
        self.assertEquals(obj.intFunc(), (1 << 30))

    def testUInt(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.uintFunc(), 0)
        self.assertEquals(obj.uintFunc(), 42)
        self.assertEquals(obj.uintFunc(), (1 << 30))

    def testShort(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.shortFunc(), -(1 << 14))
        self.assertEquals(obj.shortFunc(), -42)
        self.assertEquals(obj.shortFunc(), 0)
        self.assertEquals(obj.shortFunc(), 42)
        self.assertEquals(obj.shortFunc(), (1 << 14))

    def testUShort(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.ushortFunc(), 0)
        self.assertEquals(obj.ushortFunc(), 42)
        self.assertEquals(obj.ushortFunc(), (1 << 14))

    def testChar(self):
        obj = OC_TestClass1.new()
        # Fails with libffi due to the way we treat 'char' at the moment
        obj.reset()
        self.assertEquals(obj.charFunc(), '\x10')
        self.assertEquals(obj.charFunc(), '\x00')
        self.assertEquals(obj.charFunc(), '\xef')

    def testUChar(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.ucharFunc(), 0)
        self.assertEquals(obj.ucharFunc(), 128)
        self.assertEquals(obj.ucharFunc(), 255)

    def testFloat(self):
        # Fails, possibly rounding error
        obj = OC_TestClass1.new()
        obj.clsReset()
        self.assertEquals(obj.floatFunc(), 0.128)
        self.assertEquals(obj.floatFunc(), 1.0)
        self.assertEquals(obj.floatFunc(), 42.0)
        self.assertEquals(obj.floatFunc(), 1e10)

    def testDouble(self):
        obj = OC_TestClass1.new()
        obj.clsReset()
        self.assertEquals(obj.doubleFunc(), 0.128)
        self.assertEquals(obj.doubleFunc(), 1.0)
        self.assertEquals(obj.doubleFunc(), 42.0)
        self.assertEquals(obj.doubleFunc(), 1e10)

    def testStruct1(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.dummyFunc(), (-1, 1))

    def testStruct2(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.dummy2Func(), ((1,2,3,4),))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSimpleCalls))
    return suite

if __name__ == '__main__':
    unittest.main()
