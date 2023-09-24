from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKSyncEngineRecordZoneChangeBatch(TestCase):
    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(CloudKit.CKSyncEngineRecordZoneChangeBatch.atomicByZone)
        self.assertArgIsBOOL(
            CloudKit.CKSyncEngineRecordZoneChangeBatch.setAtomicByZone_, 0
        )
