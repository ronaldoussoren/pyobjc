'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import Automator

class TestAutomator (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(Automator, 'AMAction') )
        self.assert_( isinstance(Automator.AMAction, objc.objc_class) )
        
        self.assert_( hasattr(Automator, 'AMAppleScriptAction') )
        self.assert_( isinstance(Automator.AMAppleScriptAction, objc.objc_class) )

    def testInformalProtocols(self):
        self.assert_(hasattr(Automator, 'protocols'))
        self.assert_(hasattr(Automator.protocols, 'AMWorkflowControllerDelegate'))
        self.assert_(isinstance(Automator.protocols.AMWorkflowControllerDelegate, objc.informal_protocol))

    def testValues(self):
        # Use this to test for a number of enum and #define values
        
        self.assert_( hasattr(Automator, 'AMActionErrorKey') )
        self.assert_( isinstance(Automator.AMActionErrorKey, (str, unicode)) )
        self.assertEquals(Automator.AMActionErrorKey, "AMActionErrorKey")

        self.assert_( hasattr(Automator, 'AMAutomatorErrorDomain') )
        self.assert_( isinstance(Automator.AMAutomatorErrorDomain, (str, unicode)) )
        self.assertEquals(Automator.AMAutomatorErrorDomain, "com.apple.Automator")
        
        self.assert_( hasattr(Automator, 'AMWorkflowNewerVersionError') )
        self.assert_( isinstance(Automator.AMWorkflowNewerVersionError, (int, long)) )
        self.assertEquals(Automator.AMWorkflowNewerVersionError, -100)


if __name__ == "__main__":
    unittest.main()

