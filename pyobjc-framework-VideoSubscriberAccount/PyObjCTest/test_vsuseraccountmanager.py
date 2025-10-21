from PyObjCTools.TestSupport import TestCase, min_os_level
import VideoSubscriberAccount


class TestVSUserAccountManager(TestCase):
    def test_constants(self):
        self.assertIsEnumType(VideoSubscriberAccount.VSUserAccountQueryOptions)
        self.assertEqual(VideoSubscriberAccount.VSUserAccountQueryNone, 0)
        self.assertEqual(VideoSubscriberAccount.VSUserAccountQueryAllDevices, 1)

    @min_os_level("13.3")
    def test_methods13_3(self):
        self.assertArgIsBlock(
            VideoSubscriberAccount.VSUserAccountManager.updateUserAccount_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            VideoSubscriberAccount.VSUserAccountManager.queryUserAccountsWithOptions_completion_,
            1,
            b"v@@",
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertArgIsBlock(
            VideoSubscriberAccount.VSUserAccountManager.queryAutoSignInTokenWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            VideoSubscriberAccount.VSUserAccountManager.deleteAutoSignInTokenWithCompletionHandler_,
            0,
            b"v@",
        )
