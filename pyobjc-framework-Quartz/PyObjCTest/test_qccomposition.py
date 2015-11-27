
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

class TestQCComposition (TestCase):

    def testConstants(self):
        self.assertIsInstance(QCCompositionAttributeNameKey, unicode)
        self.assertIsInstance(QCCompositionAttributeDescriptionKey, unicode)
        self.assertIsInstance(QCCompositionAttributeCopyrightKey, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(QCCompositionAttributeBuiltInKey, unicode)
        self.assertIsInstance(QCCompositionAttributeIsTimeDependentKey, unicode)
        self.assertIsInstance(QCCompositionAttributeHasConsumersKey, unicode)
        self.assertIsInstance(QCCompositionAttributeCategoryKey, unicode)
        self.assertIsInstance(QCCompositionCategoryDistortion, unicode)
        self.assertIsInstance(QCCompositionCategoryStylize, unicode)
        self.assertIsInstance(QCCompositionCategoryUtility, unicode)
        self.assertIsInstance(QCCompositionInputImageKey, unicode)
        self.assertIsInstance(QCCompositionInputSourceImageKey, unicode)
        self.assertIsInstance(QCCompositionInputDestinationImageKey, unicode)
        self.assertIsInstance(QCCompositionInputRSSFeedURLKey, unicode)
        self.assertIsInstance(QCCompositionInputRSSArticleDurationKey, unicode)
        self.assertIsInstance(QCCompositionInputPreviewModeKey, unicode)
        self.assertIsInstance(QCCompositionInputXKey, unicode)
        self.assertIsInstance(QCCompositionInputYKey, unicode)
        self.assertIsInstance(QCCompositionInputScreenImageKey, unicode)
        self.assertIsInstance(QCCompositionInputAudioPeakKey, unicode)
        self.assertIsInstance(QCCompositionInputAudioSpectrumKey, unicode)
        self.assertIsInstance(QCCompositionInputTrackPositionKey, unicode)
        self.assertIsInstance(QCCompositionInputTrackInfoKey, unicode)
        self.assertIsInstance(QCCompositionInputTrackSignalKey, unicode)
        self.assertIsInstance(QCCompositionInputPrimaryColorKey, unicode)
        self.assertIsInstance(QCCompositionInputSecondaryColorKey, unicode)
        self.assertIsInstance(QCCompositionInputPaceKey, unicode)
        self.assertIsInstance(QCCompositionOutputImageKey, unicode)
        self.assertIsInstance(QCCompositionOutputWebPageURLKey, unicode)
        self.assertIsInstance(QCCompositionProtocolGraphicAnimation, unicode)
        self.assertIsInstance(QCCompositionProtocolGraphicTransition, unicode)
        self.assertIsInstance(QCCompositionProtocolImageFilter, unicode)
        self.assertIsInstance(QCCompositionProtocolScreenSaver, unicode)
        self.assertIsInstance(QCCompositionProtocolRSSVisualizer, unicode)
        self.assertIsInstance(QCCompositionProtocolMusicVisualizer, unicode)

    @min_os_level('10.6')
    @expectedFailure
    def testConstants10_6(self):
        self.assertIsInstance(QCCompositionInputMeshKey, unicode)
        self.assertIsInstance(QCCompositionOutputMeshKey, unicode)
        self.assertIsInstance(QCCompositionProtocolMeshFilter, unicode)


if __name__ == "__main__":
    main()
