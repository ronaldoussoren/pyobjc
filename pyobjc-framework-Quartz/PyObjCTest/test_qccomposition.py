from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    expectedFailure,
    os_level_between,
)
import Quartz


class TestQCComposition(TestCase):
    def testConstants(self):
        self.assertIsInstance(Quartz.QCCompositionAttributeNameKey, str)
        self.assertIsInstance(Quartz.QCCompositionAttributeDescriptionKey, str)
        self.assertIsInstance(Quartz.QCCompositionAttributeCopyrightKey, str)

    @os_level_between("10.5", "10.13")
    def testConstants10_5_to_13(self):
        # Removed in 10.14
        self.assertIsInstance(Quartz.QCCompositionInputRSSFeedURLKey, str)
        self.assertIsInstance(Quartz.QCCompositionInputRSSArticleDurationKey, str)
        self.assertIsInstance(Quartz.QCCompositionProtocolRSSVisualizer, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
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

    @min_os_level("10.6")
    @expectedFailure
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.QCCompositionInputMeshKey, str)
        self.assertIsInstance(Quartz.QCCompositionOutputMeshKey, str)
        self.assertIsInstance(Quartz.QCCompositionProtocolMeshFilter, str)
