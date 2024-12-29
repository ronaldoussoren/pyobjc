"""
Test lowlevel message passing details (Python -> ObjC)

XXX:
    - Create script to regenerate this file (and corresponding C code)
    - Create multiple variants for tests (and support code):
        - objc.selector
        - objc.IMP
        - objc.function
        - Obective-C blocks
    - For all of these: create "simple" and "regular" variants
      (this definitely requires a generation script because the
       definition of "simple" can and will change).


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

import struct
import sys
import warnings

import objc
from PyObjCTest.testbndl import OC_TestClass1, OC_TestClass2
from PyObjCTools.TestSupport import TestCase

# Can't set the right signatures in plain Objective-C.
for method, argmeta in [
    (b"passInOutChar:", {2: {"type_modifier": b"N"}}),
    (b"passOutChar:", {2: {"type_modifier": b"o"}}),
    (b"passInChar:", {2: {"type_modifier": b"n"}}),
    (b"passInOutUChar:", {2: {"type_modifier": b"N", "type": "^C"}}),
    (b"passOutUChar:", {2: {"type_modifier": b"o", "type": "^C"}}),
    (b"passInUChar:", {2: {"type_modifier": b"n", "type": "^C"}}),
    (b"passInOutShort:", {2: {"type_modifier": b"N"}}),
    (b"passOutShort:", {2: {"type_modifier": b"o"}}),
    (b"passInShort:", {2: {"type_modifier": b"n"}}),
    (b"passInOutUShort:", {2: {"type_modifier": b"N"}}),
    (b"passOutUShort:", {2: {"type_modifier": b"o"}}),
    (b"passInUShort:", {2: {"type_modifier": b"n"}}),
    (b"passInOutInt:", {2: {"type_modifier": b"N"}}),
    (b"passOutInt:", {2: {"type_modifier": b"o"}}),
    (b"passInInt:", {2: {"type_modifier": b"n"}}),
    (b"passInOutUInt:", {2: {"type_modifier": b"N"}}),
    (b"passOutUInt:", {2: {"type_modifier": b"o"}}),
    (b"passInUInt:", {2: {"type_modifier": b"n"}}),
    (b"passInOutLong:", {2: {"type_modifier": b"N"}}),
    (b"passOutLong:", {2: {"type_modifier": b"o"}}),
    (b"passInLong:", {2: {"type_modifier": b"n"}}),
    (b"passInOutULong:", {2: {"type_modifier": b"N"}}),
    (b"passOutULong:", {2: {"type_modifier": b"o"}}),
    (b"passInULong:", {2: {"type_modifier": b"n"}}),
    (b"passInOutLongLong:", {2: {"type_modifier": b"N"}}),
    (b"passOutLongLong:", {2: {"type_modifier": b"o"}}),
    (b"passInLongLong:", {2: {"type_modifier": b"n"}}),
    (b"passInOutULongLong:", {2: {"type_modifier": b"N"}}),
    (b"passOutULongLong:", {2: {"type_modifier": b"o"}}),
    (b"passInULongLong:", {2: {"type_modifier": b"n"}}),
    (b"passInOutFloat:", {2: {"type_modifier": b"N"}}),
    (b"passOutFloat:", {2: {"type_modifier": b"o"}}),
    (b"passInFloat:", {2: {"type_modifier": b"n"}}),
    (b"passInOutDouble:", {2: {"type_modifier": b"N"}}),
    (b"passInOutLongDouble:", {2: {"type_modifier": b"N"}}),
    (b"passOutDouble:", {2: {"type_modifier": b"o"}}),
    (b"passOutLongDouble:", {2: {"type_modifier": b"o"}}),
    (b"passInDouble:", {2: {"type_modifier": b"n"}}),
    (b"passInLongDouble:", {2: {"type_modifier": b"n"}}),
    (b"passInOutCharp:", {2: {"type_modifier": b"N"}}),
    (b"passOutCharp:", {2: {"type_modifier": b"o"}}),
    (b"passInCharp:", {2: {"type_modifier": b"n"}}),
    (b"passInOutID:", {2: {"type_modifier": b"N"}}),
    (b"passOutID:", {2: {"type_modifier": b"o"}}),
    (b"passInID:", {2: {"type_modifier": b"n"}}),
]:
    objc.registerMetaDataForSelector(b"OC_TestClass1", method, {"arguments": argmeta})


def makeCFloat(value):
    """
    C floats and doubles have a different representation, this function returns
    the result of converting a python float (== C double) to a C float and back.
    """
    return struct.unpack("f", struct.pack("f", value))[0]


class PyOCTestSimpleReturns(TestCase):
    #
    # Test returns of simple types from instance and classs methods
    #
    def testClsLongLong(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.longlongClsFunc(), -(1 << 60))
        self.assertEqual(OC_TestClass1.longlongClsFunc(), -42)
        self.assertEqual(OC_TestClass1.longlongClsFunc(), 0)
        self.assertEqual(OC_TestClass1.longlongClsFunc(), 42)
        self.assertEqual(OC_TestClass1.longlongClsFunc(), (1 << 60))

    def testClsULongLong(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.ulonglongClsFunc(), 0)
        self.assertEqual(OC_TestClass1.ulonglongClsFunc(), 42)
        self.assertEqual(OC_TestClass1.ulonglongClsFunc(), (1 << 63))

    def testClsLong(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.longClsFunc(), -(1 << 30))
        self.assertEqual(OC_TestClass1.longClsFunc(), -42)
        self.assertEqual(OC_TestClass1.longClsFunc(), 0)
        self.assertEqual(OC_TestClass1.longClsFunc(), 42)
        self.assertEqual(OC_TestClass1.longClsFunc(), (1 << 30))

    def testClsULong(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.ulongClsFunc(), 0)
        self.assertEqual(OC_TestClass1.ulongClsFunc(), 42)
        self.assertEqual(OC_TestClass1.ulongClsFunc(), (1 << 30))

    def testClsInt(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.intClsFunc(), -(1 << 30))
        self.assertEqual(OC_TestClass1.intClsFunc(), -42)
        self.assertEqual(OC_TestClass1.intClsFunc(), 0)
        self.assertEqual(OC_TestClass1.intClsFunc(), 42)
        self.assertEqual(OC_TestClass1.intClsFunc(), (1 << 30))

    def testClsUInt(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.uintClsFunc(), 0)
        self.assertEqual(OC_TestClass1.uintClsFunc(), 42)
        self.assertEqual(OC_TestClass1.uintClsFunc(), (1 << 30))

    def testClsShort(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.shortClsFunc(), -(1 << 14))
        self.assertEqual(OC_TestClass1.shortClsFunc(), -42)
        self.assertEqual(OC_TestClass1.shortClsFunc(), 0)
        self.assertEqual(OC_TestClass1.shortClsFunc(), 42)
        self.assertEqual(OC_TestClass1.shortClsFunc(), (1 << 14))

    def testClsUShort(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.ushortClsFunc(), 0)
        self.assertEqual(OC_TestClass1.ushortClsFunc(), 42)
        self.assertEqual(OC_TestClass1.ushortClsFunc(), (1 << 14))

    def testClsChar(self):
        # Fails with libffi due to the way we treat 'char' at the moment
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.charClsFunc(), -128)
        self.assertEqual(OC_TestClass1.charClsFunc(), 0)
        self.assertEqual(OC_TestClass1.charClsFunc(), 127)

    def testClsUChar(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.ucharClsFunc(), 0)
        self.assertEqual(OC_TestClass1.ucharClsFunc(), 128)
        self.assertEqual(OC_TestClass1.ucharClsFunc(), 255)

    def testClsFloat(self):
        # Fails, possibly rounding error
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.floatClsFunc(), makeCFloat(0.128))
        self.assertEqual(OC_TestClass1.floatClsFunc(), makeCFloat(1.0))
        self.assertEqual(OC_TestClass1.floatClsFunc(), makeCFloat(42.0))
        self.assertEqual(OC_TestClass1.floatClsFunc(), makeCFloat(1e10))

    def testClsDouble(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.doubleClsFunc(), 0.128)
        self.assertEqual(OC_TestClass1.doubleClsFunc(), 1.0)
        self.assertEqual(OC_TestClass1.doubleClsFunc(), 42.0)
        self.assertEqual(OC_TestClass1.doubleClsFunc(), 1e10)

    def testClsLongDouble(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.longdoubleClsFunc(), 0.128)
        self.assertEqual(OC_TestClass1.longdoubleClsFunc(), 1.0)
        self.assertEqual(OC_TestClass1.longdoubleClsFunc(), 42.0)
        self.assertEqual(OC_TestClass1.longdoubleClsFunc(), 1e10)

    def testClsCharp(self):
        OC_TestClass1.clsReset()
        self.assertEqual(OC_TestClass1.charpClsFunc(), b"hello")
        self.assertEqual(OC_TestClass1.charpClsFunc(), b"world")
        self.assertEqual(OC_TestClass1.charpClsFunc(), b"foobar")

    def testClsID(self):
        OC_TestClass1.clsReset()
        self.assertEqual(len(OC_TestClass1.idClsFunc()), 0)
        self.assertEqual(type(OC_TestClass1.idClsFunc()).__name__, "NSHost")
        self.assertIn(str(OC_TestClass1.idClsFunc()), ("{}", "{\n}"))
        self.assertEqual(OC_TestClass1.idClsFunc(), None)

    # testCls* ends here

    def testLongLong(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.longlongFunc(), -(1 << 60))
        self.assertEqual(obj.longlongFunc(), -42)
        self.assertEqual(obj.longlongFunc(), 0)
        self.assertEqual(obj.longlongFunc(), 42)
        self.assertEqual(obj.longlongFunc(), (1 << 60))

    def testULongLong(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.ulonglongFunc(), 0)
        self.assertEqual(obj.ulonglongFunc(), 42)
        self.assertEqual(obj.ulonglongFunc(), (1 << 63))

    def testLong(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.longFunc(), -(1 << 30))
        self.assertEqual(obj.longFunc(), -42)
        self.assertEqual(obj.longFunc(), 0)
        self.assertEqual(obj.longFunc(), 42)
        self.assertEqual(obj.longFunc(), (1 << 30))

    def testULong(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.ulongFunc(), 0)
        self.assertEqual(obj.ulongFunc(), 42)
        self.assertEqual(obj.ulongFunc(), (1 << 30))

    def testInt(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.intFunc(), -(1 << 30))
        self.assertEqual(obj.intFunc(), -42)
        self.assertEqual(obj.intFunc(), 0)
        self.assertEqual(obj.intFunc(), 42)
        self.assertEqual(obj.intFunc(), (1 << 30))

    def testUInt(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.uintFunc(), 0)
        self.assertEqual(obj.uintFunc(), 42)
        self.assertEqual(obj.uintFunc(), (1 << 30))

    def testShort(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.shortFunc(), -(1 << 14))
        self.assertEqual(obj.shortFunc(), -42)
        self.assertEqual(obj.shortFunc(), 0)
        self.assertEqual(obj.shortFunc(), 42)
        self.assertEqual(obj.shortFunc(), (1 << 14))

    def testUShort(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.ushortFunc(), 0)
        self.assertEqual(obj.ushortFunc(), 42)
        self.assertEqual(obj.ushortFunc(), (1 << 14))

    def testChar(self):
        obj = OC_TestClass1.new()
        # Fails with libffi due to the way we treat 'char' at the moment
        obj.reset()
        self.assertEqual(obj.charFunc(), -128)
        self.assertEqual(obj.charFunc(), 0)
        self.assertEqual(obj.charFunc(), 127)

    def testUChar(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.ucharFunc(), 0)
        self.assertEqual(obj.ucharFunc(), 128)
        self.assertEqual(obj.ucharFunc(), 255)

    def testFloat(self):
        # Fails, possibly rounding error
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.floatFunc(), makeCFloat(0.128))
        self.assertEqual(obj.floatFunc(), makeCFloat(1.0))
        self.assertEqual(obj.floatFunc(), makeCFloat(42.0))
        self.assertEqual(obj.floatFunc(), makeCFloat(1e10))

    def testDouble(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.doubleFunc(), 0.128)
        self.assertEqual(obj.doubleFunc(), 1.0)
        self.assertEqual(obj.doubleFunc(), 42.0)
        self.assertEqual(obj.doubleFunc(), 1e10)

    def testLongDouble(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.longdoubleFunc(), 0.128)
        self.assertEqual(obj.longdoubleFunc(), 1.0)
        self.assertEqual(obj.longdoubleFunc(), 42.0)
        self.assertEqual(obj.longdoubleFunc(), 1e10)

    def testCharp(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(obj.charpFunc(), b"hello")
        self.assertEqual(obj.charpFunc(), b"world")
        self.assertEqual(obj.charpFunc(), b"foobar")

    def testID(self):
        obj = OC_TestClass1.new()
        obj.reset()
        self.assertEqual(len(obj.idFunc()), 0)
        self.assertEqual(type(obj.idFunc()).__name__, "NSHost")
        self.assertIn(str(obj.idFunc()), ("{}", "{\n}"))
        self.assertEqual(obj.idFunc(), None)

    def testStruct1(self):
        obj = OC_TestClass1.new()

        self.assertEqual(obj.dummyFunc(), (-1, 1))

    def testStruct2(self):
        obj = OC_TestClass1.new()

        self.assertEqual(obj.dummy2Func(), ((1, 2, 3, 4),))


class PyOCTestSimpleArguments(TestCase):
    #
    # Test argument passing of single basic values.
    #
    def setUp(self):
        self.obj = OC_TestClass1.new()

    def testLongLong(self):
        self.assertEqual(self.obj.longlongArg_(0), 0)
        self.assertEqual(self.obj.longlongArg_(10), 5)
        self.assertEqual(self.obj.longlongArg_(10), 5)
        self.assertEqual(self.obj.longlongArg_(1 << 60), (1 << 59))
        self.assertEqual(self.obj.longlongArg_(-10), -5)
        self.assertEqual(self.obj.longlongArg_(-10), -5)
        self.assertEqual(self.obj.longlongArg_(-1 << 60), -(1 << 59))

        # TODO: Out of range values

    def testULongLong(self):
        self.assertEqual(self.obj.ulonglongArg_(0), 0)
        self.assertEqual(self.obj.ulonglongArg_(10), 5)
        self.assertEqual(self.obj.ulonglongArg_(10), 5)
        self.assertEqual(self.obj.ulonglongArg_(1 << 60), (1 << 59))

        # TODO: Out of range values

    def testLong(self):
        self.assertEqual(self.obj.longArg_(0), 0)
        self.assertEqual(self.obj.longArg_(10), 5)
        self.assertEqual(self.obj.longArg_(10), 5)
        self.assertEqual(self.obj.longArg_(1 << 30), (1 << 29))
        self.assertEqual(self.obj.longArg_(-10), -5)
        self.assertEqual(self.obj.longArg_(-10), -5)
        self.assertEqual(self.obj.longArg_(-1 << 30), -(1 << 29))

        # TODO: Out of range values

    def testULong(self):
        self.assertEqual(self.obj.ulongArg_(0), 0)
        self.assertEqual(self.obj.ulongArg_(10), 5)
        self.assertEqual(self.obj.ulongArg_(10), 5)
        self.assertEqual(self.obj.ulongArg_(1 << 30), (1 << 29))

        # TODO: Out of range values

    def testInt(self):
        self.assertEqual(self.obj.intArg_(0), 0)
        self.assertEqual(self.obj.intArg_(10), 5)
        self.assertEqual(self.obj.intArg_(10), 5)
        self.assertEqual(self.obj.intArg_(1 << 30), (1 << 29))
        self.assertEqual(self.obj.intArg_(-10), -5)
        self.assertEqual(self.obj.intArg_(-10), -5)
        self.assertEqual(self.obj.intArg_(-1 << 30), -(1 << 29))

        self.assertEqual(self.obj.intArg_(10.0), 5)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'int', got 'int' of wrong magnitude"
        ):
            self.obj.intArg_(sys.maxsize + 1)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'int', got 'int' of wrong magnitude"
        ):
            self.obj.intArg_(-sys.maxsize - 2)
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'float'"):
            self.obj.intArg_(-float(sys.maxsize) - 2)

    def testUInt(self):
        self.assertEqual(self.obj.uintArg_(0), 0)
        self.assertEqual(self.obj.uintArg_(10), 5)
        self.assertEqual(self.obj.uintArg_(10), 5)
        self.assertEqual(self.obj.uintArg_(1 << 30), (1 << 29))

        self.assertEqual(self.obj.uintArg_(10.0), 5)

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned int', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.uintArg_(-5)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned int', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.uintArg_(-5)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned int', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.uintArg_(1 + 2 * (sys.maxsize + 1))

    def testShort(self):
        self.assertEqual(self.obj.shortArg_(0), 0)
        self.assertEqual(self.obj.shortArg_(10), 5)
        self.assertEqual(self.obj.shortArg_(10), 5)
        self.assertEqual(self.obj.shortArg_(1 << 14), (1 << 13))
        self.assertEqual(self.obj.shortArg_(-10), -5)
        self.assertEqual(self.obj.shortArg_(-10), -5)
        self.assertEqual(self.obj.shortArg_(-(1 << 14)), -(1 << 13))

        self.assertEqual(self.obj.shortArg_(10.0), 5)

        # Out of range arguments, assumes a short is 16 bits
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'short', got 'int' of wrong magnitude"
        ):
            self.obj.shortArg_(-(1 << 16) - 1)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'short', got 'int' of wrong magnitude"
        ):
            self.obj.shortArg_(1 << 16)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'short', got 'int' of wrong magnitude"
        ):
            self.obj.shortArg_(-(1 << 16) - 1)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'short', got 'int' of wrong magnitude"
        ):
            self.obj.shortArg_(1 << 16)

    def testUShort(self):
        self.assertEqual(self.obj.ushortArg_(0), 0)
        self.assertEqual(self.obj.ushortArg_(10), 5)
        self.assertEqual(self.obj.ushortArg_(10), 5)
        self.assertEqual(self.obj.ushortArg_(1 << 14), (1 << 13))

        self.assertEqual(self.obj.ushortArg_(10.0), 5)

        # Out of range arguments, assumes a short is 16 bits
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned short', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ushortArg_(-5)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned short', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ushortArg_(-(1 << 16) - 1)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned short', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ushortArg_(1 << 16)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned short', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ushortArg_(-5)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned short', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ushortArg_(-(1 << 16) - 1)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned short', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ushortArg_(1 << 16)

    def testChar(self):
        self.assertEqual(self.obj.charArg_(0), (0))
        self.assertEqual(self.obj.charArg_(10), (5))
        self.assertEqual(self.obj.charArg_(10), (5))
        self.assertEqual(self.obj.charArg_(1 << 6), (1 << 5))
        self.assertEqual(self.obj.charArg_(b"\x00"), 0x00)
        self.assertEqual(self.obj.charArg_(b"\x10"), int(ord(b"\x10") / 2))

        # TODO: Out of range arguments

    def testUChar(self):
        self.assertEqual(self.obj.ucharArg_(0), 0)
        self.assertEqual(self.obj.ucharArg_(10), 5)
        self.assertEqual(self.obj.ucharArg_(10), 5)
        self.assertEqual(self.obj.ucharArg_(1 << 7), (1 << 6))
        self.assertEqual(self.obj.ucharArg_(b"\x00"), 0)
        self.assertEqual(self.obj.ucharArg_(b"\x10"), int(ord(b"\x10") / 2))

        self.assertEqual(self.obj.ucharArg_(10.0), 5)

        # Out of range arguments
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned char', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ucharArg_(-5)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned char', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ucharArg_(-256)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned char', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ucharArg_(256)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned char', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ucharArg_(-5)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned char', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ucharArg_(-256)
            with self.assertRaisesRegex(
                ValueError,
                r"depythonifying 'unsigned char', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
            ):
                self.obj.ucharArg_(256)

    def testCharp(self):
        self.assertEqual(self.obj.charpArg_(b"hello world"), b"dlrow olleh")

        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'int'"):
            self.obj.charpArg_(256)
        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'str'"):
            self.obj.charpArg_("hello world")

    def testIDPython(self):
        # Test a Python object as the argument
        s = self.obj.idArg_("hello")
        self.assertEqual(len(s), 1)
        self.assertEqual(s[0], "hello")

    def testIDOC(self):
        # Test an Objective-C object as the argument

        # NSHost gives problems on GNUstep, better check those problems
        # seperately in the Foundation test suite.
        # c = objc.lookUpClass("NSHost")
        # o = c.hostWithAddress_('127.0.0.1')

        c = objc.lookUpClass("NSScanner")
        o = c.scannerWithString_("hello world")
        s = self.obj.idArg_(o)
        self.assertEqual(len(s), 1)
        self.assertIs(s[0], o)

    def testStruct1(self):
        self.assertEqual(self.obj.dummyArg_((-1, 1)), (-2, 2))

        with self.assertRaisesRegex(
            TypeError, "depythonifying struct, got no sequence"
        ):
            self.obj.dummyArg_(256)
        with self.assertRaisesRegex(
            ValueError, "depythonifying struct of 2 members, got tuple of 1"
        ):
            self.obj.dummyArg_((-1,))
        with self.assertRaisesRegex(
            ValueError, "depythonifying struct of 2 members, got tuple of 3"
        ):
            self.obj.dummyArg_((-1, 1, 2))

    def testStruct2(self):
        self.assertEqual(self.obj.dummy2Arg_(((1, 2, 3, 4),)), ((8, 6, 4, 2),))

        with self.assertRaisesRegex(
            ValueError, "depythonifying struct of 1 members, got tuple of 2"
        ):
            self.obj.dummy2Arg_(((8, 6, 4, 2), 1))
        with self.assertRaisesRegex(
            ValueError, "depythonifying array of 4 items, got one of 3"
        ):
            self.obj.dummy2Arg_(((8, 6, 4),))
        with self.assertRaisesRegex(
            ValueError, "depythonifying array of 4 items, got one of 5"
        ):
            self.obj.dummy2Arg_(((8, 6, 4, 2, 1),))


class PyOCTestByReferenceArguments(TestCase):
    #
    # Test argument passing of single basic values by reference.
    #
    def setUp(self):
        self.obj = OC_TestClass1.new()

    def testCharIn(self):
        self.assertEqual(self.obj.passInChar_(b"\x10"), 0x19)

    def testCharOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutChar_(None), -128)
        self.assertEqual(self.obj.passOutChar_(None), 0)
        self.assertEqual(self.obj.passOutChar_(None), 127)

    def testCharInOut(self):
        self.assertEqual(self.obj.passInOutChar_(b"\x10"), 0x3A)

    def testUCharIn(self):
        self.assertEqual(self.obj.passInUChar_(10), 19)

    def testUCharOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutUChar_(None), 0)
        self.assertEqual(self.obj.passOutUChar_(None), 128)
        self.assertEqual(self.obj.passOutUChar_(None), 255)

    def testUCharInOut(self):
        self.assertEqual(self.obj.passInOutUChar_(10), 52)

    def testShortIn(self):
        self.assertEqual(self.obj.passInShort_(10), 19)
        self.assertEqual(self.obj.passInShort_(-100), -91)
        self.assertEqual(self.obj.passInShort_(-100.0), -91)

    def testShortOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutShort_(None), -(1 << 14))
        self.assertEqual(self.obj.passOutShort_(None), -42)
        self.assertEqual(self.obj.passOutShort_(None), 0)
        self.assertEqual(self.obj.passOutShort_(None), 42)
        self.assertEqual(self.obj.passOutShort_(None), 1 << 14)

    def testShortInOut(self):
        self.assertEqual(self.obj.passInOutShort_(10), 52)
        self.assertEqual(self.obj.passInOutShort_(-100), -58)
        self.assertEqual(self.obj.passInOutShort_(-100.0), -58)

    def testUShortIn(self):
        self.assertEqual(self.obj.passInUShort_(10), 19)

    def testUShortOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutUShort_(None), 0)
        self.assertEqual(self.obj.passOutUShort_(None), 42)
        self.assertEqual(self.obj.passOutUShort_(None), (1 << 14))

    def testUShortInOut(self):
        self.assertEqual(self.obj.passInOutUShort_(10), 52)

    def testIntIn(self):
        self.assertEqual(self.obj.passInInt_(10), 19)
        self.assertEqual(self.obj.passInInt_(-100), -91)

    def testIntOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutInt_(None), -(1 << 30))
        self.assertEqual(self.obj.passOutInt_(None), -42)
        self.assertEqual(self.obj.passOutInt_(None), 0)
        self.assertEqual(self.obj.passOutInt_(None), 42)
        self.assertEqual(self.obj.passOutInt_(None), (1 << 30))

    def testIntInOut(self):
        self.assertEqual(self.obj.passInOutInt_(10), 52)
        self.assertEqual(self.obj.passInOutInt_(-100), -58)
        self.assertEqual(self.obj.passInOutInt_(-100.0), -58)

    def testUIntIn(self):
        self.assertEqual(self.obj.passInUInt_(10), 19)

    def testUIntOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutUInt_(None), 0)
        self.assertEqual(self.obj.passOutUInt_(None), 42)
        self.assertEqual(self.obj.passOutUInt_(None), (1 << 30))

    def testUIntInOut(self):
        self.assertEqual(self.obj.passInOutUInt_(10), 52)
        self.assertEqual(self.obj.passInOutUInt_(10.0), 52)

    def testLongIn(self):
        self.assertEqual(self.obj.passInLong_(10), 19)
        self.assertEqual(self.obj.passInLong_(-100), -91)

    def testLongOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutLong_(None), -(1 << 30))
        self.assertEqual(self.obj.passOutLong_(None), -42)
        self.assertEqual(self.obj.passOutLong_(None), 0)
        self.assertEqual(self.obj.passOutLong_(None), 42)
        self.assertEqual(self.obj.passOutLong_(None), (1 << 30))

    def testLongInOut(self):
        self.assertEqual(self.obj.passInOutLong_(10), 52)
        self.assertEqual(self.obj.passInOutLong_(-100), -58)
        self.assertEqual(self.obj.passInOutLong_(-100.0), -58)

    def testULongIn(self):
        self.assertEqual(self.obj.passInULong_(10), 19)

    def testULongOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutULong_(None), 0)
        self.assertEqual(self.obj.passOutULong_(None), 42)
        self.assertEqual(self.obj.passOutULong_(None), (1 << 30))

    def testULongInOut(self):
        self.assertEqual(self.obj.passInOutULong_(10), 52)
        self.assertEqual(self.obj.passInOutULong_(10.0), 52)

    def testLongLongIn(self):
        self.assertEqual(self.obj.passInLongLong_(10), 19)
        self.assertEqual(self.obj.passInLongLong_(-100), -91)

    def testLongLongOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutLongLong_(None), -(1 << 60))
        self.assertEqual(self.obj.passOutLongLong_(None), -42)
        self.assertEqual(self.obj.passOutLongLong_(None), 0)
        self.assertEqual(self.obj.passOutLongLong_(None), 42)
        self.assertEqual(self.obj.passOutLongLong_(None), (1 << 60))

    def testLongLongInOut(self):
        self.assertEqual(self.obj.passInOutLongLong_(10), 52)
        self.assertEqual(self.obj.passInOutLongLong_(-100), -58)
        self.assertEqual(self.obj.passInOutLongLong_(-100.0), -58)

    def testULongLongIn(self):
        self.assertEqual(self.obj.passInULongLong_(10), 19)

    def testULongLongOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutULongLong_(None), 0)
        self.assertEqual(self.obj.passOutULongLong_(None), 42)
        self.assertEqual(self.obj.passOutULongLong_(None), (1 << 63))

    def testULongLongInOut(self):
        self.assertEqual(self.obj.passInOutULongLong_(10), 52)
        self.assertEqual(self.obj.passInOutULongLong_(10.0), 52)

    def testFloatIn(self):
        self.assertEqual(self.obj.passInFloat_(10), makeCFloat(90.0))
        self.assertEqual(self.obj.passInFloat_(0.11), makeCFloat(0.99))

    def testFloatOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutFloat_(None), makeCFloat(0.128))
        self.assertEqual(self.obj.passOutFloat_(None), makeCFloat(1.0))
        self.assertEqual(self.obj.passOutFloat_(None), makeCFloat(42.0))
        self.assertEqual(self.obj.passOutFloat_(None), makeCFloat(1e10))

    def testFloatInOut(self):
        self.assertEqual(self.obj.passInOutFloat_(10), makeCFloat(420))
        self.assertEqual(self.obj.passInOutFloat_(10.0), makeCFloat(420))
        self.assertEqual(self.obj.passInOutFloat_(0.01), makeCFloat(0.42))

    def testDoubleIn(self):
        self.assertEqual(self.obj.passInDouble_(10), 90.0)
        self.assertEqual(self.obj.passInDouble_(0.11), 0.99)

    def testLongDoubleIn(self):
        self.assertEqual(self.obj.passInLongDouble_(10), 90.0)
        self.assertEqual(self.obj.passInLongDouble_(0.11), 0.99)

    def testDoubleOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutDouble_(None), 0.128)
        self.assertEqual(self.obj.passOutDouble_(None), 1.0)
        self.assertEqual(self.obj.passOutDouble_(None), 42.0)
        self.assertEqual(self.obj.passOutDouble_(None), 1e10)

    def testLongDoubleOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutLongDouble_(None), 0.128)
        self.assertEqual(self.obj.passOutLongDouble_(None), 1.0)
        self.assertEqual(self.obj.passOutLongDouble_(None), 42.0)
        self.assertEqual(self.obj.passOutLongDouble_(None), 1e10)

    def testDoubleInOut(self):
        self.assertEqual(self.obj.passInOutDouble_(10), 420)
        self.assertEqual(self.obj.passInOutDouble_(10.0), 420)
        self.assertEqual(self.obj.passInOutDouble_(0.01), 0.42)

    def testLongDoubleInOut(self):
        self.assertEqual(self.obj.passInOutLongDouble_(10), 420)
        self.assertEqual(self.obj.passInOutLongDouble_(10.0), 420)
        self.assertEqual(self.obj.passInOutLongDouble_(0.01), 0.42)

    def testCharpIn(self):
        self.assertEqual(self.obj.passInCharp_(b"hello"), b"hheelllloo")
        self.assertEqual(self.obj.passInCharp_(b"abcde"), b"aabbccddee")

    def testCharpOut(self):
        self.obj.reset()
        self.assertEqual(self.obj.passOutCharp_(None), b"hello")
        self.assertEqual(self.obj.passOutCharp_(None), b"world")
        self.assertEqual(self.obj.passOutCharp_(None), b"foobar")

    def testCharpInOut(self):
        self.assertEqual(self.obj.passInOutCharp_(b"hello"), b"hheelllloo")
        self.assertEqual(self.obj.passInOutCharp_(b"abcdef"), b"aabbccddeeff")

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
CHAR_NUMBERS = [-128, -42, 0, 42, 127, b"a", 128, "hello", None]
UCHAR_NUMBERS = [0, 42, 255, b"a", 256, "hello", None]
SHORT_NUMBERS = [-32768, -42, 0, 32767, 32768, "hello", None]
USHORT_NUMBERS = [0, 42, 65535, 65536, "hello", None]
INT_NUMBERS = [-2_147_483_648, -42, 0, 2_147_483_647, 2_147_483_648, "hello", None]
UINT_NUMBERS = [0, 42, 4_294_967_295, 4_294_967_296, "hello", None]
LONG_NUMBERS = [-2_147_483_648, -42, 0, 2_147_483_647, sys.maxsize + 1, "hello", None]
ULONG_NUMBERS = [0, 42, 4_294_967_295, 2 * (sys.maxsize + 1), "hello", None]
LONGLONG_NUMBERS = [
    -9_223_372_036_854_775_808,
    -42,
    0,
    42,
    9_223_372_036_854_775_807,
    9_223_372_036_854_775_808,
    "hello",
    None,
]
ULONGLONG_NUMBERS = [
    0,
    42,
    18_446_744_073_709_551_615,
    18_446_744_073_709_551_616,
    "hello",
    None,
]

FLOAT_NUMBERS = [makeCFloat(0.1), makeCFloat(100.0)]
DOUBLE_NUMBERS = [1.5, 3.5, 1e10, 1.99e10]
LONG_DOUBLE_NUMBERS = [1.5, 3.5, 1e10, 1.99e10]
OBJECTS = ["hello", 1.0, range(4), lambda x: 10]
DUMMY_OBJECTS = [(1, 1), (-10, -10), (-4, -5), (0, 0), (10, 20)]
DUMMY2_OBJECTS = [((1, 2, 3, 4),), ((-9, -8, -7, -6),)]
POINTS = [(1.0, 2.0), (1e10, 2e10), (-0.5, 0.5)]


class MyPyClass:
    def __init__(self):
        self.idx = 0

    def reset(self):
        self.idx = 0

    def idFunc(self):
        i = self.idx
        self.idx += 1
        return OBJECTS[i]


class MyOCClass(objc.lookUpClass("NSObject")):
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

    longlongFunc = objc.selector(
        longlongFunc, signature=OC_TestClass1.longlongFunc.signature
    )

    def ulonglongFunc(self):
        i = self.idx
        self.idx += 1
        return ULONGLONG_NUMBERS[i]

    ulonglongFunc = objc.selector(
        ulonglongFunc, signature=OC_TestClass1.ulonglongFunc.signature
    )

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

    def longdoubleFunc(self):
        i = self.idx
        self.idx += 1
        return LONG_DOUBLE_NUMBERS[i]

    longdoubleFunc = objc.selector(
        longdoubleFunc, signature=OC_TestClass1.longdoubleFunc.signature
    )

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

    nspointFunc = objc.selector(
        nspointFunc, signature=OC_TestClass1.nspointFunc.signature
    )

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

    longlongArg_ = objc.selector(
        longlongArg_, signature=OC_TestClass1.longlongArg_.signature
    )

    def ulonglongArg_(self, arg):
        return arg * 2

    ulonglongArg_ = objc.selector(
        ulonglongArg_, signature=OC_TestClass1.ulonglongArg_.signature
    )

    def floatArg_(self, arg):
        return arg * 2

    floatArg_ = objc.selector(floatArg_, signature=OC_TestClass1.floatArg_.signature)

    def doubleArg_(self, arg):
        return arg * 2

    doubleArg_ = objc.selector(doubleArg_, signature=OC_TestClass1.doubleArg_.signature)

    def longdoubleArg_(self, arg):
        return arg * 2

    longdoubleArg_ = objc.selector(
        longdoubleArg_, signature=OC_TestClass1.longdoubleArg_.signature
    )


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
            if isinstance(o, (bytes, str)):
                o = ord(o)
            self.assertEqual(self.obj.callInstanceCharFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'char', got 'int' of wrong magnitude"
        ):
            self.obj.callInstanceCharFuncOf_(self.ocobj)
        with self.assertRaisesRegex(ValueError, "depythonifying 'char', got 'str'"):
            self.obj.callInstanceCharFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "charFunc: returned None, expecting a value"
        ):
            self.obj.callInstanceCharFuncOf_(self.ocobj)

    def testIChar(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in CHAR_NUMBERS[:-3]:
            if isinstance(o, (str, bytes)):
                o = ord(o)
            self.assertEqual(self.obj.invokeInstanceCharFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'char', got 'int' of wrong magnitude"
        ):
            self.obj.invokeInstanceCharFuncOf_(self.ocobj)
        with self.assertRaisesRegex(ValueError, "depythonifying 'char', got 'str'"):
            self.obj.invokeInstanceCharFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "charFunc: returned None, expecting a value"
        ):
            self.obj.invokeInstanceCharFuncOf_(self.ocobj)

    def testCUChar(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in UCHAR_NUMBERS[:-3]:
            if isinstance(o, (str, bytes)):
                o = ord(o)
            self.assertEqual(self.obj.callInstanceUnsignedCharFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError,
            r"depythonifying 'unsigned char', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
        ):
            self.obj.callInstanceUnsignedCharFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned char', got 'str'"
        ):
            self.obj.callInstanceUnsignedCharFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "ucharFunc: returned None, expecting a value"
        ):
            self.obj.callInstanceUnsignedCharFuncOf_(self.ocobj)

    def testIUChar(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in UCHAR_NUMBERS[:-3]:
            if isinstance(o, (bytes, str)):
                o = ord(o)
            self.assertEqual(self.obj.invokeInstanceUnsignedCharFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError,
            r"depythonifying 'unsigned char', got 'int' of wrong magnitude \(max 255, value 256\)",
        ):
            self.obj.invokeInstanceUnsignedCharFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned char', got 'str'"
        ):
            self.obj.invokeInstanceUnsignedCharFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "ucharFunc: returned None, expecting a value"
        ):
            self.obj.invokeInstanceUnsignedCharFuncOf_(self.ocobj)

    def testCShort(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in SHORT_NUMBERS[:-3]:
            self.assertEqual(self.obj.callInstanceShortFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'short', got 'int' of wrong magnitude"
        ):
            self.obj.callInstanceShortFuncOf_(self.ocobj)
        with self.assertRaisesRegex(ValueError, "depythonifying 'short', got 'str'"):
            self.obj.callInstanceShortFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "shortFunc: returned None, expecting a value"
        ):
            self.obj.callInstanceShortFuncOf_(self.ocobj)

    def testIShort(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in SHORT_NUMBERS[:-3]:
            self.assertEqual(self.obj.invokeInstanceShortFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'short', got 'int' of wrong magnitude"
        ):
            self.obj.invokeInstanceShortFuncOf_(self.ocobj)
        with self.assertRaisesRegex(ValueError, "depythonifying 'short', got 'str'"):
            self.obj.invokeInstanceShortFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "shortFunc: returned None, expecting a value"
        ):
            self.obj.invokeInstanceShortFuncOf_(self.ocobj)

    def testCUShort(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in USHORT_NUMBERS[:-3]:
            self.assertEqual(self.obj.callInstanceUnsignedShortFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError,
            r"depythonifying 'unsigned short', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
        ):
            self.obj.callInstanceUnsignedShortFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned short', got 'str'"
        ):
            self.obj.callInstanceUnsignedShortFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "ushortFunc: returned None, expecting a value"
        ):
            self.obj.callInstanceUnsignedShortFuncOf_(self.ocobj)

    def testIUShort(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in USHORT_NUMBERS[:-3]:
            self.assertEqual(self.obj.invokeInstanceUnsignedShortFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError,
            r"depythonifying 'unsigned short', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
        ):
            self.obj.invokeInstanceUnsignedShortFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, r"depythonifying 'unsigned short', got 'str'"
        ):
            self.obj.invokeInstanceUnsignedShortFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, r"ushortFunc: returned None, expecting a value"
        ):
            self.obj.invokeInstanceUnsignedShortFuncOf_(self.ocobj)

    def testCInt(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in INT_NUMBERS[:-3]:
            self.assertEqual(self.obj.callInstanceIntFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'int', got 'int' of wrong magnitude"
        ):
            self.obj.callInstanceIntFuncOf_(self.ocobj)
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            self.obj.callInstanceIntFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "intFunc: returned None, expecting a value"
        ):
            self.obj.callInstanceIntFuncOf_(self.ocobj)

    def testIInt(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in INT_NUMBERS[:-3]:
            self.assertEqual(self.obj.invokeInstanceIntFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'int', got 'int' of wrong magnitude"
        ):
            self.obj.invokeInstanceIntFuncOf_(self.ocobj)
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str' of 5"):
            self.obj.invokeInstanceIntFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "intFunc: returned None, expecting a value"
        ):
            self.obj.invokeInstanceIntFuncOf_(self.ocobj)

    def testCUInt(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in UINT_NUMBERS[:-3]:
            self.assertEqual(self.obj.callInstanceUnsignedIntFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError,
            r"depythonifying 'unsigned int', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
        ):
            self.obj.callInstanceUnsignedIntFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            self.obj.callInstanceUnsignedIntFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "uintFunc: returned None, expecting a value"
        ):
            self.obj.callInstanceUnsignedIntFuncOf_(self.ocobj)

    def testIUInt(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in UINT_NUMBERS[:-3]:
            self.assertEqual(self.obj.invokeInstanceUnsignedIntFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError,
            r"depythonifying 'unsigned int', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
        ):
            self.obj.invokeInstanceUnsignedIntFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            self.obj.invokeInstanceUnsignedIntFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "uintFunc: returned None, expecting a value"
        ):
            self.obj.invokeInstanceUnsignedIntFuncOf_(self.ocobj)

    def testCLong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in LONG_NUMBERS[:-3]:
            self.assertEqual(self.obj.callInstanceLongFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'int' of wrong magnitude"
        ):
            self.obj.callInstanceLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            self.obj.callInstanceLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "longFunc: returned None, expecting a value"
        ):
            self.obj.callInstanceLongFuncOf_(self.ocobj)

    def testILong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in LONG_NUMBERS[:-3]:
            self.assertEqual(self.obj.invokeInstanceLongFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying '(long )?long', got 'int' of wrong magnitude"
        ):
            self.obj.invokeInstanceLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying '(long )?long', got 'str'"
        ):
            self.obj.invokeInstanceLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "longFunc: returned None, expecting a value"
        ):
            self.obj.invokeInstanceLongFuncOf_(self.ocobj)

    def testCULong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in ULONG_NUMBERS[:-3]:
            self.assertEqual(self.obj.callInstanceUnsignedLongFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError,
            r"depythonifying 'unsigned long long', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
        ):
            self.obj.callInstanceUnsignedLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            self.obj.callInstanceUnsignedLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "ulongFunc: returned None, expecting a value"
        ):
            self.obj.callInstanceUnsignedLongFuncOf_(self.ocobj)

    def testIULong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in ULONG_NUMBERS[:-3]:
            self.assertEqual(self.obj.invokeInstanceUnsignedLongFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError,
            r"depythonifying 'unsigned long long', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
        ):
            self.obj.invokeInstanceUnsignedLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            self.obj.invokeInstanceUnsignedLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "ulongFunc: returned None, expecting a value"
        ):
            self.obj.invokeInstanceUnsignedLongFuncOf_(self.ocobj)

    def testCLongLong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in LONGLONG_NUMBERS[:-3]:
            self.assertEqual(self.obj.callInstanceLongLongFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'int' of wrong magnitude"
        ):
            self.obj.callInstanceLongLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            self.obj.callInstanceLongLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "longlongFunc: returned None, expecting a value"
        ):
            self.obj.callInstanceLongLongFuncOf_(self.ocobj)

    def testILongLong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in LONGLONG_NUMBERS[:-3]:
            self.assertEqual(self.obj.invokeInstanceLongLongFuncOf_(self.ocobj), o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'int' of wrong magnitude"
        ):
            self.obj.invokeInstanceLongLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            self.obj.invokeInstanceLongLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "longlongFunc: returned None, expecting a value"
        ):
            self.obj.invokeInstanceLongLongFuncOf_(self.ocobj)

    def testCULongLong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in ULONGLONG_NUMBERS[:-3]:
            self.assertEqual(
                self.obj.callInstanceUnsignedLongLongFuncOf_(self.ocobj), o
            )

        with self.assertRaisesRegex(
            ValueError,
            r"depythonifying 'unsigned long long', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
        ):
            self.obj.callInstanceUnsignedLongLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            self.obj.callInstanceUnsignedLongLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "ulonglongFunc: returned None, expecting a value"
        ):
            self.obj.callInstanceUnsignedLongLongFuncOf_(self.ocobj)

    def testIULongLong(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in ULONGLONG_NUMBERS[:-3]:
            self.assertEqual(
                self.obj.invokeInstanceUnsignedLongLongFuncOf_(self.ocobj), o
            )

        with self.assertRaisesRegex(
            ValueError,
            r"depythonifying 'unsigned long long', got 'int' of wrong magnitude \(max [0-9]+, value [0-9]+\)",
        ):
            self.obj.invokeInstanceUnsignedLongLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            self.obj.invokeInstanceUnsignedLongLongFuncOf_(self.ocobj)
        with self.assertRaisesRegex(
            ValueError, "ulonglongFunc: returned None, expecting a value"
        ):
            self.obj.invokeInstanceUnsignedLongLongFuncOf_(self.ocobj)

    def testCFloat(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in FLOAT_NUMBERS:
            self.assertEqual(self.obj.callInstanceFloatFuncOf_(self.ocobj), o)

    def testIFloat(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in FLOAT_NUMBERS:
            self.assertEqual(self.obj.invokeInstanceFloatFuncOf_(self.ocobj), o)

    def testCDouble(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DOUBLE_NUMBERS:
            self.assertEqual(self.obj.callInstanceDoubleFuncOf_(self.ocobj), o)

    def testLongCDouble(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in LONG_DOUBLE_NUMBERS:
            self.assertEqual(self.obj.callInstanceLongDoubleFuncOf_(self.ocobj), o)

    def testIDouble(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DOUBLE_NUMBERS:
            self.assertEqual(self.obj.invokeInstanceDoubleFuncOf_(self.ocobj), o)

    def testILongDouble(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in LONG_DOUBLE_NUMBERS:
            self.assertEqual(self.obj.invokeInstanceLongDoubleFuncOf_(self.ocobj), o)

    def testCId(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in OBJECTS:
            self.assertEqual(self.obj.callInstanceIdFuncOf_(self.ocobj), o)

    def testIId(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in OBJECTS:
            self.assertEqual(self.obj.invokeInstanceIdFuncOf_(self.ocobj), o)

    def testCId2(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in OBJECTS:
            self.assertEqual(self.obj.callInstanceIdFuncOf_(self.pyobj), o)

    def testIId2(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in OBJECTS:
            self.assertEqual(self.obj.invokeInstanceIdFuncOf_(self.pyobj), o)

    def testCStruct1(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DUMMY_OBJECTS:
            self.assertEqual(self.obj.callInstanceDummyFuncOf_(self.ocobj), o)

    def testIStruct1(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DUMMY_OBJECTS:
            self.assertEqual(self.obj.invokeInstanceDummyFuncOf_(self.ocobj), o)

    def testCStruct2(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DUMMY2_OBJECTS:
            self.assertEqual(self.obj.callInstanceDummy2FuncOf_(self.ocobj), o)

    def testIStruct2(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in DUMMY2_OBJECTS:
            self.assertEqual(self.obj.invokeInstanceDummy2FuncOf_(self.ocobj), o)

    def testCNSPoint(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in POINTS:
            self.assertEqual(self.obj.callInstanceNSPointFuncOf_(self.ocobj), o)

    def testINSPoint(self):
        self.pyobj.reset()
        self.ocobj.reset()

        for o in POINTS:
            self.assertEqual(self.obj.invokeInstanceNSPointFuncOf_(self.ocobj), o)


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
        self.assertEqual(self.obj.callInstanceLongLongArg_on_(0, self.ocobj), 0)
        self.assertEqual(self.obj.callInstanceLongLongArg_on_(10, self.ocobj), 20)
        self.assertEqual(
            self.obj.callInstanceLongLongArg_on_(1 << 60, self.ocobj), 1 << 61
        )
        self.assertEqual(self.obj.callInstanceLongLongArg_on_(-10, self.ocobj), -20)
        self.assertEqual(
            self.obj.callInstanceLongLongArg_on_(-(1 << 60), self.ocobj), -(1 << 61)
        )

    def testILongLong(self):
        self.assertEqual(self.obj.invokeInstanceLongLongArg_on_(0, self.ocobj), 0)
        self.assertEqual(self.obj.invokeInstanceLongLongArg_on_(10, self.ocobj), 20)
        self.assertEqual(
            self.obj.invokeInstanceLongLongArg_on_(1 << 60, self.ocobj), 1 << 61
        )
        self.assertEqual(self.obj.invokeInstanceLongLongArg_on_(-10, self.ocobj), -20)
        self.assertEqual(
            self.obj.invokeInstanceLongLongArg_on_(-(1 << 60), self.ocobj), -(1 << 61)
        )
