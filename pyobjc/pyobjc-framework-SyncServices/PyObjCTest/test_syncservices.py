'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import SyncServices

class TestSyncServices (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(SyncServices, 'ISyncClient') )
        self.assert_( isinstance(SyncServices.ISyncClient, objc.objc_class) )

    def testValues(self):
        self.assert_( hasattr(SyncServices, 'ISyncChangeTypeModify') )
        self.assert_( isinstance(SyncServices.ISyncChangeTypeModify, (int, long)) )
        self.assertEquals(SyncServices.ISyncChangeTypeModify, 2)

    def testVariables(self):
        self.assert_( hasattr(SyncServices, 'ISyncChangePropertyNameKey') )
        self.assert_( isinstance(SyncServices.ISyncChangePropertyNameKey, unicode) )

        self.assert_( hasattr(SyncServices, 'ISyncErrorDomain') )
        self.assert_( isinstance(SyncServices.ISyncErrorDomain, unicode) )

    def testProtocols(self):
        self.assert_( hasattr(SyncServices, 'protocols') )

        self.assert_( hasattr(SyncServices.protocols, 'ISyncSessionDriverDataSourceOptionalMethods') )
        self.assert_( isinstance(SyncServices.protocols.ISyncSessionDriverDataSourceOptionalMethods, objc.informal_protocol) )



if __name__ == "__main__":
    unittest.main()

