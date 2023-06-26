from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKSyncEngineConfiguration(TestCase):
    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(CloudKit.CKSyncEngineConfiguration.automaticallySync)
        self.assertArgIsBOOL(
            CloudKit.CKSyncEngineConfiguration.setAutomaticallySync_, 0
        )
