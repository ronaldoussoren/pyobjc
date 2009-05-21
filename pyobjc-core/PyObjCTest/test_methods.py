"""
XXX: Should verify if test_methods2.py implements all tests in this file.

Test lowlevel message passing details (Python -> ObjC)


NOTE: 'long long' return-value test for calls from Objective-C are disabled,
  they crash the interpreter.

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
- Done: Return simple values, return structs, pass in basic types (c part)

NOTES:
- Always use makeCFloat when testing the value of a C float against a
  precomputed (literal) value. Just comparing against a Python float won't work
  as that is a C double which has a different representation from C floats
  resulting in spurious test failures.
- See also testbndl.m, the implementation there must be synchronized
  with this file.
"""
from PyObjCTools.TestSupport import *
import objc
import sys
import struct

# Can't set the right signatures in plain Objective-C.
for method, argmeta in [
        ( "passInOutChar:", { 2: dict(type_modifier='N')}),
        ( "passOutChar:", { 2: dict(type_modifier='o')}),
        ( "passInChar:", { 2: dict(type_modifier='n')}),
        ( "passInOutUChar:", { 2: dict(type_modifier='N', type='^C')}),
        ( "passOutUChar:", { 2: dict(type_modifier='o', type='^C')}),
        ( "passInUChar:", { 2: dict(type_modifier='n', type='^C')}),
        ( "passInOutShort:", { 2: dict(type_modifier='N')}),
        ( "passOutShort:", { 2: dict(type_modifier='o')}),
        ( "passInShort:", { 2: dict(type_modifier='n')}),
        ( "passInOutUShort:", { 2: dict(type_modifier='N')}),
        ( "passOutUShort:", { 2: dict(type_modifier='o')}),
        ( "passInUShort:", { 2: dict(type_modifier='n')}),
        ( "passInOutInt:", { 2: dict(type_modifier='N')}),
        ( "passOutInt:", { 2: dict(type_modifier='o')}),
        ( "passInInt:", { 2: dict(type_modifier='n')}),
        ( "passInOutUInt:", { 2: dict(type_modifier='N')}),
        ( "passOutUInt:", { 2: dict(type_modifier='o')}),
        ( "passInUInt:", { 2: dict(type_modifier='n')}),
        ( "passInOutLong:", { 2: dict(type_modifier='N')}),
        ( "passOutLong:", { 2: dict(type_modifier='o')}),
        ( "passInLong:", { 2: dict(type_modifier='n')}),
        ( "passInOutULong:", { 2: dict(type_modifier='N')}),
        ( "passOutULong:", { 2: dict(type_modifier='o')}),
        ( "passInULong:", { 2: dict(type_modifier='n')}),
        ( "passInOutLongLong:", { 2: dict(type_modifier='N')}),
        ( "passOutLongLong:", { 2: dict(type_modifier='o')}),
        ( "passInLongLong:", { 2: dict(type_modifier='n')}),
        ( "passInOutULongLong:", { 2: dict(type_modifier='N')}),
        ( "passOutULongLong:", { 2: dict(type_modifier='o')}),
        ( "passInULongLong:", { 2: dict(type_modifier='n')}),
        ( "passInOutFloat:", { 2: dict(type_modifier='N')}),
        ( "passOutFloat:", { 2: dict(type_modifier='o')}),
        ( "passInFloat:", { 2: dict(type_modifier='n')}),
        ( "passInOutDouble:", { 2: dict(type_modifier='N')}),
        ( "passOutDouble:", { 2: dict(type_modifier='o')}),
        ( "passInDouble:", { 2: dict(type_modifier='n')}),
        ( "passInOutCharp:", { 2: dict(type_modifier='N')}),
        ( "passOutCharp:", { 2: dict(type_modifier='o')}),
        ( "passInCharp:", { 2: dict(type_modifier='n')}),
        ( "passInOutID:", { 2: dict(type_modifier='N')}),
        ( "passOutID:", { 2: dict(type_modifier='o')}),
        ( "passInID:", { 2: dict(type_modifier='n')}),
    ]:

    objc.registerMetaDataForSelector("OC_TestClass1", method,
                    dict(arguments=argmeta))


from PyObjCTest.testbndl import *

def makeCFloat(value):
    """
    C floats and doubles have a different representation, this function returns
    the result of converting a python float (== C double) to a C float and back.
    """
    return struct.unpack('f',struct.pack('f', value))[0]


class PyOCTestSimpleReturns(TestCase):
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
        self.assert_(str(OC_TestClass1.idClsFunc()) in ('{}', '{\n}'))
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
        obj.reset()
        self.assertEquals(obj.floatFunc(), makeCFloat(0.128))
        self.assertEquals(obj.floatFunc(), makeCFloat(1.0))
        self.assertEquals(obj.floatFunc(), makeCFloat(42.0))
        self.assertEquals(obj.floatFunc(), makeCFloat(1e10))

    def testDouble(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.doubleFunc(), 0.128)
        self.assertEquals(obj.doubleFunc(), 1.0)
        self.assertEquals(obj.doubleFunc(), 42.0)
        self.assertEquals(obj.doubleFunc(), 1e10)

    def testCharp(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(obj.charpFunc(), 'hello')
        self.assertEquals(obj.charpFunc(), 'world')
        self.assertEquals(obj.charpFunc(), 'foobar')

    def testID(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEquals(len(obj.idFunc()), 0)
        self.assertEquals(type(obj.idFunc()).__name__, 'NSHost')
        self.assert_(str(obj.idFunc()) in ('{}', '{\n}'))
        self.assertEquals(obj.idFunc(), None)

    def testStruct1(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.dummyFunc(), (-1, 1))

    def testStruct2(self):
        obj = OC_TestClass1.new()

        self.assertEquals(obj.dummy2Func(), ((1,2,3,4),))


class PyOCTestSimpleArguments(TestCase):
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

        self.assertRaises(ValueError, self.obj.intArg_, long(sys.maxint)+1)
        self.assertRaises(ValueError, self.obj.intArg_, -long(sys.maxint)-2)
        self.assertRaises(ValueError, self.obj.intArg_, -float(sys.maxint)-2)

    def testUInt(self):
        self.assertEquals(self.obj.uintArg_(0), 0)
        self.assertEquals(self.obj.uintArg_(10), 5)
        self.assertEquals(self.obj.uintArg_(10L), 5)
        self.assertEquals(self.obj.uintArg_(1 << 30), (1 << 29))

        self.assertEquals(self.obj.uintArg_(10.0), 5)

        self.assertRaises(ValueError, self.obj.uintArg_, -5)
        self.assertRaises(ValueError, self.obj.uintArg_, -5L)
        self.assertRaises(ValueError, self.obj.uintArg_, 1+2*(long(sys.maxint)+1))


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
        self.assertRaises(ValueError, self.obj.shortArg_, -(1<<16)-1)
        self.assertRaises(ValueError, self.obj.shortArg_, 1<<16)
        self.assertRaises(ValueError, self.obj.shortArg_, -(1L<<16)-1)
        self.assertRaises(ValueError, self.obj.shortArg_, 1L<<16)

    def testUShort(self):
        self.assertEquals(self.obj.ushortArg_(0), 0)
        self.assertEquals(self.obj.ushortArg_(10), 5)
        self.assertEquals(self.obj.ushortArg_(10L), 5)
        self.assertEquals(self.obj.ushortArg_(1 << 14), (1 << 13))

        self.assertEquals(self.obj.ushortArg_(10.0), 5)

        # Out of range arguments, assumes a short is 16 bits
        self.assertRaises(ValueError, self.obj.ushortArg_, -5)
        self.assertRaises(ValueError, self.obj.ushortArg_, -(1<<16)-1)
        self.assertRaises(ValueError, self.obj.ushortArg_, 1<<16)
        self.assertRaises(ValueError, self.obj.ushortArg_, -5L)
        self.assertRaises(ValueError, self.obj.ushortArg_, -(1L<<16)-1)
        self.assertRaises(ValueError, self.obj.ushortArg_, 1L<<16)


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
        self.assertRaises(ValueError, self.obj.ucharArg_, -5)
        self.assertRaises(ValueError, self.obj.ucharArg_, -256)
        self.assertRaises(ValueError, self.obj.ucharArg_, 256)
        self.assertRaises(ValueError, self.obj.ucharArg_, -5L)
        self.assertRaises(ValueError, self.obj.ucharArg_, -256L)
        self.assertRaises(ValueError, self.obj.ucharArg_, 256L)

    def testCharp(self):
        self.assertEquals(self.obj.charpArg_("hello world"), 'dlrow olleh')

        self.assertRaises(ValueError, self.obj.charpArg_, 256L)
        self.assertRaises(ValueError, self.obj.charpArg_, u"hello world")

    def testIDPython(self):
        # Test a Python object as the argument
        s = self.obj.idArg_(u"hello")
        self.assertEquals(len(s), 1)
        self.assertEquals(s[0], u"hello")

    def testIDOC(self):
        # Test an Objective-C object as the argument

        # NSHost gives problems on GNUstep, better check those problems
        # seperately in the Foundation test suite.
        #c = objc.lookUpClass("NSHost")
        #o = c.hostWithAddress_('127.0.0.1')

        c = objc.lookUpClass("NSScanner")
        o = c.scannerWithString_(u"hello world")
        s = self.obj.idArg_(o)
        self.assertEquals(len(s), 1)
        self.assert_(s[0] is o)

    def testStruct1(self):
        self.assertEquals(self.obj.dummyArg_((-1, 1)), (-2, 2))

        self.assertRaises(TypeError, self.obj.dummyArg_, 256L)
        self.assertRaises(ValueError, self.obj.dummyArg_, (-1,))
        self.assertRaises(ValueError, self.obj.dummyArg_, (-1,1,2))

    def testStruct2(self):
        self.assertEquals(self.obj.dummy2Arg_(((1,2,3,4),)), ((8,6,4,2),))

        self.assertRaises(ValueError, self.obj.dummy2Arg_, ((8,6,4,2),1))
        self.assertRaises(ValueError, self.obj.dummy2Arg_, ((8,6,4,),))
        self.assertRaises(ValueError, self.obj.dummy2Arg_, ((8,6,4,2,1),))


class PyOCTestByReferenceArguments(TestCase):
    #
    # Test argument passing of single basic values by reference.
    #
    def setUp(self):
        self.obj = OC_TestClass1.new()

    def testCharIn(self):
        self.assertEquals(self.obj.passInChar_('\x10'), 0x19)

    def testCharOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutChar_(None), -128)
        self.assertEquals(self.obj.passOutChar_(None), 0)
        self.assertEquals(self.obj.passOutChar_(None), 127)

    def testCharInOut(self):
        self.assertEquals(self.obj.passInOutChar_('\x10'), 0x3a)

    def testUCharIn(self):
        self.assertEquals(self.obj.passInUChar_(10), 19)

    def testUCharOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutUChar_(None), 0)
        self.assertEquals(self.obj.passOutUChar_(None), 128)
        self.assertEquals(self.obj.passOutUChar_(None), 255)

    def testUCharInOut(self):
        self.assertEquals(self.obj.passInOutUChar_(10), 52)

    def testShortIn(self):
        self.assertEquals(self.obj.passInShort_(10), 19)
        self.assertEquals(self.obj.passInShort_(-100), -91)
        self.assertEquals(self.obj.passInShort_(-100.0), -91)

    def testShortOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutShort_(None), -(1 << 14))
        self.assertEquals(self.obj.passOutShort_(None), -42)
        self.assertEquals(self.obj.passOutShort_(None), 0)
        self.assertEquals(self.obj.passOutShort_(None), 42)
        self.assertEquals(self.obj.passOutShort_(None), 1 << 14)

    def testShortInOut(self):
        self.assertEquals(self.obj.passInOutShort_(10), 52)
        self.assertEquals(self.obj.passInOutShort_(-100), -58)
        self.assertEquals(self.obj.passInOutShort_(-100.0), -58)

    def testUShortIn(self):
        self.assertEquals(self.obj.passInUShort_(10), 19)

    def testUShortOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutUShort_(None), 0)
        self.assertEquals(self.obj.passOutUShort_(None), 42)
        self.assertEquals(self.obj.passOutUShort_(None), (1 << 14))

    def testUShortInOut(self):
        self.assertEquals(self.obj.passInOutUShort_(10), 52)

    def testIntIn(self):
        self.assertEquals(self.obj.passInInt_(10), 19)
        self.assertEquals(self.obj.passInInt_(-100), -91)

    def testIntOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutInt_(None), -(1 << 30))
        self.assertEquals(self.obj.passOutInt_(None), -42)
        self.assertEquals(self.obj.passOutInt_(None), 0)
        self.assertEquals(self.obj.passOutInt_(None), 42)
        self.assertEquals(self.obj.passOutInt_(None), (1 << 30))

    def testIntInOut(self):
        self.assertEquals(self.obj.passInOutInt_(10), 52)
        self.assertEquals(self.obj.passInOutInt_(-100), -58)
        self.assertEquals(self.obj.passInOutInt_(-100.0), -58)

    def testUIntIn(self):
        self.assertEquals(self.obj.passInUInt_(10), 19)

    def testUIntOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutUInt_(None), 0)
        self.assertEquals(self.obj.passOutUInt_(None), 42)
        self.assertEquals(self.obj.passOutUInt_(None), (1 << 30))

    def testUIntInOut(self):
        self.assertEquals(self.obj.passInOutUInt_(10), 52)
        self.assertEquals(self.obj.passInOutUInt_(10.0), 52)

    def testLongIn(self):
        self.assertEquals(self.obj.passInLong_(10), 19)
        self.assertEquals(self.obj.passInLong_(-100), -91)

    def testLongOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutLong_(None), -(1 << 30))
        self.assertEquals(self.obj.passOutLong_(None), -42)
        self.assertEquals(self.obj.passOutLong_(None), 0)
        self.assertEquals(self.obj.passOutLong_(None), 42)
        self.assertEquals(self.obj.passOutLong_(None), (1 << 30))

    def testLongInOut(self):
        self.assertEquals(self.obj.passInOutLong_(10), 52)
        self.assertEquals(self.obj.passInOutLong_(-100), -58)
        self.assertEquals(self.obj.passInOutLong_(-100.0), -58)

    def testULongIn(self):
        self.assertEquals(self.obj.passInULong_(10), 19)

    def testULongOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutULong_(None), 0)
        self.assertEquals(self.obj.passOutULong_(None), 42)
        self.assertEquals(self.obj.passOutULong_(None), (1 << 30))

    def testULongInOut(self):
        self.assertEquals(self.obj.passInOutULong_(10), 52)
        self.assertEquals(self.obj.passInOutULong_(10.0), 52)

    def testLongLongIn(self):
        self.assertEquals(self.obj.passInLongLong_(10), 19)
        self.assertEquals(self.obj.passInLongLong_(-100), -91)

    def testLongLongOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutLongLong_(None), -(1L << 60))
        self.assertEquals(self.obj.passOutLongLong_(None), -42)
        self.assertEquals(self.obj.passOutLongLong_(None), 0)
        self.assertEquals(self.obj.passOutLongLong_(None), 42)
        self.assertEquals(self.obj.passOutLongLong_(None), (1L << 60))

    def testLongLongInOut(self):
        self.assertEquals(self.obj.passInOutLongLong_(10), 52)
        self.assertEquals(self.obj.passInOutLongLong_(-100), -58)
        self.assertEquals(self.obj.passInOutLongLong_(-100.0), -58)

    def testULongLongIn(self):
        self.assertEquals(self.obj.passInULongLong_(10), 19)

    def testULongLongOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutULongLong_(None), 0)
        self.assertEquals(self.obj.passOutULongLong_(None), 42)
        self.assertEquals(self.obj.passOutULongLong_(None), (1L << 63))

    def testULongLongInOut(self):
        self.assertEquals(self.obj.passInOutULongLong_(10), 52)
        self.assertEquals(self.obj.passInOutULongLong_(10.0), 52)

    def testFloatIn(self):
        self.assertEquals(self.obj.passInFloat_(10), makeCFloat(90.0))
        self.assertEquals(self.obj.passInFloat_(0.11), makeCFloat(0.99))

    def testFloatOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutFloat_(None), makeCFloat(0.128))
        self.assertEquals(self.obj.passOutFloat_(None), makeCFloat(1.0))
        self.assertEquals(self.obj.passOutFloat_(None), makeCFloat(42.0))
        self.assertEquals(self.obj.passOutFloat_(None), makeCFloat(1e10))

    def testFloatInOut(self):
        self.assertEquals(self.obj.passInOutFloat_(10), makeCFloat(420))
        self.assertEquals(self.obj.passInOutFloat_(10.0), makeCFloat(420))
        self.assertEquals(self.obj.passInOutFloat_(0.01), makeCFloat(0.42))

    def testDoubleIn(self):
        self.assertEquals(self.obj.passInDouble_(10), 90.0)
        self.assertEquals(self.obj.passInDouble_(0.11), 0.99)

    def testDoubleOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutDouble_(None), 0.128)
        self.assertEquals(self.obj.passOutDouble_(None), 1.0)
        self.assertEquals(self.obj.passOutDouble_(None), 42.0)
        self.assertEquals(self.obj.passOutDouble_(None), 1e10)

    def testDoubleInOut(self):
        self.assertEquals(self.obj.passInOutDouble_(10), 420)
        self.assertEquals(self.obj.passInOutDouble_(10.0), 420)
        self.assertEquals(self.obj.passInOutDouble_(0.01), 0.42)

    def testCharpIn(self):
        self.assertEquals(self.obj.passInCharp_("hello"), "hheelllloo")
        self.assertEquals(self.obj.passInCharp_("abcde"), "aabbccddee")

    def testCharpOut(self):
        self.obj.reset()
        self.assertEquals(self.obj.passOutCharp_(None), "hello")
        self.assertEquals(self.obj.passOutCharp_(None), "world")
        self.assertEquals(self.obj.passOutCharp_(None), "foobar")

    def testCharpInOut(self):
        self.assertEquals(self.obj.passInOutCharp_("hello"), "hheelllloo")
        self.assertEquals(self.obj.passInOutCharp_("abcdef"), "aabbccddeeff")

    # TODO: structs (including Objective-C part)



#
# Below this point only TestCases that test calling Python from Objective-C
#
# Notes:
# - There is both a pure python and an Python-ObjC hybrid class
#   (MyPyClass and MyOCClass). The former is not used in the first few tests,
#   we need to decide what functionality we'll support for these (e.g. do
#   we support selector objects, or only normal methods?)
# - Every test below should exists in two variants:
#   * 'invoke' - Calls back from ObjC to Python using an NSInvocation
#                and the forwardInvocation method
#   * 'call'   - Calls back from ObjC to Python using a normal ObjC method call

# Values for
# - 8-bit char
# - 16-bit short
# - 32-bit int/long
# - 64-bit long long
# Values are: max-negative, -42, 0, 42, max-positive, out-of-range, bad-type, None
#
CHAR_NUMBERS=[ -128, -42, 0, 42, 127, 'a', 128, "hello", None ]
UCHAR_NUMBERS=[ 0, 42, 255, 'a', 256, "hello", None ]
SHORT_NUMBERS=[ -32768, -42, 0, 32767, 32768, "hello", None ]
USHORT_NUMBERS=[ 0, 42, 65535, 65536, "hello", None ]
INT_NUMBERS=[ -2147483648, -42, 0, 2147483647, 2147483648, "hello", None ]
UINT_NUMBERS=[ 0, 42, 4294967295, 4294967296, "hello", None ]
LONG_NUMBERS=[ -2147483648, -42, 0, 2147483647, sys.maxint+1, "hello", None ]
ULONG_NUMBERS=[ 0, 42, 4294967295L, 2*(sys.maxint+1), "hello", None ]
LONGLONG_NUMBERS=[ -9223372036854775808L, -42, 0, 42, 9223372036854775807L, 9223372036854775808L, "hello", None ]
ULONGLONG_NUMBERS=[0, 42, 18446744073709551615L, 18446744073709551616L, "hello", None ]

FLOAT_NUMBERS = [ makeCFloat(0.1), makeCFloat(100.0) ]
DOUBLE_NUMBERS = [ 1.5, 3.5, 1e10, 1.99e10 ]
OBJECTS = [ u"hello", 1.0, range(4), lambda x: 10 ]
DUMMY_OBJECTS = [ (1, 1), (-10, -10), (-4, -5), (0, 0), (10, 20) ]
DUMMY2_OBJECTS = [ ((1, 2, 3, 4),), ((-9, -8, -7, -6),)]
POINTS=[ (1.0, 2.0), (1e10, 2e10), (-0.5, 0.5) ]

class MyPyClass:
    def __init__(self):
        self.idx = 0

    def reset(self):
        self.idx = 0

    def idFunc(self):
        i = self.idx
        self.idx += 1
        return OBJECTS[i]

class MyOCClass (objc.lookUpClass('NSObject')):
    def __init__(self):
        self.idx = 0

    def reset(self):
        self.idx = 0

    def charFunc(self):
        i = self.idx
        self.idx += 1
        return CHAR_NUMBERS[i]
    charFunc = objc.selector(charFunc, signature=OC_TestClass1.charFunc.signature)

    def ucharFunc(self):
        i = self.idx
        self.idx += 1
        return UCHAR_NUMBERS[i]
    ucharFunc = objc.selector(ucharFunc, signature=OC_TestClass1.ucharFunc.signature)

    def shortFunc(self):
        i = self.idx
        self.idx += 1
        return SHORT_NUMBERS[i]
    shortFunc = objc.selector(shortFunc, signature=OC_TestClass1.shortFunc.signature)

    def ushortFunc(self):
        i = self.idx
        self.idx += 1
        return USHORT_NUMBERS[i]
    ushortFunc = objc.selector(ushortFunc, signature=OC_TestClass1.ushortFunc.signature)

    def intFunc(self):
        i = self.idx
        self.idx += 1
        return INT_NUMBERS[i]
    intFunc = objc.selector(intFunc, signature=OC_TestClass1.intFunc.signature)

    def uintFunc(self):
        i = self.idx
        self.idx += 1
        return UINT_NUMBERS[i]
    uintFunc = objc.selector(uintFunc, signature=OC_TestClass1.uintFunc.signature)

    def longFunc(self):
        i = self.idx
        self.idx += 1
        return LONG_NUMBERS[i]
    longFunc = objc.selector(longFunc, signature=OC_TestClass1.longFunc.signature)

    def ulongFunc(self):
        i = self.idx
        self.idx += 1
        return ULONG_NUMBERS[i]
    ulongFunc = objc.selector(ulongFunc, signature=OC_TestClass1.ulongFunc.signature)

    def longlongFunc(self):
        i = self.idx
        self.idx += 1
        return LONGLONG_NUMBERS[i]
    longlongFunc = objc.selector(longlongFunc, signature=OC_TestClass1.longlongFunc.signature)

    def ulonglongFunc(self):
        i = self.idx
        self.idx += 1
        return ULONGLONG_NUMBERS[i]
    ulonglongFunc = objc.selector(ulonglongFunc, signature=OC_TestClass1.ulonglongFunc.signature)

    def floatFunc(self):
        i = self.idx
        self.idx += 1
        return FLOAT_NUMBERS[i]
    floatFunc = objc.selector(floatFunc, signature=OC_TestClass1.floatFunc.signature)

    def doubleFunc(self):
        i = self.idx
        self.idx += 1
        return DOUBLE_NUMBERS[i]
    doubleFunc = objc.selector(doubleFunc, signature=OC_TestClass1.doubleFunc.signature)

    def idFunc(self):
        i = self.idx
        self.idx += 1
        return OBJECTS[i]

    def dummyFunc(self):
        i = self.idx
        self.idx += 1
        return DUMMY_OBJECTS[i]
    dummyFunc = objc.selector(dummyFunc, signature=OC_TestClass1.dummyFunc.signature)

    def dummy2Func(self):
        i = self.idx
        self.idx += 1
        return DUMMY2_OBJECTS[i]
    dummy2Func = objc.selector(dummy2Func, signature=OC_TestClass1.dummy2Func.signature)

    def nspointFunc(self):
        i = self.idx
        self.idx += 1
        return POINTS[i]
    nspointFunc = objc.selector(nspointFunc, signature=OC_TestClass1.nspointFunc.signature)

    def charArg_(self, arg):
        return arg * 2
    charArg_ = objc.selector(charArg_, signature=OC_TestClass1.charArg_.signature)
    def ucharArg_(self, arg):
        return arg * 2
    ucharArg_ = objc.selector(ucharArg_, signature=OC_TestClass1.ucharArg_.signature)

    def shortArg_(self, arg):
        return arg * 2
    shortArg_ = objc.selector(shortArg_, signature=OC_TestClass1.shortArg_.signature)

    def ushortArg_(self, arg):
        return arg * 2
    ushortArg_ = objc.selector(ushortArg_, signature=OC_TestClass1.ushortArg_.signature)

    def intArg_(self, arg):
        return arg * 2
    intArg_ = objc.selector(intArg_, signature=OC_TestClass1.intArg_.signature)

    def uintArg_(self, arg):
        return arg * 2
    uintArg_ = objc.selector(uintArg_, signature=OC_TestClass1.uintArg_.signature)

    def longArg_(self, arg):
        return arg * 2
    longArg_ = objc.selector(longArg_, signature=OC_TestClass1.longArg_.signature)

    def ulongArg_(self, arg):
        return arg * 2
    ulongArg_ = objc.selector(ulongArg_, signature=OC_TestClass1.ulongArg_.signature)

    def longlongArg_(self, arg):
        return arg * 2
    longlongArg_ = objc.selector(longlongArg_, signature=OC_TestClass1.longlongArg_.signature)

    def ulonglongArg_(self, arg):
        return arg * 2
    ulonglongArg_ = objc.selector(ulonglongArg_, signature=OC_TestClass1.ulonglongArg_.signature)

    def floatArg_(self, arg):
        return arg * 2
    floatArg_ = objc.selector(floatArg_, signature=OC_TestClass1.floatArg_.signature)

    def doubleArg_(self, arg):
        return arg * 2
    doubleArg_ = objc.selector(doubleArg_, signature=OC_TestClass1.doubleArg_.signature)


class OCPyTestSimpleCalls(TestCase):
    #
    # Test argument passing of single basic values by reference.
    #
    def setUp(self):
        self.pyobj = MyPyClass()
        self.ocobj = MyOCClass.new()
        self.obj = OC_TestClass2.new()

    def testCChar(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in CHAR_NUMBERS[:-3]:
            if isinstance(o, str):
                o = ord(o)
            self.assertEquals(self.obj.callInstanceCharFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.callInstanceCharFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceCharFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceCharFuncOf_, self.ocobj)

    def testIChar(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in CHAR_NUMBERS[:-3]:
            if isinstance(o, str):
                o = ord(o)
            self.assertEquals(self.obj.invokeInstanceCharFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.invokeInstanceCharFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceCharFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceCharFuncOf_, self.ocobj)

    def testCUChar(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in UCHAR_NUMBERS[:-3]:
            if isinstance(o, str):
                o = ord(o)
            self.assertEquals(self.obj.callInstanceUnsignedCharFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.callInstanceUnsignedCharFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceUnsignedCharFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceUnsignedCharFuncOf_, self.ocobj)

    def testIUChar(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in UCHAR_NUMBERS[:-3]:
            if isinstance(o, str):
                o = ord(o)
            self.assertEquals(self.obj.invokeInstanceUnsignedCharFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedCharFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedCharFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedCharFuncOf_, self.ocobj)

    def testCShort(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in SHORT_NUMBERS[:-3]:
            self.assertEquals(self.obj.callInstanceShortFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.callInstanceShortFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceShortFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceShortFuncOf_, self.ocobj)

    def testIShort(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in SHORT_NUMBERS[:-3]:
            self.assertEquals(self.obj.invokeInstanceShortFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.invokeInstanceShortFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceShortFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceShortFuncOf_, self.ocobj)

    def testCUShort(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in USHORT_NUMBERS[:-3]:
            self.assertEquals(self.obj.callInstanceUnsignedShortFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.callInstanceUnsignedShortFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceUnsignedShortFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceUnsignedShortFuncOf_, self.ocobj)

    def testIUShort(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in USHORT_NUMBERS[:-3]:
            self.assertEquals(self.obj.invokeInstanceUnsignedShortFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedShortFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedShortFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedShortFuncOf_, self.ocobj)

    def testCInt(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in INT_NUMBERS[:-3]:
            self.assertEquals(self.obj.callInstanceIntFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.callInstanceIntFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceIntFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceIntFuncOf_, self.ocobj)

    def testIInt(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in INT_NUMBERS[:-3]:
            self.assertEquals(self.obj.invokeInstanceIntFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.invokeInstanceIntFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceIntFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceIntFuncOf_, self.ocobj)

    def testCUInt(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in UINT_NUMBERS[:-3]:
            self.assertEquals(self.obj.callInstanceUnsignedIntFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.callInstanceUnsignedIntFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceUnsignedIntFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceUnsignedIntFuncOf_, self.ocobj)

    def testIUInt(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in UINT_NUMBERS[:-3]:
            self.assertEquals(self.obj.invokeInstanceUnsignedIntFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedIntFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedIntFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedIntFuncOf_, self.ocobj)

    def testCLong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in LONG_NUMBERS[:-3]:
            self.assertEquals(self.obj.callInstanceLongFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.callInstanceLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceLongFuncOf_, self.ocobj)

    def testILong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in LONG_NUMBERS[:-3]:
            self.assertEquals(self.obj.invokeInstanceLongFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.invokeInstanceLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceLongFuncOf_, self.ocobj)

    def testCULong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in ULONG_NUMBERS[:-3]:
            self.assertEquals(self.obj.callInstanceUnsignedLongFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.callInstanceUnsignedLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceUnsignedLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceUnsignedLongFuncOf_, self.ocobj)

    def testIULong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in ULONG_NUMBERS[:-3]:
            self.assertEquals(self.obj.invokeInstanceUnsignedLongFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedLongFuncOf_, self.ocobj)

    def testCLongLong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in LONGLONG_NUMBERS[:-3]:
            self.assertEquals(self.obj.callInstanceLongLongFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.callInstanceLongLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceLongLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceLongLongFuncOf_, self.ocobj)

    def testILongLong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in LONGLONG_NUMBERS[:-3]:
            self.assertEquals(self.obj.invokeInstanceLongLongFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.invokeInstanceLongLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceLongLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceLongLongFuncOf_, self.ocobj)

    def testCULongLong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in ULONGLONG_NUMBERS[:-3]:
            self.assertEquals(self.obj.callInstanceUnsignedLongLongFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.callInstanceUnsignedLongLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceUnsignedLongLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.callInstanceUnsignedLongLongFuncOf_, self.ocobj)

    def testIULongLong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in ULONGLONG_NUMBERS[:-3]:
            self.assertEquals(self.obj.invokeInstanceUnsignedLongLongFuncOf_(self.ocobj), o)

        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedLongLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedLongLongFuncOf_, self.ocobj)
        self.assertRaises(ValueError, self.obj.invokeInstanceUnsignedLongLongFuncOf_, self.ocobj)

    def testCFloat(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in FLOAT_NUMBERS:
            self.assertEquals(self.obj.callInstanceFloatFuncOf_(self.ocobj), o)

    def testIFloat(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in FLOAT_NUMBERS:
            self.assertEquals(self.obj.invokeInstanceFloatFuncOf_(self.ocobj), o)

    def testCDouble(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DOUBLE_NUMBERS:
            self.assertEquals(self.obj.callInstanceDoubleFuncOf_(self.ocobj), o)

    def testIDouble(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DOUBLE_NUMBERS:
            self.assertEquals(self.obj.invokeInstanceDoubleFuncOf_(self.ocobj), o)

    def testCId(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in OBJECTS:
            self.assertEquals(self.obj.callInstanceIdFuncOf_(self.ocobj), o)

    def testIId(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in OBJECTS:
            self.assertEquals(self.obj.invokeInstanceIdFuncOf_(self.ocobj), o)

    def testCId2(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in OBJECTS:
            self.assertEquals(self.obj.callInstanceIdFuncOf_(self.pyobj), o)

    def testIId2(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in OBJECTS:
            self.assertEquals(self.obj.invokeInstanceIdFuncOf_(self.pyobj), o)

    def testCStruct1(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DUMMY_OBJECTS:
            self.assertEquals(self.obj.callInstanceDummyFuncOf_(self.ocobj), o)

    def testIStruct1(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DUMMY_OBJECTS:
            self.assertEquals(self.obj.invokeInstanceDummyFuncOf_(self.ocobj), o)

    def testCStruct2(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DUMMY2_OBJECTS:
            self.assertEquals(self.obj.callInstanceDummy2FuncOf_(self.ocobj), o)

    def testIStruct2(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DUMMY2_OBJECTS:
            self.assertEquals(self.obj.invokeInstanceDummy2FuncOf_(self.ocobj), o)

    def testCNSPoint(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in POINTS:
            self.assertEquals(self.obj.callInstanceNSPointFuncOf_(self.ocobj), o)

    def testINSPoint(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in POINTS:
            self.assertEquals(self.obj.invokeInstanceNSPointFuncOf_(self.ocobj), o)

class OCPyTestSimpleArguments(TestCase):
    #
    # Test argument passing of single basic values.
    #
    # TODO: Copy and adapt rest of OCPyTestSimpleArguments
    #

    def setUp(self):
        self.ocobj = MyOCClass.new()
        self.obj = OC_TestClass2.new()

    def testCLongLong(self):
        self.assertEquals(self.obj.callInstanceLongLongArg_on_(0, self.ocobj), 0)
        self.assertEquals(self.obj.callInstanceLongLongArg_on_(10, self.ocobj), 20)
        self.assertEquals(self.obj.callInstanceLongLongArg_on_(1L << 60, self.ocobj), 1L << 61)
        self.assertEquals(self.obj.callInstanceLongLongArg_on_(-10, self.ocobj), -20)
        self.assertEquals(self.obj.callInstanceLongLongArg_on_(-(1L << 60), self.ocobj), -(1L << 61))

    def testILongLong(self):
        self.assertEquals(self.obj.invokeInstanceLongLongArg_on_(0, self.ocobj), 0)
        self.assertEquals(self.obj.invokeInstanceLongLongArg_on_(10, self.ocobj), 20)
        self.assertEquals(self.obj.invokeInstanceLongLongArg_on_(1L << 60, self.ocobj), 1L << 61)
        self.assertEquals(self.obj.invokeInstanceLongLongArg_on_(-10, self.ocobj), -20)
        self.assertEquals(self.obj.invokeInstanceLongLongArg_on_(-(1L << 60), self.ocobj), -(1L << 61))

if __name__ == '__main__':
    main()
