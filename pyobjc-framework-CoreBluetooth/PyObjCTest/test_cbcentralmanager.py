import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBCentralManagerHelper(CoreBluetooth.NSObject):
    def centralManager_connectionEventDidOccur_forPeripheral_(self, a, b, c):
        pass


class TestCBCentralManager(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertHasAttr(CoreBluetooth, "CBCentralManager")
        self.assertIsInstance(CoreBluetooth.CBCentralManager, objc.objc_class)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(CoreBluetooth.CBCentralManagerStateUnknown, 0)
        self.assertEqual(CoreBluetooth.CBCentralManagerStateResetting, 1)
        self.assertEqual(CoreBluetooth.CBCentralManagerStateUnsupported, 2)
        self.assertEqual(CoreBluetooth.CBCentralManagerStateUnauthorized, 3)
        self.assertEqual(CoreBluetooth.CBCentralManagerStatePoweredOff, 4)
        self.assertEqual(CoreBluetooth.CBCentralManagerStatePoweredOn, 5)

        self.assertEqual(CoreBluetooth.CBConnectionEventPeerDisconnected, 0)
        self.assertEqual(CoreBluetooth.CBConnectionEventPeerConnected, 1)

        self.assertEqual(
            CoreBluetooth.CBCentralManagerFeatureExtendedScanAndConnect, 1 << 0
        )

    @min_os_level("10.9")
    def testProtocols(self):
        self.assertIsInstance(
            objc.protocolNamed("CBCentralManagerDelegate"), objc.formal_protocol
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(CoreBluetooth.CBCentralManager.isScanning)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgHasType(
            CoreBluetooth.TestCBCentralManagerHelper.centralManager_connectionEventDidOccur_forPeripheral_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )

    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertResultIsBOOL(CoreBluetooth.CBCentralManager.supportsFeatures_)
