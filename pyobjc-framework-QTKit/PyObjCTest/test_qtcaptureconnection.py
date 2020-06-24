from PyObjCTools.TestSupport import TestCase, min_os_level
import QTKit


class TestQTCaptureConnection(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(
            QTKit.QTCaptureConnectionFormatDescriptionWillChangeNotification, str
        )
        self.assertIsInstance(
            QTKit.QTCaptureConnectionFormatDescriptionDidChangeNotification, str
        )
        self.assertIsInstance(
            QTKit.QTCaptureConnectionAttributeWillChangeNotification, str
        )
        self.assertIsInstance(
            QTKit.QTCaptureConnectionAttributeDidChangeNotification, str
        )
        self.assertIsInstance(QTKit.QTCaptureConnectionChangedAttributeKey, str)
        self.assertIsInstance(
            QTKit.QTCaptureConnectionAudioAveragePowerLevelsAttribute, str
        )
        self.assertIsInstance(
            QTKit.QTCaptureConnectionAudioPeakHoldLevelsAttribute, str
        )
        self.assertIsInstance(QTKit.QTCaptureConnectionAudioMasterVolumeAttribute, str)
        self.assertIsInstance(QTKit.QTCaptureConnectionAudioVolumesAttribute, str)
        self.assertIsInstance(
            QTKit.QTCaptureConnectionEnabledAudioChannelsAttribute, str
        )

    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTCaptureConnection.isEnabled)
        self.assertArgIsBOOL(QTKit.QTCaptureConnection.setEnabled_, 0)
        self.assertResultIsBOOL(QTKit.QTCaptureConnection.attributeIsReadOnly_)
