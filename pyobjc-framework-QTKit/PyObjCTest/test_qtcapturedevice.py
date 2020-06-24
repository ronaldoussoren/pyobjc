from PyObjCTools.TestSupport import TestCase, min_os_level
import QTKit


class TestQTCaptureDevice(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(QTKit.QTCaptureDeviceWasConnectedNotification, str)
        self.assertIsInstance(QTKit.QTCaptureDeviceWasDisconnectedNotification, str)
        self.assertIsInstance(
            QTKit.QTCaptureDeviceFormatDescriptionsWillChangeNotification, str
        )
        self.assertIsInstance(
            QTKit.QTCaptureDeviceFormatDescriptionsDidChangeNotification, str
        )
        self.assertIsInstance(QTKit.QTCaptureDeviceAttributeWillChangeNotification, str)
        self.assertIsInstance(QTKit.QTCaptureDeviceAttributeDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTCaptureDeviceChangedAttributeKey, str)
        self.assertIsInstance(QTKit.QTCaptureDeviceSuspendedAttribute, str)
        self.assertIsInstance(QTKit.QTCaptureDeviceLinkedDevicesAttribute, str)
        self.assertIsInstance(QTKit.QTCaptureDeviceAvailableInputSourcesAttribute, str)
        self.assertIsInstance(QTKit.QTCaptureDeviceInputSourceIdentifierAttribute, str)
        self.assertIsInstance(QTKit.QTCaptureDeviceInputSourceIdentifierKey, str)
        self.assertIsInstance(
            QTKit.QTCaptureDeviceInputSourceLocalizedDisplayNameKey, str
        )
        self.assertIsInstance(
            QTKit.QTCaptureDeviceInputSourceLocalizedDisplayNameKey, str
        )
        self.assertIsInstance(QTKit.QTCaptureDeviceAVCTransportControlsAttribute, str)
        self.assertIsInstance(
            QTKit.QTCaptureDeviceAVCTransportControlsPlaybackModeKey, str
        )
        self.assertIsInstance(QTKit.QTCaptureDeviceAVCTransportControlsSpeedKey, str)

        self.assertEqual(QTKit.QTCaptureDeviceAVCTransportControlsNotPlayingMode, 0)
        self.assertEqual(QTKit.QTCaptureDeviceAVCTransportControlsPlayingMode, 1)

        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsFastestReverseSpeed, -19000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsVeryFastReverseSpeed, -16000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsFastReverseSpeed, -13000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsNormalReverseSpeed, -10000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsSlowReverseSpeed, -7000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsVerySlowReverseSpeed, -4000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsSlowestReverseSpeed, -1000
        )
        self.assertEqual(QTKit.QTCaptureDeviceAVCTransportControlsStoppedSpeed, 0)
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsSlowestForwardSpeed, 1000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsVerySlowForwardSpeed, 4000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsSlowForwardSpeed, 7000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsNormalForwardSpeed, 10000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsFastForwardSpeed, 13000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsVeryFastForwardSpeed, 16000
        )
        self.assertEqual(
            QTKit.QTCaptureDeviceAVCTransportControlsFastestForwardSpeed, 19000
        )

    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTCaptureDevice.hasMediaType_)
        self.assertResultIsBOOL(QTKit.QTCaptureDevice.attributeIsReadOnly_)
        self.assertResultIsBOOL(QTKit.QTCaptureDevice.isConnected)
        self.assertResultIsBOOL(QTKit.QTCaptureDevice.isInUseByAnotherApplication)
        self.assertResultIsBOOL(QTKit.QTCaptureDevice.isOpen)
        self.assertResultIsBOOL(QTKit.QTCaptureDevice.open_)
        self.assertArgIsOut(QTKit.QTCaptureDevice.open_, 0)
