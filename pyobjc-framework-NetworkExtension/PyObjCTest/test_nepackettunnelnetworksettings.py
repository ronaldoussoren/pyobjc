from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEPacketTunnelNetworkSettings(TestCase):

    def test_enums(self):
        self.assertIsEnumType(NetworkExtension.NEPacketTunnelNetworkSettingsIPFamily)
        self.assertEqual(NetworkExtension.NEPacketTunnelNetworkSettingsIPFamilyNone, 0)
        self.assertEqual(NetworkExtension.NEPacketTunnelNetworkSettingsIPFamilyAny, 1)
        self.assertEqual(NetworkExtension.NEPacketTunnelNetworkSettingsIPFamilyIPv4, 2)
        self.assertEqual(NetworkExtension.NEPacketTunnelNetworkSettingsIPFamilyIPv6, 3)

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            NetworkExtension.NEPacketTunnelNetworkSettings.excludeCellularServices
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEPacketTunnelNetworkSettings.setExcludeCellularServices_,
            0,
        )
        self.assertResultIsBOOL(
            NetworkExtension.NEPacketTunnelNetworkSettings.excludeAPNs
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEPacketTunnelNetworkSettings.setExcludeAPNs_, 0
        )
        self.assertResultIsBOOL(
            NetworkExtension.NEPacketTunnelNetworkSettings.excludeDeviceCommunication
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEPacketTunnelNetworkSettings.setExcludeDeviceCommunication_,
            0,
        )
        self.assertResultIsBOOL(
            NetworkExtension.NEPacketTunnelNetworkSettings.enforceRoutes
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEPacketTunnelNetworkSettings.setEnforceRoutes_, 0
        )
