"""
Some basic tests for converting values to and from Objective-C

TODO: This only tests C values at the moment.
"""
from __future__ import absolute_import

import array
import sys
import warnings

import objc
from PyObjCTools.TestSupport import TestCase

from .testbndl import (
    CHAR_MAX,
    CHAR_MIN,
    DBL_EPSILON,
    DBL_MAX,
    DBL_MIN,
    FLT_EPSILON,
    FLT_MAX,
    FLT_MIN,
    INT_MAX,
    INT_MIN,
    LLONG_MAX,
    LLONG_MIN,
    LONG_MAX,
    LONG_MIN,
    SCHAR_MIN,
    SHRT_MAX,
    SHRT_MIN,
    UCHAR_MAX,
    UINT_MAX,
    ULLONG_MAX,
    ULONG_MAX,
    USHRT_MAX,
    carrayMaker,
    pyObjCPy,
)


class TestNumbers(TestCase):
    """
    Test of conversion of numbers, especially boundary cases
    """

    def test_unsigned_char(self):
        self.assertEqual(0, pyObjCPy(objc._C_UCHR, 0))
        self.assertEqual(0, pyObjCPy(objc._C_UCHR, b"\0"))

        self.assertEqual(0, pyObjCPy(objc._C_UCHR, float(0)))

        self.assertEqual(UCHAR_MAX, pyObjCPy(objc._C_UCHR, UCHAR_MAX))
        self.assertEqual(UCHAR_MAX, pyObjCPy(objc._C_UCHR, bytes([UCHAR_MAX])))
        self.assertEqual(UCHAR_MAX, pyObjCPy(objc._C_UCHR, bytearray([UCHAR_MAX])))

        self.assertEqual(UCHAR_MAX, pyObjCPy(objc._C_UCHR, float(UCHAR_MAX)))

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            self.assertRaises(
                (IndexError, ValueError), pyObjCPy, objc._C_UCHR, SCHAR_MIN
            )
            self.assertRaises(
                (IndexError, ValueError), pyObjCPy, objc._C_UCHR, SCHAR_MIN - 1
            )

    def test_char(self):
        self.assertEqual(0, pyObjCPy(objc._C_CHR, 0))
        self.assertEqual(0, pyObjCPy(objc._C_CHR, b"\x00"))

        self.assertEqual(CHAR_MAX, pyObjCPy(objc._C_CHR, CHAR_MAX))
        self.assertEqual(CHAR_MAX, pyObjCPy(objc._C_CHR, bytes([CHAR_MAX])))
        self.assertEqual(CHAR_MAX, pyObjCPy(objc._C_CHR, bytearray([CHAR_MAX])))
        self.assertEqual(CHAR_MIN, pyObjCPy(objc._C_CHR, CHAR_MIN))
        self.assertEqual(CHAR_MAX, pyObjCPy(objc._C_CHR, float(CHAR_MAX)))
        self.assertEqual(CHAR_MIN, pyObjCPy(objc._C_CHR, float(CHAR_MIN)))

        # XXX: Is this right, chr(-1) raises an exception, and is not
        # equivalent to '\xff'. Should (char)-1 be converted to '\xff'/255 ?
        self.assertEqual(-1, pyObjCPy(objc._C_CHR, b"\xff"))

        self.assertRaises(ValueError, pyObjCPy, objc._C_CHR, CHAR_MAX + 1)
        self.assertRaises(ValueError, pyObjCPy, objc._C_CHR, CHAR_MIN - 1)

    def test_unsigned_short(self):
        self.assertEqual(0, pyObjCPy(objc._C_USHT, 0))
        self.assertEqual(USHRT_MAX, pyObjCPy(objc._C_USHT, USHRT_MAX))
        self.assertEqual(0, pyObjCPy(objc._C_USHT, float(0)))
        self.assertEqual(USHRT_MAX, pyObjCPy(objc._C_USHT, float(USHRT_MAX)))

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            self.assertRaises(ValueError, pyObjCPy, objc._C_USHT, SHRT_MIN)
            self.assertRaises(ValueError, pyObjCPy, objc._C_USHT, SHRT_MIN - 1)

            self.assertRaises(ValueError, pyObjCPy, objc._C_USHT, "1")
            self.assertRaises(ValueError, pyObjCPy, objc._C_USHT, b"1")

    def test_short(self):
        self.assertEqual(0, pyObjCPy(objc._C_SHT, 0))
        self.assertEqual(SHRT_MAX, pyObjCPy(objc._C_SHT, SHRT_MAX))
        self.assertEqual(SHRT_MIN, pyObjCPy(objc._C_SHT, SHRT_MIN))
        self.assertEqual(0, pyObjCPy(objc._C_SHT, float(0)))
        self.assertEqual(SHRT_MAX, pyObjCPy(objc._C_SHT, float(SHRT_MAX)))
        self.assertEqual(SHRT_MIN, pyObjCPy(objc._C_SHT, float(SHRT_MIN)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_SHT, SHRT_MAX + 1)
        self.assertRaises(ValueError, pyObjCPy, objc._C_SHT, SHRT_MIN - 1)

        self.assertRaises(ValueError, pyObjCPy, objc._C_SHT, "1")
        self.assertRaises(ValueError, pyObjCPy, objc._C_SHT, b"1")

    def test_unsigned_int(self):
        self.assertEqual(0, pyObjCPy(objc._C_UINT, 0))
        self.assertEqual(UINT_MAX, pyObjCPy(objc._C_UINT, UINT_MAX))
        self.assertEqual(0, pyObjCPy(objc._C_UINT, float(0)))
        self.assertEqual(UINT_MAX, pyObjCPy(objc._C_UINT, float(UINT_MAX)))

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            self.assertRaises(ValueError, pyObjCPy, objc._C_UINT, INT_MIN)
            self.assertRaises(ValueError, pyObjCPy, objc._C_UINT, INT_MIN - 1)

            self.assertRaises(ValueError, pyObjCPy, objc._C_UINT, "1")
            self.assertRaises(ValueError, pyObjCPy, objc._C_UINT, b"1")

    def test_int(self):
        self.assertEqual(0, pyObjCPy(objc._C_INT, 0))
        self.assertEqual(INT_MAX, pyObjCPy(objc._C_INT, INT_MAX))
        self.assertEqual(INT_MIN, pyObjCPy(objc._C_INT, INT_MIN))
        self.assertEqual(0, pyObjCPy(objc._C_INT, float(0)))
        self.assertEqual(INT_MAX, pyObjCPy(objc._C_INT, float(INT_MAX)))
        self.assertEqual(INT_MIN, pyObjCPy(objc._C_INT, float(INT_MIN)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_INT, INT_MAX + 1)
        self.assertRaises(ValueError, pyObjCPy, objc._C_INT, INT_MIN - 1)

        # Check implicit conversion
        self.assertRaises(ValueError, pyObjCPy, objc._C_INT, "1")
        self.assertRaises(ValueError, pyObjCPy, objc._C_INT, b"1")

    def test_unsigned_long(self):
        self.assertEqual(0, pyObjCPy(objc._C_ULNG, 0))
        self.assertEqual(ULONG_MAX, pyObjCPy(objc._C_ULNG, ULONG_MAX))
        self.assertEqual(0, pyObjCPy(objc._C_ULNG, float(0)))

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            if sys.maxsize < 2 ** 32:
                self.assertEqual(ULONG_MAX, pyObjCPy(objc._C_ULNG, float(ULONG_MAX)))
                self.assertRaises(ValueError, pyObjCPy, objc._C_ULNG, LONG_MIN)
                self.assertRaises(ValueError, pyObjCPy, objc._C_ULNG, LONG_MIN - 1)

            self.assertRaises(ValueError, pyObjCPy, objc._C_ULNG, "1")
            self.assertRaises(ValueError, pyObjCPy, objc._C_ULNG, b"1")

    def test_long(self):
        self.assertEqual(0, pyObjCPy(objc._C_LNG, 0))
        self.assertEqual(LONG_MAX, pyObjCPy(objc._C_LNG, LONG_MAX))
        self.assertEqual(LONG_MIN, pyObjCPy(objc._C_LNG, LONG_MIN))
        self.assertEqual(0, pyObjCPy(objc._C_LNG, float(0)))
        if sys.maxsize < 2 ** 32:
            self.assertEqual(LONG_MAX, pyObjCPy(objc._C_LNG, float(LONG_MAX)))
            self.assertEqual(LONG_MIN, pyObjCPy(objc._C_LNG, float(LONG_MIN)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_LNG, LONG_MAX + 1)
        self.assertRaises(ValueError, pyObjCPy, objc._C_LNG, LONG_MIN - 1)

        self.assertRaises(ValueError, pyObjCPy, objc._C_LNG, "1")
        self.assertRaises(ValueError, pyObjCPy, objc._C_LNG, b"1")

    def test_unsigned_long_long(self):
        self.assertEqual(0, pyObjCPy(objc._C_ULNG_LNG, 0))
        self.assertEqual(ULLONG_MAX, pyObjCPy(objc._C_ULNG_LNG, ULLONG_MAX))
        self.assertEqual(0, pyObjCPy(objc._C_ULNG_LNG, float(0)))

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            pyObjCPy(objc._C_ULNG_LNG, LLONG_MIN + 100)

        self.assertEqual(len(w), 1)
        self.assertEqual(w[0].category, DeprecationWarning)

        with warnings.catch_warnings(record=True):
            warnings.simplefilter("ignore")
            self.assertEqual(
                -LLONG_MIN + 100, pyObjCPy(objc._C_ULNG_LNG, LLONG_MIN + 100)
            )

        # self.assertRaises(ValueError, pyObjCPy, objc._C_ULNG_LNG, LLONG_MIN)
        self.assertRaises(
            (ValueError, IndexError), pyObjCPy, objc._C_ULNG_LNG, LLONG_MIN - 1
        )

        self.assertRaises(ValueError, pyObjCPy, objc._C_ULNG_LNG, "1")
        self.assertRaises(ValueError, pyObjCPy, objc._C_ULNG_LNG, b"1")

    def test_long_long(self):
        self.assertEqual(0, pyObjCPy(objc._C_LNG_LNG, 0))

        if sys.maxsize < 2 ** 32:
            self.assertEqual(LONG_MAX, pyObjCPy(objc._C_LNG_LNG, float(LONG_MAX)))
        self.assertEqual(LLONG_MAX, pyObjCPy(objc._C_LNG_LNG, LLONG_MAX))
        self.assertEqual(LLONG_MIN, pyObjCPy(objc._C_LNG_LNG, LLONG_MIN))

        self.assertRaises(ValueError, pyObjCPy, objc._C_LNG_LNG, LLONG_MAX + 1)
        self.assertRaises(ValueError, pyObjCPy, objc._C_LNG_LNG, LLONG_MIN - 1)

        self.assertRaises(ValueError, pyObjCPy, objc._C_LNG_LNG, "1")
        self.assertRaises(ValueError, pyObjCPy, objc._C_LNG_LNG, b"1")

    def test_double(self):
        self.assertEqual(0, pyObjCPy(objc._C_DBL, 0))
        self.assertEqual(float(INT_MAX), pyObjCPy(objc._C_DBL, INT_MAX))
        self.assertEqual(DBL_MAX, pyObjCPy(objc._C_DBL, DBL_MAX))
        self.assertEqual(DBL_MIN, pyObjCPy(objc._C_DBL, DBL_MIN))
        self.assertEqual(-DBL_MAX, pyObjCPy(objc._C_DBL, -DBL_MAX))
        self.assertEqual(-DBL_MIN, pyObjCPy(objc._C_DBL, -DBL_MIN))
        self.assertEqual(DBL_EPSILON, pyObjCPy(objc._C_DBL, DBL_EPSILON))
        self.assertEqual(-DBL_EPSILON, pyObjCPy(objc._C_DBL, -DBL_EPSILON))

        self.assertRaises(
            (OverflowError, ValueError), pyObjCPy, objc._C_DBL, 1 << 10000
        )

        self.assertRaises(ValueError, pyObjCPy, objc._C_DBL, "1")
        self.assertRaises(ValueError, pyObjCPy, objc._C_DBL, b"1")

    def test_float(self):
        self.assertEqual(0, pyObjCPy(objc._C_FLT, 0))
        self.assertEqual(float(SHRT_MAX), pyObjCPy(objc._C_FLT, SHRT_MAX))
        self.assertEqual(FLT_MAX, pyObjCPy(objc._C_FLT, FLT_MAX))
        self.assertEqual(FLT_MIN, pyObjCPy(objc._C_FLT, FLT_MIN))
        self.assertEqual(-FLT_MAX, pyObjCPy(objc._C_FLT, -FLT_MAX))
        self.assertEqual(-FLT_MIN, pyObjCPy(objc._C_FLT, -FLT_MIN))
        self.assertEqual(FLT_EPSILON, pyObjCPy(objc._C_FLT, FLT_EPSILON))
        self.assertEqual(-FLT_EPSILON, pyObjCPy(objc._C_FLT, -FLT_EPSILON))

        # Just in cause we do something stupid and convert to double instead
        # of float
        self.assertNotEqual(DBL_MAX, pyObjCPy(objc._C_FLT, DBL_MAX))

        self.assertRaises(
            (ValueError, OverflowError), pyObjCPy, objc._C_FLT, 1 << 10000
        )

        self.assertRaises(ValueError, pyObjCPy, objc._C_FLT, "1")
        self.assertRaises(ValueError, pyObjCPy, objc._C_FLT, b"1")


class TestStruct(TestCase):
    """
    Structs are usually represented as tuples, but any sequence type is
    accepted as input, as long as it has the right number of elements
    """

    def testSimple(self):
        # struct Foo {
        #    int;
        #    int;
        # };
        signature = b"{Foo=ii}"

        inval = (1, 2)

        self.assertEqual(inval, pyObjCPy(signature, inval))
        self.assertEqual(inval, pyObjCPy(signature, list(inval)))
        self.assertEqual(inval, pyObjCPy(signature, iter(inval)))
        self.assertEqual(inval, pyObjCPy(signature, iter(list(inval))))

    def testHoles(self):
        # This struct usually contains holes
        #
        # struct Foo {
        #   short;
        #   int;
        #   short;
        #   double;
        #   short;
        # };
        signature = b"{Foo=sisds}"

        inval = (1, 2, 3, 4.0, 5)

        self.assertEqual(inval, pyObjCPy(signature, inval))
        self.assertEqual(inval, pyObjCPy(signature, list(inval)))
        self.assertEqual(inval, pyObjCPy(signature, iter(inval)))
        self.assertEqual(inval, pyObjCPy(signature, iter(list(inval))))


class TestArray(TestCase):
    def test_simple(self):
        signature = b"[10i]"
        value = tuple(range(10))

        self.assertEqual(value, tuple(pyObjCPy(signature, value)))
        self.assertEqual(value, tuple(pyObjCPy(signature, list(value))))
        self.assertEqual(value, tuple(pyObjCPy(signature, iter(value))))
        self.assertEqual(value, tuple(pyObjCPy(signature, iter(list(value)))))

        self.assertRaises(ValueError, pyObjCPy, signature, value + value[:1])
        self.assertRaises(ValueError, pyObjCPy, signature, value[:9])
        self.assertRaises(ValueError, pyObjCPy, signature, iter(value + value[:1]))
        self.assertRaises(ValueError, pyObjCPy, signature, iter(value[:9]))
        self.assertRaises(TypeError, pyObjCPy, signature, None)


class TestCArray(TestCase):
    # Tests for the PyObjC_PythonToCArray (C-)function, this function is
    # used to build variable-length C Arrays from Python objects.

    # TODO: "{_NSPoint=ff}", "{_NSRect={_NSPoint=ff}{_NSSize=ff}}"
    #       "[4i]" "[4[4i]]" "[2{foo=ii}]" "{foo=[4i]}"
    #       "{_Foo=fi}" (fail with array.array) + version with [{foo=if}]
    #       - other simple types
    def testShortTuple(self):
        arr = (1, 2, 3, 4, 5)

        res = carrayMaker(objc._C_SHT, arr, None)
        self.assertEqual(res, arr)

        res = carrayMaker(objc._C_SHT, arr, 2)
        self.assertEqual(res, arr[:2])

        self.assertRaises(ValueError, carrayMaker, objc._C_SHT, arr, 7)
        self.assertRaises(ValueError, carrayMaker, objc._C_SHT, ["a", "b"], 1)

    def testShortArray(self):
        arr = array.array("h", [1, 2, 3, 4, 5])
        arr2 = array.array("f", [1, 2, 3, 4, 5])

        res = carrayMaker(objc._C_SHT, arr, None)
        self.assertEqual(res, tuple(arr))

        res = carrayMaker(objc._C_SHT, arr, 2)
        self.assertEqual(res, tuple(arr)[:2])

        self.assertRaises(ValueError, carrayMaker, objc._C_SHT, arr, 7)
        self.assertRaises(ValueError, carrayMaker, objc._C_SHT, arr2, None)

    def testIntTuple(self):
        arr = (1, 2, 3, 4, 5)

        res = carrayMaker(objc._C_INT, arr, None)
        self.assertEqual(res, arr)

        res = carrayMaker(objc._C_INT, arr, 2)
        self.assertEqual(res, arr[:2])

        self.assertRaises(ValueError, carrayMaker, objc._C_INT, arr, 7)
        self.assertRaises(ValueError, carrayMaker, objc._C_INT, ["a", "b"], 1)

    def testIntArray(self):
        arr = array.array("i", [1, 2, 3, 4, 5])
        arr2 = array.array("f", [1, 2, 3, 4, 5])
        arr3 = array.array("h", [1, 2, 3, 4, 5])

        res = carrayMaker(objc._C_INT, arr, None)
        self.assertEqual(res, tuple(arr))

        res = carrayMaker(objc._C_INT, arr, 2)
        self.assertEqual(res, tuple(arr)[:2])

        self.assertRaises(ValueError, carrayMaker, objc._C_INT, arr, 7)
        self.assertRaises(ValueError, carrayMaker, objc._C_INT, arr2, None)
        self.assertRaises(ValueError, carrayMaker, objc._C_INT, arr3, None)

    def testFloatTuple(self):
        arr = (1, 2, 3, 4, 5)

        res = carrayMaker(objc._C_FLT, arr, None)
        self.assertEqual(res, arr)

        res = carrayMaker(objc._C_FLT, arr, 2)
        self.assertEqual(res, arr[:2])

        self.assertRaises(ValueError, carrayMaker, objc._C_INT, arr, 7)
        self.assertRaises(ValueError, carrayMaker, objc._C_INT, ["a", "b"], 1)

    def testFloatArray(self):
        arr = array.array("f", [1.5, 2.5, 3.5, 4.5, 5.5])
        arr2 = array.array("i", [1, 2, 3, 4, 5])

        res = carrayMaker(objc._C_FLT, arr, None)
        self.assertEqual(res, tuple(arr))

        res = carrayMaker(objc._C_FLT, arr, 2)
        self.assertEqual(res, tuple(arr)[:2])

        self.assertRaises(ValueError, carrayMaker, objc._C_FLT, arr, 7)
        self.assertRaises(ValueError, carrayMaker, objc._C_FLT, arr2, None)

    def testPointTuple(self):
        arr = ((1.0, 1.5), (2.0, 2.5), (3.0, 3.5), (4.0, 4.5), (5.0, 5.5))
        arr2 = (1.5, 2.5, 3.5, 4.5, 5.5)

        res = carrayMaker(b"{Point=ff}", arr, None)
        self.assertEqual(res, arr)

        res = carrayMaker(b"{Point=ff}", arr, 2)
        self.assertEqual(res, arr[:2])

        self.assertRaises(ValueError, carrayMaker, b"{Point=ff}", arr, 7)
        self.assertRaises(ValueError, carrayMaker, b"{Point=ff}", ["a", "b"], 1)
        self.assertRaises(TypeError, carrayMaker, b"{Point=ff}", arr2, None)

    def testPointArray(self):
        arr = array.array("f", [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5])
        lst = ((1.0, 1.5), (2.0, 2.5), (3.0, 3.5), (4.0, 4.5), (5.0, 5.5))

        arr2 = array.array("i", [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

        res = carrayMaker(b"{Point=ff}", arr, None)
        self.assertEqual(res, lst)

        res = carrayMaker(b"{Point=ff}", arr, 2)
        self.assertEqual(res, lst[:2])

        self.assertRaises(ValueError, carrayMaker, b"{Point=ff}", arr2, None)

    def testRectArray(self):
        arr = array.array(
            "f",
            [
                1.0,
                1.5,
                -1.0,
                -1.5,
                2.0,
                2.5,
                -2.0,
                -2.5,
                3.0,
                3.5,
                -3.0,
                -3.5,
                4.0,
                4.5,
                -4.0,
                -4.5,
                5.0,
                5.5,
                -5.0,
                -5.5,
            ],
        )
        lst = (
            ((1.0, 1.5), (-1.0, -1.5)),
            ((2.0, 2.5), (-2.0, -2.5)),
            ((3.0, 3.5), (-3.0, -3.5)),
            ((4.0, 4.5), (-4.0, -4.5)),
            ((5.0, 5.5), (-5.0, -5.5)),
        )

        arr2 = array.array(
            "i", [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
        )

        res = carrayMaker(b"{Rect={P=ff}{S=ff}}", arr, None)
        self.assertEqual(res, lst)

        res = carrayMaker(b"{Rect={P=ff}{S=ff}}", arr, 2)
        self.assertEqual(res, lst[:2])

        res = carrayMaker(b"{Rect=[2f][2f]}", arr, None)
        self.assertEqual(res, lst)

        res = carrayMaker(b"[2[2f]]}", arr, None)
        self.assertEqual(res, lst)

        self.assertRaises(ValueError, carrayMaker, b"{Rect={P=ff}{S=ff}}", arr2, None)

    def testMixedArray(self):
        arr = array.array(
            "f",
            [
                1.0,
                1.5,
                -1.0,
                -1.5,
                2.0,
                2.5,
                -2.0,
                -2.5,
                3.0,
                3.5,
                -3.0,
                -3.5,
                4.0,
                4.5,
                -4.0,
                -4.5,
                5.0,
                5.5,
                -5.0,
                -5.5,
            ],
        )

        self.assertRaises(ValueError, carrayMaker, b"{M={P=ff}{S=ii}}", arr, 4)
        self.assertRaises(ValueError, carrayMaker, b"{M=if{S=ii}}", arr, None)
        self.assertRaises(ValueError, carrayMaker, b"{M=fi{S=ff}}", arr, None)


class PyOCTestTypeStr(TestCase):
    #
    # Check that typestrings have the expected values.
    # We currently depend on these values in this file as wel as in the
    # modules that set method signatures to 'better' values.
    #
    def testAll(self):
        self.assertEqual(objc._C_BOOL, b"B")
        self.assertEqual(objc._C_ID, b"@")
        self.assertEqual(objc._C_CLASS, b"#")
        self.assertEqual(objc._C_SEL, b":")
        self.assertEqual(objc._C_CHR, b"c")
        self.assertEqual(objc._C_UCHR, b"C")
        self.assertEqual(objc._C_SHT, b"s")
        self.assertEqual(objc._C_USHT, b"S")
        self.assertEqual(objc._C_INT, b"i")
        self.assertEqual(objc._C_UINT, b"I")
        self.assertEqual(objc._C_LNG, b"l")
        self.assertEqual(objc._C_ULNG, b"L")
        self.assertEqual(objc._C_LNG_LNG, b"q")
        self.assertEqual(objc._C_ULNG_LNG, b"Q")
        self.assertEqual(objc._C_FLT, b"f")
        self.assertEqual(objc._C_DBL, b"d")
        self.assertEqual(objc._C_VOID, b"v")
        self.assertEqual(objc._C_CHARPTR, b"*")
        self.assertEqual(objc._C_PTR, b"^")
        self.assertEqual(objc._C_UNDEF, b"?")
        self.assertEqual(objc._C_ARY_B, b"[")
        self.assertEqual(objc._C_ARY_E, b"]")
        self.assertEqual(objc._C_UNION_B, b"(")
        self.assertEqual(objc._C_UNION_E, b")")
        self.assertEqual(objc._C_STRUCT_B, b"{")
        self.assertEqual(objc._C_STRUCT_E, b"}")
        self.assertEqual(objc._C_IN, b"n")
        self.assertEqual(objc._C_OUT, b"o")
        self.assertEqual(objc._C_INOUT, b"N")
