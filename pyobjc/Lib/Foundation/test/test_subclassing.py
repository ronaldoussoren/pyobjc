import unittest
import objc

from Foundation import *

class TestSubclassing( unittest.TestCase ):
    def testBasicSubclassing( self ):
        class NSObjectSubclass( NSObject ):
            def someRandomMethod(self):
                return 42

        subclassClass = NSClassFromString( "NSObjectSubclass" )

        self.assert_( subclassClass , "Failed to subclass NSObject." )

        subclassInstance = subclassClass.new()
        self.assert_( isinstance( subclassInstance, subclassClass ), "Subclass instance was not an instance of NSObjectSubclass." )
        self.assert_( isinstance( subclassInstance, NSObject ), "Subclass instance was not a subclass of NSObject." )
        self.assert_( not isinstance( subclassInstance, NSArray ), "Not a subclass of NSArray, but instanceof() thinks so." )

        subclassInstance.description()
        self.assert_( subclassInstance.someRandomMethod() == 42, "someRandomMethod() did not return expected response." )

        self.assert_( subclassInstance is subclassInstance, "Identity check failed." )
        self.assert_( subclassInstance is subclassInstance.self(), "Identity check failed." )
    

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
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestNSObjectInteraction ) )
    suite.addTest( unittest.makeSuite( TestSubclassing ) )
    return suite

if __name__ == '__main__':
    unittest.main( )
