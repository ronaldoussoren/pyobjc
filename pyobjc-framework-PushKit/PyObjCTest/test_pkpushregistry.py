from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import PushKit


class TestPKPushRegistryHelper(PushKit.NSObject):
    def pushRegistry_didReceiveIncomingPushWithPayload_forType_withCompletionHandler_(
        self, a, b, c, d
    ):
        pass


class TestPKPushRegistry(TestCase):
    @min_os_level("10.15")
    def test_constants(self):
        self.assertIsInstance(PushKit.PKPushTypeFileProvider, str)

    @min_sdk_level("10.15")
    def test_methods(self):
        self.assertArgIsBlock(
            TestPKPushRegistryHelper.pushRegistry_didReceiveIncomingPushWithPayload_forType_withCompletionHandler_,  # noqa: B950
            3,
            b"v",
        )

    @min_sdk_level("10.15")
    def test_protocols(self):
        self.assertProtocolExists("PKPushRegistryDelegate")
