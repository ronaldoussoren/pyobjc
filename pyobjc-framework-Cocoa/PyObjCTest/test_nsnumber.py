from PyObjCTools.TestSupport import *
import objc
import re
import sys
import operator
import os

try:
    long
except NameError:
    long = int


from Foundation import *

PLIST=b"""\
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
""".decode('latin1')

def stripDocType(val):
    """
    Strip non-significant information. This is needed because the proplists
    on MacOS X 10.1 are slightly different from the ones on MacOS X 10.2 (
    different DOCTYPE and version).
    """
    r =  re.sub(b'<!DOCTYPE [^>]*>'.decode('ascii'), b'<!DOCTYPE>'.decode('ascii'), val)
    return r.replace(b'version="0.9"'.decode('ascii'), b'version="1.0"'.decode('ascii'))


class TestNSNumber( TestCase ):
    def testSimple(self):
        self.assertEqual(NSNumber.numberWithFloat_(1.0), 1,0)
        self.assertEqual(NSNumber.numberWithInt_(1), 1)
        self.assertEqual(NSNumber.numberWithFloat_(-0.5), -0.5)
        self.assertEqual(NSNumber.numberWithInt_(-4), -4)
        self.assertEqual(NSNumber.numberWithInt_(0), 0)
        self.assertEqual(NSNumber.numberWithFloat_(0.0), 0.0)

    def testReadOnly(self):
        n = NSNumber.numberWithFloat_(1.2)
        self.assertRaises(AttributeError, setattr, n, 'foo', 2)

        n = NSNumber.numberWithInt_(1)
        self.assertRaises(AttributeError, setattr, n, 'foo', 2)

        n = NSNumber.numberWithLongLong_(2**32 + 2)
        self.assertRaises(AttributeError, setattr, n, 'foo', 2)

    def testUseAsBasicType(self):
        lstValue = list(range(0, 20, 2))
        for idx, v in enumerate(lstValue):
            self.assertEqual(v, lstValue[NSNumber.numberWithInt_(idx)])
            self.assertEqual(v, lstValue[NSNumber.numberWithLong_(idx)])
            self.assertEqual(v, lstValue[NSNumber.numberWithLongLong_(idx)])

        self.assertRaises(TypeError, operator.getitem, lstValue,
                NSNumber.numberWithFloat_(2.0))

    def testUnsignedIssues(self):
        # NSNumber stores unsigned numbers as signed numbers
        # This is a bug in Cocoa... (RADAR #4007594), fixed in 10.5
        if sdkForPython() is not None and sdkForPython() < (10, 5):
            self.assertEqual(NSNumber.numberWithUnsignedInt_(2**31),
                -(2**31))
        else:
            self.assertEqual(NSNumber.numberWithUnsignedInt_(2**31),
                (2**31))

    def testMethods(self):
        v = NSNumber.numberWithUnsignedInt_(2**31)

        self.assertEqual(v.unsignedIntValue(), 2**31)
        self.assertEqual(v.intValue(), -(2**31))

        v = NSNumber.numberWithInt_(10)
        self.assertEqual(v.doubleValue(), float(10))

    def testMath(self):
        Xs = list(range(10, 40, 3))
        Ys = list(range(-12, 44, 5))

        self.assertTrue(0 not in Ys)
        self.assertTrue(0 not in Xs)

        for x in Xs:
            for y in Ys:
                Nx = NSNumber.numberWithInt_(x)
                Ny = NSNumber.numberWithInt_(y)

                self.assertEqual(x + y, Nx + Ny)
                self.assertEqual(x - y, Nx - Ny)
                self.assertEqual(x * y, Nx * Ny)
                self.assertEqual(x / y, Nx / Ny)
                self.assertEqual(x % y, Nx % Ny)
                self.assertEqual(x ** y, Nx ** Ny)

                Nx = NSNumber.numberWithFloat_(x+0.5)
                Ny = NSNumber.numberWithFloat_(y+0.5)

                self.assertEqual((x+0.5) + (y+0.5), Nx + Ny)
                self.assertEqual((x+0.5) - (y+0.5), Nx - Ny)
                self.assertEqual((x+0.5) * (y+0.5), Nx * Ny)
                self.assertEqual((x+0.5) / (y+0.5), Nx / Ny)
                self.assertEqual((x+0.5) % (y+0.5), Nx % Ny)
                self.assertEqual((x+0.5) ** (y+0.5), Nx ** Ny)

                Nx = NSNumber.numberWithLongLong_(x)
                Ny = NSNumber.numberWithLongLong_(y)

                self.assertEqual(long(x) + long(y), Nx + Ny)
                self.assertEqual(long(x) - long(y), Nx - Ny)
                self.assertEqual(long(x) * long(y), Nx * Ny)
                self.assertEqual(long(x) / long(y), Nx / Ny)
                self.assertEqual(long(x) % long(y), Nx % Ny)
                self.assertEqual(long(x) ** long(y), Nx ** Ny)


    def testTyping(self):
        # Thanks to some tricks and a cooperating Python runtime,
        # NSNumber "instances" seem to be subclasses of both NSNumber and
        # the corresponding Python number type.
        #

        n = NSNumber.numberWithInt_(10)
        self.assertIsInstance(n, (int, long))
        self.assertIsInstance(n, NSNumber)

        n = NSNumber.numberWithUnsignedInt_(10)
        self.assertIsInstance(n, (int, long))
        self.assertIsInstance(n, NSNumber)

        n = NSNumber.numberWithLong_(10)
        self.assertIsInstance(n, (int, long))
        self.assertIsInstance(n, NSNumber)

        n = NSNumber.numberWithUnsignedLong_(10)
        self.assertIsInstance(n, (int, long))
        self.assertIsInstance(n, NSNumber)

        n = NSNumber.numberWithLongLong_(2**32 * 1024)
        self.assertEqual(n, 2**32 * 1024)
        self.assertIsInstance(n, (int, long))
        self.assertIsInstance(n, NSNumber)

        n = NSNumber.numberWithUnsignedLongLong_(2**32 + 100)
        self.assertEqual(n, 2**32 + 100)
        self.assertIsInstance(n, (int, long))
        self.assertIsInstance(n, NSNumber)

        n = NSNumber.numberWithFloat_(10)
        self.assertIsInstance(n, float)
        self.assertIsInstance(n, NSNumber)

        n = NSNumber.numberWithDouble_(10)
        self.assertIsInstance(n, float)
        self.assertIsInstance(n, NSNumber)


if objc.platform == 'MACOSX':
    class TestPropList (TestCase):
        #Test if numbers are stored properly in property-list. The most
        #important part of the testcase are boolean values.
        #
        # NOTE: GNUstep uses the old NeXT property lists, and these tests
        # will fail.

        def testPropertyList1(self):
            d = NSMutableDictionary.dictionary()

            # Python 2.3 only...
            d[b'plain'.decode('ascii')] = 1
            d[b'bool'.decode('ascii')] = objc.YES

            self.assertEqual(d.writeToFile_atomically_(
                b"/tmp/pyobjctest.plist".decode('ascii'), 0), 1)

            fd = open(b'/tmp/pyobjctest.plist'.decode('ascii'), 'rb')
            data = fd.read().decode('utf8')
            fd.close()

            self.assertEqual(stripDocType(data), stripDocType(PLIST))

        def testPropertyList2(self):
            d = NSMutableDictionary.dictionary()

            d[b'plain'.decode('ascii')] = NSNumber.numberWithLong_(1)
            d[b'bool'.decode('ascii')] = NSNumber.numberWithBool_(1)

            self.assertEqual(d.writeToFile_atomically_(
                b"/tmp/pyobjctest.plist".decode('ascii'), 0), 1)

            fd = open(b'/tmp/pyobjctest.plist'.decode('ascii'), 'rb')
            data = fd.read().decode('utf8')
            fd.close()

            self.assertEqual(stripDocType(data), stripDocType(PLIST))

class TestDecimalNumber (TestCase):
    def testProxy (self):
        one = NSDecimalNumber.decimalNumberWithString_(b"1.00".decode('ascii'))
        self.assertIsInstance(one, NSDecimalNumber)

        two = NSDecimalNumber.decimalNumberWithString_(b"2.00".decode('ascii'))
        self.assertIsInstance(two, NSDecimalNumber)

        three = NSDecimalNumber.decimalNumberWithString_(b"3.00".decode('ascii'))
        self.assertIsInstance(three, NSDecimalNumber)

        six = NSDecimalNumber.decimalNumberWithString_(b"6.00".decode('ascii'))
        self.assertIsInstance(six, NSDecimalNumber)

        one_half = NSDecimalNumber.decimalNumberWithString_(b"0.50".decode('ascii'))
        self.assertIsInstance(one_half, NSDecimalNumber)


        self.assertEqual(one + two, three)
        self.assertEqual(three - one, two)
        self.assertEqual(three * two, six)
        self.assertEqual(one / two, one_half)
        self.assertEqual(three // two, one)

        if sys.version_info[0] > 2:
            self.assertEqual(round(three / two), one)
            self.assertEqual(round(one / two, 1), one_half)



if __name__ == '__main__':
    main( )
