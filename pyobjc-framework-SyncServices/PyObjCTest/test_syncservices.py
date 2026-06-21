"""
Some simple tests to check that the framework is properly wrapped.
"""

import objc
import SyncServices
from PyObjCTools.TestSupport import TestCase


class TestSyncServices(TestCase):
    def testClasses(self):
        self.assertHasAttr(SyncServices, "ISyncClient")
        self.assertIsInstance(SyncServices.ISyncClient, objc.objc_class)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(SyncServices)
