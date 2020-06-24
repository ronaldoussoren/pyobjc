import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCMMetadata(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_AllocationFailed, -16300)
        self.assertEqual(
            CoreMedia.kCMMetadataIdentifierError_RequiredParameterMissing, -16301
        )
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadKey, -16302)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadKeyLength, -16303)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadKeyType, -16304)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadNumberKey, -16305)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadKeySpace, -16306)
        self.assertEqual(CoreMedia.kCMMetadataIdentifierError_BadIdentifier, -16307)
        self.assertEqual(
            CoreMedia.kCMMetadataIdentifierError_NoKeyValueAvailable, -16308
        )

        self.assertEqual(
            CoreMedia.kCMMetadataDataTypeRegistryError_AllocationFailed, -16310
        )
        self.assertEqual(
            CoreMedia.kCMMetadataDataTypeRegistryError_RequiredParameterMissing, -16311
        )
        self.assertEqual(
            CoreMedia.kCMMetadataDataTypeRegistryError_BadDataTypeIdentifier, -16312
        )
        self.assertEqual(
            CoreMedia.kCMMetadataDataTypeRegistryError_DataTypeAlreadyRegistered, -16313
        )
        self.assertEqual(
            CoreMedia.kCMMetadataDataTypeRegistryError_RequiresConformingBaseType,
            -16314,
        )
        self.assertEqual(
            CoreMedia.kCMMetadataDataTypeRegistryError_MultipleConformingBaseTypes,
            -16315,
        )

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_QuickTimeUserData, str)
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_ISOUserData, str)
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_QuickTimeMetadata, str)
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_iTunes, str)
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_ID3, str)
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_Icy, str)
        self.assertIsInstance(
            CoreMedia.kCMMetadataIdentifier_QuickTimeMetadataLocation_ISO6709, str
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataIdentifier_QuickTimeMetadataDirection_Facing, str
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataIdentifier_QuickTimeMetadataPreferredAffineTransform,
            str,
        )

        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_RawData, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UTF8, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UTF16, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_GIF, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_JPEG, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_PNG, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_BMP, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_Float32, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_Float64, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_SInt8, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_SInt16, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_SInt32, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_SInt64, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UInt8, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UInt16, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UInt32, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_UInt64, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_PointF32, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_DimensionsF32, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_AffineTransformF64, str)
        self.assertIsInstance(
            CoreMedia.kCMMetadataDataType_QuickTimeMetadataLocation_ISO6709, str
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataDataType_QuickTimeMetadataDirection, str
        )

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(
            CoreMedia.kCMMetadataIdentifier_QuickTimeMetadataVideoOrientation, str
        )

        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_PolygonF32, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_PolylineF32, str)
        self.assertIsInstance(CoreMedia.kCMMetadataBaseDataType_JSON, str)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(CoreMedia.kCMMetadataKeySpace_HLSDateRange, str)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            CoreMedia.kCMMetadataIdentifier_QuickTimeMetadataLivePhotoStillImageTransform,
            str,
        )
        self.assertIsInstance(
            CoreMedia.kCMMetadataBaseDataType_PerspectiveTransformF64, str
        )

    @min_os_level("10.15.1")
    def test_constants10_15_1(self):
        self.assertIsInstance(
            CoreMedia.kCMMetadataIdentifier_QuickTimeMetadataLivePhotoStillImageTransformReferenceDimensions,
            str,
        )

    @min_os_level("10.10")
    def test_functions10_10(self):
        self.assertArgIsOut(CoreMedia.CMMetadataCreateIdentifierForKeyAndKeySpace, 3)
        self.assertArgIsCFRetained(
            CoreMedia.CMMetadataCreateIdentifierForKeyAndKeySpace, 3
        )

        self.assertArgIsOut(CoreMedia.CMMetadataCreateKeyFromIdentifier, 2)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataCreateKeyFromIdentifier, 2)

        self.assertArgIsOut(CoreMedia.CMMetadataCreateKeyFromIdentifierAsCFData, 2)
        self.assertArgIsCFRetained(
            CoreMedia.CMMetadataCreateKeyFromIdentifierAsCFData, 2
        )

        self.assertArgIsOut(CoreMedia.CMMetadataCreateKeySpaceFromIdentifier, 2)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataCreateKeySpaceFromIdentifier, 2)

        CoreMedia.CMMetadataDataTypeRegistryRegisterDataType

        self.assertResultIsBOOL(
            CoreMedia.CMMetadataDataTypeRegistryDataTypeIsRegistered
        )

        CoreMedia.CMMetadataDataTypeRegistryGetDataTypeDescription
        CoreMedia.CMMetadataDataTypeRegistryGetConformingDataTypes

        self.assertResultIsBOOL(
            CoreMedia.CMMetadataDataTypeRegistryDataTypeConformsToDataType
        )

        CoreMedia.CMMetadataDataTypeRegistryGetBaseDataTypes

        self.assertResultIsBOOL(
            CoreMedia.CMMetadataDataTypeRegistryDataTypeIsBaseDataType
        )

        CoreMedia.CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType
