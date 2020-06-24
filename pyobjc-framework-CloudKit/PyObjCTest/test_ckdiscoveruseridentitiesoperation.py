from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKDiscoverUserIdentitiesOperation(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBlock(
            CloudKit.CKDiscoverUserIdentitiesOperation.userIdentityDiscoveredBlock,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKDiscoverUserIdentitiesOperation.setUserIdentityDiscoveredBlock_,
            0,
            b"v@@",
        )

        self.assertResultIsBlock(
            CloudKit.CKDiscoverUserIdentitiesOperation.discoverUserIdentitiesCompletionBlock,  # noqa:  B950
            b"v@",
        )
        self.assertArgIsBlock(
            CloudKit.CKDiscoverUserIdentitiesOperation.setDiscoverUserIdentitiesCompletionBlock_,  # noqa: B950
            0,
            b"v@",
        )
