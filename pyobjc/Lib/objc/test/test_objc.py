import unittest

import objc

class TestBOOL(unittest.TestCase):
    def testBooleans(self):
        self.assert_( objc.YES, "YES was not true." )
        self.assert_( not objc.NO, "NO was true." )
    
class TestClassLookup(unittest.TestCase):
    def testLookupClassNoSuchClassErrorRaised(self):
        self.assertRaises( objc.nosuchclass_error, objc.lookup_class, "" )
        self.assertRaises( objc.nosuchclass_error, objc.lookup_class, "ThisClassReallyShouldNotExist" )
        self.assertRaises( TypeError, objc.lookup_class, 1 )

    def testRuntimeNoSuchClassErrorRaised(self):
        try:
            objc.runtime.ThisClassReallyShouldNotExist
        except objc.nosuchclass_error:
            pass
        else:
            fail("objc.runtime.ThisClassReallyShouldNotExist should have thrown a nosuchclass_error.  It didn't.")

    def testRuntimeConsistency(self):
        self.assert_( objc.lookup_class("NSObject"), "Failed to find NSObject class." )
        self.assertEqual( objc.lookup_class( "NSObject" ), objc.runtime.NSObject,
                          "objc.runtime.NSObject and objc.lookup_class('NSObject') were different." )

    def testClassList(self):
        ###! This test should probably be moved down to the Foundation test suite... 
        self.assert_( objc.runtime.NSObject in objc.class_list(), "class_list() does not appear to contain NSObject class" )
        self.assert_( objc.runtime.NSException in objc.class_list(), "class_list() does not appear to contain NSException class" )
        self.assert_( objc.runtime.NSMutableArray in objc.class_list(), "class_list() does not appear to contain NSMutableArray class" )

class TestObjectInstantiation(unittest.TestCase):
    def testInstantiation(self):
        anInstance = objc.runtime.NSObject.new()
        self.assert_( anInstance, "Failed to instantiate an instance" )
        self.assert_( isinstance( anInstance, objc.runtime.NSObject ), "Instantiated object not an instance of NSObject." )
        self.assert_( anInstance.isEqual_( anInstance ), "Instance !isEqual: to itself." )

class TestMethodInvocation(unittest.TestCase):
    def setUp(self):
        self.NSObjectInstance = objc.runtime.NSObject.alloc()

    def testClassInvocation(self):
        self.assert_( objc.runtime.NSObject.description(), "Failed to invoke the +description method." )

    def testInstanceInvocation(self):
        self.assert_( self.NSObjectInstance.description(), "Failed to invoke the -description method." )
        self.assertEqual( self.NSObjectInstance.self(), self.NSObjectInstance, "-self did not return same self." )
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestBOOL ) )
    suite.addTest( unittest.makeSuite( TestClassLookup ) )
    suite.addTest( unittest.makeSuite( TestObjectInstantiation ) )
    suite.addTest( unittest.makeSuite( TestMethodInvocation ) )
    return suite

if __name__ == '__main__':
    unittest.main( )
