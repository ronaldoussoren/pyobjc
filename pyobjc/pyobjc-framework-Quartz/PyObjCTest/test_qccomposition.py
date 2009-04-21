
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

class TestQCComposition (TestCase):

    def testConstants(self):
        self.failUnlessIsInstance(QCCompositionAttributeNameKey, unicode)
        self.failUnlessIsInstance(QCCompositionAttributeDescriptionKey, unicode)
        self.failUnlessIsInstance(QCCompositionAttributeCopyrightKey, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(QCCompositionAttributeBuiltInKey, unicode)
        self.failUnlessIsInstance(QCCompositionAttributeIsTimeDependentKey, unicode)
        self.failUnlessIsInstance(QCCompositionAttributeHasConsumersKey, unicode)
        self.failUnlessIsInstance(QCCompositionAttributeCategoryKey, unicode)
        self.failUnlessIsInstance(QCCompositionCategoryDistortion, unicode)
        self.failUnlessIsInstance(QCCompositionCategoryStylize, unicode)
        self.failUnlessIsInstance(QCCompositionCategoryUtility, unicode)
        self.failUnlessIsInstance(QCCompositionInputImageKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputSourceImageKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputDestinationImageKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputRSSFeedURLKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputRSSArticleDurationKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputPreviewModeKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputXKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputYKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputScreenImageKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputAudioPeakKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputAudioSpectrumKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputTrackPositionKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputTrackInfoKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputTrackSignalKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputPrimaryColorKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputSecondaryColorKey, unicode)
        self.failUnlessIsInstance(QCCompositionInputPaceKey, unicode)
        self.failUnlessIsInstance(QCCompositionOutputImageKey, unicode)
        self.failUnlessIsInstance(QCCompositionOutputWebPageURLKey, unicode)
        self.failUnlessIsInstance(QCCompositionProtocolGraphicAnimation, unicode)
        self.failUnlessIsInstance(QCCompositionProtocolGraphicTransition, unicode)
        self.failUnlessIsInstance(QCCompositionProtocolImageFilter, unicode)
        self.failUnlessIsInstance(QCCompositionProtocolScreenSaver, unicode)
        self.failUnlessIsInstance(QCCompositionProtocolRSSVisualizer, unicode)
        self.failUnlessIsInstance(QCCompositionProtocolMusicVisualizer, unicode)


if __name__ == "__main__":
    main()
