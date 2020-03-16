import CoreWLAN
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCWWifiClientHelper(CoreWLAN.NSObject):
    def linkQualityDidChangeForWiFiInterfaceWithName_rssi_transmitRate_(
        self, nm, rs, tr
    ):
        pass


class TestCWWiFiClient(TestCase):
    @min_os_level("10.10")
    def testProtocols10_10(self):
        self.assertIsInstance(
            objc.protocolNamed("CWEventDelegate"), objc.formal_protocol
        )

        self.assertArgHasType(
            TestCWWifiClientHelper.linkQualityDidChangeForWiFiInterfaceWithName_rssi_transmitRate_,  # noqa: B950
            1,
            objc._C_NSInteger,
            objc._C_DBL,
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            CoreWLAN.CWWiFiClient.startMonitoringEventWithType_error_
        )
        self.assertArgIsOut(
            CoreWLAN.CWWiFiClient.startMonitoringEventWithType_error_, 1
        )

        self.assertResultIsBOOL(
            CoreWLAN.CWWiFiClient.stopMonitoringEventWithType_error_
        )
        self.assertArgIsOut(CoreWLAN.CWWiFiClient.stopMonitoringEventWithType_error_, 1)

        self.assertResultIsBOOL(
            CoreWLAN.CWWiFiClient.stopMonitoringAllEventsAndReturnError_
        )
        self.assertArgIsOut(
            CoreWLAN.CWWiFiClient.stopMonitoringAllEventsAndReturnError_, 0
        )
