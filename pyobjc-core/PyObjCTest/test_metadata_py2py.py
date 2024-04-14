"""
Tests for the new-style metadata format interface.

Note: Tests for calling from python into ObjC are in test_metadata.py

TODO:
-> OutputOptional version for TestByReference
-> Testcode might need changes, C code definitely needs changes

- Add more testcases: python methods that return the wrong value
- The python->C interface (that is the contents of the metadata object) is
  likely to change when the bridge is feature-complete.
- Probably need special-casing for arrays (numarray and array.array)!

XXX: python-to-python calls often don't pass through PyObjC's machinery,
     resulting in slightly different behaviour. Fixing this likely breaks
     user code.
"""

import objc

# To ensure we have the right metadata
import PyObjCTest.test_metadata  # noqa: F401
from PyObjCTest.metadata import OC_MetaDataTest
from PyObjCTest.test_metadata_py import Py_MetaDataTest_AllArgs
from PyObjCTools.TestSupport import TestCase

if 0:
    from PyObjCTest.test_metadata_py2 import Py_MetaDataTest_OutputOptional


class TestArraysOut_AllArgs(TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = o.fill4Tuple_(None)
        self.assertEqual(list(v), list(range(9, 13)))

        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.fill4Tuple_on_(objc.NULL, o)

        n, v = o.nullfill4Tuple_(None)
        self.assertEqual(n, 1)
        self.assertEqual(list(v), list(range(1, 5)))

        n, v = o.nullfill4Tuple_(objc.NULL)
        self.assertEqual(n, 2)
        # FIXME:
        # self.assertIs(v, objc.NULL )

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?

        # self.assertRaises(TypeError, o.fillStringArray_)
        # self.assertRaises(TypeError, o.fillStringArray_, None)
        # self.assertRaises(ValueError, o.fillStringArray_, objc.NULL)

        # self.assertRaises(TypeError, o.nullfillStringArray_)
        # self.assertRaises(TypeError, o.nullfillStringArray_, None)
        n, v = o.nullfillStringArray_(objc.NULL)
        self.assertEqual(n, 9)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = o.fillArray_count_(None, 3)
        self.assertEqual(list(v), [10, 11, 12])

        v = o.fillArray_count_(None, 5)
        self.assertEqual(list(v), [10, 11, 12, 13, 14])

        v = o.fillArray_count_(None, 0)
        self.assertEqual(list(v), [])

        # self.assertRaises(ValueError, o.fillArray_count_, objc.NULL, 0)

        n, v = o.nullfillArray_count_(None, 3)
        self.assertEqual(n, 2)
        self.assertEqual(list(v), [30, 31, 32])

        n, v = o.nullfillArray_count_(objc.NULL, 3)
        self.assertEqual(n, 1)
        # self.assertIs(v, objc.NULL )

    def testWithCountInResult(self):
        o = Py_MetaDataTest_AllArgs.new()

        c, v = o.fillArray_uptoCount_(None, 20)
        self.assertEqual(c, 10)
        self.assertEqual(list(v), [i + 10 for i in range(10)])

        c, v = o.maybeFillArray_(None)
        self.assertEqual(c, 2)
        self.assertEqual(list(v), [0, 1])


if 0:

    class TestArraysOut_OutputOptional(TestCase):
        def testFixedSize(self):
            o = Py_MetaDataTest_OutputOptional.new()

            v = o.fill4Tuple_()
            self.assertEqual(list(v), list(range(9, 13)))

            v = o.fill4Tuple_(None)
            self.assertEqual(list(v), list(range(9, 13)))

            with self.assertRaisesRegex(
                ValueError, "argument 0 isn't allowed to be NULL"
            ):
                OC_MetaDataTest.fill4Tuple_on_(objc.NULL, o)

            n, v = o.nullfill4Tuple_()
            self.assertEqual(n, 1)
            self.assertEqual(list(v), list(range(1, 5)))

            n, v = o.nullfill4Tuple_(None)
            self.assertEqual(n, 1)
            self.assertEqual(list(v), list(range(1, 5)))

            n, v = o.nullfill4Tuple_(objc.NULL)
            # self.assertEqual(n, 2)
            # self.assertIs(v, objc.NULL)

        def testNullTerminated(self):
            _ = Py_MetaDataTest_OutputOptional.new()

            # Output only arrays of null-terminated arrays cannot be
            # wrapped automaticly. How is the bridge supposed to know
            # how much memory it should allocate for the C-array?

            # self.assertRaises(TypeError, o.fillStringArray_)
            # self.assertRaises(TypeError, o.fillStringArray_, None)
            # self.assertRaises(ValueError, o.fillStringArray_, objc.NULL)

            # self.assertRaises(TypeError, o.nullfillStringArray_)
            # self.assertRaises(TypeError, o.nullfillStringArray_, None)
            # n, v = o.nullfillStringArray_(objc.NULL)
            # self.assertEqual(n, 9)
            # self.assertIs(v, objc.NULL)

        def testWithCount(self):
            o = Py_MetaDataTest_OutputOptional.new()

            v = o.fillArray_count_(3)
            self.assertEqual(list(v), [10, 11, 12])

            v = o.fillArray_count_(None, 3)
            self.assertEqual(list(v), [10, 11, 12])

            v = o.fillArray_count_(5)
            self.assertEqual(list(v), [10, 11, 12, 13, 14])

            v = o.fillArray_count_(0)
            self.assertEqual(list(v), [])

            # self.assertRaises(ValueError, o.fillArray_count_, objc.NULL, 0)

            n, v = o.nullfillArray_count_(3)
            self.assertEqual(n, 2)
            self.assertEqual(list(v), [30, 31, 32])
            n, v = o.nullfillArray_count_(None, 3)
            self.assertEqual(n, 2)
            self.assertEqual(list(v), [30, 31, 32])

            n, v = o.nullfillArray_count_(objc.NULL, 3)
            # self.assertEqual(n, 1)
            # self.assertIs(v, objc.NULL)

        def testWithCountInResult(self):
            o = Py_MetaDataTest_OutputOptional.new()

            c, v = o.fillArray_uptoCount_(20)
            self.assertEqual(c, 10)
            self.assertEqual(list(v), [i + 10 for i in range(10)])

            c, v = o.maybeFillArray_()
            self.assertEqual(c, 2)
            self.assertEqual(list(v), [0, 1])


class TestArraysInOut_AllArgs(TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (1, 2, 3, 4)
        v = o.reverse4Tuple_(a)
        self.assertEqual(a, (1, 2, 3, 4))
        self.assertEqual(list(v), [43, 44, 45, 46])

        # self.assertRaises(ValueError, o.reverse4Tuple_, (1,2,3))
        # self.assertRaises(ValueError, o.reverse4Tuple_, (1,2,3,4,5))
        # self.assertRaises(ValueError, o.reverse4Tuple_, objc.NULL)

        a = (1, 2, 3, 4)
        n, v = o.nullreverse4Tuple_(a)
        self.assertEqual(n, 1)
        self.assertEqual(a, (1, 2, 3, 4))
        self.assertEqual(list(v), [43, 44, 45, 46])

        n, v = o.nullreverse4Tuple_(objc.NULL)
        self.assertEqual(n, -1)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = ("aap", "boot", "cello")
        v = o.reverseStrings_(a)
        self.assertEqual(a, ("aap", "boot", "cello"))
        self.assertEqual(list(v), ["paa", "toob", "ollec"])

        # self.assertRaises(ValueError, o.reverseStrings_, (1,2))
        # self.assertRaises(ValueError, o.reverseStrings_, objc.NULL)

        a = ("aap", "boot", "cello")
        n, v = o.nullreverseStrings_(a)
        self.assertEqual(n, 10)
        self.assertEqual(a, ("aap", "boot", "cello"))
        self.assertEqual(list(v), ["paa", "toob", "ollec"])

        n, v = o.nullreverseStrings_(objc.NULL)
        self.assertEqual(n, 9)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = o.reverseArray_count_(a, 4)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))

        # Python->python: same semantics as normal python calls, therefore
        # the result is 5 long, and there is 2 added to the result (that is
        # the method sees the actual argument array instead of a truncated one)
        self.assertEqual(list(v[:4]), [3.0, 4.0, 5.0, 6.0])

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = o.reverseArray_count_(a, 5)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(list(v), [2.0, 3.0, 4.0, 5.0, 6.0])

        # Nice to have, but doesn't work without major
        # surgery:
        # a = (1.0, 2.0, 3.0, 4.0, 5.0)
        # v = o.reverseArray_count_(a, None)
        # self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        # self.assertEqual(v, (2.0, 3.0, 4.0, 5.0, 6.0))

        # self.assertRaises(ValueError, o.reverseArray_count_, (1.0, 2.0), 5)
        # self.assertRaises(ValueError, o.reverseArray_count_, objc.NULL, 0)

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = o.nullreverseArray_count_(a, 5)
        self.assertEqual(n, 9)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(list(v), [43.0, 44.0, 45.0, 46.0, 47.0])

        n, v = o.nullreverseArray_count_(objc.NULL, 0)
        self.assertEqual(n, 2)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):
        o = Py_MetaDataTest_AllArgs.new()

        # XXX: caling python->python has the usual python semantics, hence
        # the argument won't be truncated!
        c, v = o.reverseArray_uptoCount_(range(10), 10)
        self.assertEqual(c, 5)
        self.assertEqual(len(v), 10)
        self.assertEqual(list(v)[: int(c)], [0, 10, 20, 30, 40])

        c, v = o.maybeReverseArray_([1, 2, 3, 4])
        self.assertEqual(c, 2)
        self.assertEqual(len(v), 2)
        self.assertEqual(list(v), [45, 51])


class TestArraysIn_AllArgs(TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        (v,) = o.make4Tuple_((1.0, 4.0, 8.0, 12.5))
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 4.0, 8.0, 12.5])

        (v,) = o.make4Tuple_((1, 2, 3, 4))
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 2.0, 3.0, 4.0])

        # XXX: Calling python->python has a the same semantics as a normal
        # python call.
        # self.assertRaises(ValueError, o.make4Tuple_, (1, 2, 3))
        # self.assertRaises(ValueError, o.make4Tuple_, (1, 2, 3, 4, 5))
        # self.assertRaises(ValueError, o.make4Tuple_, objc.NULL)

        (v,) = o.null4Tuple_(objc.NULL)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        (v,) = OC_MetaDataTest.makeStringArray_on_((b"hello", b"world", b"there"), o)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), ["hello", "world", "there"])

        NSObject = objc.lookUpClass("NSObject")
        p, q = NSObject.new(), NSObject.new()
        (v,) = o.makeObjectArray_((p, q))
        self.assertEqual(len(v), 2)
        self.assertIs(v[0], p)
        self.assertIs(v[1], q)

        (v,) = OC_MetaDataTest.makeStringArray_on_((), o)
        self.assertEqual(len(v), 0)

        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'int'"):
            OC_MetaDataTest.makeStringArray_on_([1, 2], o)
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.makeStringArray_on_(objc.NULL, o)

        (v,) = OC_MetaDataTest.nullStringArray_on_(objc.NULL, o)
        self.assertEqual(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        v, c = o.makeIntArray_count_((1, 2, 3, 4), 3)
        self.assertEqual(c, 3)

        # Calling python -> python doesn't pass through C, hence the usual
        # python semantics are used which are slightly different from calling
        # into C or from C.
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v)[:c], [1, 2, 3])

        # XXX: This one would be nice to have, but not entirely trivial
        # v, c = o.makeIntArray_count_((1,2,3,4), None)
        # self.assertEqual(c, 3)
        # self.assertEqual(len(v), 3)
        # self.assertEqual(list(v), [1,2,3,4])

        # See above
        # self.assertRaises(ValueError, o.makeIntArray_count_, [1,2,3], 4)
        # self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 0)
        # self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 1)

        v, c = o.nullIntArray_count_(objc.NULL, 0)
        self.assertEqual(c, 0)
        self.assertEqual(v, objc.NULL)

        # See above
        # self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 1)

        # Make sure this also works when the length is in a pass-by-reference argument
        v, c = o.makeIntArray_countPtr_((1, 2, 3, 4), 4)
        self.assertEqual(c, 4)
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1, 2, 3, 4])


class TestArrayReturns_AllArgs(TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = o.makeIntArrayOf5()
        self.assertEqual(len(v), 5)
        self.assertEqual(list(v), [100, 200, 300, 400, 500])

        v = o.nullIntArrayOf5()
        self.assertEqual(v, objc.NULL)

    def testSizeInArgument(self):
        o = Py_MetaDataTest_AllArgs.new()
        v = o.makeIntArrayOf_(3)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [20, 21, 22])

        v = o.makeIntArrayOf_(10)
        self.assertEqual(len(v), 10)
        self.assertEqual(list(v), list(range(20, 30)))

        v = o.nullIntArrayOf_(100)
        self.assertEqual(v, objc.NULL)

    def testNULLterminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = o.makeStringArray()
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [b"jaap", b"pieter", b"hans"])

        v = o.nullStringArray()
        self.assertEqual(v, objc.NULL)


class TestByReference_AllArgs(TestCase):
    # Pass by reference arguments.
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        o = Py_MetaDataTest_AllArgs.new()

        r = o.sumX_andY_(1, 2)
        self.assertEqual(r, 1**2 + 2**2)

        r = o.sumX_andY_(2535, 5325)
        self.assertEqual(r, 2535**2 + 5325**2)

        # self.assertRaises(ValueError, o.sumX_andY_, 42, objc.NULL)

    def testOutput(self):
        o = Py_MetaDataTest_AllArgs.new()

        div, rem = o.divBy5_remainder_(55, None)
        self.assertEqual(div, 55 / 7)
        self.assertEqual(rem, 55 % 7)

        div, rem = o.divBy5_remainder_(13, None)
        self.assertEqual(div, 13 / 7)
        self.assertEqual(rem, 13 % 7)

        # XXX: To be fixed:
        # self.assertRaises(ValueError, o.divBy5_remainder_, 42, objc.NULL)

    def testInputOutput(self):
        o = Py_MetaDataTest_AllArgs.new()
        x, y = o.swapX_andY_(42, 284)
        self.assertEqual(x, 284 * 2)
        self.assertEqual(y, 42 * 2)

        # self.assertRaises(ValueError, o.swapX_andY_, 42, objc.NULL)

    def testNullAccepted(self):
        # Note: the commented-out test-cases require a change in the pyobjc-core
        o = Py_MetaDataTest_AllArgs.new()

        def makeNum(value):
            return int(value, 0)

        # All arguments present
        r, y, z = o.input_output_inputAndOutput_(1, None, 2)  # XXX
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 3)
        self.assertEqual(y, 9)
        self.assertEqual(z, 10)

        r, y, z = o.input_output_inputAndOutput_(1, None, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 3)
        self.assertEqual(y, 9)
        self.assertEqual(z, 10)

        # Argument 1 is NULL
        r, y, z = o.input_output_inputAndOutput_(objc.NULL, None, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 11)
        self.assertEqual(z, 12)

        # Argument 2 is NULL
        r, y, z = o.input_output_inputAndOutput_(1, objc.NULL, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 13)  # objc.NULL ...
        self.assertEqual(z, 14)

        # Argument 3 is NULL
        r, y, z = o.input_output_inputAndOutput_(1, None, objc.NULL)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 15)
        self.assertEqual(z, 16)  # , objc.NULL)
