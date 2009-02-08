
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTMedia (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(QTMediaTypeVideo, unicode)
        self.failUnlessIsInstance(QTMediaTypeSound, unicode)
        self.failUnlessIsInstance(QTMediaTypeText, unicode)
        self.failUnlessIsInstance(QTMediaTypeBase, unicode)
        self.failUnlessIsInstance(QTMediaTypeMPEG, unicode)
        self.failUnlessIsInstance(QTMediaTypeMusic, unicode)
        self.failUnlessIsInstance(QTMediaTypeTimeCode, unicode)
        self.failUnlessIsInstance(QTMediaTypeSprite, unicode)
        self.failUnlessIsInstance(QTMediaTypeFlash, unicode)
        self.failUnlessIsInstance(QTMediaTypeMovie, unicode)
        self.failUnlessIsInstance(QTMediaTypeTween, unicode)
        self.failUnlessIsInstance(QTMediaType3D, unicode)
        self.failUnlessIsInstance(QTMediaTypeSkin, unicode)
        self.failUnlessIsInstance(QTMediaTypeQTVR, unicode)
        self.failUnlessIsInstance(QTMediaTypeHint, unicode)
        self.failUnlessIsInstance(QTMediaTypeStream, unicode)
        self.failUnlessIsInstance(QTMediaTypeMuxed, unicode)
        self.failUnlessIsInstance(QTMediaTypeQuartzComposer, unicode)
        self.failUnlessIsInstance(QTMediaCharacteristicVisual, unicode)
        self.failUnlessIsInstance(QTMediaCharacteristicAudio, unicode)
        self.failUnlessIsInstance(QTMediaCharacteristicCanSendVideo, unicode)
        self.failUnlessIsInstance(QTMediaCharacteristicProvidesActions, unicode)
        self.failUnlessIsInstance(QTMediaCharacteristicNonLinear, unicode)
        self.failUnlessIsInstance(QTMediaCharacteristicCanStep, unicode)
        self.failUnlessIsInstance(QTMediaCharacteristicHasNoDuration, unicode)
        self.failUnlessIsInstance(QTMediaCharacteristicHasSkinData, unicode)
        self.failUnlessIsInstance(QTMediaCharacteristicProvidesKeyFocus, unicode)
        self.failUnlessIsInstance(QTMediaCharacteristicHasVideoFrameRate, unicode)
        self.failUnlessIsInstance(QTMediaCreationTimeAttribute, unicode)
        self.failUnlessIsInstance(QTMediaDurationAttribute, unicode)
        self.failUnlessIsInstance(QTMediaModificationTimeAttribute, unicode)
        self.failUnlessIsInstance(QTMediaSampleCountAttribute, unicode)
        self.failUnlessIsInstance(QTMediaQualityAttribute, unicode)
        self.failUnlessIsInstance(QTMediaTimeScaleAttribute, unicode)
        self.failUnlessIsInstance(QTMediaTypeAttribute, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(QTMedia.hasCharacteristic_)

if __name__ == "__main__":
    main()
