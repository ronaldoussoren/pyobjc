from PyObjCTools.TestSupport import TestCase, min_os_level

import VideoToolbox


class TestVTRAWProcessingProperties(TestCase):
    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsInstance(
            VideoToolbox.kVTRAWProcessingPropertyKey_MetalDeviceRegistryID, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTRAWProcessingPropertyKey_MetalDeviceRegistryID, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTRAWProcessingPropertyKey_OutputColorAttachments, str
        )
