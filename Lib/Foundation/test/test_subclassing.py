import unittest
import objc

from Foundation import *

class TestSubclassing(unittest.TestCase):
    def testBasicSubclassing(self):
        class NSObjectSubclass(NSObject):
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

if __name__ == '__main__':
    unittest.main( )
