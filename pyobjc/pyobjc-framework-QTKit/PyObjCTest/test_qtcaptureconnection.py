
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureConnection (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(QTCaptureConnectionFormatDescriptionWillChangeNotification, unicode)
        self.failUnlessIsInstance(QTCaptureConnectionFormatDescriptionDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTCaptureConnectionAttributeWillChangeNotification, unicode)
        self.failUnlessIsInstance(QTCaptureConnectionAttributeDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTCaptureConnectionChangedAttributeKey, unicode)
        self.failUnlessIsInstance(QTCaptureConnectionAudioAveragePowerLevelsAttribute, unicode)
        self.failUnlessIsInstance(QTCaptureConnectionAudioPeakHoldLevelsAttribute, unicode)
        self.failUnlessIsInstance(QTCaptureConnectionAudioMasterVolumeAttribute, unicode)
        self.failUnlessIsInstance(QTCaptureConnectionAudioVolumesAttribute, unicode)
        self.failUnlessIsInstance(QTCaptureConnectionEnabledAudioChannelsAttribute, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(QTCaptureConnection.isEnabled)
        self.failUnlessArgIsBOOL(QTCaptureConnection.setEnabled_, 0)
        self.failUnlessResultIsBOOL(QTCaptureConnection.attributeIsReadOnly_)


if __name__ == "__main__":
    main()
