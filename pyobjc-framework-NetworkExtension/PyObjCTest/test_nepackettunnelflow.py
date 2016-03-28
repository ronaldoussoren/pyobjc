from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEPacketTunnelFlow (TestCase):

        @min_os_level('10.11')
        def testMethods(self):
            self.assertArgIsBlock(NetworkExtension.NEPacketTunnelFlow.readPacketsWithCompletionHandler_, 0, b'v@@')
            self.assertResultIsBOOL(NetworkExtension.NEPacketTunnelFlow.writePackets_withProtocols_)


if __name__ == "__main__":
    main()
