from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNETunnelProviderSession (TestCase):
        @min_os_level('10.11')
        def testMethods(self):
            self.assertResultIsBOOL(NetworkExtension.NETunnelProviderSession.startTunnelWithOptions_andReturnError_)
            self.assertArgIsOut(NetworkExtension.NETunnelProviderSession.startTunnelWithOptions_andReturnError_, 1)

            self.assertResultIsBOOL(NetworkExtension.NETunnelProviderSession.sendProviderMessage_returnError_responseHandler_)
            self.assertArgIsOut(NetworkExtension.NETunnelProviderSession.sendProviderMessage_returnError_responseHandler_, 1)
            self.assertArgIsBlock(NetworkExtension.NETunnelProviderSession.sendProviderMessage_returnError_responseHandler_, 2, b'v@')

if __name__ == "__main__":
    main()
