"""
Some basic tests for converting values to and from Objective-C

TODO: This only tests C values at the moment.
"""
import unittest
from objc.test.testbndl import pyObjCPy
from objc.test.testbndl import UCHAR_MAX
from objc.test.testbndl import CHAR_MAX, CHAR_MIN
from objc.test.testbndl import SCHAR_MAX, SCHAR_MIN
from objc.test.testbndl import USHRT_MAX, SHRT_MAX, SHRT_MIN
from objc.test.testbndl import UINT_MAX, INT_MAX, INT_MIN
from objc.test.testbndl import ULONG_MAX, LONG_MAX, LONG_MIN
from objc.test.testbndl import ULLONG_MAX, LLONG_MAX, LLONG_MIN
from objc.test.testbndl import DBL_MAX, DBL_MIN, DBL_EPSILON
from objc.test.testbndl import FLT_MAX, FLT_MIN, FLT_EPSILON
import objc


class TestNumbers (unittest.TestCase):
    """
    Test of conversion of numbers, especially boundary cases
    """

    def test_unsigned_char(self):
        self.assertEquals(0, pyObjCPy(objc._C_UCHR, 0))
        self.assertEquals(0, pyObjCPy(objc._C_UCHR, '\0'))
        self.assertEquals(0, pyObjCPy(objc._C_UCHR, long(0)))
        self.assertEquals(0, pyObjCPy(objc._C_UCHR, float(0)))

        self.assertEquals(UCHAR_MAX, pyObjCPy(objc._C_UCHR, UCHAR_MAX))
        self.assertEquals(UCHAR_MAX, pyObjCPy(objc._C_UCHR, chr(UCHAR_MAX)))
        self.assertEquals(UCHAR_MAX, pyObjCPy(objc._C_UCHR, long(UCHAR_MAX)))
        self.assertEquals(UCHAR_MAX, pyObjCPy(objc._C_UCHR, float(UCHAR_MAX)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_UCHR, SCHAR_MIN)
        self.assertRaises(ValueError, pyObjCPy, objc._C_UCHR, SCHAR_MIN - 1)

    def test_char(self):
        self.assertEquals(0, pyObjCPy(objc._C_CHR, 0))
        self.assertEquals(0, pyObjCPy(objc._C_CHR, chr(0)))
        self.assertEquals(0, pyObjCPy(objc._C_CHR, long(0)))

        self.assertEquals(CHAR_MAX, pyObjCPy(objc._C_CHR, CHAR_MAX))
        self.assertEquals(CHAR_MAX, pyObjCPy(objc._C_CHR, chr(CHAR_MAX)))
        self.assertEquals(CHAR_MIN, pyObjCPy(objc._C_CHR, CHAR_MIN))
        self.assertEquals(CHAR_MAX, pyObjCPy(objc._C_CHR, long(CHAR_MAX)))
        self.assertEquals(CHAR_MIN, pyObjCPy(objc._C_CHR, long(CHAR_MIN)))
        self.assertEquals(CHAR_MAX, pyObjCPy(objc._C_CHR, float(CHAR_MAX)))
        self.assertEquals(CHAR_MIN, pyObjCPy(objc._C_CHR, float(CHAR_MIN)))

        # XXX: Is the right, chr(-1) raises an exception, and is not
        # equivalent to '\xff'. Should (char)-1 be converted to '\xff'/255 ? 
        self.assertEquals(-1, pyObjCPy(objc._C_CHR, '\xff'))

        self.assertRaises(ValueError, pyObjCPy, objc._C_CHR, CHAR_MAX + 1)
        self.assertRaises(ValueError, pyObjCPy, objc._C_CHR, CHAR_MIN - 1)

    def test_unsigned_short(self):
        self.assertEquals(0, pyObjCPy(objc._C_USHT, 0))
        self.assertEquals(USHRT_MAX, pyObjCPy(objc._C_USHT, USHRT_MAX))
        self.assertEquals(0, pyObjCPy(objc._C_USHT, long(0)))
        self.assertEquals(USHRT_MAX, pyObjCPy(objc._C_USHT, long(USHRT_MAX)))
        self.assertEquals(0, pyObjCPy(objc._C_USHT, float(0)))
        self.assertEquals(USHRT_MAX, pyObjCPy(objc._C_USHT, float(USHRT_MAX)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_USHT, SHRT_MIN)
        self.assertRaises(ValueError, pyObjCPy, objc._C_USHT, SHRT_MIN - 1)

    def test_short(self):
        self.assertEquals(0, pyObjCPy(objc._C_SHT, 0))
        self.assertEquals(SHRT_MAX, pyObjCPy(objc._C_SHT, SHRT_MAX))
        self.assertEquals(SHRT_MIN, pyObjCPy(objc._C_SHT, SHRT_MIN))
        self.assertEquals(0, pyObjCPy(objc._C_SHT, long(0)))
        self.assertEquals(SHRT_MAX, pyObjCPy(objc._C_SHT, long(SHRT_MAX)))
        self.assertEquals(SHRT_MIN, pyObjCPy(objc._C_SHT, long(SHRT_MIN)))
        self.assertEquals(0, pyObjCPy(objc._C_SHT, float(0)))
        self.assertEquals(SHRT_MAX, pyObjCPy(objc._C_SHT, float(SHRT_MAX)))
        self.assertEquals(SHRT_MIN, pyObjCPy(objc._C_SHT, float(SHRT_MIN)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_SHT, SHRT_MAX + 1)
        self.assertRaises(ValueError, pyObjCPy, objc._C_SHT, SHRT_MIN - 1)

    def test_unsigned_int(self):
        self.assertEquals(0, pyObjCPy(objc._C_UINT, 0))
        self.assertEquals(UINT_MAX, pyObjCPy(objc._C_UINT, UINT_MAX))
        self.assertEquals(0, pyObjCPy(objc._C_UINT, long(0)))
        self.assertEquals(UINT_MAX, pyObjCPy(objc._C_UINT, long(UINT_MAX)))
        self.assertEquals(0, pyObjCPy(objc._C_UINT, float(0)))
        self.assertEquals(UINT_MAX, pyObjCPy(objc._C_UINT, float(UINT_MAX)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_UINT, INT_MIN)
        self.assertRaises(ValueError, pyObjCPy, objc._C_UINT, INT_MIN - 1)

    def test_int(self):
        self.assertEquals(0, pyObjCPy(objc._C_INT, 0))
        self.assertEquals(INT_MAX, pyObjCPy(objc._C_INT, INT_MAX))
        self.assertEquals(INT_MIN, pyObjCPy(objc._C_INT, INT_MIN))
        self.assertEquals(0, pyObjCPy(objc._C_INT, long(0)))
        self.assertEquals(INT_MAX, pyObjCPy(objc._C_INT, long(INT_MAX)))
        self.assertEquals(INT_MIN, pyObjCPy(objc._C_INT, long(INT_MIN)))
        self.assertEquals(0, pyObjCPy(objc._C_INT, float(0)))
        self.assertEquals(INT_MAX, pyObjCPy(objc._C_INT, float(INT_MAX)))
        self.assertEquals(INT_MIN, pyObjCPy(objc._C_INT, float(INT_MIN)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_INT, INT_MAX + 1)
        self.assertRaises(ValueError, pyObjCPy, objc._C_INT, INT_MIN - 1)

    def test_unsigned_long(self):
        self.assertEquals(0, pyObjCPy(objc._C_ULNG, 0))
        self.assertEquals(ULONG_MAX, pyObjCPy(objc._C_ULNG, ULONG_MAX))
        self.assertEquals(0, pyObjCPy(objc._C_ULNG, long(0)))
        self.assertEquals(ULONG_MAX, pyObjCPy(objc._C_ULNG, long(ULONG_MAX)))
        self.assertEquals(0, pyObjCPy(objc._C_ULNG, float(0)))
        self.assertEquals(ULONG_MAX, pyObjCPy(objc._C_ULNG, float(ULONG_MAX)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_ULNG, LONG_MIN)
        self.assertRaises(ValueError, pyObjCPy, objc._C_ULNG, LONG_MIN - 1)

    def test_long(self):
        self.assertEquals(0, pyObjCPy(objc._C_LNG, 0))
        self.assertEquals(LONG_MAX, pyObjCPy(objc._C_LNG, LONG_MAX))
        self.assertEquals(LONG_MIN, pyObjCPy(objc._C_LNG, LONG_MIN))
        self.assertEquals(0, pyObjCPy(objc._C_LNG, long(0)))
        self.assertEquals(LONG_MAX, pyObjCPy(objc._C_LNG, long(LONG_MAX)))
        self.assertEquals(LONG_MIN, pyObjCPy(objc._C_LNG, long(LONG_MIN)))
        self.assertEquals(0, pyObjCPy(objc._C_LNG, float(0)))
        self.assertEquals(LONG_MAX, pyObjCPy(objc._C_LNG, float(LONG_MAX)))
        self.assertEquals(LONG_MIN, pyObjCPy(objc._C_LNG, float(LONG_MIN)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_LNG, LONG_MAX + 1)
        self.assertRaises(ValueError, pyObjCPy, objc._C_LNG, LONG_MIN - 1)

    def test_unsigned_long_long(self):
        self.assertEquals(0, pyObjCPy(objc._C_ULNGLNG, 0))
        self.assertEquals(ULLONG_MAX, pyObjCPy(objc._C_ULNGLNG, ULLONG_MAX))
        self.assertEquals(0, pyObjCPy(objc._C_ULNGLNG, long(0)))
        self.assertEquals(ULLONG_MAX, pyObjCPy(objc._C_ULNGLNG, long(ULLONG_MAX)))
        self.assertEquals(0, pyObjCPy(objc._C_ULNGLNG, float(0)))

        self.assertRaises(ValueError, pyObjCPy, objc._C_ULNGLNG, LLONG_MIN)
        self.assertRaises(ValueError, pyObjCPy, objc._C_ULNGLNG, LLONG_MIN - 1)

    def test_long_long(self):
        self.assertEquals(0, pyObjCPy(objc._C_LNGLNG, 0))
        self.assertEquals(LONG_MAX, pyObjCPy(objc._C_LNGLNG, float(LONG_MAX)))
        self.assertEquals(LLONG_MAX, pyObjCPy(objc._C_LNGLNG, LLONG_MAX))
        self.assertEquals(LLONG_MIN, pyObjCPy(objc._C_LNGLNG, LLONG_MIN))

        self.assertRaises(ValueError, pyObjCPy, objc._C_LNGLNG, LLONG_MAX + 1)
        self.assertRaises(ValueError, pyObjCPy, objc._C_LNGLNG, LLONG_MIN - 1)

    def test_double(self):
        self.assertEquals(0, pyObjCPy(objc._C_DBL, 0))
        self.assertEquals(float(INT_MAX), pyObjCPy(objc._C_DBL, INT_MAX))
        self.assertEquals(DBL_MAX, pyObjCPy(objc._C_DBL, DBL_MAX))
        self.assertEquals(DBL_MIN, pyObjCPy(objc._C_DBL, DBL_MIN))
        self.assertEquals(-DBL_MAX, pyObjCPy(objc._C_DBL, -DBL_MAX))
        self.assertEquals(-DBL_MIN, pyObjCPy(objc._C_DBL, -DBL_MIN))
        self.assertEquals(DBL_EPSILON, pyObjCPy(objc._C_DBL, DBL_EPSILON))
        self.assertEquals(-DBL_EPSILON, pyObjCPy(objc._C_DBL, -DBL_EPSILON))

        self.assertRaises(ValueError, pyObjCPy, objc._C_DBL, 1L << 10000)

    def test_float(self):
        self.assertEquals(0, pyObjCPy(objc._C_FLT, 0))
        self.assertEquals(float(SHRT_MAX), pyObjCPy(objc._C_FLT, SHRT_MAX))
        self.assertEquals(FLT_MAX, pyObjCPy(objc._C_FLT, FLT_MAX))
        self.assertEquals(FLT_MIN, pyObjCPy(objc._C_FLT, FLT_MIN))
        self.assertEquals(-FLT_MAX, pyObjCPy(objc._C_FLT, -FLT_MAX))
        self.assertEquals(-FLT_MIN, pyObjCPy(objc._C_FLT, -FLT_MIN))
        self.assertEquals(FLT_EPSILON, pyObjCPy(objc._C_FLT, FLT_EPSILON))
        self.assertEquals(-FLT_EPSILON, pyObjCPy(objc._C_FLT, -FLT_EPSILON))

        # Just in cause we do something stupid and convert to double instead
        # of float
        self.assertNotEquals(DBL_MAX, pyObjCPy(objc._C_FLT, DBL_MAX))

        self.assertRaises(ValueError, pyObjCPy, objc._C_FLT, 1L << 10000)


class TestStruct (unittest.TestCase):
    """
    Structs are usually represented as tuples, but any sequence type is
    accepted as input, as long as it has the right number of elements
    """

    def testSimple(self):
        # struct Foo {
        #    int;
        #    int;
        # };
        signature = "{Foo=ii}"

        inval = (1, 2)

        self.assertEquals(inval, pyObjCPy(signature, inval))
        self.assertEquals(inval, pyObjCPy(signature, list(inval)))
        self.assertEquals(inval, pyObjCPy(signature, iter(inval)))
        self.assertEquals(inval, pyObjCPy(signature, iter(list(inval))))

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
        signature = "{Foo=sisds}"

        inval = (1, 2, 3, 4.0, 5)

        self.assertEquals(inval, pyObjCPy(signature, inval))
        self.assertEquals(inval, pyObjCPy(signature, list(inval)))
        self.assertEquals(inval, pyObjCPy(signature, iter(inval)))
        self.assertEquals(inval, pyObjCPy(signature, iter(list(inval))))

class TestArray (unittest.TestCase):
    def test_simple(self):
        signature = '[10i]'
        value = tuple(range(10))

        self.assertEquals(value, tuple(pyObjCPy(signature, value)))
        self.assertEquals(value, tuple(pyObjCPy(signature, list(value))))
        self.assertEquals(value, tuple(pyObjCPy(signature, iter(value))))
        self.assertEquals(value, tuple(pyObjCPy(signature, iter(list(value)))))

        self.assertRaises(ValueError, pyObjCPy, signature, value + value[:1])
        self.assertRaises(ValueError, pyObjCPy, signature, value[:9])
        self.assertRaises(ValueError, pyObjCPy, signature, iter(value + value[:1]))
        self.assertRaises(ValueError, pyObjCPy, signature, iter(value[:9]))
        self.assertRaises(TypeError, pyObjCPy, signature, None)


class PyOCTestTypeStr(unittest.TestCase):
    # 
    # Check that typestrings have the expected values. 
    # We currently depend on these values in this file as wel as in the 
    # modules that set method signatures to 'better' values.
    #
    def testAll(self):
        if hasattr(objc, '_C_BOOL'):
            self.assertEquals(objc._C_BOOL, "B")
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

if __name__ == "__main__":
    unittest.main()
