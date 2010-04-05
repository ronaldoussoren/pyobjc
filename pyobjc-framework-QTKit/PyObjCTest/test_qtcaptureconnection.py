
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureConnection (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(QTCaptureConnectionFormatDescriptionWillChangeNotification, unicode)
        self.assertIsInstance(QTCaptureConnectionFormatDescriptionDidChangeNotification, unicode)
        self.assertIsInstance(QTCaptureConnectionAttributeWillChangeNotification, unicode)
        self.assertIsInstance(QTCaptureConnectionAttributeDidChangeNotification, unicode)
        self.assertIsInstance(QTCaptureConnectionChangedAttributeKey, unicode)
        self.assertIsInstance(QTCaptureConnectionAudioAveragePowerLevelsAttribute, unicode)
        self.assertIsInstance(QTCaptureConnectionAudioPeakHoldLevelsAttribute, unicode)
        self.assertIsInstance(QTCaptureConnectionAudioMasterVolumeAttribute, unicode)
        self.assertIsInstance(QTCaptureConnectionAudioVolumesAttribute, unicode)
        self.assertIsInstance(QTCaptureConnectionEnabledAudioChannelsAttribute, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(QTCaptureConnection.isEnabled)
        self.assertArgIsBOOL(QTCaptureConnection.setEnabled_, 0)
        self.assertResultIsBOOL(QTCaptureConnection.attributeIsReadOnly_)


if __name__ == "__main__":
    main()
