from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEVPNProtocol(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(NetworkExtension.NEVPNProtocol.disconnectOnSleep)
        self.assertArgIsBOOL(NetworkExtension.NEVPNProtocol.setDisconnectOnSleep_, 0)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(NetworkExtension.NEVPNProtocol.includeAllNetworks)
        self.assertArgIsBOOL(NetworkExtension.NEVPNProtocol.setIncludeAllNetworks_, 0)

        self.assertResultIsBOOL(NetworkExtension.NEVPNProtocol.excludeLocalNetworks)
        self.assertArgIsBOOL(NetworkExtension.NEVPNProtocol.setExcludeLocalNetworks_, 0)

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(NetworkExtension.NEVPNProtocol.enforceRoutes)
        self.assertArgIsBOOL(NetworkExtension.NEVPNProtocol.setEnforceRoutes_, 0)

    @min_os_level("13.3")
    def testMethods13_3(self):
        self.assertResultIsBOOL(NetworkExtension.NEVPNProtocol.excludeCellularServices)
        self.assertArgIsBOOL(
            NetworkExtension.NEVPNProtocol.setExcludeCellularServices_, 0
        )

        self.assertResultIsBOOL(NetworkExtension.NEVPNProtocol.excludeAPNs)
        self.assertArgIsBOOL(NetworkExtension.NEVPNProtocol.setExcludeAPNs_, 0)

    @min_os_level("14.4")
    def testMethods14_4(self):
        self.assertResultIsBOOL(
            NetworkExtension.NEVPNProtocol.excludeDeviceCommunication
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEVPNProtocol.setExcludeDeviceCommunication_, 0
        )
