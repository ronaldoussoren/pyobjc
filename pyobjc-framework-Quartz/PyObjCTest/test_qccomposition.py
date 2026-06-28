from PyObjCTools.TestSupport import (
    TestCase,
    max_os_level,
)
import Quartz


class TestQCComposition(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.QCCompositionAttributeNameKey, str)
        self.assertIsInstance(Quartz.QCCompositionAttributeDescriptionKey, str)
        self.assertIsInstance(Quartz.QCCompositionAttributeCopyrightKey, str)
        self.assertIsInstance(Quartz.QCCompositionAttributeBuiltInKey, str)
        self.assertIsInstance(Quartz.QCCompositionAttributeIsTimeDependentKey, str)
        self.assertIsInstance(Quartz.QCCompositionAttributeHasConsumersKey, str)
        self.assertIsInstance(Quartz.QCCompositionAttributeCategoryKey, str)
        self.assertIsInstance(Quartz.QCCompositionCategoryDistortion, str)
        self.assertIsInstance(Quartz.QCCompositionCategoryStylize, str)
        self.assertIsInstance(Quartz.QCCompositionCategoryUtility, str)
        self.assertIsInstance(Quartz.QCCompositionInputImageKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputSourceImageKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputDestinationImageKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputPreviewModeKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputXKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputYKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputScreenImageKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputAudioPeakKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputAudioSpectrumKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputTrackPositionKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputTrackInfoKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputTrackSignalKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputPrimaryColorKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputSecondaryColorKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputPaceKey, str)
        self.assertIsInstance(Quartz.QCCompositionOutputImageKey, str)
        self.assertIsInstance(Quartz.QCCompositionOutputWebPageURLKey, str)
        self.assertIsInstance(Quartz.QCCompositionProtocolGraphicAnimation, str)
        self.assertIsInstance(Quartz.QCCompositionProtocolGraphicTransition, str)
        self.assertIsInstance(Quartz.QCCompositionProtocolImageFilter, str)
        self.assertIsInstance(Quartz.QCCompositionProtocolScreenSaver, str)
        self.assertIsInstance(Quartz.QCCompositionProtocolMusicVisualizer, str)

    @max_os_level("10.13")
    def test_constants_removed_in_10_14(self):
        self.assertIsInstance(Quartz.QCCompositionInputRSSFeedURLKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputRSSArticleDurationKey, str)
        self.assertIsInstance(Quartz.QCCompositionProtocolRSSVisualizer, str)
