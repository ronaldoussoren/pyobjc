'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import SyncServices

class TestSyncServices (TestCase):
    def testClasses(self):
        self.assertHasAttr(SyncServices, 'ISyncClient')
        self.assertIsInstance(SyncServices.ISyncClient, objc.objc_class)

    def testProtocols(self):
        objc.protocolNamed('ISyncFiltering')

    @min_os_level('10.6')
    def testProtocols10_5(self):
        # Document for 10.5, but not actually present there
        objc.protocolNamed('ISyncSessionDriverDataSource')
        objc.protocolNamed('NSPersistentStoreCoordinatorSyncing')


if __name__ == "__main__":
    main()
