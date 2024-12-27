"""
Tests for the proxy of Python numbers

NOTE: Decimal conversion is not tested, the required proxy is part of
the Foundation bindings :-(
"""

import sys
import warnings
import operator
import struct

import objc
from PyObjCTest.fnd import NSNumber, NSNumberFormatter
from PyObjCTest.misc import OC_Misc
from PyObjCTest.pythonnumber import OC_NumberInt
from PyObjCTools.TestSupport import TestCase, os_level_key, os_release
from PyObjCTest.test_object_proxy import NoObjectiveC

OC_PythonNumber = objc.lookUpClass("OC_PythonNumber")
OC_BuiltinPythonNumber = objc.lookUpClass("OC_BuiltinPythonNumber")
NSDecimalNumber = objc.lookUpClass("NSDecimalNumber")
try:
    NSCFNumber = objc.lookUpClass("__NSCFNumber")
except objc.error:
    NSCFNumber = objc.lookUpClass("NSCFNumber")


NSOrderedAscending = -1
NSOrderedSame = 0
NSOrderedDescending = 1


def as_nsnumber(value, encoding=None):
    """\
    Return an NSNumber equivalent to 'value'

    For integers and floats a type encoding can
    optionally be specified (defaults to the
    respective type with the largest range)
    """
    if isinstance(value, float):
        if encoding is None:
            return NSNumber.numberWithDouble_(value)

        elif encoding == objc._C_FLT:
            return NSNumber.numberWithFloat_(value)

        elif encoding == objc._C_DBL:
            return NSNumber.numberWithDouble_(value)

    elif isinstance(value, bool):
        return NSNumber.numberWithBool_(value)

    elif isinstance(value, int):
        if encoding is None:
            if -sys.maxsize - 1 <= value <= sys.maxsize:
                return NSNumber.numberWithLongLong_(value)
            elif 0 <= value <= 2**64 - 1:
                return NSNumber.numberWithUnsignedLongLong_(value)

        elif encoding == objc._C_CHR and -128 <= value < 128:
            return NSNumber.numberWithChar_(value)
        elif encoding == objc._C_UCHR and 0 <= value < 256:
            return NSNumber.numberWithUnsignedChar_(value)

        elif encoding == objc._C_SHT and -(2**15) <= value < 2**15:
            return NSNumber.numberWithShort_(value)
        elif encoding == objc._C_USHT and 0 <= value < 2**16:
            return NSNumber.numberWithUnsignedShort_(value)

        elif encoding == objc._C_INT and -(2**31) <= value < 2**31:
            return NSNumber.numberWithInt_(value)
        elif encoding == objc._C_UINT and 0 <= value < 2**32:
            return NSNumber.numberWithUnsignedInt_(value)

        elif encoding == objc._C_LNG and -(2**63) <= value < 2**63:
            return NSNumber.numberWithLong_(value)
        elif encoding == objc._C_ULNG and 0 <= value < 2**64:
            return NSNumber.numberWithUnsignedLong_(value)

        elif encoding == objc._C_LNG_LNG and -(2**63) <= value < 2**63:
            return NSNumber.numberWithLongLong_(value)
        elif encoding == objc._C_ULNG_LNG and 0 <= value < 2**64:
            return NSNumber.numberWithUnsignedLongLong_(value)

    raise ValueError(r"Cannot create NSNumber for {value!r} of {type(value).__name__}")


class TestNSNumber(TestCase):
    # These testcases check the behaviour of NSNumber, these
    # are mostly here to verify that NSNumbers behave as
    # we expect them to.

    def testClass(self):
        for m in (
            "numberWithInt_",
            "numberWithFloat_",
            "numberWithDouble_",
            "numberWithShort_",
        ):
            v = getattr(NSNumber, m)(0)
            self.assertIsInstance(v, NSNumber)
            self.assertNotIsInstance(v, OC_PythonNumber)
            self.assertIs(OC_NumberInt.numberClass_(v), NSCFNumber)

    def testDecimal(self):
        NSDecimalNumber = objc.lookUpClass("NSDecimalNumber")
        v = NSDecimalNumber.numberWithInt_(10)
        self.assertIsInstance(v, NSDecimalNumber)

        from objc._pythonify import numberWrapper

        o = numberWrapper(v)
        self.assertIs(o, v)

    def testLongValue(self):
        v = NSNumber.numberWithUnsignedLongLong_(2**63 + 5000)
        self.assertIsInstance(v, int)

        if os_level_key(os_release()) < os_level_key("10.5"):
            self.assertEqual(v.description(), str(-(2**63) + 5000))
        else:
            self.assertEqual(v.description(), str(2**63 + 5000))

        self.assertIsNot(type(v), int)

        with self.assertRaisesRegex(
            AttributeError, "'.*NSCFNumber' object has no attribute 'x'"
        ):
            v.x = 42

    def testEdgeCases(self):
        from objc._pythonify import numberWrapper

        n = objc.lookUpClass("NSObject").alloc().init()

        with warnings.catch_warnings(record=True) as w:
            warnings.filterwarnings("always")
            numberWrapper(n)
        self.assertEqual(len(w), 1)
        self.assertEqual(w[0].category, RuntimeWarning)

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=RuntimeWarning)

            self.assertIs(numberWrapper(n), n)

        # Fake number class, to ensure that all of
        # numberWrapper can be tested with a 64-bit runtime
        class Number(objc.lookUpClass("NSObject")):
            def objCType(self):
                return objc._C_INT

            def longValue(self):
                return 42

        n = Number.alloc().init()
        v = numberWrapper(n)
        self.assertEqual(v, 42)
        self.assertIs(v.__pyobjc_object__, n)

    def testPickling(self):
        v = {
            "long": NSNumber.numberWithUnsignedLongLong_(2**63 + 5000),
            "int": NSNumber.numberWithInt_(42),
            "float": NSNumber.numberWithDouble_(2.0),
        }
        import pickle

        data = pickle.dumps(v)

        w = pickle.loads(data)
        if os_level_key(os_release()) < os_level_key("10.5"):
            self.assertEqual(w, {"long": -(2**63) + 5000, "int": 42, "float": 2.0})
        else:
            self.assertEqual(w, {"long": 2**63 + 5000, "int": 42, "float": 2.0})

        for o in v.values():
            self.assertTrue(hasattr(o, "__pyobjc_object__"))

        for o in w.values():
            self.assertFalse(hasattr(o, "__pyobjc_object__"))

    def testShortConversions(self):
        v = NSNumber.numberWithShort_(42)

        self.assertEqual(v.stringValue(), "42")

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsFloat_(v), 42.0)
        self.assertEqual(OC_NumberInt.numberAsDouble_(v), 42.0)

    def testIntConversions(self):
        v = NSNumber.numberWithInt_(42)

        self.assertEqual(v.stringValue(), "42")

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsFloat_(v), 42.0)
        self.assertEqual(OC_NumberInt.numberAsDouble_(v), 42.0)

        # Negative values
        v = NSNumber.numberWithInt_(-42)

        self.assertEqual(v.stringValue(), "-42")

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 214)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 65494)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 4_294_967_254)

        if sys.maxsize == (2**31) - 1:
            self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 4_294_967_254)
            self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 4_294_967_254)
        else:
            self.assertEqual(
                OC_NumberInt.numberAsUnsignedLong_(v), 18_446_744_073_709_551_574
            )
            self.assertEqual(
                OC_NumberInt.numberAsUnsignedInteger_(v), 18_446_744_073_709_551_574
            )

        self.assertEqual(
            OC_NumberInt.numberAsUnsignedLongLong_(v), 18_446_744_073_709_551_574
        )
        self.assertEqual(OC_NumberInt.numberAsFloat_(v), -42.0)
        self.assertEqual(OC_NumberInt.numberAsDouble_(v), -42.0)

        # Overflow
        v = NSNumber.numberWithInt_(892_455)

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 39)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), -25049)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 39)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 40487)

    def testDoubleConversions(self):
        v = NSNumber.numberWithDouble_(75.5)
        self.assertEqual(v.stringValue(), "75.5")
        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsFloat_(v), 75.5)
        self.assertEqual(OC_NumberInt.numberAsDouble_(v), 75.5)

        # Negative values
        v = NSNumber.numberWithDouble_(-127.6)
        self.assertEqual(v.stringValue(), "-127.6")

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 129)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 65409)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 4_294_967_169)

        # NOTE: The expected values in the test below were determined by running
        #       the equivalent ObjC code.

        # Test disabled because this tests an implementation detail of NSNumber and
        # causes test failures on newer versions of macOS (that can be reproduced in
        # Objective-C code).
        # if objc.arch == "arm64":
        #    self.assertEqual(
        #        OC_NumberInt.numberAsUnsignedLong_(v), 18_446_744_073_709_551_615
        #    )
        #    self.assertEqual(
        #        OC_NumberInt.numberAsUnsignedInteger_(v), 18_446_744_073_709_551_615
        #    )
        # else:
        #    self.assertEqual(
        #        OC_NumberInt.numberAsUnsignedLong_(v), 18_446_744_073_709_551_488
        #    )
        #    self.assertEqual(
        #        OC_NumberInt.numberAsUnsignedInteger_(v), 18_446_744_073_709_551_488
        #    )

        # The first entry in the tuple below is incorrect, that happens to be what
        # is returned by NSNumber on some platforms (in particular, any Python where
        # the python framework itself is linked against the 10.4 SDK)
        #
        #   double v = -127.6;
        #   unsigned long long lv = v;
        #   printf("%llu\n", lv);
        #

        self.assertIn(
            OC_NumberInt.numberAsUnsignedLongLong_(v),
            (
                9_223_372_036_854_775_808,
                18_446_744_073_709_551_489,
                18_446_744_073_709_551_488,
                18_446_744_073_709_551_615,
            ),
        )

        self.assertEqual(OC_NumberInt.numberAsDouble_(v), -127.6)

        # Overflow
        v = NSNumber.numberWithDouble_(float(2**64 + 99))

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)

        if objc.arch == "arm64":
            self.assertEqual(OC_NumberInt.numberAsChar_(v), -1)
            self.assertEqual(OC_NumberInt.numberAsShort_(v), -1)
            self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 255)
            self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 65535)
        else:
            self.assertEqual(OC_NumberInt.numberAsChar_(v), 0)
            self.assertEqual(OC_NumberInt.numberAsShort_(v), 0)
            self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 0)
            self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 0)

    def testCompare(self):
        self.assertEqual(
            OC_NumberInt.compareA_andB_(
                NSNumber.numberWithLong_(0), NSNumber.numberWithLong_(1)
            ),
            NSOrderedAscending,
        )
        self.assertEqual(
            OC_NumberInt.compareA_andB_(
                NSNumber.numberWithLong_(0),
                NSNumber.numberWithUnsignedLongLong_(2**40),
            ),
            NSOrderedAscending,
        )
        self.assertEqual(
            OC_NumberInt.compareA_andB_(
                NSNumber.numberWithLong_(0), NSNumber.numberWithDouble_(42.0)
            ),
            NSOrderedAscending,
        )

        self.assertEqual(
            OC_NumberInt.compareA_andB_(
                NSNumber.numberWithLong_(0), NSNumber.numberWithLong_(-1)
            ),
            NSOrderedDescending,
        )
        self.assertEqual(
            OC_NumberInt.compareA_andB_(
                NSNumber.numberWithLong_(0), NSNumber.numberWithLongLong_(-(2**60))
            ),
            NSOrderedDescending,
        )
        self.assertEqual(
            OC_NumberInt.compareA_andB_(
                NSNumber.numberWithLong_(0), NSNumber.numberWithDouble_(-42.0)
            ),
            NSOrderedDescending,
        )

        self.assertEqual(
            OC_NumberInt.compareA_andB_(
                NSNumber.numberWithLong_(0), NSNumber.numberWithLong_(0)
            ),
            NSOrderedSame,
        )
        self.assertEqual(
            OC_NumberInt.compareA_andB_(
                NSNumber.numberWithLong_(0), NSNumber.numberWithDouble_(0.0)
            ),
            NSOrderedSame,
        )
        self.assertEqual(
            OC_NumberInt.compareA_andB_(
                NSNumber.numberWithLong_(0), NSNumber.numberWithLongLong_(0)
            ),
            NSOrderedSame,
        )

    def testDescription(self):
        v = OC_NumberInt.numberDescription_(NSNumber.numberWithInt_(0))
        self.assertIsInstance(v, str)
        self.assertEqual(v, "0")

        v = OC_NumberInt.numberDescription_(NSNumber.numberWithLongLong_(2**60))
        self.assertIsInstance(v, str)
        self.assertEqual(v, str(2**60))

        v = OC_NumberInt.numberDescription_(NSNumber.numberWithLongLong_(-(2**60)))
        self.assertIsInstance(v, str)
        self.assertEqual(v, str(-(2**60)))

        v = OC_NumberInt.numberDescription_(NSNumber.numberWithDouble_(264.0))
        self.assertIsInstance(v, str)
        self.assertEqual(v, "264")

        class num(int):
            def __repr__(self):
                return False

        with self.assertRaises(TypeError):
            repr(num())

        with self.assertRaises(TypeError):
            OC_NumberInt.numberDescription_(num())

        class num(int):
            def __repr__(self):
                return NoObjectiveC()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_NumberInt.numberDescription_(num())


class TestPyNumber(TestCase):
    # Basic tests of the proxy methods

    def testClasses(self):
        # Ensure that python numbers are proxied using the right proxy type
        for v in (0, 1, 2**32 + 1, 2**64 + 1, 42.5):
            self.assertIs(OC_NumberInt.numberClass_(v), OC_BuiltinPythonNumber)

        # The booleans True and False must be proxied as the corresponding
        # NSNumber constants, otherwise lowlevel Cocoa/CoreFoundation code
        # get's upset.
        try:
            boolClass = objc.lookUpClass("__NSCFBoolean")
        except objc.error:
            boolClass = objc.lookUpClass("NSCFBoolean")

        for v in (True, False):
            self.assertIs(OC_NumberInt.numberClass_(v), boolClass)
            self.assertIs(objc.repythonify(v), v)

    def test_repythonify_invalid(self):
        with self.assertRaisesRegex(
            TypeError,
            r"(function missing required argument 'obj' \(pos 1\))|(Required argument 'obj' \(pos 1\) not found)",
        ):
            objc.repythonify()

        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'str'"
        ):
            objc.repythonify(42, "i")

        with self.assertRaisesRegex(
            objc.internal_error, "PyObjCRT_SizeOfType: Unhandled type '0x5f', _"
        ):
            objc.repythonify(42, b"_")

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str' of 1"):
            objc.repythonify("a", b"i")

    def testPythonIntConversions(self):
        # Conversions to other values. Note that values are converted
        # using C casts, without any exceptions when converting a
        # negative value to an unsigned one and without exceptions for
        # overflow.
        v = 42

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsFloat_(v), 42.0)
        self.assertEqual(OC_NumberInt.numberAsDouble_(v), 42.0)

        # Negative values
        v = -42

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 214)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 65494)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 4_294_967_254)

        if sys.maxsize == (2**31) - 1:
            self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 4_294_967_254)
            self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 4_294_967_254)
        else:
            self.assertEqual(
                OC_NumberInt.numberAsUnsignedLong_(v), 18_446_744_073_709_551_574
            )
            self.assertEqual(
                OC_NumberInt.numberAsUnsignedInteger_(v), 18_446_744_073_709_551_574
            )

        self.assertEqual(
            OC_NumberInt.numberAsUnsignedLongLong_(v), 18_446_744_073_709_551_574
        )
        self.assertEqual(OC_NumberInt.numberAsFloat_(v), -42.0)
        self.assertEqual(OC_NumberInt.numberAsDouble_(v), -42.0)

        # Overflow
        v = 892_455

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 39)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), -25049)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 39)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 40487)

        # Python integer
        v = 42

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsFloat_(v), 42.0)
        self.assertEqual(OC_NumberInt.numberAsDouble_(v), 42.0)

    def testPythonLongConversions(self):
        v = 42

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 42)
        self.assertEqual(OC_NumberInt.numberAsFloat_(v), 42.0)
        self.assertEqual(OC_NumberInt.numberAsDouble_(v), 42.0)

        # Negative values
        v = -42

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), -42)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 214)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 65494)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 4_294_967_254)

        if sys.maxsize == (2**31) - 1:
            self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 4_294_967_254)
            self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 4_294_967_254)
        else:
            self.assertEqual(
                OC_NumberInt.numberAsUnsignedLong_(v), 18_446_744_073_709_551_574
            )
            self.assertEqual(
                OC_NumberInt.numberAsUnsignedInteger_(v), 18_446_744_073_709_551_574
            )

        self.assertEqual(
            OC_NumberInt.numberAsUnsignedLongLong_(v), 18_446_744_073_709_551_574
        )
        self.assertEqual(OC_NumberInt.numberAsFloat_(v), -42.0)
        self.assertEqual(OC_NumberInt.numberAsDouble_(v), -42.0)

        # Overflow
        v = 892_455

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 39)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), -25049)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 39)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 40487)

        # Very much overflow
        v = 2**64 + 1
        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 1)

    def testDoubleConversions(self):
        v = 75.5

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 75)
        self.assertEqual(OC_NumberInt.numberAsFloat_(v), 75.5)
        self.assertEqual(OC_NumberInt.numberAsDouble_(v), 75.5)

        # Negative values
        v = -127.6

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)
        self.assertEqual(OC_NumberInt.numberAsChar_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsShort_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsInt_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsInteger_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsLong_(v), -127)
        self.assertEqual(OC_NumberInt.numberAsLongLong_(v), -127)

        self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 129)
        self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 65409)
        self.assertEqual(OC_NumberInt.numberAsUnsignedInt_(v), 4_294_967_169)

        if sys.maxsize == (2**31) - 1:
            self.assertEqual(OC_NumberInt.numberAsUnsignedLong_(v), 4_294_967_169)
            self.assertEqual(OC_NumberInt.numberAsUnsignedInteger_(v), 4_294_967_169)
        else:
            self.assertEqual(
                OC_NumberInt.numberAsUnsignedLong_(v), 18_446_744_073_709_551_489
            )
            self.assertEqual(
                OC_NumberInt.numberAsUnsignedInteger_(v), 18_446_744_073_709_551_489
            )

        # if sys.byteorder == 'big':
        #    self.assertEqual(OC_NumberInt.numberAsUnsignedLongLong_(v), 4294967169)
        # else:
        self.assertEqual(
            OC_NumberInt.numberAsUnsignedLongLong_(v), 18_446_744_073_709_551_489
        )

        self.assertEqual(OC_NumberInt.numberAsDouble_(v), -127.6)

        # Overflow
        v = float(2**64 + 99)

        self.assertEqual(OC_NumberInt.numberAsBOOL_(v), 1)

        if objc.arch == "arm64":
            self.assertEqual(OC_NumberInt.numberAsChar_(v), -1)
            self.assertEqual(OC_NumberInt.numberAsShort_(v), -1)
            self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 255)
            self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 65535)
        else:
            self.assertEqual(OC_NumberInt.numberAsChar_(v), 0)
            self.assertEqual(OC_NumberInt.numberAsShort_(v), 0)
            self.assertEqual(OC_NumberInt.numberAsUnsignedChar_(v), 0)
            self.assertEqual(OC_NumberInt.numberAsUnsignedShort_(v), 0)

    def testCompare(self):
        self.assertEqual(OC_NumberInt.compareA_andB_(0, 1), NSOrderedAscending)
        self.assertEqual(OC_NumberInt.compareA_andB_(0, 2**64), NSOrderedAscending)
        self.assertEqual(OC_NumberInt.compareA_andB_(0, 42.0), NSOrderedAscending)

        self.assertEqual(OC_NumberInt.compareA_andB_(0, -1), NSOrderedDescending)
        self.assertEqual(OC_NumberInt.compareA_andB_(0, -(2**64)), NSOrderedDescending)
        self.assertEqual(OC_NumberInt.compareA_andB_(0, -42.0), NSOrderedDescending)

        self.assertEqual(OC_NumberInt.compareA_andB_(0, 0), NSOrderedSame)
        self.assertEqual(OC_NumberInt.compareA_andB_(0, 0.0), NSOrderedSame)

    def testNumberEqualToValue(self):
        self.assertFalse(OC_NumberInt.number_isEqualToValue_(0, 1))
        self.assertFalse(OC_NumberInt.number_isEqualToValue_(0, 2**64))
        self.assertFalse(OC_NumberInt.number_isEqualToValue_(0, 42.0))

        self.assertFalse(OC_NumberInt.number_isEqualToValue_(0, -1))
        self.assertFalse(OC_NumberInt.number_isEqualToValue_(0, -(2**64)))
        self.assertFalse(OC_NumberInt.number_isEqualToValue_(0, -42.0))

        self.assertTrue(OC_NumberInt.number_isEqualToValue_(0, 0))
        self.assertTrue(OC_NumberInt.number_isEqualToValue_(0, 0.0))

    def testNumberEqual(self):
        self.assertFalse(OC_NumberInt.number_isEqualTo_(0, 1))
        self.assertFalse(OC_NumberInt.number_isEqualTo_(0, 2**64))
        self.assertFalse(OC_NumberInt.number_isEqualTo_(0, 42.0))

        self.assertFalse(OC_NumberInt.number_isEqualTo_(0, -1))
        self.assertFalse(OC_NumberInt.number_isEqualTo_(0, -(2**64)))
        self.assertFalse(OC_NumberInt.number_isEqualTo_(0, -42.0))

        self.assertTrue(OC_NumberInt.number_isEqualTo_(0, 0))
        self.assertTrue(OC_NumberInt.number_isEqualTo_(0, 0.0))

    def testDescription(self):
        v = OC_NumberInt.numberDescription_(0)
        self.assertIsInstance(v, str)
        self.assertEqual(v, "0")

        v = OC_NumberInt.numberDescription_(2**64)
        self.assertIsInstance(v, str)
        self.assertEqual(v, repr(2**64))

        v = OC_NumberInt.numberDescription_(-(2**64))
        self.assertIsInstance(v, str)
        self.assertEqual(v, repr(-(2**64)))

        v = OC_NumberInt.numberDescription_(264.0)
        self.assertIsInstance(v, str)
        self.assertEqual(v, "264.0")

        v = OC_NumberInt.numberDescription_(False)
        self.assertIsInstance(v, str)
        self.assertEqual(v, "0")

        v = OC_NumberInt.numberDescription_(True)
        self.assertIsInstance(v, str)
        self.assertEqual(v, "1")


class TestInteractions(TestCase):
    # Test interactions between Python and NSNumber numbers

    def testMixedCompare(self):
        # compare for:
        #   - python number to nsnumber
        #   - nsnumber to python number
        # For: (bool, int, long, float) vs (char, short, ...)
        methods = [
            "numberWithInt_",
            "numberWithChar_",
            "numberWithLong_",
            "numberWithDouble_",
        ]

        self.assertEqual(OC_NumberInt.compareA_andB_(42, 42), NSOrderedSame)
        for m in methods:
            self.assertEqual(
                OC_NumberInt.compareA_andB_(getattr(NSNumber, m)(42), 42),
                NSOrderedSame,
            )
            self.assertEqual(
                OC_NumberInt.compareA_andB_(42, getattr(NSNumber, m)(42)),
                NSOrderedSame,
            )

        self.assertEqual(OC_NumberInt.compareA_andB_(42, 99), NSOrderedAscending)
        for m in methods:
            self.assertEqual(
                OC_NumberInt.compareA_andB_(getattr(NSNumber, m)(42), 99),
                NSOrderedAscending,
            )
            self.assertEqual(
                OC_NumberInt.compareA_andB_(42, getattr(NSNumber, m)(99)),
                NSOrderedAscending,
            )

    def testMixedEquals(self):
        # isEqualToNumber for:
        #   - python number to nsnumber
        #   - nsnumber to python number
        # For: (bool, int, long, float) vs (char, short, ...)
        self.assertTrue(OC_NumberInt.number_isEqualTo_(0, NSNumber.numberWithInt_(0)))
        self.assertTrue(OC_NumberInt.number_isEqualTo_(0, NSNumber.numberWithLong_(0)))
        self.assertTrue(OC_NumberInt.number_isEqualTo_(0, NSNumber.numberWithFloat_(0)))
        self.assertTrue(OC_NumberInt.number_isEqualTo_(NSNumber.numberWithInt_(0), 0))
        self.assertTrue(OC_NumberInt.number_isEqualTo_(NSNumber.numberWithLong_(0), 0))
        self.assertTrue(OC_NumberInt.number_isEqualTo_(NSNumber.numberWithFloat_(0), 0))

        self.assertFalse(OC_NumberInt.number_isEqualTo_(42, NSNumber.numberWithInt_(0)))
        self.assertFalse(
            OC_NumberInt.number_isEqualTo_(42, NSNumber.numberWithLong_(0))
        )
        self.assertFalse(
            OC_NumberInt.number_isEqualTo_(42, NSNumber.numberWithFloat_(0))
        )
        self.assertFalse(OC_NumberInt.number_isEqualTo_(NSNumber.numberWithInt_(0), 42))
        self.assertFalse(
            OC_NumberInt.number_isEqualTo_(NSNumber.numberWithLong_(0), 42)
        )
        self.assertFalse(
            OC_NumberInt.number_isEqualTo_(NSNumber.numberWithFloat_(0), 42)
        )


class TestNumberFormatter(TestCase):
    # Test behaviour of an NSNumberFormatter, both with
    # Python numbers and NSNumbers
    def testFormatting(self):
        formatter = NSNumberFormatter.alloc().init()

        n = NSNumber.numberWithInt_(42)
        p = 42
        self.assertEqual(
            formatter.stringForObjectValue_(n), formatter.stringForObjectValue_(p)
        )

        n = NSNumber.numberWithInt_(-42)
        p = -42
        self.assertEqual(
            formatter.stringForObjectValue_(n), formatter.stringForObjectValue_(p)
        )

        n = NSNumber.numberWithDouble_(10.42)
        p = 10.42
        self.assertEqual(
            formatter.stringForObjectValue_(n), formatter.stringForObjectValue_(p)
        )


class FailedComparison:
    def __eq__(self, other):
        raise ValueError("comparing is not supported")

    def __ne__(self, other):
        raise ValueError("comparing is not supported")


class NotLess:
    def __lt__(self, other):
        return False


class NotComparable:
    def __lt__(self, other):
        return False

    def __gt__(self, other):
        return False


class FailedComparisonInt(int):
    def __eq__(self, other):
        raise ValueError("comparing is not supported")

    def __ne__(self, other):
        raise ValueError("comparing is not supported")


class TestFailedComparisions(TestCase):
    def test_exception_while_comparing(self):
        num = 42
        other = FailedComparison()
        other_num = FailedComparisonInt(42)

        with self.assertRaisesRegex(ValueError, "comparing is not supported"):
            OC_Misc.compare_and_(num, other)

        with self.assertRaisesRegex(ValueError, "comparing is not supported"):
            OC_Misc.compare_and_(other, num)

        with self.assertRaisesRegex(ValueError, "comparing is not supported"):
            OC_Misc.compare_and_(num, other_num)

        with self.assertRaisesRegex(ValueError, "comparing is not supported"):
            OC_Misc.compare_and_(other_num, num)

    def test_comparison_failures(self):
        with self.assertRaisesRegex(
            TypeError, r"'.{1,2}' not supported between instances of 'int' and 'object'"
        ):
            OC_Misc.compare_and_(42, object())

        with self.assertRaisesRegex(
            TypeError, r"'.{1,2}' not supported between instances of 'object' and 'int'"
        ):
            OC_Misc.compare_and_(object(), 42)

        with self.assertRaisesRegex(
            TypeError,
            r"'.{1,2}' not supported between instances of 'int' and 'NotLess'",
        ):
            OC_Misc.compare_and_(42, NotLess())

        with self.assertRaisesRegex(
            TypeError,
            r"'.{1,2}' not supported between instances of 'NotLess' and 'int'",
        ):
            OC_Misc.compare_and_(NotLess(), 42)

        with self.assertRaisesRegex(TypeError, r".* and .* cannot be compared"):
            OC_Misc.compare_and_(42, NotComparable())

        with self.assertRaisesRegex(TypeError, r".* and .* cannot be compared"):
            OC_Misc.compare_and_(NotComparable(), 42)

        with self.assertRaisesRegex(
            TypeError,
            r"'.{1,2}' not supported between instances of 'object' and 'object'",
        ):
            OC_Misc.compare_and_(object(), object())

        with self.assertRaisesRegex(
            TypeError,
            r"'.{1,2}' not supported between instances of 'object' and 'object'",
        ):
            OC_Misc.compare_and_(object(), object())

        with self.assertRaisesRegex(
            TypeError,
            r"'.{1,2}' not supported between instances of 'object' and 'NotLess'",
        ):
            OC_Misc.compare_and_(object(), NotLess())

        with self.assertRaisesRegex(
            TypeError,
            r"'.{1,2}' not supported between instances of 'NotLess' and 'object'",
        ):
            OC_Misc.compare_and_(NotLess(), object())

        with self.assertRaisesRegex(TypeError, r".* and .* cannot be compared"):
            OC_Misc.compare_and_(object(), NotComparable())

        with self.assertRaisesRegex(TypeError, r".* and .* cannot be compared"):
            OC_Misc.compare_and_(NotComparable(), object())


class TestComparsionMethods(TestCase):
    def check_equal_values(self, left, right, expected):
        for left_as_nsnumber in [False, True]:
            for right_as_nsnumber in [False, True]:
                with self.subTest(
                    left=left,
                    left_as_nsnumber=left_as_nsnumber,
                    right=right,
                    right_as_nsnumber=right_as_nsnumber,
                    expected=expected,
                ):
                    actual = OC_NumberInt.number_isEqualTo_(
                        as_nsnumber(left) if left_as_nsnumber else left,
                        as_nsnumber(right) if right_as_nsnumber else right,
                    )
                    self.assertEqual(actual, expected, f"{left} != {right}")

    def check_notequal_values(self, left, right, expected):
        for left_as_nsnumber in [False, True]:
            for right_as_nsnumber in [False, True]:
                with self.subTest(
                    left=left,
                    left_as_nsnumber=left_as_nsnumber,
                    right=right,
                    right_as_nsnumber=right_as_nsnumber,
                    expected=expected,
                ):
                    actual = OC_NumberInt.number_isNotEqualTo_(
                        as_nsnumber(left) if left_as_nsnumber else left,
                        as_nsnumber(right) if right_as_nsnumber else right,
                    )
                    self.assertEqual(actual, expected, f"{left} != {right}")

    def test_misc_comparisons(self):
        # Checks for the values comparison methods.
        # This uses some deeply nested loops to test all of them in one go:
        #  - All methods
        #  - Left and right hand can be both Python numbers and NSNumbers
        values = [1, 2, 1.0, 2.0, -0.0, 0, 2.5, -44, -44.0, -44.5, -44.5, True, False]

        for test_method, check_method in [
            (OC_NumberInt.number_isEqualTo_, operator.eq),
            (OC_NumberInt.number_isNotEqualTo_, operator.ne),
            (OC_NumberInt.number_isGreaterThan_, operator.gt),
            (OC_NumberInt.number_isGreaterThanOrEqualTo_, operator.ge),
            (OC_NumberInt.number_isLessThan_, operator.lt),
            (OC_NumberInt.number_isLessThanOrEqualTo_, operator.le),
        ]:
            s = set()
            for left in values:
                for right in values:
                    for left_as_nsnumber in [False, True]:
                        for right_as_nsnumber in [False, True]:
                            with self.subTest(
                                func=check_method.__name__,
                                left=left,
                                left_as_nsnumber=left_as_nsnumber,
                                right=right,
                                right_as_nsnumber=right_as_nsnumber,
                            ):
                                l = (  # noqa: E741
                                    as_nsnumber(left) if left_as_nsnumber else left
                                )
                                r = as_nsnumber(right) if right_as_nsnumber else right
                                actual = test_method(l, r)
                                expected = check_method(l, r)
                                s.add(expected)

                                self.assertEqual(actual, expected)
            with self.subTest(func=check_method.__name__):
                self.assertEqual(s, {True, False})

    def test_comparision_with_large_long(self):
        OC_NumberInt.number_isEqualTo_(2**63 + 10, 2**63 + 10)
        OC_NumberInt.number_isEqualTo_(2**63 + 10, as_nsnumber(2**63 + 10))
        OC_NumberInt.number_isEqualTo_(as_nsnumber(2**63 + 10), 2**63 + 10)
        OC_NumberInt.number_isEqualTo_(as_nsnumber(2**63 + 10), as_nsnumber(2**63 + 10))

    def test_encoding(self):
        self.assertEqual(OC_NumberInt.objCTypeOf_(0), objc._C_LNG_LNG)
        self.assertEqual(OC_NumberInt.objCTypeOf_(-50), objc._C_LNG_LNG)
        self.assertEqual(OC_NumberInt.objCTypeOf_(5.0), objc._C_DBL)
        self.assertEqual(OC_NumberInt.objCTypeOf_(False), objc._C_CHR)
        self.assertEqual(OC_NumberInt.objCTypeOf_(2**63 + 10), objc._C_ULNG_LNG)
        self.assertEqual(OC_NumberInt.objCTypeOf_(2**80 + 10), objc._C_LNG_LNG)

    def test_getValue(self):
        value = OC_NumberInt.getValueOf_(42)
        self.assertTrue(bytes(value).startswith(struct.pack("q", 42)))

        value = OC_NumberInt.getValueOf_(-42)
        self.assertTrue(bytes(value).startswith(struct.pack("q", -42)))

        value = OC_NumberInt.getValueOf_(2**63 + 10)
        self.assertTrue(bytes(value).startswith(struct.pack("Q", 2**63 + 10)))

        value = OC_NumberInt.getValueOf_(53.4)
        self.assertTrue(bytes(value).startswith(struct.pack("d", 53.4)))

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'int' of wrong magnitude"
        ):
            OC_NumberInt.getValueOf_(2**64 + 10)

    def test_returning_decimal(self):
        value = OC_NumberInt.numberAsDecimal_(42)
        self.assertIsInstance(value, NSDecimalNumber)
        self.assertIsInstance(value.decimalValue(), objc.NSDecimal)
        self.assertEqual(value.decimalValue(), objc.NSDecimal(42))

        value = OC_NumberInt.numberAsDecimal_(42.5)
        self.assertIsInstance(value, NSDecimalNumber)
        self.assertIsInstance(value.decimalValue(), objc.NSDecimal)
        self.assertEqual(value.decimalValue(), objc.NSDecimal(42.5))

        with self.assertRaisesRegex(OverflowError, "int too big to convert"):
            OC_NumberInt.numberAsDecimal_(2**65)

    def test_number_options(self):
        orig = objc.options._nsnumber_wrapper
        try:
            v = NSNumber.numberWithInt_(42)

            self.assertIn("OC_PythonLong", type(v).__name__)
            self.assertIsInstance(v, NSNumber)

            objc.options._nsnumber_wrapper = None

            v = NSNumber.numberWithInt_(43)

            self.assertNotIn("OC_PythonLong", type(v).__name__)
            self.assertIsInstance(v, NSNumber)

            def raiser(*args):
                raise RuntimeError

            objc.options._nsnumber_wrapper = raiser

            with self.assertRaises(RuntimeError):
                NSNumber.numberWithInt_(44)

        finally:
            objc.options._nsnumber_wrapper = orig
