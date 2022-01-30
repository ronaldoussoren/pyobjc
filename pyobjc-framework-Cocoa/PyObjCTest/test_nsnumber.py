import operator
import os
import re
import sys

import objc
import Foundation
from PyObjCTools.TestSupport import TestCase, sdkForPython

# flake8: noqa: B950
PLIST = b"""\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
\t<key>bool</key>
\t<true/>
\t<key>plain</key>
\t<integer>1</integer>
</dict>
</plist>
""".decode(
    "latin1"
)


def stripDocType(val):
    """
    Strip non-significant information. This is needed because the proplists
    on macOS 10.1 are slightly different from the ones on macOS 10.2 (
    different DOCTYPE and version).
    """
    r = re.sub("<!DOCTYPE [^>]*>", "<!DOCTYPE>", val)
    return r.replace('version="0.9"', 'version="1.0"')


class TestNSNumber(TestCase):
    def testSimple(self):
        self.assertEqual(Foundation.NSNumber.numberWithFloat_(1.0), 1, 0)
        self.assertEqual(Foundation.NSNumber.numberWithInt_(1), 1)
        self.assertEqual(Foundation.NSNumber.numberWithFloat_(-0.5), -0.5)
        self.assertEqual(Foundation.NSNumber.numberWithInt_(-4), -4)
        self.assertEqual(Foundation.NSNumber.numberWithInt_(0), 0)
        self.assertEqual(Foundation.NSNumber.numberWithFloat_(0.0), 0.0)

    def testReadOnly(self):
        n = Foundation.NSNumber.numberWithFloat_(1.2)
        self.assertRaises(AttributeError, setattr, n, "foo", 2)

        n = Foundation.NSNumber.numberWithInt_(1)
        self.assertRaises(AttributeError, setattr, n, "foo", 2)

        n = Foundation.NSNumber.numberWithLongLong_(2**32 + 2)
        self.assertRaises(AttributeError, setattr, n, "foo", 2)

    def testUseAsBasicType(self):
        lstValue = list(range(0, 20, 2))
        for idx, v in enumerate(lstValue):
            self.assertEqual(v, lstValue[Foundation.NSNumber.numberWithInt_(idx)])
            self.assertEqual(v, lstValue[Foundation.NSNumber.numberWithLong_(idx)])
            self.assertEqual(v, lstValue[Foundation.NSNumber.numberWithLongLong_(idx)])

        self.assertRaises(
            TypeError,
            operator.getitem,
            lstValue,
            Foundation.NSNumber.numberWithFloat_(2.0),
        )

    def testUnsignedIssues(self):
        # Foundation.NSNumber stores unsigned numbers as signed numbers
        # This is a bug in Cocoa... (RADAR #4007594), fixed in 10.5
        if sdkForPython() is not None and sdkForPython() < (10, 5):
            self.assertEqual(
                Foundation.NSNumber.numberWithUnsignedInt_(2**31), -(2**31)
            )
        else:
            self.assertEqual(
                Foundation.NSNumber.numberWithUnsignedInt_(2**31), (2**31)
            )

    def testMethods(self):
        v = Foundation.NSNumber.numberWithUnsignedInt_(2**31)

        self.assertEqual(v.unsignedIntValue(), 2**31)
        self.assertEqual(v.intValue(), -(2**31))

        v = Foundation.NSNumber.numberWithInt_(10)
        self.assertEqual(v.doubleValue(), float(10))

    def testMath(self):
        Xs = list(range(10, 40, 3))
        Ys = list(range(-12, 44, 5))

        self.assertTrue(0 not in Ys)
        self.assertTrue(0 not in Xs)

        for x in Xs:
            for y in Ys:
                Nx = Foundation.NSNumber.numberWithInt_(x)
                Ny = Foundation.NSNumber.numberWithInt_(y)

                self.assertEqual(x + y, Nx + Ny)
                self.assertEqual(x - y, Nx - Ny)
                self.assertEqual(x * y, Nx * Ny)
                self.assertEqual(x / y, Nx / Ny)
                self.assertEqual(x % y, Nx % Ny)
                self.assertEqual(x**y, Nx**Ny)

                Nx = Foundation.NSNumber.numberWithFloat_(x + 0.5)
                Ny = Foundation.NSNumber.numberWithFloat_(y + 0.5)

                self.assertEqual((x + 0.5) + (y + 0.5), Nx + Ny)
                self.assertEqual((x + 0.5) - (y + 0.5), Nx - Ny)
                self.assertEqual((x + 0.5) * (y + 0.5), Nx * Ny)
                self.assertEqual((x + 0.5) / (y + 0.5), Nx / Ny)
                self.assertEqual((x + 0.5) % (y + 0.5), Nx % Ny)
                self.assertEqual((x + 0.5) ** (y + 0.5), Nx**Ny)

                Nx = Foundation.NSNumber.numberWithLongLong_(x)
                Ny = Foundation.NSNumber.numberWithLongLong_(y)

                self.assertEqual((x) + (y), Nx + Ny)
                self.assertEqual((x) - (y), Nx - Ny)
                self.assertEqual((x) * (y), Nx * Ny)
                self.assertEqual((x) / (y), Nx / Ny)
                self.assertEqual((x) % (y), Nx % Ny)
                self.assertEqual((x) ** (y), Nx**Ny)

    def testTyping(self):
        # Thanks to some tricks and a cooperating Python runtime,
        # Foundation.NSNumber "instances" seem to be subclasses of both Foundation.NSNumber and
        # the corresponding Python number type.
        #

        n = Foundation.NSNumber.numberWithInt_(10)
        self.assertIsInstance(n, int)
        self.assertIsInstance(n, Foundation.NSNumber)

        n = Foundation.NSNumber.numberWithUnsignedInt_(10)
        self.assertIsInstance(n, int)
        self.assertIsInstance(n, Foundation.NSNumber)

        n = Foundation.NSNumber.numberWithLong_(10)
        self.assertIsInstance(n, int)
        self.assertIsInstance(n, Foundation.NSNumber)

        n = Foundation.NSNumber.numberWithUnsignedLong_(10)
        self.assertIsInstance(n, int)
        self.assertIsInstance(n, Foundation.NSNumber)

        n = Foundation.NSNumber.numberWithLongLong_(2**32 * 1024)
        self.assertEqual(n, 2**32 * 1024)
        self.assertIsInstance(n, int)
        self.assertIsInstance(n, Foundation.NSNumber)

        n = Foundation.NSNumber.numberWithUnsignedLongLong_(2**32 + 100)
        self.assertEqual(n, 2**32 + 100)
        self.assertIsInstance(n, int)
        self.assertIsInstance(n, Foundation.NSNumber)

        n = Foundation.NSNumber.numberWithFloat_(10)
        self.assertIsInstance(n, float)
        self.assertIsInstance(n, Foundation.NSNumber)

        n = Foundation.NSNumber.numberWithDouble_(10)
        self.assertIsInstance(n, float)
        self.assertIsInstance(n, Foundation.NSNumber)


if objc.platform == "MACOSX":

    class TestPropList(TestCase):
        # Test if numbers are stored properly in property-list. The most
        # important part of the testcase are boolean values.
        #
        # NOTE: GNUstep uses the old NeXT property lists, and these tests
        # will fail.

        def testPropertyList1(self):
            d = Foundation.NSMutableDictionary.dictionary()

            # Python 2.3 only...
            d["plain"] = 1
            d["bool"] = objc.YES

            self.assertEqual(d.writeToFile_atomically_("/tmp/pyobjctest.plist", 0), 1)

            fd = open("/tmp/pyobjctest.plist", "rb")
            data = fd.read().decode("utf8")
            fd.close()

            self.assertEqual(stripDocType(data), stripDocType(PLIST))

        def testPropertyList2(self):
            d = Foundation.NSMutableDictionary.dictionary()

            d["plain"] = Foundation.NSNumber.numberWithLong_(1)
            d["bool"] = Foundation.NSNumber.numberWithBool_(1)

            self.assertEqual(d.writeToFile_atomically_("/tmp/pyobjctest.plist", 0), 1)

            fd = open("/tmp/pyobjctest.plist", "rb")
            data = fd.read().decode("utf8")
            fd.close()

            self.assertEqual(stripDocType(data), stripDocType(PLIST))


class TestDecimalNumber(TestCase):
    def testProxy(self):
        one = Foundation.NSDecimalNumber.decimalNumberWithString_("1.00")
        self.assertIsInstance(one, Foundation.NSDecimalNumber)

        two = Foundation.NSDecimalNumber.decimalNumberWithString_("2.00")
        self.assertIsInstance(two, Foundation.NSDecimalNumber)

        three = Foundation.NSDecimalNumber.decimalNumberWithString_("3.00")
        self.assertIsInstance(three, Foundation.NSDecimalNumber)

        six = Foundation.NSDecimalNumber.decimalNumberWithString_("6.00")
        self.assertIsInstance(six, Foundation.NSDecimalNumber)

        one_half = Foundation.NSDecimalNumber.decimalNumberWithString_("0.50")
        self.assertIsInstance(one_half, Foundation.NSDecimalNumber)

        self.assertEqual(one + two, three)
        self.assertEqual(three - one, two)
        self.assertEqual(three * two, six)
        self.assertEqual(one / two, one_half)
        self.assertEqual(three // two, one)

        if sys.version_info[0] > 2:
            self.assertEqual(round(three / two), two)
            self.assertEqual(round(one / two, 1), one_half)
