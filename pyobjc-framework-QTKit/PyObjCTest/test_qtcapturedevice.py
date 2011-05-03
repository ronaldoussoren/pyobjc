
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureDevice (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(QTCaptureDeviceWasConnectedNotification, unicode)
        self.assertIsInstance(QTCaptureDeviceWasDisconnectedNotification, unicode)
        self.assertIsInstance(QTCaptureDeviceFormatDescriptionsWillChangeNotification, unicode)
        self.assertIsInstance(QTCaptureDeviceFormatDescriptionsDidChangeNotification, unicode)
        self.assertIsInstance(QTCaptureDeviceAttributeWillChangeNotification, unicode)
        self.assertIsInstance(QTCaptureDeviceAttributeDidChangeNotification, unicode)
        self.assertIsInstance(QTCaptureDeviceChangedAttributeKey, unicode)
        self.assertIsInstance(QTCaptureDeviceSuspendedAttribute, unicode)
        self.assertIsInstance(QTCaptureDeviceLinkedDevicesAttribute, unicode)
        self.assertIsInstance(QTCaptureDeviceAvailableInputSourcesAttribute, unicode)
        self.assertIsInstance(QTCaptureDeviceInputSourceIdentifierAttribute, unicode)
        self.assertIsInstance(QTCaptureDeviceInputSourceIdentifierKey, unicode)
        self.assertIsInstance(QTCaptureDeviceInputSourceLocalizedDisplayNameKey, unicode)
        self.assertIsInstance(QTCaptureDeviceInputSourceLocalizedDisplayNameKey, unicode)
        self.assertIsInstance(QTCaptureDeviceAVCTransportControlsAttribute, unicode)
        self.assertIsInstance(QTCaptureDeviceAVCTransportControlsPlaybackModeKey, unicode)
        self.assertIsInstance(QTCaptureDeviceAVCTransportControlsSpeedKey, unicode)

        self.assertEqual(QTCaptureDeviceAVCTransportControlsNotPlayingMode, 0)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsPlayingMode, 1)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsFastestReverseSpeed, -19000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsVeryFastReverseSpeed, -16000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsFastReverseSpeed, -13000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsNormalReverseSpeed, -10000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsSlowReverseSpeed, -7000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsVerySlowReverseSpeed, -4000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsSlowestReverseSpeed, -1000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsStoppedSpeed, 0)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsSlowestForwardSpeed, 1000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsVerySlowForwardSpeed, 4000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsSlowForwardSpeed, 7000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsNormalForwardSpeed, 10000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsFastForwardSpeed, 13000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsVeryFastForwardSpeed, 16000)
        self.assertEqual(QTCaptureDeviceAVCTransportControlsFastestForwardSpeed, 19000)


    @min_os_level('10.5')
    @onlyOn32Bit
    def testConstants32bit(self):
        self.assertIsInstance(QTCaptureDeviceLegacySequenceGrabberAttribute, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(QTCaptureDevice.hasMediaType_)
        self.assertResultIsBOOL(QTCaptureDevice.attributeIsReadOnly_)
        self.assertResultIsBOOL(QTCaptureDevice.isConnected)
        self.assertResultIsBOOL(QTCaptureDevice.isInUseByAnotherApplication)
        self.assertResultIsBOOL(QTCaptureDevice.isOpen)
        self.assertResultIsBOOL(QTCaptureDevice.open_)
        self.assertArgIsOut(QTCaptureDevice.open_, 0)


if __name__ == "__main__":
    main()
