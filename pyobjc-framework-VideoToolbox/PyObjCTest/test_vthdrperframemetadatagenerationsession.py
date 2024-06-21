import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTHDRPerFrameMetadataGenerationSession(TestCase):
    @min_os_level("15.0")
    def test_constants15_0(self):
        self.assertIsTypedEnum(
            VideoToolbox.VTHDRPerFrameMetadataGenerationHDRFormatType, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTHDRPerFrameMetadataGenerationHDRFormatType_DolbyVision, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTHDRPerFrameMetadataGenerationOptionsKey_HDRFormats, str
        )

    @min_os_level("15.0")
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTHDRPerFrameMetadataGenerationSessionRef)

    @min_os_level("15.0")
    def test_functions(self):
        VideoToolbox.VTHDRPerFrameMetadataGenerationSessionGetTypeID

        self.assertArgIsOut(
            VideoToolbox.VTHDRPerFrameMetadataGenerationSessionCreate, 3
        )
        self.assertArgIsCFRetained(
            VideoToolbox.VTHDRPerFrameMetadataGenerationSessionCreate, 3
        )

        self.assertArgIsBOOL(
            VideoToolbox.VTHDRPerFrameMetadataGenerationSessionAttachMetadata, 2
        )
