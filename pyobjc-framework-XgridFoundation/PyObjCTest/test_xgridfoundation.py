'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import XgridFoundation

class TestXgridFoundation (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(XgridFoundation, 'XGActionMonitorInternal') )
        self.assert_( isinstance(XgridFoundation.XGActionMonitorInternal, objc.objc_class) )

    def testValues(self):
        self.assert_( hasattr(XgridFoundation, 'XGResourceActionRestart') )
        self.assert_( isinstance(XgridFoundation.XGResourceActionRestart, (int, long)) )
        self.assertEquals(XgridFoundation.XGResourceActionRestart, 2)

        self.assert_( hasattr(XgridFoundation, 'XGResourceActionGetSpecification') )
        self.assert_( isinstance(XgridFoundation.XGResourceActionGetSpecification, (int, long)) )
        self.assertEquals(XgridFoundation.XGResourceActionGetSpecification, 11)

        self.assert_( hasattr(XgridFoundation, 'XGAuthenticatorStateFailed') )
        self.assert_( isinstance(XgridFoundation.XGAuthenticatorStateFailed, (int, long)) )
        self.assertEquals(XgridFoundation.XGAuthenticatorStateFailed, 3)

    def testVariables(self):
        self.assert_( hasattr(XgridFoundation, 'XGActionMonitorResultsOutputStreamsKey') )
        self.assert_( isinstance(XgridFoundation.XGActionMonitorResultsOutputStreamsKey, unicode) )

        self.assert_( hasattr(XgridFoundation, 'XGJobSpecificationIsExecutableKey') )
        self.assert_( isinstance(XgridFoundation.XGJobSpecificationIsExecutableKey, unicode) )

        self.assert_( hasattr(XgridFoundation, 'XGConnectionKeyIsClosed') )
        self.assert_( isinstance(XgridFoundation.XGConnectionKeyIsClosed, unicode) )

    def testProtocols(self):
        self.assert_( hasattr(XgridFoundation, 'protocols') )

        self.assert_( hasattr(XgridFoundation.protocols, 'XGAuthenticatorDelegate') )
        self.assert_( isinstance(XgridFoundation.protocols.XGAuthenticatorDelegate, objc.informal_protocol) )

        self.assert_( hasattr(XgridFoundation.protocols, 'XGFileDownloadDelegate') )
        self.assert_( isinstance(XgridFoundation.protocols.XGFileDownloadDelegate, objc.informal_protocol) )


if __name__ == "__main__":
    unittest.main()

