from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKDiscoverUserInfosOperation(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKDiscoveredUserInfo")
        self.assertIsInstance(CloudKit.CKDiscoveredUserInfo, objc.objc_class)

        self.assertResultIsBlock(
            CloudKit.CKDiscoverUserInfosOperation.discoverUserInfosCompletionBlock,
            b"v@@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKDiscoverUserInfosOperation.setDiscoverUserInfosCompletionBlock_,
            0,
            b"v@@@",
        )
