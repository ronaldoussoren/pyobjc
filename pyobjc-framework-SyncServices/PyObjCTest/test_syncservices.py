"""
Some simple tests to check that the framework is properly wrapped.
"""

import objc
import SyncServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSyncServices(TestCase):
    def testClasses(self):
        self.assertHasAttr(SyncServices, "ISyncClient")
        self.assertIsInstance(SyncServices.ISyncClient, objc.objc_class)

    def testProtocols(self):
        self.assertProtocolExists("ISyncFiltering")

    @min_os_level("10.6")
    def testProtocols10_5(self):
        # Document for 10.5, but not actually present there
        self.assertProtocolExists("ISyncSessionDriverDataSource")
        self.assertProtocolExists("NSPersistentStoreCoordinatorSyncing")


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(SyncServices)
