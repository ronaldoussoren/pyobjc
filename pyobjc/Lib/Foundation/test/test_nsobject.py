import unittest
import objc

from Foundation import *

class TestNSObjectInteraction( unittest.TestCase ):
    def testNSObjectClass( self ):
        self.assert_( NSObject.instancesRespondToSelector_( "description" ), "NSObject class claims it doesn't respond to a selector that it does." )
        # self.assert_( NSObject.description(), "NSObject class failed to respond to +description selector." )

    def testNSObjectInstance( self ):
        instance = NSObject.new()

        self.assert_( instance, "Failed to instantiate an instance" )
        self.assert_( instance.description(), "NSObject instance didn't respond to -description selector." )
        self.assert_( not instance.isProxy(), "Instance of NSObject claimed it was a proxy.   That seems odd." )
        self.assert_( isinstance( instance, objc.runtime.NSObject ), "Instantiated object not an instance of NSObject." )
        self.assert_( instance == instance, "Python identity check failed." )
        self.assert_( instance.isEqual_( instance ), "Obj-C identity check failed." )

class TestNSArrayInteraction( unittest.TestCase ):
    def testNSArrayAllocation( self ):
        for i in range(1,1000):
            a = NSArray.array()
            b = NSArray.alloc().init()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestNSObjectInteraction ) )
    suite.addTest( unittest.makeSuite( TestNSArrayInteraction ) )
    return suite

if __name__ == '__main__':
    unittest.main( )

