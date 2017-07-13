from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLTexture (TestCase):
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
            self.assertArgIsBOOL(ModelIO.MDLTexture.initWithData_topLeftOrigin_name_dimensions_rowStride_channelCount_channelEncoding_isCube_, 1)
            #self.assertArgIsBOOL(ModelIO.MDLTexture.initWithData_topLeftOrigin_name_dimensions_rowStride_channelCount_channelEncoding_isCube_, 7) # SIMD

            self.assertResultIsBOOL(ModelIO.MDLTexture.writeToURL_)
            self.assertResultIsBOOL(ModelIO.MDLTexture.writeToURL_type_)

            self.assertArgIsBOOL(ModelIO.MDLTexture.texelDataWithTopLeftOriginAtMipLevel_create_, 1)
            self.assertArgIsBOOL(ModelIO.MDLTexture.texelDataWithBottomLeftOriginAtMipLevel_create_, 1)

            self.assertResultIsBOOL(ModelIO.MDLTexture.isCube)
            self.assertArgIsBOOL(ModelIO.MDLTexture.setIsCube_, 0)


            #self.assertArgIsBOOL(ModelIO.MDLNoiseTexture.initScalarNoiseWithSmoothness_name_textureDimensions_channelCount_channelEncoding_grayscale_, 5) # SIMD

        @min_os_level('10.12')
        def testMethods10_12(self):
            self.assertResultIsBOOL(ModelIO.MDLTexture.hasAlphaValues)
            self.assertArgIsBOOL(ModelIO.MDLTexture.setHasAlphaValues_, 0)

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertResultIsBOOL(ModelIO.MDLTexture.writeToURL_level_)
            self.assertResultIsBOOL(ModelIO.MDLTexture.writeToURL_type_level_)

if __name__ == "__main__":
    main()
