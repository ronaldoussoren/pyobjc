from PyObjCTools.TestSupport import *
import VideoToolbox


class TestVTVideoEncoderList(TestCase):
    def test_constants(self):
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_CodecType, unicode)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_EncoderID, unicode)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_CodecName, unicode)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_EncoderName, unicode)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_DisplayName, unicode)

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_GPURegistryID, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderList_SupportedSelectionProperties, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderList_PerformanceRating, unicode
        )
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_QualityRating, unicode)
        self.assertIsInstance(VideoToolbox.kVTVideoEncoderList_InstanceLimit, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderList_IsHardwareAccelerated, unicode
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


if __name__ == "__main__":
    main()
