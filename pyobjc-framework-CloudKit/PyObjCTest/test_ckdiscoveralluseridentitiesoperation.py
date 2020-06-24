from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKDiscoverAllUserIdentitiesOperation(TestCase):
    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBlock(
            CloudKit.CKDiscoverAllUserIdentitiesOperation.setUserIdentityDiscoveredBlock_,
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKDiscoverAllUserIdentitiesOperation.userIdentityDiscoveredBlock,
            b"v@",
        )

        self.assertArgIsBlock(
            CloudKit.CKDiscoverAllUserIdentitiesOperation.setDiscoverAllUserIdentitiesCompletionBlock_,  # noqa: B950
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKDiscoverAllUserIdentitiesOperation.discoverAllUserIdentitiesCompletionBlock,  # noqa: B950
            b"v@",
        )
