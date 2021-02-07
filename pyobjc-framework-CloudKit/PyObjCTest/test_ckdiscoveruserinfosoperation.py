from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKDiscoverUserInfosOperation(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKDiscoverUserInfosOperation")
        self.assertIsInstance(CloudKit.CKDiscoverUserInfosOperation, objc.objc_class)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            CloudKit.CKDiscoverUserInfosOperation.setDiscoverUserInfosCompletionBlock_,
            0,
            b"v@@@",
        )
        self.assertResultIsBlock(
            CloudKit.CKDiscoverUserInfosOperation.discoverUserInfosCompletionBlock,
            b"v@@@",
        )
