import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTVideoEncoderList(TestCase):
    def test_constants(self):
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_CodecType, str)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_EncoderID, str)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_CodecName, str)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_EncoderName, str)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_DisplayName, str)

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_GPURegistryID, str)
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderList_SupportedSelectionProperties, str
        )
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_PerformanceRating, str)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_QualityRating, str)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_InstanceLimit, str)
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderList_IsHardwareAccelerated, str
        )

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderList_SupportsFrameReordering, str
        )

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderListOption_IncludeStandardDefinitionDVEncoders,
            str,
        )

    def test_functions(self):
        self.assertArgIsOut(VideoToolbox.VTCopyVideoEncoderList, 1)
        self.assertArgIsCFRetained(VideoToolbox.VTCopyVideoEncoderList, 1)

    @min_os_level("10.13")
    def test_functions10_13(self):
        self.assertArgIsOut(VideoToolbox.VTCopySupportedPropertyDictionaryForEncoder, 4)
        self.assertArgIsCFRetained(
            VideoToolbox.VTCopySupportedPropertyDictionaryForEncoder, 4
        )
        self.assertArgIsOut(VideoToolbox.VTCopySupportedPropertyDictionaryForEncoder, 5)
        self.assertArgIsCFRetained(
            VideoToolbox.VTCopySupportedPropertyDictionaryForEncoder, 5
        )
