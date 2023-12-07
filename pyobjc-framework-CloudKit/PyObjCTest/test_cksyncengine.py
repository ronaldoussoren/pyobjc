from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import CloudKit


class TestCKSyncEngine(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CloudKit.CKSyncEngineSyncReason)
        self.assertEqual(CloudKit.CKSyncEngineSyncReasonScheduled, 0)
        self.assertEqual(CloudKit.CKSyncEngineSyncReasonManual, 1)

    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists("CKSyncEngineDelegate")

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBlock(
            CloudKit.CKSyncEngine.fetchChangesWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            CloudKit.CKSyncEngine.fetchChangesWithOptions_completionHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            CloudKit.CKSyncEngine.sendChangesWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            CloudKit.CKSyncEngine.sendChangesWithOptions_completionHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            CloudKit.CKSyncEngine.cancelOperationsWithCompletionHandler_, 0, b"v"
        )

    @min_os_level("14.2")
    def test_methods14_2(self):
        self.assertResultIsBOOL(CloudKit.CKSyncEngineFetchChangesScope.containsZoneID_)
