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
    def test_enum_types(self):
        self.assertIsEnumType(CoreBluetooth.CBPeripheralManagerAuthorizationStatus)
        self.assertIsEnumType(CoreBluetooth.CBPeripheralManagerConnectionLatency)
        self.assertIsEnumType(CoreBluetooth.CBPeripheralManagerState)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusNotDetermined, 0)
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusRestricted, 1)
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusDenied, 2)
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusAuthorized, 3)

        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateUnknown, 0)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateResetting, 1)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateUnsupported, 2)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateUnauthorized, 3)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStatePoweredOff, 4)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStatePoweredOn, 5)

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

    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(CoreBluetooth.CBPeripheralManager, objc.objc_class)

    @min_os_level("10.9")
    def testProtocols(self):
        self.assertProtocolExists("CBPeripheralManagerDelegate")

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(CoreBluetooth.CBPeripheralManager.isAdvertising)
        self.assertResultIsBOOL(
            CoreBluetooth.CBPeripheralManager.updateValue_forCharacteristic_onSubscribedCentrals_  # noqa: B950
        )

        # XXX: A number of methods have a dispatch_queue as their argument

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

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertArgIsBOOL(
            CoreBluetooth.CBPeripheralManager.publishL2CAPChannelWithEncryption_, 0
        )
