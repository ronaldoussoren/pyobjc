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

    def test_varargsConstruction(self):
        w = NSSet.setWithObjects_(0,1,2,3,None)
        x = NSSet.alloc().initWithObjects_(0,1,2,3,None)
        y = NSSet.setWithObjects_count_(range(10), 4)
        z = NSSet.alloc().initWithObjects_count_(range(10), 4)

        self.assert_(len(w) == 4)
        self.assert_(len(x) == 4)
        self.assert_(len(y) == 4)
        self.assert_(len(z) == 4)

        self.assert_(0 in w)
        self.assert_(1 in x)
        self.assert_(2 in y)
        self.assert_(3 in z)

    def test_varargsConstruction2(self):
        w = NSMutableSet.setWithObjects_(0,1,2,3,None)
        x = NSMutableSet.alloc().initWithObjects_(0,1,2,3,None)
        y = NSMutableSet.setWithObjects_count_(range(10), 4)
        z = NSMutableSet.alloc().initWithObjects_count_(range(10), 4)

        self.assert_(len(w) == 4)
        self.assert_(len(x) == 4)
        self.assert_(len(y) == 4)
        self.assert_(len(z) == 4)

        self.assert_(0 in w)
        self.assert_(1 in x)
        self.assert_(2 in y)
        self.assert_(3 in z)

def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestNSSetInteraction ) )
    return suite

if __name__ == '__main__':
    unittest.main( )
