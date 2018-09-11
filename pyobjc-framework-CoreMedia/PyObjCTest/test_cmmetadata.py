from PyObjCTools.TestSupport import *

import CoreMedia

class TestCMMetadata (TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_AllocationFailed, -16300)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_RequiredParameterMissing, -16301)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadKey, -16302)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadKeyLength, -16303)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadKeyType, -16304)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadNumberKey, -16305)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadKeySpace, -16306)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadIdentifier, -16307)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_NoKeyValueAvailable, -16308)

        self.assertEqual(CoreMedia.kCMMetadataDataTypeRegistryError_AllocationFailed, -16310)
        self.assertEqual(CoreMedia.kCMMetadataDataTypeRegistryError_RequiredParameterMissing, -16311)
        self.assertEqual(CoreMedia.kCMMetadataDataTypeRegistryError_BadDataTypeIdentifier, -16312)
        self.assertEqual(CoreMedia.kCMMetadataDataTypeRegistryError_DataTypeAlreadyRegistered, -16313)
        self.assertEqual(CoreMedia.kCMMetadataDataTypeRegistryError_RequiresConformingBaseType, -16314)
        self.assertEqual(CoreMedia.kCMMetadataDataTypeRegistryError_MultipleConformingBaseTypes, -16315)

    @min_os_level('10.10')
    def test_constants10_10(self):
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_QuickTimeUserData, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_ISOUserData, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_QuickTimeMetadata, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_iTunes, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_ID3, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_Icy, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataIdentifier_QuickTimeMetadataLocation_ISO6709, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataIdentifier_QuickTimeMetadataDirection_Facing, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataIdentifier_QuickTimeMetadataPreferredAffineTransform, unicode)

        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_RawData, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UTF8, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UTF16, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_GIF, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_JPEG, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_PNG, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_BMP, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_Float32, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_Float64, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_SInt8, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_SInt16, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_SInt32, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_SInt64, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UInt8, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UInt16, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UInt32, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UInt64, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_PointF32, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_DimensionsF32, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_AffineTransformF64, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataDataType_QuickTimeMetadataLocation_ISO6709, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataDataType_QuickTimeMetadataDirection, unicode)

    @min_os_level('10.11')
    def test_constants10_11(self):
        self.assertIsInstance(CoreMedia.kCMMetadataIdentifier_QuickTimeMetadataVideoOrientation, unicode)

        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_PolygonF32, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_PolylineF32, unicode)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_JSON, unicode)

    @min_os_level('10.13')
    def test_constants10_13(self):
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_HLSDateRange, unicode)

    @min_os_level('10.10')
    def test_functions10_10(self):
        self.assertArgIsOut(CoreMedia.CMMetadataCreateIdentifierForKeyAndKeySpace, 3)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataCreateIdentifierForKeyAndKeySpace, 3)

        self.assertArgIsOut(CoreMedia.CMMetadataCreateKeyFromIdentifier, 2)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataCreateKeyFromIdentifier, 2)

        self.assertArgIsOut(CoreMedia.CMMetadataCreateKeyFromIdentifierAsCFData, 2)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataCreateKeyFromIdentifierAsCFData, 2)

        self.assertArgIsOut(CoreMedia.CMMetadataCreateKeySpaceFromIdentifier, 2)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataCreateKeySpaceFromIdentifier, 2)

        CoreMedia.CMMetadataDataTypeRegistryRegisterDataType

        self.assertResultIsBOOL(CoreMedia.CMMetadataDataTypeRegistryDataTypeIsRegistered)

        CoreMedia.CMMetadataDataTypeRegistryGetDataTypeDescription
        CoreMedia.CMMetadataDataTypeRegistryGetConformingDataTypes

        self.assertResultIsBOOL(CoreMedia.CMMetadataDataTypeRegistryDataTypeConformsToDataType)

        CoreMedia.CMMetadataDataTypeRegistryGetBaseDataTypes

        self.assertResultIsBOOL(CoreMedia.CMMetadataDataTypeRegistryDataTypeIsBaseDataType)

        CoreMedia.CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType


if __name__ == "__main__":
    main()
