"""
Test lowlevel message passing details (Python -> ObjC)

Note: See also testbndl.m, the implementation there must be synchronized with
this file.

Done:
- Return simple values, but need to add limit-cases (exactly INT_MAX et.al.)
- Return structs, but need to add more complex cases
- Pass in basic types

Todo:
- Pass in struct types
- Pass by reference of basic types (in, out, inout)
- Pass by reference of struct types (in, out, inout)
- more than 1 argument

Also Todo: Passing from Objective-C to python
- Using NSInvocation '[obj forwardInvocation:inv]'
- Using normal calls

NOTES:
- Always use makeCFloat when testing the value of a C float against a 
  precomputed (literal) value. Just comparing against a Python float won't work
  as that is a C double which has a different representation from C floats 
  resulting in spurious test failures.
"""
import unittest
import objc
import sys
import struct

# This should be an extension module (basicly an empty module that happens
# to define objective-C classes), that should allow for using distutils to
# build the extension module and removes the need for an absolute path.
from objc.test.testbndl import *

def makeCFloat(value):
    """
    C floats and doubles have a different representation, this function returns
    the result of converting a python float (== C double) to a C float and back.
    """
    return struct.unpack('f',struct.pack('f', value))[0]

class TestSimpleReturns(unittest.TestCase):
    #
    # Test returns of simple types from instance and classs methods
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
        self.assertEquals(OC_TestClass1.floatClsFunc(), makeCFloat(0.128))
        self.assertEquals(OC_TestClass1.floatClsFunc(), makeCFloat(1.0))
        self.assertEquals(OC_TestClass1.floatClsFunc(), makeCFloat(42.0))
        self.assertEquals(OC_TestClass1.floatClsFunc(), makeCFloat(1e10))

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
        self.assertEquals(obj.floatFunc(), makeCFloat(0.128))
        self.assertEquals(obj.floatFunc(), makeCFloat(1.0))
        self.assertEquals(obj.floatFunc(), makeCFloat(42.0))
        self.assertEquals(obj.floatFunc(), makeCFloat(1e10))

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


class TestSimpleArguments(unittest.TestCase):
    #
    # Test argument passing of single basic values.
    #
    def testLongLong(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.longlongArg_(0), 0)
        self.assertEquals(obj.longlongArg_(10), 5)
        self.assertEquals(obj.longlongArg_(10L), 5)
        self.assertEquals(obj.longlongArg_(1L << 60), (1L << 59))
        self.assertEquals(obj.longlongArg_(-10), -5)
        self.assertEquals(obj.longlongArg_(-10L), -5)
        self.assertEquals(obj.longlongArg_(-1L << 60), -(1L << 59))

    def testULongLong(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.ulonglongArg_(0), 0)
        self.assertEquals(obj.ulonglongArg_(10), 5)
        self.assertEquals(obj.ulonglongArg_(10L), 5)
        self.assertEquals(obj.ulonglongArg_(1L << 60), (1L << 59))

    def testLong(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.longArg_(0), 0)
        self.assertEquals(obj.longArg_(10), 5)
        self.assertEquals(obj.longArg_(10L), 5)
        self.assertEquals(obj.longArg_(1 << 30), (1 << 29))
        self.assertEquals(obj.longArg_(-10), -5)
        self.assertEquals(obj.longArg_(-10L), -5)
        self.assertEquals(obj.longArg_(-1 << 30), -(1 << 29))

    def testULong(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.ulongArg_(0), 0)
        self.assertEquals(obj.ulongArg_(10), 5)
        self.assertEquals(obj.ulongArg_(10L), 5)
        self.assertEquals(obj.ulongArg_(1 << 30), (1 << 29))

    def testInt(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.intArg_(0), 0)
        self.assertEquals(obj.intArg_(10), 5)
        self.assertEquals(obj.intArg_(10L), 5)
        self.assertEquals(obj.intArg_(1 << 30), (1 << 29))
        self.assertEquals(obj.intArg_(-10), -5)
        self.assertEquals(obj.intArg_(-10L), -5)
        self.assertEquals(obj.intArg_(-1 << 30), -(1 << 29))

        self.assertRaises(objc.error, obj.intArg_, long(sys.maxint)+1)
        self.assertRaises(objc.error, obj.intArg_, -long(sys.maxint)-2)

    def testUInt(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.uintArg_(0), 0)
        self.assertEquals(obj.uintArg_(10), 5)
        self.assertEquals(obj.uintArg_(10L), 5)
        self.assertEquals(obj.uintArg_(1 << 30), (1 << 29))

        self.assertRaises(objc.error, obj.uintArg_, -5)
        self.assertRaises(objc.error, obj.uintArg_, -5L)
        self.assertRaises(objc.error, obj.uintArg_, 1+2*(long(sys.maxint)+1))


    def testShort(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.shortArg_(0), 0)
        self.assertEquals(obj.shortArg_(10), 5)
        self.assertEquals(obj.shortArg_(10L), 5)
        self.assertEquals(obj.shortArg_(1 << 14), (1 << 13))
        self.assertEquals(obj.shortArg_(-10), -5)
        self.assertEquals(obj.shortArg_(-10L), -5)
        self.assertEquals(obj.shortArg_(-(1 << 14)), -(1 << 13))

        # Out of range arguments, assumes a short is 16 bits
        self.assertRaises(objc.error, obj.shortArg_, -(1<<16)-1)
        self.assertRaises(objc.error, obj.shortArg_, 1<<16)
        self.assertRaises(objc.error, obj.shortArg_, -(1L<<16)-1)
        self.assertRaises(objc.error, obj.shortArg_, 1L<<16)

    def testUShort(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.ushortArg_(0), 0)
        self.assertEquals(obj.ushortArg_(10), 5)
        self.assertEquals(obj.ushortArg_(10L), 5)
        self.assertEquals(obj.ushortArg_(1 << 14), (1 << 13))

        # Out of range arguments, assumes a short is 16 bits
        self.assertRaises(objc.error, obj.ushortArg_, -5)
        self.assertRaises(objc.error, obj.ushortArg_, -(1<<16)-1)
        self.assertRaises(objc.error, obj.ushortArg_, 1<<16)
        self.assertRaises(objc.error, obj.ushortArg_, -5L)
        self.assertRaises(objc.error, obj.ushortArg_, -(1L<<16)-1)
        self.assertRaises(objc.error, obj.ushortArg_, 1L<<16)


    def testChar(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.charArg_(0), chr(0))
        self.assertEquals(obj.charArg_(10), chr(5))
        self.assertEquals(obj.charArg_(10L), chr(5))
        self.assertEquals(obj.charArg_(1 << 6), chr(1 << 5))
        self.assertEquals(obj.ucharArg_('\x00'), '\x00')
        self.assertEquals(obj.ucharArg_('\x10'), chr(ord('\x10')/2))

        # TODO: Out of range arguments

    def testUChar(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.ucharArg_(0), 0)
        self.assertEquals(obj.ucharArg_(10), 5)
        self.assertEquals(obj.ucharArg_(10L), 5)
        self.assertEquals(obj.ucharArg_(1 << 7), (1 << 6))
        self.assertEquals(obj.ucharArg_('\x00'), 0)
        self.assertEquals(obj.ucharArg_('\x10'), ord('\x10')/2)

        # Out of range arguments
        self.assertRaises(objc.error, obj.ucharArg_, -5)
        self.assertRaises(objc.error, obj.ucharArg_, -256)
        self.assertRaises(objc.error, obj.ucharArg_, 256)
        self.assertRaises(objc.error, obj.ucharArg_, -5L)
        self.assertRaises(objc.error, obj.ucharArg_, -256L)
        self.assertRaises(objc.error, obj.ucharArg_, 256L)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSimpleCalls))
    suite.addTest(unittest.makeSuite(TestSimpleArguments))
    return suite

if __name__ == '__main__':
    unittest.main()
