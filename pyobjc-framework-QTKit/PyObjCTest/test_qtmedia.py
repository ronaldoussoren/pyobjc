from PyObjCTools.TestSupport import TestCase, min_os_level
import QTKit


class TestQTMedia(TestCase):
    def testConstants(self):
        self.assertIsInstance(QTKit.QTMediaTypeVideo, str)
        self.assertIsInstance(QTKit.QTMediaTypeSound, str)
        self.assertIsInstance(QTKit.QTMediaTypeText, str)
        self.assertIsInstance(QTKit.QTMediaTypeBase, str)
        self.assertIsInstance(QTKit.QTMediaTypeMPEG, str)
        self.assertIsInstance(QTKit.QTMediaTypeMusic, str)
        self.assertIsInstance(QTKit.QTMediaTypeTimeCode, str)
        self.assertIsInstance(QTKit.QTMediaTypeSprite, str)
        self.assertIsInstance(QTKit.QTMediaTypeFlash, str)
        self.assertIsInstance(QTKit.QTMediaTypeMovie, str)
        self.assertIsInstance(QTKit.QTMediaTypeTween, str)
        self.assertIsInstance(QTKit.QTMediaType3D, str)
        self.assertIsInstance(QTKit.QTMediaTypeSkin, str)
        self.assertIsInstance(QTKit.QTMediaTypeQTVR, str)
        self.assertIsInstance(QTKit.QTMediaTypeHint, str)
        self.assertIsInstance(QTKit.QTMediaTypeStream, str)
        self.assertIsInstance(QTKit.QTMediaTypeMuxed, str)
        self.assertIsInstance(QTKit.QTMediaTypeQuartzComposer, str)
        self.assertIsInstance(QTKit.QTMediaCharacteristicVisual, str)
        self.assertIsInstance(QTKit.QTMediaCharacteristicAudio, str)
        self.assertIsInstance(QTKit.QTMediaCharacteristicCanSendVideo, str)
        self.assertIsInstance(QTKit.QTMediaCharacteristicProvidesActions, str)
        self.assertIsInstance(QTKit.QTMediaCharacteristicNonLinear, str)
        self.assertIsInstance(QTKit.QTMediaCharacteristicCanStep, str)
        self.assertIsInstance(QTKit.QTMediaCharacteristicHasNoDuration, str)
        self.assertIsInstance(QTKit.QTMediaCharacteristicHasSkinData, str)
        self.assertIsInstance(QTKit.QTMediaCharacteristicProvidesKeyFocus, str)
        self.assertIsInstance(QTKit.QTMediaCharacteristicHasVideoFrameRate, str)
        self.assertIsInstance(QTKit.QTMediaCreationTimeAttribute, str)
        self.assertIsInstance(QTKit.QTMediaDurationAttribute, str)
        self.assertIsInstance(QTKit.QTMediaModificationTimeAttribute, str)
        self.assertIsInstance(QTKit.QTMediaSampleCountAttribute, str)
        self.assertIsInstance(QTKit.QTMediaQualityAttribute, str)
        self.assertIsInstance(QTKit.QTMediaTimeScaleAttribute, str)
        self.assertIsInstance(QTKit.QTMediaTypeAttribute, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(QTKit.QTMediaTypeSubtitle, str)
        self.assertIsInstance(QTKit.QTMediaTypeClosedCaption, str)

    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTMedia.hasCharacteristic_)
