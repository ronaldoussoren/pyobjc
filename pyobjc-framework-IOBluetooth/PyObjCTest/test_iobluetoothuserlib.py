from PyObjCTools.TestSupport import TestCase

import IOBluetooth


IOBluetoothUserNotificationCallback = (
    b"v^v^{OpaqueIOBluetoothObjectRef=}^{OpaqueIOBluetoothObjectRef=}"
)


class TestIOBluetoothUserLib(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(IOBluetooth.IOBluetoothObjectRef)
        self.assertIs(
            IOBluetooth.IOBluetoothDeviceRef, IOBluetooth.IOBluetoothObjectRef
        )
        self.assertIs(
            IOBluetooth.IOBluetoothL2CAPChannelRef, IOBluetooth.IOBluetoothObjectRef
        )
        self.assertIs(
            IOBluetooth.IOBluetoothRFCOMMChannelRef, IOBluetooth.IOBluetoothObjectRef
        )
        self.assertIs(
            IOBluetooth.IOBluetoothSDPServiceRecordRef, IOBluetooth.IOBluetoothObjectRef
        )
        self.assertIs(
            IOBluetooth.IOBluetoothSDPUUIDRef, IOBluetooth.IOBluetoothObjectRef
        )
        self.assertIs(
            IOBluetooth.IOBluetoothSDPDataElementRef, IOBluetooth.IOBluetoothObjectRef
        )
        self.assertIs(
            IOBluetooth.IOBluetoothUserNotificationRef, IOBluetooth.IOBluetoothObjectRef
        )

    def test_constants(self):
        self.assertEqual(IOBluetooth.kIOBluetoothObjectIDNULL, 0)

        self.assertIsEnumType(IOBluetooth.IOBluetoothDeviceSearchOptionsBits)
        self.assertEqual(IOBluetooth.kSearchOptionsNone, 0)
        self.assertEqual(IOBluetooth.kSearchOptionsAlwaysStartInquiry, 1 << 0)
        self.assertEqual(IOBluetooth.kSearchOptionsDiscardCachedResults, 1 << 1)

        self.assertIsEnumType(IOBluetooth.IOBluetoothDeviceSearchTypesBits)
        self.assertEqual(IOBluetooth.kIOBluetoothDeviceSearchClassic, 1)
        self.assertEqual(IOBluetooth.kIOBluetoothDeviceSearchLE, 2)

        self.assertIsEnumType(IOBluetooth.IOBluetoothUserNotificationChannelDirection)
        self.assertEqual(IOBluetooth.kIOBluetoothUserNotificationChannelDirectionAny, 0)
        self.assertEqual(
            IOBluetooth.kIOBluetoothUserNotificationChannelDirectionIncoming, 1
        )
        self.assertEqual(
            IOBluetooth.kIOBluetoothUserNotificationChannelDirectionOutgoing, 2
        )

    def test_structs(self):
        v = IOBluetooth.IOBluetoothDeviceSearchDeviceAttributes()
        self.assertEqual(v.address, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.name, None)
        self.assertEqual(v.serviceClassMajor, 0)
        self.assertEqual(v.deviceClassMajor, 0)
        self.assertEqual(v.deviceClassMinor, 0)

        # XXX: Needs manual helpers
        v = IOBluetooth.IOBluetoothDeviceSearchAttributes()
        self.assertEqual(v.options, 0)
        self.assertEqual(v.maxResults, 0)
        self.assertEqual(v.deviceAttributeCount, 0)
        self.assertEqual(v.attributeList, None)

    def test_functions(self):
        IOBluetooth.IOBluetoothIgnoreHIDDevice
        IOBluetooth.IOBluetoothRemoveIgnoredHIDDevice
        IOBluetooth.IOBluetoothUserNotificationUnregister

        self.assertArgIsFunction(
            IOBluetooth.IOBluetoothL2CAPChannelRegisterForChannelCloseNotification,
            1,
            IOBluetoothUserNotificationCallback,
            True,
        )

        IOBluetooth.IOBluetoothAddSCOAudioDevice
        IOBluetooth.IOBluetoothRemoveSCOAudioDevice
