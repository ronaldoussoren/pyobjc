from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNETunnelProviderSession(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(
            NetworkExtension.NETunnelProviderSession.startTunnelWithOptions_andReturnError_
        )
        self.assertArgIsOut(
            NetworkExtension.NETunnelProviderSession.startTunnelWithOptions_andReturnError_,
            1,
        )

        self.assertResultIsBOOL(
            NetworkExtension.NETunnelProviderSession.sendProviderMessage_returnError_responseHandler_
        )
        self.assertArgIsOut(
            NetworkExtension.NETunnelProviderSession.sendProviderMessage_returnError_responseHandler_,
            1,
        )
        self.assertArgIsBlock(
            NetworkExtension.NETunnelProviderSession.sendProviderMessage_returnError_responseHandler_,
            2,
            b"v@",
        )
