from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKUserIdentity(TestCase):
    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertResultIsBOOL(CloudKit.CKUserIdentity.hasiCloudAccount)
