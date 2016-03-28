from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEVPNProtocol (TestCase):
        @min_os_level('10.11')
        def testMethods(self):
            self.assertResultIsBOOL(NetworkExtension.NEVPNProtocol.disconnectOnSleep)
            self.assertArgIsBOOL(NetworkExtension.NEVPNProtocol.setDisconnectOnSleep_, 0)


if __name__ == "__main__":
    main()
