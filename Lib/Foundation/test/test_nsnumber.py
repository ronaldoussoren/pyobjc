import unittest
import objc

from Foundation import *

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

def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestNSNumber ) )
    return suite

if __name__ == '__main__':
    unittest.main( )
