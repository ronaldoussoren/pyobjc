import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import PushKit

    class TestPKPushRegistryHelper(PushKit.NSObject):
        def pushRegistry_didReceiveIncomingPushWithPayload_forType_withCompletionHandler_(
            self, a, b, c, d
        ):
            pass

    class TestPKPushRegistry(TestCase):
        @min_os_level("10.15")
        def test_constants(self):
            self.assertIsInstance(PushKit.PKPushTypeFileProvider, unicode)

        @min_sdk_level("10.15")
        def test_methods(self):
            self.assertArgIsBlock(
                TestPKPushRegistryHelper.pushRegistry_didReceiveIncomingPushWithPayload_forType_withCompletionHandler_,
                3,
                b"v",
            )

        @min_sdk_level("10.15")
        def test_protocols(self):
            objc.protocolNamed("PKPushRegistryDelegate")
