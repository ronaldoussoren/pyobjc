import CoreBluetooth
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBCentral(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(CoreBluetooth.CBConnectionEventMatchingOption, str)

    @min_os_level("10.9")
    def test_constants(self):
        self.assertIsInstance(
            CoreBluetooth.CBCentralManagerOptionShowPowerAlertKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBCentralManagerScanOptionAllowDuplicatesKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBCentralManagerScanOptionSolicitedServiceUUIDsKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBConnectPeripheralOptionNotifyOnDisconnectionKey, str
        )

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(
            CoreBluetooth.CBCentralManagerOptionRestoreIdentifierKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBConnectPeripheralOptionNotifyOnConnectionKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBConnectPeripheralOptionNotifyOnNotificationKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBCentralManagerRestoredStatePeripheralsKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBCentralManagerRestoredStateScanServicesKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBCentralManagerRestoredStateScanOptionsKey, str
        )

    # @min_os_level("11.0")
    # def test_constants11_0(self):
    # XXX: unavailable according to macOS 12 SDK.
    # self.assertIsInstance(
    #   CoreBluetooth.CBConnectionEventMatchingOptionServiceUUIDs, str
    # )
    # self.assertIsInstance(
    #    CoreBluetooth.CBConnectionEventMatchingOptionPeripheralUUIDs, str
    # )
    # pass

    @min_os_level("10.14")
    def test_constants10_14(self):
        # XXX: This is currently documented as a 10.13 constant, but isn't available there
        self.assertIsInstance(CoreBluetooth.CBConnectPeripheralOptionStartDelayKey, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(
            CoreBluetooth.CBConnectPeripheralOptionEnableAutoReconnect, str
        )
