import VideoToolbox
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestVTSession(TestCase):
    @expectedFailure
    @min_os_level("10.10")
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTSessionRef)

    def test_constants(self):
        self.assertIsInstance(VideoToolbox.kVTPropertyTypeKey, str)
        self.assertIsInstance(VideoToolbox.kVTPropertyType_Enumeration, str)
        self.assertIsInstance(VideoToolbox.kVTPropertyType_Boolean, str)
        self.assertIsInstance(VideoToolbox.kVTPropertyType_Number, str)
        self.assertIsInstance(VideoToolbox.kVTPropertyReadWriteStatusKey, str)
        self.assertIsInstance(VideoToolbox.kVTPropertyReadWriteStatus_ReadOnly, str)
        self.assertIsInstance(VideoToolbox.kVTPropertyReadWriteStatus_ReadWrite, str)
        self.assertIsInstance(VideoToolbox.kVTPropertyShouldBeSerializedKey, str)
        self.assertIsInstance(VideoToolbox.kVTPropertySupportedValueMinimumKey, str)
        self.assertIsInstance(VideoToolbox.kVTPropertySupportedValueMaximumKey, str)
        self.assertIsInstance(VideoToolbox.kVTPropertySupportedValueListKey, str)
        self.assertIsInstance(VideoToolbox.kVTPropertyDocumentationKey, str)

    def test_functions(self):
        self.assertArgIsOut(VideoToolbox.VTSessionCopySupportedPropertyDictionary, 1)
        self.assertArgIsCFRetained(
            VideoToolbox.VTSessionCopySupportedPropertyDictionary, 1
        )

        self.assertArgHasType(VideoToolbox.VTSessionSetProperty, 2, objc._C_ID)

        self.assertArgIsOut(VideoToolbox.VTSessionCopyProperty, 3)
        self.assertArgHasType(VideoToolbox.VTSessionCopyProperty, 3, b"o^@")
        self.assertArgIsCFRetained(VideoToolbox.VTSessionCopyProperty, 3)

        VideoToolbox.VTSessionSetProperties

        self.assertArgIsOut(VideoToolbox.VTSessionCopySerializableProperties, 2)
        self.assertArgIsCFRetained(VideoToolbox.VTSessionCopySerializableProperties, 2)
