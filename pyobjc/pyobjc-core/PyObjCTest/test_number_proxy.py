"""
Tests for the proxy of Python numbers

NOTE: Decimal conversion is not tested, the required proxy is part of 
the Foundation bindings :-(
"""
import sys, os
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSNumber, NSNumberFormatter
from PyObjCTest.pythonnumber import OC_TestNumber
import objc

OC_PythonNumber = objc.lookUpClass("OC_PythonNumber")
NSCFNumber = objc.lookUpClass("NSCFNumber")

NSOrderedAscending = -1
NSOrderedSame = 0
NSOrderedDescending = 1

class TestNSNumber (TestCase):
    # These testcases check the behaviour of NSNumber, these
    # are mostly here to verify that NSNumbers behave as
    # we expect them to.

    def testClass(self):
        for m in ('numberWithInt_', 'numberWithFloat_', 'numberWithDouble_', 'numberWithShort_'):
            v = getattr(NSNumber, m)(0)
            self.assert_(isinstance(v, NSNumber))
            self.assert_(not isinstance(v, OC_PythonNumber))
            self.assert_(OC_TestNumber.numberClass_(v) is NSCFNumber)

    def testShortConversions(self):
        v = NSNumber.numberWithShort_(42)

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsFloat_(v), 42.0)
        self.assertEquals(OC_TestNumber.numberAsDouble_(v), 42.0)

    def testIntConversions(self):
        v = NSNumber.numberWithInt_(42)

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsFloat_(v), 42.0)
        self.assertEquals(OC_TestNumber.numberAsDouble_(v), 42.0)

        # Negative values
        v = NSNumber.numberWithInt_(-42)

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 214)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 65494)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 4294967254)

        if sys.maxint == (2 ** 31) -1:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 4294967254)
        else:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 18446744073709551574)

        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 18446744073709551574)
        self.assertEquals(OC_TestNumber.numberAsFloat_(v), -42.0)
        self.assertEquals(OC_TestNumber.numberAsDouble_(v), -42.0)

        # Overflow
        v = NSNumber.numberWithInt_(892455)

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), 39)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), -25049)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 39)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 40487)

    def testDoubleConversions(self):
        v = NSNumber.numberWithDouble_(75.5)

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsFloat_(v), 75.5)
        self.assertEquals(OC_TestNumber.numberAsDouble_(v), 75.5)

        # Negative values
        v = NSNumber.numberWithDouble_(-127.6)

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), -127)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), -127)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), -127)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), -127)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), -127)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 129)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 65409)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 4294967169)

        if sys.maxint == (2 ** 31) -1:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 4294967169)
        else:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 18446744073709551488)

        # The first entry in the tuple below is incorrect, that happens to be what
        # is returned by NSNumber on some platforms (in particular, any Python where
        # the python framework itself is linked against the 10.4 SDK)
        #
        #   double v = -127.6;
        #   unsigned long long lv = v;
        #   printf("%llu\n", lv);
        # 

        self.failUnless(
                OC_TestNumber.numberAsUnsignedLongLong_(v) in 
                    (18446744073709551489, 18446744073709551488))

        self.assertEquals(OC_TestNumber.numberAsDouble_(v), -127.6)

        # Overflow
        v = NSNumber.numberWithDouble_(float(2**64 + 99))

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)

        if sys.byteorder == 'big':
            self.assertEquals(OC_TestNumber.numberAsChar_(v), -1)
            self.assertEquals(OC_TestNumber.numberAsShort_(v), -1)
            self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 255)
            self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 65535)
        else:
            self.assertEquals(OC_TestNumber.numberAsChar_(v), 0)
            self.assertEquals(OC_TestNumber.numberAsShort_(v), 0)
            self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 0)
            self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 0)

    def testCompare(self):
        self.assertEquals(OC_TestNumber.compareA_andB_(NSNumber.numberWithLong_(0), NSNumber.numberWithLong_(1)), NSOrderedAscending)
        self.assertEquals(OC_TestNumber.compareA_andB_(NSNumber.numberWithLong_(0), NSNumber.numberWithUnsignedLongLong_(2**40)), NSOrderedAscending)
        self.assertEquals(OC_TestNumber.compareA_andB_(NSNumber.numberWithLong_(0), NSNumber.numberWithDouble_(42.0)), NSOrderedAscending)

        self.assertEquals(OC_TestNumber.compareA_andB_(NSNumber.numberWithLong_(0), NSNumber.numberWithLong_(-1)), NSOrderedDescending)
        self.assertEquals(OC_TestNumber.compareA_andB_(NSNumber.numberWithLong_(0), NSNumber.numberWithLongLong_(-2**60)), NSOrderedDescending)
        self.assertEquals(OC_TestNumber.compareA_andB_(NSNumber.numberWithLong_(0), NSNumber.numberWithDouble_(-42.0)), NSOrderedDescending)

        self.assertEquals(OC_TestNumber.compareA_andB_(NSNumber.numberWithLong_(0), NSNumber.numberWithLong_(0)), NSOrderedSame)
        self.assertEquals(OC_TestNumber.compareA_andB_(NSNumber.numberWithLong_(0), NSNumber.numberWithDouble_(0.0)), NSOrderedSame)
        self.assertEquals(OC_TestNumber.compareA_andB_(NSNumber.numberWithLong_(0), NSNumber.numberWithLongLong_(0)), NSOrderedSame)

    def testDescription(self):
        v = OC_TestNumber.numberDescription_(NSNumber.numberWithInt_(0))
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, u"0")

        v = OC_TestNumber.numberDescription_(NSNumber.numberWithLongLong_(2**60))
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, unicode(str(2**60)))

        v = OC_TestNumber.numberDescription_(NSNumber.numberWithLongLong_(-2**60))
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, unicode(str(-2**60)))

        v = OC_TestNumber.numberDescription_(NSNumber.numberWithDouble_(264.0))
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, u"264")


class TestPyNumber (TestCase):
    # Basic tests of the proxy methods

    def testClasses(self):
        # Ensure that python numbers are proxied using the right proxy type
        for v in (0, 1, 2**32+1, 2**64+1, 42.5):
            self.assert_(OC_TestNumber.numberClass_(v) is OC_PythonNumber)

        # The booleans True and False must be proxied as the corresponding
        # NSNumber constants, otherwise lowlevel Cocoa/CoreFoundation code
        # get's upset.
        boolClass = objc.lookUpClass('NSCFBoolean')
        for v in (True, False):
            self.assert_(OC_TestNumber.numberClass_(v) is boolClass)
            self.assert_(objc.repythonify(v) is v)


    def testPythonIntConversions(self):
        # Conversions to other values. Note that values are converted
        # using C casts, without any exceptions when converting a
        # negative value to an unsigned one and without exceptions for
        # overflow.
        v = 42

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsFloat_(v), 42.0)
        self.assertEquals(OC_TestNumber.numberAsDouble_(v), 42.0)

        # Negative values
        v = -42

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 214)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 65494)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 4294967254)

        if sys.maxint == (2 ** 31) -1:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 4294967254)
        else:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 18446744073709551574)

        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 18446744073709551574)
        self.assertEquals(OC_TestNumber.numberAsFloat_(v), -42.0)
        self.assertEquals(OC_TestNumber.numberAsDouble_(v), -42.0)

        # Overflow
        v = 892455

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), 39)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), -25049)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 39)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 40487)

    def testPythonLongConversions(self):
        v = long(42)
        self.assert_(isinstance(v, long))

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 42)
        self.assertEquals(OC_TestNumber.numberAsFloat_(v), 42.0)
        self.assertEquals(OC_TestNumber.numberAsDouble_(v), 42.0)

        # Negative values
        v = long(-42)
        self.assert_(isinstance(v, long))

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), -42)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 214)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 65494)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 4294967254)

        if sys.maxint == (2 ** 31) -1:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 4294967254)
        else:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 18446744073709551574)

        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 18446744073709551574)
        self.assertEquals(OC_TestNumber.numberAsFloat_(v), -42.0)
        self.assertEquals(OC_TestNumber.numberAsDouble_(v), -42.0)

        # Overflow
        v = long(892455)
        self.assert_(isinstance(v, long))

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), 39)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), -25049)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 39)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 40487)

        # Very much overflow
        v = 2 ** 64 + 1
        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 1)

    def testDoubleConversions(self):
        v = 75.5

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 75)
        self.assertEquals(OC_TestNumber.numberAsFloat_(v), 75.5)
        self.assertEquals(OC_TestNumber.numberAsDouble_(v), 75.5)

        # Negative values
        v = -127.6

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)
        self.assertEquals(OC_TestNumber.numberAsChar_(v), -127)
        self.assertEquals(OC_TestNumber.numberAsShort_(v), -127)
        self.assertEquals(OC_TestNumber.numberAsInt_(v), -127)
        self.assertEquals(OC_TestNumber.numberAsLong_(v), -127)
        self.assertEquals(OC_TestNumber.numberAsLongLong_(v), -127)
        self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 129)
        self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 65409)
        self.assertEquals(OC_TestNumber.numberAsUnsignedInt_(v), 4294967169)

        if sys.maxint == (2 ** 31) -1:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 4294967169)
        else:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLong_(v), 18446744073709551489)

        if sys.byteorder == 'big':
            self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 4294967169)
        else:
            self.assertEquals(OC_TestNumber.numberAsUnsignedLongLong_(v), 18446744073709551489)

        self.assertEquals(OC_TestNumber.numberAsDouble_(v), -127.6)

        # Overflow
        v = float(2**64 + 99)

        self.assertEquals(OC_TestNumber.numberAsBOOL_(v), 1)

        if sys.byteorder == 'big':
            self.assertEquals(OC_TestNumber.numberAsChar_(v), -1)
            self.assertEquals(OC_TestNumber.numberAsShort_(v), -1)
            self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 255)
            self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 65535)
        else:
            self.assertEquals(OC_TestNumber.numberAsChar_(v), 0)
            self.assertEquals(OC_TestNumber.numberAsShort_(v), 0)
            self.assertEquals(OC_TestNumber.numberAsUnsignedChar_(v), 0)
            self.assertEquals(OC_TestNumber.numberAsUnsignedShort_(v), 0)

    def testCompare(self):
        self.assertEquals(OC_TestNumber.compareA_andB_(0, 1), NSOrderedAscending)
        self.assertEquals(OC_TestNumber.compareA_andB_(0, 2**64), NSOrderedAscending)
        self.assertEquals(OC_TestNumber.compareA_andB_(0, 42.0), NSOrderedAscending)

        self.assertEquals(OC_TestNumber.compareA_andB_(0, -1), NSOrderedDescending)
        self.assertEquals(OC_TestNumber.compareA_andB_(0, -2**64), NSOrderedDescending)
        self.assertEquals(OC_TestNumber.compareA_andB_(0, -42.0), NSOrderedDescending)

        self.assertEquals(OC_TestNumber.compareA_andB_(0, 0), NSOrderedSame)
        self.assertEquals(OC_TestNumber.compareA_andB_(0, 0.0), NSOrderedSame)
        self.assertEquals(OC_TestNumber.compareA_andB_(0, long(0)), NSOrderedSame)

    def testNumberEqual(self):
        self.assert_(not OC_TestNumber.number_isEqualTo_(0, 1))
        self.assert_(not OC_TestNumber.number_isEqualTo_(0, 2**64))
        self.assert_(not OC_TestNumber.number_isEqualTo_(0, 42.0))

        self.assert_(not OC_TestNumber.number_isEqualTo_(0, -1))
        self.assert_(not OC_TestNumber.number_isEqualTo_(0, -2**64))
        self.assert_(not OC_TestNumber.number_isEqualTo_(0, -42.0))

        self.assert_(OC_TestNumber.number_isEqualTo_(0, 0))
        self.assert_(OC_TestNumber.number_isEqualTo_(0, 0.0))
        self.assert_(OC_TestNumber.number_isEqualTo_(0, long(0)))

    def testDescription(self):
        v = OC_TestNumber.numberDescription_(0)
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, u"0")

        v = OC_TestNumber.numberDescription_(2**64)
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, unicode(repr(2**64)))

        v = OC_TestNumber.numberDescription_(-2**64)
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, unicode(repr(-2**64)))

        v = OC_TestNumber.numberDescription_(264.0)
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, u"264.0")

        v = OC_TestNumber.numberDescription_(False)
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, u"0")

        v = OC_TestNumber.numberDescription_(True)
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, u"1")

class TestInteractions (TestCase):
    # Test interactions between Python and NSNumber numbers

    def testMixedCompare(self):
        # compare for:
        #   - python number to nsnumber
        #   - nsnumber to python number
        # For: (bool, int, long, float) vs (char, short, ...)
        methods = [
                'numberWithInt_',
                'numberWithChar_',
                'numberWithLong_',
                'numberWithDouble_',
            ]

        self.assertEqual(OC_TestNumber.compareA_andB_(42, 42), NSOrderedSame)
        for m in methods:
            self.assertEqual(OC_TestNumber.compareA_andB_(getattr(NSNumber, m)(42), 42), NSOrderedSame)
            self.assertEqual(OC_TestNumber.compareA_andB_(42, getattr(NSNumber, m)(42)), NSOrderedSame)

        self.assertEqual(OC_TestNumber.compareA_andB_(42, 99), NSOrderedAscending)
        for m in methods:
            self.assertEqual(OC_TestNumber.compareA_andB_(getattr(NSNumber, m)(42), 99), NSOrderedAscending)
            self.assertEqual(OC_TestNumber.compareA_andB_(42, getattr(NSNumber, m)(99)), NSOrderedAscending)

    def testMixedEquals(self):
        # isEqualToNumber for:
        #   - python number to nsnumber
        #   - nsnumber to python number
        # For: (bool, int, long, float) vs (char, short, ...)
        self.assert_(OC_TestNumber.number_isEqualTo_(0, NSNumber.numberWithInt_(0)))
        self.assert_(OC_TestNumber.number_isEqualTo_(0, NSNumber.numberWithLong_(0)))
        self.assert_(OC_TestNumber.number_isEqualTo_(0, NSNumber.numberWithFloat_(0)))
        self.assert_(OC_TestNumber.number_isEqualTo_(NSNumber.numberWithInt_(0), 0))
        self.assert_(OC_TestNumber.number_isEqualTo_(NSNumber.numberWithLong_(0), 0))
        self.assert_(OC_TestNumber.number_isEqualTo_(NSNumber.numberWithFloat_(0), 0))

        self.assert_(not OC_TestNumber.number_isEqualTo_(42, NSNumber.numberWithInt_(0)))
        self.assert_(not OC_TestNumber.number_isEqualTo_(42, NSNumber.numberWithLong_(0)))
        self.assert_(not OC_TestNumber.number_isEqualTo_(42, NSNumber.numberWithFloat_(0)))
        self.assert_(not OC_TestNumber.number_isEqualTo_(NSNumber.numberWithInt_(0), 42))
        self.assert_(not OC_TestNumber.number_isEqualTo_(NSNumber.numberWithLong_(0), 42))
        self.assert_(not OC_TestNumber.number_isEqualTo_(NSNumber.numberWithFloat_(0), 42))


class TestNumberFormatter (TestCase):
    # Test behaviour of an NSNumberFormatter, both with 
    # Python numbers and NSNumbers
    def testFormatting(self):
        formatter = NSNumberFormatter.alloc().init()

        n = NSNumber.numberWithInt_(42)
        p = 42
        self.assertEquals(formatter.stringForObjectValue_(n), formatter.stringForObjectValue_(p))

        n = NSNumber.numberWithInt_(-42)
        p = -42
        self.assertEquals(formatter.stringForObjectValue_(n), formatter.stringForObjectValue_(p))


        n = NSNumber.numberWithDouble_(10.42)
        p = 10.42
        self.assertEquals(formatter.stringForObjectValue_(n), formatter.stringForObjectValue_(p))

if __name__ == "__main__":
    main()
