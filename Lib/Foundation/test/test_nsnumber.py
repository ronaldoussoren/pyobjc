import unittest
import objc
import re
import sys

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


# NSNumber instances are converted to Python numbers

class TestNSNumber( unittest.TestCase ):
    def testSimple(self):
        self.assertEquals(NSNumber.numberWithFloat_(1.0), 1,0)
        self.assertEquals(NSNumber.numberWithInt_(1), 1)
        self.assertEquals(NSNumber.numberWithFloat_(-0.5), -0.5)
        self.assertEquals(NSNumber.numberWithInt_(-4), -4)
        self.assertEquals(NSNumber.numberWithInt_(0), 0)
        self.assertEquals(NSNumber.numberWithFloat_(0.0), 0,0)

    def testUseAsBasicType(self):
        lstValue = list(range(0, 20, 2))
        for idx, v in enumerate(lstValue):
            self.assertEquals(v, lstValue[NSNumber.numberWithInt_(idx)])

    def testUnsignedIssues(self):
        # NSNumber stores unsigned numbers as signed numbers
        # This is a bug in Cocoa...

        self.assertEquals(NSNumber.numberWithUnsignedInt_(sys.maxint+1),
                    -sys.maxint-1)

    def testMethods(self):
        v = NSNumber.numberWithUnsignedInt_(sys.maxint+1)

        self.assertEquals(v.unsignedIntValue(), sys.maxint+1)
        self.assertEquals(v.intValue(), -sys.maxint-1)

        v = NSNumber.numberWithInt_(10)
        self.assertEquals(v.doubleValue(), float(10))

if objc.platform == 'MACOSX':
    class TestPropList (unittest.TestCase):
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

if isinstance(NSDecimalNumber.decimalNumberWithString_(u'1.00'), NSDecimalNumber):
    class TestDecimalNumber (unittest.TestCase):
        # NSDecimalNumber is treated specially

        # TODO: Add tests for using decimal numbers (addition, multiplication, ...)

        def testProxy (self):
            o = NSDecimalNumber.decimalNumberWithString_(u"1.00")
            self.assert_(isinstance(o, NSDecimalNumber))

else:
    class TestDecimalNumber (unittest.TestCase):
        # NSDecimalNumber is treated specially

        # TODO: Add tests for using decimal numbers (addition, multiplication, ...)

        def testProxy (self):
            o = NSDecimalNumber.decimalNumberWithString_(u"1.00")
            self.assert_(isinstance(o, NSDecimal))

if __name__ == '__main__':
    unittest.main( )
