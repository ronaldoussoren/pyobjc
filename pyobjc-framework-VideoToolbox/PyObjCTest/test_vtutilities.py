import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTUtilities(TestCase):
    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsTypedEnum(VideoToolbox.VTExtensionPropertiesKey, str)
        self.assertIsInstance(VideoToolbox.kVTExtensionProperties_ExtensionNameKey, str)
        self.assertIsInstance(
            VideoToolbox.kVTExtensionProperties_ContainingBundleNameKey, str
        )
        self.assertIsInstance(VideoToolbox.kVTExtensionProperties_ExtensionURLKey, str)
        self.assertIsInstance(
            VideoToolbox.kVTExtensionProperties_ContainingBundleURLKey, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTExtensionProperties_ExtensionIdentifierKey, str
        )
        self.assertIsInstance(VideoToolbox.kVTExtensionProperties_CodecNameKey, str)

    @min_os_level("10.11")
    def test_functions(self):
        self.assertArgIsOut(VideoToolbox.VTCreateCGImageFromCVPixelBuffer, 2)
        self.assertArgIsCFRetained(VideoToolbox.VTCreateCGImageFromCVPixelBuffer, 2)

    @min_os_level("11.0")
    def test_functions11_0(self):
        VideoToolbox.VTRegisterSupplementalVideoDecoderIfAvailable

    @min_os_level("15.0")
    def test_functions15_0(self):
        self.assertArgIsOut(VideoToolbox.VTCopyRAWProcessorExtensionProperties, 1)
        self.assertArgIsCFRetained(VideoToolbox.VTCopyRAWProcessorExtensionProperties, 1)

        self.assertArgIsOut(VideoToolbox.VTCopyVideoDecoderExtensionProperties, 1)
        self.assertArgIsCFRetained(VideoToolbox.VTCopyVideoDecoderExtensionProperties, 1)
