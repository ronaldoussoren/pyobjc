import unittest

import objc

class Test_lookup_class(unittest.TestCase):
    def testNoSuchClassErrorRaised(self):
        self.assertRaises( objc.nosuchclass_error, objc.lookup_class, "" )
        self.assertRaises( objc.nosuchclass_error, objc.lookup_class, "ThisClassReallyShouldNotExist" )
        self.assertRaises( TypeError, objc.lookup_class, 1 )

    def testNSObject(self):
        self.assert_( objc.lookup_class("NSObject"), "Failed to find NSObject class." )
        self.assertEqual( objc.lookup_class( "NSObject" ), objc.runtime.NSObject,
                          "objc.runtime.NSObject and objc.lookup_class('NSObject') were different." )

class Test_runtime(unittest.TestCase):
    def testNoSuchClassErrorRaised(self):
        try:
            objc.runtime.ThisClassReallyShouldNotExist
        except objc.nosuchclass_error:
            pass
        else:
            fail("objc.runtime.ThisClassReallyShouldNotExist should have thrown a nosuchclass_error.  It didn't.")

    def testNSObject(self):
        self.assert_( objc.runtime.NSObject, "Failed to find NSObject class." )
        self.assertEqual( objc.runtime.NSObject, objc.lookup_class( "NSObject" ),
                          "objc.runtime.NSObject and objc.lookup_class('NSObject') were different." )

class Test_Object_Instantiation(unittest.TestCase):
    def testInstantiation(self):
        anInstance = objc.runtime.NSObject.new()
        self.assert_( anInstance, "Failed to instantiate an instance" )
        self.assert_( isinstance( anInstance, objc.runtime.NSObject ), "Instantiated object not an instance of NSObject." )

class Test_method_invocation(unittest.TestCase):
    def setUp(self):
        self.NSObjectInstance = objc.runtime.NSObject.alloc()

    def testClassInvocation(self):
        self.assert_( objc.runtime.NSObject.description(), "Failed to invoke the +description method." )

    def testInstanceInvocation(self):
        self.assert_( self.NSObjectInstance.description(), "Failed to invoke the -description method." )
        self.assertEqual( self.NSObjectInstance.self(), self.NSObjectInstance, "-self did not return same self." )
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_lookup_class))
    suite.addTest(unittest.makeSuite(Test_runtime))
    suite.addTest(unittest.makeSuite(Test_Object_Instantiation))
    suite.addTest(unittest.makeSuite(Test_method_invocation))
    return suite

if __name__ == '__main__':
    unittest.main( )
