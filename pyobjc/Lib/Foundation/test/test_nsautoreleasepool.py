import unittest
import objc

from Foundation import *

class TestNSAutoreleasePoolInteraction( unittest.TestCase ):
    def testNSAutoreleasePool( self ):
        pool = NSAutoreleasePool.alloc().init()
        bar = NSMutableArray.array()
        pool.release()
        bar.addObject( "a", "b", "c" )

def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestNSAutoreleasePoolInteraction ) )
    return suite

if __name__ == '__main__':
    unittest.main( )

