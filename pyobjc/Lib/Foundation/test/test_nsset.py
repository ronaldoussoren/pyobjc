import unittest
import objc

from Foundation import *

class TestNSSetInteraction( unittest.TestCase ):
    def testRepeatedAllocInit( self ):
        for i in range(1,1000):
            a = NSSet.alloc().init()

    def testContains( self ):
        x = NSSet.setWithArray_( ["foo", "bar", "baz"] )

        self.assert_( "foo" in x )
        self.assert_( "notfoo" not in x )

    def testIteration( self ):
        x = NSSet.setWithArray_( ["foo", "bar", "baz"] )

        for i in x:
            self.assert_( i in x )
            self.assert_( x.containsObject_( i ) )

def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestNSSetInteraction ) )
    return suite

if __name__ == '__main__':
    unittest.main( )
