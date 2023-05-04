from PyObjCTools.TestSupport import TestCase, min_os_level
import ModelIO
from objc import simd


class TestMDLTexture(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ModelIO.MDLTextureChannelEncoding)

    def testConstants(self):
        self.assertEqual(ModelIO.MDLTextureChannelEncodingUInt8, 1)
        self.assertEqual(ModelIO.MDLTextureChannelEncodingUint8, 1)
        self.assertEqual(ModelIO.MDLTextureChannelEncodingUInt16, 2)
        self.assertEqual(ModelIO.MDLTextureChannelEncodingUint16, 2)
        self.assertEqual(ModelIO.MDLTextureChannelEncodingUInt24, 3)
        self.assertEqual(ModelIO.MDLTextureChannelEncodingUint24, 3)
        self.assertEqual(ModelIO.MDLTextureChannelEncodingUInt32, 4)
        self.assertEqual(ModelIO.MDLTextureChannelEncodingUint32, 4)
        self.assertEqual(ModelIO.MDLTextureChannelEncodingFloat16, 0x102)
        self.assertEqual(ModelIO.MDLTextureChannelEncodingFloat16SR, 0x302)
        self.assertEqual(ModelIO.MDLTextureChannelEncodingFloat32, 0x104)

    def testMethods(self):
        self.assertArgIsBOOL(
            ModelIO.MDLTexture.initWithData_topLeftOrigin_name_dimensions_rowStride_channelCount_channelEncoding_isCube_,
            1,
        )
        self.assertArgHasType(
            ModelIO.MDLTexture.initWithData_topLeftOrigin_name_dimensions_rowStride_channelCount_channelEncoding_isCube_,
            3,
            simd.vector_int2.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLTexture.initWithData_topLeftOrigin_name_dimensions_rowStride_channelCount_channelEncoding_isCube_,
            7,
        )

        self.assertResultIsBOOL(ModelIO.MDLTexture.writeToURL_)
        self.assertResultIsBOOL(ModelIO.MDLTexture.writeToURL_type_)

        self.assertArgIsBOOL(
            ModelIO.MDLTexture.texelDataWithTopLeftOriginAtMipLevel_create_, 1
        )
        self.assertArgIsBOOL(
            ModelIO.MDLTexture.texelDataWithBottomLeftOriginAtMipLevel_create_, 1
        )

        self.assertResultIsBOOL(ModelIO.MDLTexture.isCube)
        self.assertArgIsBOOL(ModelIO.MDLTexture.setIsCube_, 0)

        self.assertArgHasType(
            ModelIO.MDLNoiseTexture.initVectorNoiseWithSmoothness_name_textureDimensions_channelEncoding_,
            2,
            simd.vector_int2.__typestr__,
        )

        self.assertArgHasType(
            ModelIO.MDLNoiseTexture.initScalarNoiseWithSmoothness_name_textureDimensions_channelCount_channelEncoding_grayscale_,
            2,
            simd.vector_int2.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLNoiseTexture.initScalarNoiseWithSmoothness_name_textureDimensions_channelCount_channelEncoding_grayscale_,
            5,
        )

        self.assertResultHasType(
            ModelIO.MDLTexture.dimensions, simd.vector_int2.__typestr__
        )

        self.assertArgHasType(
            ModelIO.MDLTexture.irradianceTextureCubeWithTexture_name_dimensions_,
            2,
            simd.vector_int2.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLTexture.irradianceTextureCubeWithTexture_name_dimensions_roughness_,
            2,
            simd.vector_int2.__typestr__,
        )

        self.assertArgHasType(
            ModelIO.MDLCheckerboardTexture.initWithDivisions_name_dimensions_channelCount_channelEncoding_color1_color2_,
            2,
            simd.vector_int2.__typestr__,
        )

        self.assertResultHasType(
            ModelIO.MDLSkyCubeTexture.highDynamicRangeCompression,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLSkyCubeTexture.setHighDynamicRangeCompression_,
            0,
            simd.vector_float2.__typestr__,
        )

        self.assertArgHasType(
            ModelIO.MDLColorSwatchTexture.initWithColorTemperatureGradientFrom_toColorTemperature_name_textureDimensions_,
            3,
            simd.vector_int2.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLColorSwatchTexture.initWithColorGradientFrom_toColor_name_textureDimensions_,
            3,
            simd.vector_int2.__typestr__,
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(ModelIO.MDLTexture.hasAlphaValues)
        self.assertArgIsBOOL(ModelIO.MDLTexture.setHasAlphaValues_, 0)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgHasType(
            ModelIO.MDLSkyCubeTexture.initWithName_channelEncoding_textureDimensions_turbidity_sunElevation_upperAtmosphereScattering_groundAlbedo_,
            2,
            simd.vector_int2.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLSkyCubeTexture.initWithName_channelEncoding_textureDimensions_turbidity_sunElevation_sunAzimuth_upperAtmosphereScattering_groundAlbedo_,
            2,
            simd.vector_int2.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLNoiseTexture.initCellularNoiseWithFrequency_name_textureDimensions_channelEncoding_,
            2,
            simd.vector_int2.__typestr__,
        )
        self.assertResultIsBOOL(ModelIO.MDLTexture.writeToURL_level_)
        self.assertResultIsBOOL(ModelIO.MDLTexture.writeToURL_type_level_)
