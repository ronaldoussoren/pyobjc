import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import ColorSync

    class TestColorSyncTransform (TestCase):
        @min_os_level('10.13')
        def testCFType(self):
            self.assertIsCFType(ColorSync.ColorSyncTransformRef)

        @min_os_level('10.13')
        def testFunctions(self):
            self.assertIsInstance(ColorSync.ColorSyncTransformGetTypeID(), (int, long))

            self.assertResultIsCFRetained(ColorSync.ColorSyncTransformCreate)
            self.assertResultIsCFRetained(ColorSync.ColorSyncTransformCopyProperty)
            ColorSync.ColorSyncTransformSetProperty

            self.assertArgIsOut(ColorSync.ColorSyncTransformConvert, 3)
            self.assertArgIsVariableSize(ColorSync.ColorSyncTransformConvert, 3)
            self.assertArgIsIn(ColorSync.ColorSyncTransformConvert, 7)
            self.assertArgIsVariableSize(ColorSync.ColorSyncTransformConvert, 7)


        @min_os_level('10.13')
        def testConstants(self):
            self.assertEqual(ColorSync.kColorSync1BitGamut, 1)
            self.assertEqual(ColorSync.kColorSync8BitInteger, 2)
            self.assertEqual(ColorSync.kColorSync16BitInteger, 3)
            self.assertEqual(ColorSync.kColorSync16BitFloat, 4)
            self.assertEqual(ColorSync.kColorSync32BitInteger, 5)
            self.assertEqual(ColorSync.kColorSync32BitNamedColorIndex, 6)
            self.assertEqual(ColorSync.kColorSync32BitFloat, 7)
            self.assertEqual(ColorSync.kColorSync10BitInteger, 8)

            self.assertEqual(ColorSync.kColorSyncAlphaNone, 0)
            self.assertEqual(ColorSync.kColorSyncAlphaPremultipliedLast, 1)
            self.assertEqual(ColorSync.kColorSyncAlphaPremultipliedFirst, 2)
            self.assertEqual(ColorSync.kColorSyncAlphaLast, 3)
            self.assertEqual(ColorSync.kColorSyncAlphaFirst, 4)
            self.assertEqual(ColorSync.kColorSyncAlphaNoneSkipLast, 5)
            self.assertEqual(ColorSync.kColorSyncAlphaNoneSkipFirst, 6)

            self.assertEqual(ColorSync.kColorSyncAlphaInfoMask, 0x1F)
            self.assertEqual(ColorSync.kColorSyncByteOrderMask, 0x7000)
            self.assertEqual(ColorSync.kColorSyncByteOrderDefault, 0 << 12)
            self.assertEqual(ColorSync.kColorSyncByteOrder16Little, 1 << 12)
            self.assertEqual(ColorSync.kColorSyncByteOrder32Little, 2 << 12)
            self.assertEqual(ColorSync.kColorSyncByteOrder16Big, 3 << 12)
            self.assertEqual(ColorSync.kColorSyncByteOrder32Big, 4 << 12)

            self.assertIsInstance(ColorSync.kColorSyncProfile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncRenderingIntent, unicode)
            self.assertIsInstance(ColorSync.kColorSyncRenderingIntentPerceptual, unicode)
            self.assertIsInstance(ColorSync.kColorSyncRenderingIntentRelative, unicode)
            self.assertIsInstance(ColorSync.kColorSyncRenderingIntentSaturation, unicode)
            self.assertIsInstance(ColorSync.kColorSyncRenderingIntentAbsolute, unicode)
            self.assertIsInstance(ColorSync.kColorSyncRenderingIntentUseProfileHeader, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformDeviceToPCS, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformPCSToPCS, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformPCSToDevice, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformDeviceToDevice, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformGamutCheck, unicode)
            self.assertIsInstance(ColorSync.kColorSyncBlackPointCompensation, unicode)
            self.assertIsInstance(ColorSync.kColorSyncPreferredCMM, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConvertQuality, unicode)
            self.assertIsInstance(ColorSync.kColorSyncBestQuality, unicode)
            self.assertIsInstance(ColorSync.kColorSyncNormalQuality, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDraftQuality, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConvertThreadCount, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConvertUseVectorUnit, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConvertUseExtendedRange, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformCreator, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformSrcSpace, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformDstSpace, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformCodeFragmentType, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformCodeFragmentMD5, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformFullConversionData, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformSimplifiedConversionData, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformParametricConversionData, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionMatrix, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionParamCurve0, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionParamCurve1, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionParamCurve2, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionParamCurve3, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionParamCurve4, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversion1DLut, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionGridPoints, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionChannelID, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversion3DLut, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionNDLut, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionInpChan, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionOutChan, unicode)
            self.assertIsInstance(ColorSync.kColorSyncConversionBPC, unicode)
            self.assertIsInstance(ColorSync.kColorSyncFixedPointRange, unicode)

            self.assertIsInstance(ColorSync.kColorSyncTransformCreator, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformSrcSpace, unicode)
            self.assertIsInstance(ColorSync.kColorSyncTransformDstSpace, unicode)

        @min_os_level('10.13')
        @max_os_level('10.13')
        def testConstants10_13_only(self):
            self.assertIsInstance(ColorSync.kColorSyncTranformInfo, unicode)

        @min_os_level('10.14')
        def testConstants10_14(self):
            self.assertIsInstance(ColorSync.kColorSyncTransformInfo, unicode)

if __name__ == "__main__":
    main()
