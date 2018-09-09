from PyObjCTools.TestSupport import *
import VideoToolbox

class TestVTSession (TestCase):
    @expectedFailure
    @min_os_level('10.10')
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTSessionRef)

    def test_constants(self):
        self.assertIsInstance(VideoToolbox.kVTPropertyTypeKey, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertyType_Enumeration, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertyType_Boolean, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertyType_Number, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertyReadWriteStatusKey, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertyReadWriteStatus_ReadOnly, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertyReadWriteStatus_ReadWrite, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertyShouldBeSerializedKey, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertySupportedValueMinimumKey, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertySupportedValueMaximumKey, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertySupportedValueListKey, unicode)
        self.assertIsInstance(VideoToolbox.kVTPropertyDocumentationKey, unicode)

    def test_functions(self):
        self.assertArgIsOut(VideoToolbox.VTSessionCopySupportedPropertyDictionary, 1)
        self.assertArgIsCFRetained(VideoToolbox.VTSessionCopySupportedPropertyDictionary, 1)

        self.assertArgHasType(VideoToolbox.VTSessionSetProperty, 2, objc._C_ID)

        self.assertArgIsOut(VideoToolbox.VTSessionCopyProperty, 3)
        self.assertArgHasType(VideoToolbox.VTSessionCopyProperty, 3, b"o^@")
        self.assertArgIsCFRetained(VideoToolbox.VTSessionCopyProperty, 3)

        VideoToolbox.VTSessionSetProperties

        self.assertArgIsOut(VideoToolbox.VTSessionCopySerializableProperties, 2)
        self.assertArgIsCFRetained(VideoToolbox.VTSessionCopySerializableProperties, 2)


if __name__ == "__main__":
    main()
