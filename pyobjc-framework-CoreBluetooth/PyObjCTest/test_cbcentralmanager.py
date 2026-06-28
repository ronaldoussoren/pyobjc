import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBCentralManagerHelper(CoreBluetooth.NSObject):
    def centralManager_connectionEventDidOccur_forPeripheral_(self, a, b, c):
        pass

    def centralManager_didDisconnectPeripheral_timestamp_isReconnecting_error_(
        self, a, b, c, d, e
    ):
        pass


class TestCBCentralManager(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreBluetooth.CBCentralManagerState)
        self.assertEqual(CoreBluetooth.CBCentralManagerStateUnknown, 0)
        self.assertEqual(CoreBluetooth.CBCentralManagerStateResetting, 1)
        self.assertEqual(CoreBluetooth.CBCentralManagerStateUnsupported, 2)
        self.assertEqual(CoreBluetooth.CBCentralManagerStateUnauthorized, 3)
        self.assertEqual(CoreBluetooth.CBCentralManagerStatePoweredOff, 4)
        self.assertEqual(CoreBluetooth.CBCentralManagerStatePoweredOn, 5)

        self.assertIsEnumType(CoreBluetooth.CBConnectionEvent)
        self.assertEqual(CoreBluetooth.CBConnectionEventPeerDisconnected, 0)
        self.assertEqual(CoreBluetooth.CBConnectionEventPeerConnected, 1)

        self.assertIsEnumType(CoreBluetooth.CBCentralManagerFeature)
        self.assertEqual(
            CoreBluetooth.CBCentralManagerFeatureExtendedScanAndConnect, 1 << 0
        )
        self.assertEqual(CoreBluetooth.CBCentralManagerFeatureChannelSounding, 1 << 10)

    def test_classes(self):
        self.assertHasAttr(CoreBluetooth, "CBCentralManager")
        self.assertIsInstance(CoreBluetooth.CBCentralManager, objc.objc_class)

    def test_protocols(self):
        self.assertProtocolExists("CBCentralManagerDelegate", CoreBluetooth)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(CoreBluetooth.CBCentralManager.isScanning)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgHasType(
            TestCBCentralManagerHelper.centralManager_connectionEventDidOccur_forPeripheral_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestCBCentralManagerHelper.centralManager_didDisconnectPeripheral_timestamp_isReconnecting_error_,
            2,
            objc._C_DBL,
        )
        self.assertArgIsBOOL(
            TestCBCentralManagerHelper.centralManager_didDisconnectPeripheral_timestamp_isReconnecting_error_,
            3,
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(CoreBluetooth.CBCentralManager.supportsFeatures_)
