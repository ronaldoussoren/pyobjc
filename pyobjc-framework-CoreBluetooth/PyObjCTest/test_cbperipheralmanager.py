import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBPeriphalManagerHelper(CoreBluetooth.NSObject):
    def peripheralManager_didPublishL2CAPChannel_error_(self, m, c, e):
        pass

    def peripheralManager_didUnpublishL2CAPChannel_error_(self, m, c, e):
        pass

    def peripheralManager_didOpenL2CAPChannel_error_(self, m, c, e):
        pass


class TestCBPeriphicalManager(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreBluetooth.CBPeripheralManagerAuthorizationStatus)
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusNotDetermined, 0)
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusRestricted, 1)
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusDenied, 2)
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusAuthorized, 3)

        self.assertIsEnumType(CoreBluetooth.CBPeripheralManagerState)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateUnknown, 0)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateResetting, 1)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateUnsupported, 2)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateUnauthorized, 3)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStatePoweredOff, 4)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStatePoweredOn, 5)

        self.assertIsEnumType(CoreBluetooth.CBPeripheralManagerConnectionLatency)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerConnectionLatencyLow, 0)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerConnectionLatencyMedium, 1)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerConnectionLatencyHigh, 2)

        self.assertEqual(
            CoreBluetooth.CBPeripheralManagerAuthorizationStatusNotDetermined, 0
        )
        self.assertEqual(
            CoreBluetooth.CBPeripheralManagerAuthorizationStatusRestricted, 1
        )
        self.assertEqual(CoreBluetooth.CBPeripheralManagerAuthorizationStatusDenied, 2)
        self.assertEqual(
            CoreBluetooth.CBPeripheralManagerAuthorizationStatusAuthorized, 3
        )

    def test_classes(self):
        self.assertIsInstance(CoreBluetooth.CBPeripheralManager, objc.objc_class)

    def test_protocols(self):
        self.assertProtocolExists("CBPeripheralManagerDelegate", CoreBluetooth)

    def test_methods(self):
        self.assertResultIsBOOL(CoreBluetooth.CBPeripheralManager.isAdvertising)
        self.assertResultIsBOOL(
            CoreBluetooth.CBPeripheralManager.updateValue_forCharacteristic_onSubscribedCentrals_  # noqa: B950
        )

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertArgIsBOOL(
            CoreBluetooth.CBPeripheralManager.publishL2CAPChannelWithEncryption_, 0
        )

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestCBPeriphalManagerHelper.peripheralManager_didPublishL2CAPChannel_error_,
            1,
            objc._C_USHT,
        )
        self.assertArgHasType(
            TestCBPeriphalManagerHelper.peripheralManager_didUnpublishL2CAPChannel_error_,
            1,
            objc._C_USHT,
        )
        self.assertArgHasType(
            TestCBPeriphalManagerHelper.peripheralManager_didOpenL2CAPChannel_error_,
            1,
            objc._C_USHT,
        )
