from PyObjCTools.TestSupport import *

from ImageCaptureCore import *

class TestICDevice (TestCase):
    def testConstants(self):
        self.assertEqual(ICDeviceTypeCamera, 0x00000001)
        self.assertEqual(ICDeviceTypeScanner, 0x00000002)

        self.assertEqual(ICDeviceLocationTypeLocal, 0x00000100)
        self.assertEqual(ICDeviceLocationTypeShared, 0x00000200)
        self.assertEqual(ICDeviceLocationTypeBonjour, 0x00000400)
        self.assertEqual(ICDeviceLocationTypeBluetooth, 0x00000800)
        self.assertEqual(ICDeviceTypeMaskCamera, 0x00000001)
        self.assertEqual(ICDeviceTypeMaskScanner, 0x00000002)
        self.assertEqual(ICDeviceLocationTypeMaskLocal, 0x00000100)
        self.assertEqual(ICDeviceLocationTypeMaskShared, 0x00000200)
        self.assertEqual(ICDeviceLocationTypeMaskBonjour, 0x00000400)
        self.assertEqual(ICDeviceLocationTypeMaskBluetooth, 0x00000800)
        self.assertEqual(ICDeviceLocationTypeMaskRemote, 0x0000FE00)

        self.assertIsInstance(ICTransportTypeUSB, unicode)
        self.assertIsInstance(ICTransportTypeFireWire, unicode)
        self.assertIsInstance(ICTransportTypeBluetooth, unicode)
        self.assertIsInstance(ICTransportTypeTCPIP, unicode)
        self.assertIsInstance(ICTransportTypeMassStorage, unicode)
        self.assertIsInstance(ICDeviceLocationDescriptionUSB, unicode)
        self.assertIsInstance(ICDeviceLocationDescriptionFireWire, unicode)
        self.assertIsInstance(ICDeviceLocationDescriptionBluetooth, unicode)
        self.assertIsInstance(ICDeviceLocationDescriptionMassStorage, unicode)
        self.assertIsInstance(ICButtonTypeScan, unicode)
        self.assertIsInstance(ICButtonTypeMail, unicode)
        self.assertIsInstance(ICButtonTypeCopy, unicode)
        self.assertIsInstance(ICButtonTypeWeb, unicode)
        self.assertIsInstance(ICButtonTypePrint, unicode)
        self.assertIsInstance(ICButtonTypeTransfer, unicode)
        self.assertIsInstance(ICStatusNotificationKey, unicode)
        self.assertIsInstance(ICLocalizedStatusNotificationKey, unicode)
        self.assertIsInstance(ICDeviceCanEjectOrDisconnect, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(ICStatusCodeKey, unicode)

    def testProtocolObjects(self):
        objc.protocolNamed('ICDeviceDelegate')

    def testMethods(self):
        self.assertResultIsBOOL(ICDevice.isRemote)
        self.assertResultIsBOOL(ICDevice.isShared)
        self.assertResultIsBOOL(ICDevice.hasConfigurableWiFiInterface)
        self.assertResultIsBOOL(ICDevice.hasOpenSession)

        self.assertArgIsSEL(ICDevice.requestSendMessage_outData_maxReturnedDataSize_sendMessageDelegate_didSendMessageSelector_contextInfo_, 4, b'v@:I@@^v')


if __name__ == "__main__":
    main()
