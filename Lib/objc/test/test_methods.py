"""
Test lowlevel message passing details (Python -> ObjC)


Done:
- Return simple values, but need to add limit-cases (exactly INT_MAX et.al.)
- Return structs, but need to add more complex cases
- Pass in basic types
- Pass in struct types, but need to add more complex cases
- Pass by reference of basic types (in, out, inout)
  [Need to add python side of case 'id']

Todo:
- Pass by reference of struct types (in, out, inout)
- more than 1 argument
- More argument conversions

Also Todo: Passing from Objective-C to python
- Using NSInvocation '[obj forwardInvocation:inv]'
- Using normal calls

NOTES:
- Always use makeCFloat when testing the value of a C float against a 
  precomputed (literal) value. Just comparing against a Python float won't work
  as that is a C double which has a different representation from C floats 
  resulting in spurious test failures.
- See also testbndl.m, the implementation there must be synchronized 
  with this file.
"""
import unittest
import objc
import sys
import struct

# Can't set the right signatures in plain Objective-C.
set_signature = objc.set_signature_for_selector
set_signature("OC_TestClass1", "passInOutChar:", "v@:N^c")
set_signature("OC_TestClass1", "passOutChar:", "v@:o^c")
set_signature("OC_TestClass1", "passInChar:", "c@:n^c")
set_signature("OC_TestClass1", "passInOutUChar:", "v@:N^C")
set_signature("OC_TestClass1", "passOutUChar:", "v@:o^C")
set_signature("OC_TestClass1", "passInUChar:", "I@:n^C")
set_signature("OC_TestClass1", "passInOutShort:", "v@:N^s")
set_signature("OC_TestClass1", "passOutShort:", "v@:o^s")
set_signature("OC_TestClass1", "passInShort:", "i@:n^s")
set_signature("OC_TestClass1", "passInOutUShort:", "v@:N^S")
set_signature("OC_TestClass1", "passOutUShort:", "v@:o^S")
set_signature("OC_TestClass1", "passInUShort:", "I@:n^S")
set_signature("OC_TestClass1", "passInOutInt:", "v@:N^i")
set_signature("OC_TestClass1", "passOutInt:", "v@:o^i")
set_signature("OC_TestClass1", "passInInt:", "i@:n^i")
set_signature("OC_TestClass1", "passInOutUInt:", "v@:N^I")
set_signature("OC_TestClass1", "passOutUInt:", "v@:o^I")
set_signature("OC_TestClass1", "passInUInt:", "I@:n^I")
set_signature("OC_TestClass1", "passInOutLong:", "v@:N^l")
set_signature("OC_TestClass1", "passOutLong:", "v@:o^l")
set_signature("OC_TestClass1", "passInLong:", "l@:n^l")
set_signature("OC_TestClass1", "passInOutULong:", "v@:N^L")
set_signature("OC_TestClass1", "passOutULong:", "v@:o^L")
set_signature("OC_TestClass1", "passInULong:", "L@:n^L")
set_signature("OC_TestClass1", "passInOutLongLong:", "v@:N^q")
set_signature("OC_TestClass1", "passOutLongLong:", "v@:o^q")
set_signature("OC_TestClass1", "passInLongLong:", "q@:n^q")
set_signature("OC_TestClass1", "passInOutULongLong:", "v@:N^Q")
set_signature("OC_TestClass1", "passOutULongLong:", "v@:o^Q")
set_signature("OC_TestClass1", "passInULongLong:", "Q@:n^Q")
set_signature("OC_TestClass1", "passInOutFloat:", "v@:N^f")
set_signature("OC_TestClass1", "passOutFloat:", "v@:o^f")
set_signature("OC_TestClass1", "passInFloat:", "f@:n^f")
set_signature("OC_TestClass1", "passInOutDouble:", "v@:N^d")
set_signature("OC_TestClass1", "passOutDouble:", "v@:o^d")
set_signature("OC_TestClass1", "passInDouble:", "d@:n^d")
set_signature("OC_TestClass1", "passInOutCharp:", "v@:N^*")
set_signature("OC_TestClass1", "passOutCharp:", "v@:o^*")
set_signature("OC_TestClass1", "passInCharp:", "*@:n^*")
set_signature("OC_TestClass1", "passInOutID:", "v@:N^@")
set_signature("OC_TestClass1", "passOutID:", "v@:o^@")
set_signature("OC_TestClass1", "passInID:", "@@:n^@")

from objc.test.testbndl import *

def makeCFloat(value):
    """
    C floats and doubles have a different representation, this function returns
    the result of converting a python float (== C double) to a C float and back.
    """
    return struct.unpack('f',struct.pack('f', value))[0]

class TestTypeStr(unittest.TestCase):
    # 
    # Check that typestrings have the expected values. 
    # We currently depend on these values in this file as wel as in the 
    # modules that set method signatures to 'better' values.
    #
    def testAll(self):

        self.assertEquals(objc._C_ID, "@")
        self.assertEquals(objc._C_CLASS, "#")
        self.assertEquals(objc._C_SEL, ":")
        self.assertEquals(objc._C_CHR, "c")
        self.assertEquals(objc._C_UCHR, "C")
        self.assertEquals(objc._C_SHT, "s")
        self.assertEquals(objc._C_USHT, "S")
        self.assertEquals(objc._C_INT, "i")
        self.assertEquals(objc._C_UINT, "I")
        self.assertEquals(objc._C_LNG, "l")
        self.assertEquals(objc._C_ULNG, "L")
        self.assertEquals(objc._C_LNGLNG, "q")
        self.assertEquals(objc._C_ULNGLNG, "Q")
        self.assertEquals(objc._C_FLT, "f")
        self.assertEquals(objc._C_DBL, "d")
        self.assertEquals(objc._C_VOID, "v")
        self.assertEquals(objc._C_CHARPTR, "*")
        self.assertEquals(objc._C_PTR, "^")
        self.assertEquals(objc._C_UNDEF, "?")
        self.assertEquals(objc._C_ARY_B, "[")
        self.assertEquals(objc._C_ARY_E, "]")
        self.assertEquals(objc._C_UNION_B, "(")
        self.assertEquals(objc._C_UNION_E, ")")
        self.assertEquals(objc._C_STRUCT_B, "{")
        self.assertEquals(objc._C_STRUCT_E, "}")
        self.assertEquals(objc._C_IN, "n")
        self.assertEquals(objc._C_OUT, "o")
        self.assertEquals(objc._C_INOUT, "N")

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
        self.assertEquals(OC_TestClass1.charClsFunc(), -128)
        self.assertEquals(OC_TestClass1.charClsFunc(), 0)
        self.assertEquals(OC_TestClass1.charClsFunc(), 127)

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

    def testClsCharp(self):
        OC_TestClass1.clsReset()
        self.assertEquals(OC_TestClass1.charpClsFunc(), 'hello')
        self.assertEquals(OC_TestClass1.charpClsFunc(), 'world')
        self.assertEquals(OC_TestClass1.charpClsFunc(), 'foobar')

    def testClsID(self):
        OC_TestClass1.clsReset()
        self.assertEquals(len(OC_TestClass1.idClsFunc()), 0)
        self.assertEquals(type(OC_TestClass1.idClsFunc()).__name__, 'NSHost')
        self.assertEquals(str(OC_TestClass1.idClsFunc()), '{}')
        self.assertEquals(OC_TestClass1.idClsFunc(), None)

    # testCls* ends here

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
        self.assertEquals(obj.charFunc(), -128)
        self.assertEquals(obj.charFunc(), 0)
        self.assertEquals(obj.charFunc(), 127)

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

    def testCharp(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.charpClsFunc(), 'hello')
        self.assertEquals(obj.charpClsFunc(), 'world')
        self.assertEquals(obj.charpClsFunc(), 'foobar')

    def testID(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(len(obj.idClsFunc()), 0)
        self.assertEquals(type(obj.idClsFunc()).__name__, 'NSHost')
        self.assertEquals(str(obj.idClsFunc()), '{}')
        self.assertEquals(obj.idClsFunc(), None)

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
    def setUp(self):
        self.obj = OC_TestClass1.new()

    def testLongLong(self):
        self.assertEquals(self.obj.longlongArg_(0), 0)
        self.assertEquals(self.obj.longlongArg_(10), 5)
        self.assertEquals(self.obj.longlongArg_(10L), 5)
        self.assertEquals(self.obj.longlongArg_(1L << 60), (1L << 59))
        self.assertEquals(self.obj.longlongArg_(-10), -5)
        self.assertEquals(self.obj.longlongArg_(-10L), -5)
        self.assertEquals(self.obj.longlongArg_(-1L << 60), -(1L << 59))

        # TODO: Out of range values

    def testULongLong(self):
        self.assertEquals(self.obj.ulonglongArg_(0), 0)
        self.assertEquals(self.obj.ulonglongArg_(10), 5)
        self.assertEquals(self.obj.ulonglongArg_(10L), 5)
        self.assertEquals(self.obj.ulonglongArg_(1L << 60), (1L << 59))

        # TODO: Out of range values

    def testLong(self):
        self.assertEquals(self.obj.longArg_(0), 0)
        self.assertEquals(self.obj.longArg_(10), 5)
        self.assertEquals(self.obj.longArg_(10L), 5)
        self.assertEquals(self.obj.longArg_(1 << 30), (1 << 29))
        self.assertEquals(self.obj.longArg_(-10), -5)
        self.assertEquals(self.obj.longArg_(-10L), -5)
        self.assertEquals(self.obj.longArg_(-1 << 30), -(1 << 29))

        # TODO: Out of range values

    def testULong(self):
        self.assertEquals(self.obj.ulongArg_(0), 0)
        self.assertEquals(self.obj.ulongArg_(10), 5)
        self.assertEquals(self.obj.ulongArg_(10L), 5)
        self.assertEquals(self.obj.ulongArg_(1 << 30), (1 << 29))

        # TODO: Out of range values

    def testInt(self):
        self.assertEquals(self.obj.intArg_(0), 0)
        self.assertEquals(self.obj.intArg_(10), 5)
        self.assertEquals(self.obj.intArg_(10L), 5)
        self.assertEquals(self.obj.intArg_(1 << 30), (1 << 29))
        self.assertEquals(self.obj.intArg_(-10), -5)
        self.assertEquals(self.obj.intArg_(-10L), -5)
        self.assertEquals(self.obj.intArg_(-1 << 30), -(1 << 29))

        self.assertEquals(self.obj.intArg_(10.0), 5)

        self.assertRaises(objc.error, self.obj.intArg_, long(sys.maxint)+1)
        self.assertRaises(objc.error, self.obj.intArg_, -long(sys.maxint)-2)
        self.assertRaises(objc.error, self.obj.intArg_, -float(sys.maxint)-2)

    def testUInt(self):
        self.assertEquals(self.obj.uintArg_(0), 0)
        self.assertEquals(self.obj.uintArg_(10), 5)
        self.assertEquals(self.obj.uintArg_(10L), 5)
        self.assertEquals(self.obj.uintArg_(1 << 30), (1 << 29))

        self.assertEquals(self.obj.uintArg_(10.0), 5)

        self.assertRaises(objc.error, self.obj.uintArg_, -5)
        self.assertRaises(objc.error, self.obj.uintArg_, -5L)
        self.assertRaises(objc.error, self.obj.uintArg_, 1+2*(long(sys.maxint)+1))


    def testShort(self):
        self.assertEquals(self.obj.shortArg_(0), 0)
        self.assertEquals(self.obj.shortArg_(10), 5)
        self.assertEquals(self.obj.shortArg_(10L), 5)
        self.assertEquals(self.obj.shortArg_(1 << 14), (1 << 13))
        self.assertEquals(self.obj.shortArg_(-10), -5)
        self.assertEquals(self.obj.shortArg_(-10L), -5)
        self.assertEquals(self.obj.shortArg_(-(1 << 14)), -(1 << 13))

        self.assertEquals(self.obj.shortArg_(10.0), 5)

        # Out of range arguments, assumes a short is 16 bits
        self.assertRaises(objc.error, self.obj.shortArg_, -(1<<16)-1)
        self.assertRaises(objc.error, self.obj.shortArg_, 1<<16)
        self.assertRaises(objc.error, self.obj.shortArg_, -(1L<<16)-1)
        self.assertRaises(objc.error, self.obj.shortArg_, 1L<<16)

    def testUShort(self):
        self.assertEquals(self.obj.ushortArg_(0), 0)
        self.assertEquals(self.obj.ushortArg_(10), 5)
        self.assertEquals(self.obj.ushortArg_(10L), 5)
        self.assertEquals(self.obj.ushortArg_(1 << 14), (1 << 13))

        self.assertEquals(self.obj.ushortArg_(10.0), 5)

        # Out of range arguments, assumes a short is 16 bits
        self.assertRaises(objc.error, self.obj.ushortArg_, -5)
        self.assertRaises(objc.error, self.obj.ushortArg_, -(1<<16)-1)
        self.assertRaises(objc.error, self.obj.ushortArg_, 1<<16)
        self.assertRaises(objc.error, self.obj.ushortArg_, -5L)
        self.assertRaises(objc.error, self.obj.ushortArg_, -(1L<<16)-1)
        self.assertRaises(objc.error, self.obj.ushortArg_, 1L<<16)


    def testChar(self):
        self.assertEquals(self.obj.charArg_(0), (0))
        self.assertEquals(self.obj.charArg_(10), (5))
        self.assertEquals(self.obj.charArg_(10L), (5))
        self.assertEquals(self.obj.charArg_(1 << 6), (1 << 5))
        self.assertEquals(self.obj.charArg_('\x00'), 0x00)
        self.assertEquals(self.obj.charArg_('\x10'), ord('\x10')/2)

        # TODO: Out of range arguments

    def testUChar(self):
        self.assertEquals(self.obj.ucharArg_(0), 0)
        self.assertEquals(self.obj.ucharArg_(10), 5)
        self.assertEquals(self.obj.ucharArg_(10L), 5)
        self.assertEquals(self.obj.ucharArg_(1 << 7), (1 << 6))
        self.assertEquals(self.obj.ucharArg_('\x00'), 0)
        self.assertEquals(self.obj.ucharArg_('\x10'), ord('\x10')/2)

        self.assertEquals(self.obj.ucharArg_(10.0), 5)

        # Out of range arguments
        self.assertRaises(objc.error, self.obj.ucharArg_, -5)
        self.assertRaises(objc.error, self.obj.ucharArg_, -256)
        self.assertRaises(objc.error, self.obj.ucharArg_, 256)
        self.assertRaises(objc.error, self.obj.ucharArg_, -5L)
        self.assertRaises(objc.error, self.obj.ucharArg_, -256L)
        self.assertRaises(objc.error, self.obj.ucharArg_, 256L)

    def testCharp(self):
        self.assertEquals(self.obj.charpArg_("hello world"), 'dlrow olleh')

        self.assertRaises(objc.error, self.obj.charpArg_, 256L)
        self.assertRaises(objc.error, self.obj.charpArg_, u"hello world")

    def testIDPython(self):
        # Test a Python object as the argument
        s = self.obj.idArg_("hello")
        self.assertEquals(len(s), 1)
        self.assertEquals(s[0], "hello")

    def testIDOC(self):
        # Test an Objective-C object as the argument
        o = objc.lookUpClass("NSHost").hostWithAddress_('127.0.0.1')
        s = self.obj.idArg_(o)
        self.assertEquals(len(s), 1)
        self.assert_(s[0] is o)

    def testStruct1(self):
        self.assertEquals(self.obj.dummyArg_((-1, 1)), (-2, 2))

        self.assertRaises(objc.error, self.obj.dummyArg_, 256L)
        self.assertRaises(objc.error, self.obj.dummyArg_, (-1,))
        self.assertRaises(objc.error, self.obj.dummyArg_, (-1,1,2))

    def testStruct2(self):
        self.assertEquals(self.obj.dummy2Arg_(((1,2,3,4),)), ((8,6,4,2),))

        self.assertRaises(objc.error, self.obj.dummy2Arg_, ((8,6,4,2),1))
        self.assertRaises(objc.error, self.obj.dummy2Arg_, ((8,6,4,),))
        self.assertRaises(objc.error, self.obj.dummy2Arg_, ((8,6,4,2,1),))


class TestByReferenceArguments(unittest.TestCase):
    #
    # Test argument passing of single basic values by reference.
    #
    def setUp(self):
        self.obj = OC_TestClass1.new()

    def testCharIn(self):
        self.assertEquals(self.obj.passInChar_('\x10'), 0x19)

    def testCharOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutChar_(), (None, -128))
        self.assertEquals(self.obj.passOutChar_(), (None, 0))
        self.assertEquals(self.obj.passOutChar_(), (None, 127))

    def testCharInOut(self):
        self.assertEquals(self.obj.passInOutChar_('\x10'), (None, 0x3a))

    def testUCharIn(self):
        self.assertEquals(self.obj.passInUChar_(10), 19)

    def testUCharOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutUChar_(), (None, 0))
        self.assertEquals(self.obj.passOutUChar_(), (None, 128))
        self.assertEquals(self.obj.passOutUChar_(), (None, 255))

    def testUCharInOut(self):
        self.assertEquals(self.obj.passInOutUChar_(10), (None, 52))

    def testShortIn(self):
        self.assertEquals(self.obj.passInShort_(10), 19)
        self.assertEquals(self.obj.passInShort_(-100), -91)
        self.assertEquals(self.obj.passInShort_(-100.0), -91)

    def testShortOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutShort_(), (None, -(1 << 14)))
        self.assertEquals(self.obj.passOutShort_(), (None, -42))
        self.assertEquals(self.obj.passOutShort_(), (None, 0))
        self.assertEquals(self.obj.passOutShort_(), (None, 42))
        self.assertEquals(self.obj.passOutShort_(), (None, (1 << 14)))

    def testShortInOut(self):
        self.assertEquals(self.obj.passInOutShort_(10), (None, 52))
        self.assertEquals(self.obj.passInOutShort_(-100), (None, -58))
        self.assertEquals(self.obj.passInOutShort_(-100.0), (None, -58))

    def testUShortIn(self):
        self.assertEquals(self.obj.passInUShort_(10), 19)

    def testUShortOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutUShort_(), (None, 0))
        self.assertEquals(self.obj.passOutUShort_(), (None, 42))
        self.assertEquals(self.obj.passOutUShort_(), (None, (1 << 14)))

    def testUShortInOut(self):
        self.assertEquals(self.obj.passInOutUShort_(10), (None, 52))

    def testIntIn(self):
        self.assertEquals(self.obj.passInInt_(10), 19)
        self.assertEquals(self.obj.passInInt_(-100), -91)

    def testIntOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutInt_(), (None, -(1 << 30)))
        self.assertEquals(self.obj.passOutInt_(), (None, -42))
        self.assertEquals(self.obj.passOutInt_(), (None, 0))
        self.assertEquals(self.obj.passOutInt_(), (None, 42))
        self.assertEquals(self.obj.passOutInt_(), (None, (1 << 30)))

    def testIntInOut(self):
        self.assertEquals(self.obj.passInOutInt_(10), (None, 52))
        self.assertEquals(self.obj.passInOutInt_(-100), (None, -58))
        self.assertEquals(self.obj.passInOutInt_(-100.0), (None, -58))

    def testUIntIn(self):
        self.assertEquals(self.obj.passInUInt_(10), 19)

    def testUIntOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutUInt_(), (None, 0))
        self.assertEquals(self.obj.passOutUInt_(), (None, 42))
        self.assertEquals(self.obj.passOutUInt_(), (None, (1 << 30)))

    def testUIntInOut(self):
        self.assertEquals(self.obj.passInOutUInt_(10), (None, 52))
        self.assertEquals(self.obj.passInOutUInt_(10.0), (None, 52))

    def testLongIn(self):
        self.assertEquals(self.obj.passInLong_(10), 19)
        self.assertEquals(self.obj.passInLong_(-100), -91)

    def testLongOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutLong_(), (None, -(1 << 30)))
        self.assertEquals(self.obj.passOutLong_(), (None, -42))
        self.assertEquals(self.obj.passOutLong_(), (None, 0))
        self.assertEquals(self.obj.passOutLong_(), (None, 42))
        self.assertEquals(self.obj.passOutLong_(), (None, (1 << 30)))

    def testLongInOut(self):
        self.assertEquals(self.obj.passInOutLong_(10), (None, 52))
        self.assertEquals(self.obj.passInOutLong_(-100), (None, -58))
        self.assertEquals(self.obj.passInOutLong_(-100.0), (None, -58))

    def testULongIn(self):
        self.assertEquals(self.obj.passInULong_(10), 19)

    def testULongOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutULong_(), (None, 0))
        self.assertEquals(self.obj.passOutULong_(), (None, 42))
        self.assertEquals(self.obj.passOutULong_(), (None, (1 << 30)))

    def testULongInOut(self):
        self.assertEquals(self.obj.passInOutULong_(10), (None, 52))
        self.assertEquals(self.obj.passInOutULong_(10.0), (None, 52))

    def testLongLongIn(self):
        self.assertEquals(self.obj.passInLongLong_(10), 19)
        self.assertEquals(self.obj.passInLongLong_(-100), -91)

    def testLongLongOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutLongLong_(), (None, -(1L << 60)))
        self.assertEquals(self.obj.passOutLongLong_(), (None, -42))
        self.assertEquals(self.obj.passOutLongLong_(), (None, 0))
        self.assertEquals(self.obj.passOutLongLong_(), (None, 42))
        self.assertEquals(self.obj.passOutLongLong_(), (None, (1L << 60)))

    def testLongLongInOut(self):
        self.assertEquals(self.obj.passInOutLongLong_(10), (None, 52))
        self.assertEquals(self.obj.passInOutLongLong_(-100), (None, -58))
        self.assertEquals(self.obj.passInOutLongLong_(-100.0), (None, -58))

    def testULongLongIn(self):
        self.assertEquals(self.obj.passInULongLong_(10), 19)

    def testULongLongOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutULongLong_(), (None, 0))
        self.assertEquals(self.obj.passOutULongLong_(), (None, 42))
        self.assertEquals(self.obj.passOutULongLong_(), (None, (1L << 63)))

    def testULongLongInOut(self):
        self.assertEquals(self.obj.passInOutULongLong_(10), (None, 52))
        self.assertEquals(self.obj.passInOutULongLong_(10.0), (None, 52))

    def testFloatIn(self):
        self.assertEquals(self.obj.passInFloat_(10), makeCFloat(90.0))
        self.assertEquals(self.obj.passInFloat_(0.11), makeCFloat(0.99))

    def testFloatOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutFloat_(), (None, makeCFloat(0.128)))
        self.assertEquals(self.obj.passOutFloat_(), (None, makeCFloat(1.0)))
        self.assertEquals(self.obj.passOutFloat_(), (None, makeCFloat(42.0)))
        self.assertEquals(self.obj.passOutFloat_(), (None, makeCFloat(1e10)))

    def testFloatInOut(self):
        self.assertEquals(self.obj.passInOutFloat_(10), (None, makeCFloat(420)))
        self.assertEquals(self.obj.passInOutFloat_(10.0), (None, makeCFloat(420)))
        self.assertEquals(self.obj.passInOutFloat_(0.01), (None, makeCFloat(0.42)))

    def testDoubleIn(self):
        self.assertEquals(self.obj.passInDouble_(10), 90.0)
        self.assertEquals(self.obj.passInDouble_(0.11), 0.99)

    def testDoubleOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutDouble_(), (None, 0.128))
        self.assertEquals(self.obj.passOutDouble_(), (None, 1.0))
        self.assertEquals(self.obj.passOutDouble_(), (None, 42.0))
        self.assertEquals(self.obj.passOutDouble_(), (None, 1e10))

    def testDoubleInOut(self):
        self.assertEquals(self.obj.passInOutDouble_(10), (None, 420))
        self.assertEquals(self.obj.passInOutDouble_(10.0), (None, 420))
        self.assertEquals(self.obj.passInOutDouble_(0.01), (None, 0.42))

    def testCharpIn(self):
        self.assertEquals(self.obj.passInCharp_("hello"), "hheelllloo")
        self.assertEquals(self.obj.passInCharp_("abcde"), "aabbccddee")

    def testCharpOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutCharp_(), (None, "hello"))
        self.assertEquals(self.obj.passOutCharp_(), (None, "world"))
        self.assertEquals(self.obj.passOutCharp_(), (None, "foobar"))

    def testCharpInOut(self):
        self.assertEquals(self.obj.passInOutCharp_("hello"), (None, "hheelllloo"))
        self.assertEquals(self.obj.passInOutCharp_("abcdef"), (None, "aabbccddeeff"))

    # TODO: structs (including Objective-C part)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTypeStr))
    suite.addTest(unittest.makeSuite(TestSimpleCalls))
    suite.addTest(unittest.makeSuite(TestSimpleArguments))
    suite.addTest(unittest.makeSuite(TestByReferenceArguments))
    return suite

if __name__ == '__main__':
    unittest.main()
