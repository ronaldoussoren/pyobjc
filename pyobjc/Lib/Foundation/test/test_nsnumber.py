import unittest
import objc

from Foundation import *

if 0:
    # NSNumber is proxied into python

    class TestNSNumber( unittest.TestCase ):
        def testNSNumber( self ):
            x = NSMutableArray.arrayWithArray_( range(1, 10) )
            y = range( 1, 10 )

            self.assert_( isinstance( x[4], NSNumber ) )
            self.assertEquals( x[3], y[3] )
            self.assertEquals( x[3] + x[5], y[3] + y[5] )
            self.assertEquals( x[2] + y[3], y[2] + x[3] )
            self.assertEquals( x[8] * x[7], y[7] * y[8] )
            self.assertEquals( y[8] * x[7], x[7] * y[8] )

        def testAsBool(self):
            trues = (
                NSNumber.numberWithFloat_(1.0),
                NSNumber.numberWithInt_(1),
                NSNumber.numberWithFloat_(-0.01),
                NSNumber.numberWithInt_(-4),
            )
            falses = (
                NSNumber.numberWithFloat_(0.0),
                NSNumber.numberWithInt_(0),
            )

            for a in trues:
                if a:
                    pass
                else:
                    raise AssertionError, "%s is not true"%(a.description())

            for a in falses:
                if a:
                    raise AssertionError, "%s is true"%(a.description())

        def testStr(self):
            x = NSNumber.numberWithInt_(4)
            self.assertEquals(4, int(str(x)))

else:
    # NSNumber instances are converted to Python numbers

    class TestNSNumber( unittest.TestCase ):
        def testNSNumber( self ):
                self.assertEquals(NSNumber.numberWithFloat_(1.0), 1,0)
                self.assertEquals(NSNumber.numberWithInt_(1), 1)
                self.assertEquals(NSNumber.numberWithFloat_(-0.5), -0.5)
                self.assertEquals(NSNumber.numberWithInt_(-4), -4)
                self.assertEquals(NSNumber.numberWithInt_(0), 0)
                self.assertEquals(NSNumber.numberWithFloat_(0.0), 0,0)
            
    PLIST="""\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>bool</key>
	<true/>
	<key>plain</key>
	<integer>1</integer>
</dict>
</plist>
"""

    class TestPropList (unittest.TestCase):
        """
        Test if numbers are stored properly in property-list. The most 
        important part of the testcase are boolean values.
        """

        def testPropertyList1(self):
            d = NSMutableDictionary.dictionary()

            # Python 2.3 only...
            d['plain'] = 1
            d['bool'] = objc.YES

            self.assertEquals(d.writeToFile_atomically_(
                "/tmp/pyobjctest.plist", 0), 1)
            
            fd = open('/tmp/pyobjctest.plist', 'ru')
            data = fd.read()
            fd.close()

            self.assertEquals(data, PLIST)

        def testPropertyList1(self):
            d = NSMutableDictionary.dictionary()

            d['plain'] = NSNumber.numberWithLong_(1)
            d['bool'] = NSNumber.numberWithBool_(1)

            self.assertEquals(d.writeToFile_atomically_(
                "/tmp/pyobjctest.plist", 0), 1)
            
            fd = open('/tmp/pyobjctest.plist', 'ru')
            data = fd.read()
            fd.close()

            self.assertEquals(data, PLIST)

def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestNSNumber ) )
    return suite

if __name__ == '__main__':
    unittest.main( )
