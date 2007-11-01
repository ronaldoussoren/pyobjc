'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import InstantMessage

class TestInstantMessage (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(InstantMessage, 'IMAVManager') )
        self.assert_( isinstance(InstantMessage.IMAVManager, objc.objc_class) )

    def testValues(self):
        self.assert_( hasattr(InstantMessage, 'IMAVShuttingDown') )
        self.assert_( isinstance(InstantMessage.IMAVShuttingDown, (int, long)) )
        self.assertEquals(InstantMessage.IMAVShuttingDown, 2)

        self.assert_( hasattr(InstantMessage, 'IMVideoOptimizationReplacement') )
        self.assert_( isinstance(InstantMessage.IMVideoOptimizationReplacement, (int, long)) )
        self.assertEquals(InstantMessage.IMVideoOptimizationReplacement, 2)


    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        self.assert_( hasattr(InstantMessage, 'IMAVManagerStateChangedNotification') )
        self.assert_( isinstance(InstantMessage.IMAVManagerStateChangedNotification, unicode) )
        self.assert_( hasattr(InstantMessage, 'IMPersonInfoChangedNotification') )
        self.assert_( isinstance(InstantMessage.IMPersonInfoChangedNotification, unicode) )


    def test_protocols(self):
        self.assert_( hasattr(InstantMessage, 'protocols') )
        self.assert_( hasattr(InstantMessage.protocols, 'IMVideoDataSource') )
        self.assert_( isinstance(InstantMessage.protocols.IMVideoDataSource, objc.informal_protocol) )

if __name__ == "__main__":
    unittest.main()

