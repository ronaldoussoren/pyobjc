
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureDevice (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(QTCaptureDeviceWasConnectedNotification, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceWasDisconnectedNotification, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceFormatDescriptionsWillChangeNotification, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceFormatDescriptionsDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceAttributeWillChangeNotification, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceAttributeDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceChangedAttributeKey, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceSuspendedAttribute, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceLinkedDevicesAttribute, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceAvailableInputSourcesAttribute, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceInputSourceIdentifierAttribute, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceInputSourceIdentifierKey, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceInputSourceLocalizedDisplayNameKey, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceInputSourceLocalizedDisplayNameKey, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceAVCTransportControlsAttribute, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceAVCTransportControlsPlaybackModeKey, unicode)
        self.failUnlessIsInstance(QTCaptureDeviceAVCTransportControlsSpeedKey, unicode)

        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsNotPlayingMode, 0)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsPlayingMode, 1)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsFastestReverseSpeed, -19000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsVeryFastReverseSpeed, -16000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsFastReverseSpeed, -13000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsNormalReverseSpeed, -10000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsSlowReverseSpeed, -7000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsVerySlowReverseSpeed, -4000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsSlowestReverseSpeed, -1000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsStoppedSpeed, 0)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsSlowestForwardSpeed, 1000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsVerySlowForwardSpeed, 4000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsSlowForwardSpeed, 7000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsNormalForwardSpeed, 10000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsFastForwardSpeed, 13000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsVeryFastForwardSpeed, 16000)
        self.failUnlessEqual(QTCaptureDeviceAVCTransportControlsFastestForwardSpeed, 19000)


    @min_os_level('10.5')
    @onlyOn32Bit
    def testConstants32bit(self):
        self.failUnlessIsInstance(QTCaptureDeviceLegacySequenceGrabberAttribute, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(QTCaptureDevice.hasMediaType_)
        self.failUnlessResultIsBOOL(QTCaptureDevice.attributeIsReadOnly_)
        self.failUnlessResultIsBOOL(QTCaptureDevice.isConnected)
        self.failUnlessResultIsBOOL(QTCaptureDevice.isInUseByAnotherApplication)
        self.failUnlessResultIsBOOL(QTCaptureDevice.isOpen)
        self.failUnlessResultIsBOOL(QTCaptureDevice.open_)
        self.failUnlessArgIsOut(QTCaptureDevice.open_, 0)


if __name__ == "__main__":
    main()
