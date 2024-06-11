import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTUtilities(TestCase):
    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsTypedEnum(VideoToolbox.VTDecoderExtensionPropertiesKey, str)
        self.assertIsInstance(
            VideoToolbox.kVTDecoderExtensionProperties_ExtensionNameKey, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecoderExtensionProperties_ContainingBundleNameKey, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecoderExtensionProperties_ExtensionURLKey, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTDecoderExtensionProperties_ContainingBundleURLKey, str
        )

    @min_os_level("10.11")
    def test_functions(self):
        self.assertArgIsOut(VideoToolbox.VTCreateCGImageFromCVPixelBuffer, 2)
        self.assertArgIsCFRetained(VideoToolbox.VTCreateCGImageFromCVPixelBuffer, 2)

    @min_os_level("11.0")
    def test_functions11_0(self):
        VideoToolbox.VTRegisterSupplementalVideoDecoderIfAvailable

    @min_os_level("15.0")
    def test_functions15_0(self):
        self.assertArgIsOut(VideoToolbox.VTCopyVideoDecoderExtensionProperties, 1)
        self.assertArgIsCFRetained(
            VideoToolbox.VTCopyVideoDecoderExtensionProperties, 1
        )
