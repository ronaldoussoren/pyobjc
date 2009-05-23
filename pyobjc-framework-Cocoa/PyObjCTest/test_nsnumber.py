from PyObjCTools.TestSupport import *
import objc
import re
import sys
import operator
import os

from Foundation import *

PLIST=u"""\
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
"""

def stripDocType(val):
    """
    Strip non-significant information. This is needed because the proplists
    on MacOS X 10.1 are slightly different from the ones on MacOS X 10.2 (
    different DOCTYPE and version).
    """
    r =  re.sub(u'<!DOCTYPE [^>]*>', u'<!DOCTYPE>', val)
    return r.replace(u'version="0.9"', u'version="1.0"')


class TestNSNumber( TestCase ):
    def testSimple(self):
        self.assertEquals(NSNumber.numberWithFloat_(1.0), 1,0)
        self.assertEquals(NSNumber.numberWithInt_(1), 1)
        self.assertEquals(NSNumber.numberWithFloat_(-0.5), -0.5)
        self.assertEquals(NSNumber.numberWithInt_(-4), -4)
        self.assertEquals(NSNumber.numberWithInt_(0), 0)
        self.assertEquals(NSNumber.numberWithFloat_(0.0), 0.0)

    def testReadOnly(self):
        n = NSNumber.numberWithFloat_(1.2)
        self.assertRaises(AttributeError, setattr, n, 'foo', 2)

        n = NSNumber.numberWithInt_(1)
        self.assertRaises(AttributeError, setattr, n, 'foo', 2)

        n = NSNumber.numberWithLongLong_(sys.maxint + 2)
        self.assertRaises(AttributeError, setattr, n, 'foo', 2)

    def testUseAsBasicType(self):
        lstValue = list(range(0, 20, 2))
        for idx, v in enumerate(lstValue):
            self.assertEquals(v, lstValue[NSNumber.numberWithInt_(idx)])
            self.assertEquals(v, lstValue[NSNumber.numberWithLong_(idx)])
            self.assertEquals(v, lstValue[NSNumber.numberWithLongLong_(idx)])

        self.assertRaises(TypeError, operator.getitem, lstValue,
                NSNumber.numberWithFloat_(2.0))

    def testUnsignedIssues(self):
        # NSNumber stores unsigned numbers as signed numbers
        # This is a bug in Cocoa... (RADAR #4007594), fixed in 10.5
        if sdkForPython() < (10, 5):
		self.assertEquals(NSNumber.numberWithUnsignedInt_(sys.maxint+1),
			    -sys.maxint-1)
	else:
		self.assertEquals(NSNumber.numberWithUnsignedInt_(sys.maxint+1),
			    sys.maxint+1)

    def testMethods(self):
        v = NSNumber.numberWithUnsignedInt_(sys.maxint+1)

        self.assertEquals(v.unsignedIntValue(), sys.maxint+1)
        self.assertEquals(v.intValue(), -sys.maxint-1)

        v = NSNumber.numberWithInt_(10)
        self.assertEquals(v.doubleValue(), float(10))

    def testMath(self):
        Xs = list(range(10, 40, 3))
        Ys = list(range(-12, 44, 5))

        self.assert_(0 not in Ys)
        self.assert_(0 not in Xs)

        for x in Xs:
            for y in Ys:
                Nx = NSNumber.numberWithInt_(x)
                Ny = NSNumber.numberWithInt_(y)

                self.assertEquals(x + y, Nx + Ny)
                self.assertEquals(x - y, Nx - Ny)
                self.assertEquals(x * y, Nx * Ny)
                self.assertEquals(x / y, Nx / Ny)
                self.assertEquals(x % y, Nx % Ny)
                self.assertEquals(x ** y, Nx ** Ny)

                Nx = NSNumber.numberWithFloat_(x+0.5)
                Ny = NSNumber.numberWithFloat_(y+0.5)

                self.assertEquals((x+0.5) + (y+0.5), Nx + Ny)
                self.assertEquals((x+0.5) - (y+0.5), Nx - Ny)
                self.assertEquals((x+0.5) * (y+0.5), Nx * Ny)
                self.assertEquals((x+0.5) / (y+0.5), Nx / Ny)
                self.assertEquals((x+0.5) % (y+0.5), Nx % Ny)
                self.assertEquals((x+0.5) ** (y+0.5), Nx ** Ny)

                Nx = NSNumber.numberWithLongLong_(x)
                Ny = NSNumber.numberWithLongLong_(y)

                self.assertEquals(long(x) + long(y), Nx + Ny)
                self.assertEquals(long(x) - long(y), Nx - Ny)
                self.assertEquals(long(x) * long(y), Nx * Ny)
                self.assertEquals(long(x) / long(y), Nx / Ny)
                self.assertEquals(long(x) % long(y), Nx % Ny)
                self.assertEquals(long(x) ** long(y), Nx ** Ny)


    def testTyping(self):
        # Thanks to some tricks and a cooperating Python runtime,
        # NSNumber "instances" seem to be subclasses of both NSNumber and
        # the corresponding Python number type.
        #

        n = NSNumber.numberWithInt_(10)
        self.assert_(isinstance(n, (int, long)))
        self.assert_(isinstance(n, NSNumber))

        n = NSNumber.numberWithUnsignedInt_(10)
        self.assert_(isinstance(n, (int, long)))
        self.assert_(isinstance(n, NSNumber))

        n = NSNumber.numberWithLong_(10)
        self.assert_(isinstance(n, (int, long)))
        self.assert_(isinstance(n, NSNumber))

        n = NSNumber.numberWithUnsignedLong_(10)
        self.assert_(isinstance(n, (int, long)))
        self.assert_(isinstance(n, NSNumber))

        n = NSNumber.numberWithLongLong_(sys.maxint * 1024L)
        self.assertEquals(n, sys.maxint * 1024L)
        self.assert_(isinstance(n, (int, long)))
        self.assert_(isinstance(n, NSNumber))

        n = NSNumber.numberWithUnsignedLongLong_(sys.maxint + 100)
        self.assertEquals(n, sys.maxint + 100)
        self.assert_(isinstance(n, (int, long)))
        self.assert_(isinstance(n, NSNumber))

        n = NSNumber.numberWithFloat_(10)
        self.assert_(isinstance(n, float))
        self.assert_(isinstance(n, NSNumber))

        n = NSNumber.numberWithDouble_(10)
        self.assert_(isinstance(n, float))
        self.assert_(isinstance(n, NSNumber))


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
            d[u'plain'] = 1
            d[u'bool'] = objc.YES

            self.assertEquals(d.writeToFile_atomically_(
                u"/tmp/pyobjctest.plist", 0), 1)

            fd = open(u'/tmp/pyobjctest.plist', 'ru')
            data = fd.read().decode('utf8')
            fd.close()

            self.assertEquals(stripDocType(data), stripDocType(PLIST))

        def testPropertyList2(self):
            d = NSMutableDictionary.dictionary()

            d[u'plain'] = NSNumber.numberWithLong_(1)
            d[u'bool'] = NSNumber.numberWithBool_(1)

            self.assertEquals(d.writeToFile_atomically_(
                u"/tmp/pyobjctest.plist", 0), 1)

            fd = open(u'/tmp/pyobjctest.plist', 'ru')
            data = fd.read().decode('utf8')
            fd.close()

            self.assertEquals(stripDocType(data), stripDocType(PLIST))

class TestDecimalNumber (TestCase):
    def testProxy (self):
        one = NSDecimalNumber.decimalNumberWithString_(u"1.00")
        self.assert_(isinstance(one, NSDecimalNumber))

        two = NSDecimalNumber.decimalNumberWithString_(u"2.00")
        self.assert_(isinstance(two, NSDecimalNumber))

        three = NSDecimalNumber.decimalNumberWithString_(u"3.00")
        self.assert_(isinstance(three, NSDecimalNumber))

        six = NSDecimalNumber.decimalNumberWithString_(u"6.00")
        self.assert_(isinstance(six, NSDecimalNumber))

        one_half = NSDecimalNumber.decimalNumberWithString_(u"0.50")
        self.assert_(isinstance(one_half, NSDecimalNumber))

        
        self.failUnlessEqual(one + two, three)
        self.failUnlessEqual(three - one, two)
        self.failUnlessEqual(three * two, six)
        self.failUnlessEqual(one / two, one_half)



if __name__ == '__main__':
    main( )
