from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKSystemSharingUIObserver(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBlock(
            CloudKit.CKSystemSharingUIObserver.systemSharingUIDidSaveShareBlock, b"v@@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKSystemSharingUIObserver.setSystemSharingUIDidSaveShareBlock_,
            0,
            b"v@@@",
        )

        self.assertResultIsBlock(
            CloudKit.CKSystemSharingUIObserver.systemSharingUIDidStopSharingBlock,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKSystemSharingUIObserver.setSystemSharingUIDidStopSharingBlock_,
            0,
            b"v@@",
        )
