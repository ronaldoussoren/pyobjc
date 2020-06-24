from PyObjCTools.TestSupport import TestCase, min_os_level, max_os_level
import ColorSync


class TestColorSyncTransform(TestCase):
    @min_os_level("10.13")
    def testCFType(self):
        self.assertIsCFType(ColorSync.ColorSyncTransformRef)

    @min_os_level("10.13")
    def testFunctions(self):
        self.assertIsInstance(ColorSync.ColorSyncTransformGetTypeID(), int)

        self.assertResultIsCFRetained(ColorSync.ColorSyncTransformCreate)
        self.assertResultIsCFRetained(ColorSync.ColorSyncTransformCopyProperty)
        ColorSync.ColorSyncTransformSetProperty

        self.assertArgIsOut(ColorSync.ColorSyncTransformConvert, 3)
        self.assertArgIsVariableSize(ColorSync.ColorSyncTransformConvert, 3)
        self.assertArgIsIn(ColorSync.ColorSyncTransformConvert, 7)
        self.assertArgIsVariableSize(ColorSync.ColorSyncTransformConvert, 7)

    @min_os_level("10.13")
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

        self.assertIsInstance(ColorSync.kColorSyncProfile, str)
        self.assertIsInstance(ColorSync.kColorSyncRenderingIntent, str)
        self.assertIsInstance(ColorSync.kColorSyncRenderingIntentPerceptual, str)
        self.assertIsInstance(ColorSync.kColorSyncRenderingIntentRelative, str)
        self.assertIsInstance(ColorSync.kColorSyncRenderingIntentSaturation, str)
        self.assertIsInstance(ColorSync.kColorSyncRenderingIntentAbsolute, str)
        self.assertIsInstance(ColorSync.kColorSyncRenderingIntentUseProfileHeader, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformTag, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformDeviceToPCS, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformPCSToPCS, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformPCSToDevice, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformDeviceToDevice, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformGamutCheck, str)
        self.assertIsInstance(ColorSync.kColorSyncBlackPointCompensation, str)
        self.assertIsInstance(ColorSync.kColorSyncPreferredCMM, str)
        self.assertIsInstance(ColorSync.kColorSyncConvertQuality, str)
        self.assertIsInstance(ColorSync.kColorSyncBestQuality, str)
        self.assertIsInstance(ColorSync.kColorSyncNormalQuality, str)
        self.assertIsInstance(ColorSync.kColorSyncDraftQuality, str)
        self.assertIsInstance(ColorSync.kColorSyncConvertThreadCount, str)
        self.assertIsInstance(ColorSync.kColorSyncConvertUseVectorUnit, str)
        self.assertIsInstance(ColorSync.kColorSyncConvertUseExtendedRange, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformCreator, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformSrcSpace, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformDstSpace, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformCodeFragmentType, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformCodeFragmentMD5, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformFullConversionData, str)
        self.assertIsInstance(
            ColorSync.kColorSyncTransformSimplifiedConversionData, str
        )
        self.assertIsInstance(
            ColorSync.kColorSyncTransformParametricConversionData, str
        )
        self.assertIsInstance(ColorSync.kColorSyncConversionMatrix, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionParamCurve0, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionParamCurve1, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionParamCurve2, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionParamCurve3, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionParamCurve4, str)
        self.assertIsInstance(ColorSync.kColorSyncConversion1DLut, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionGridPoints, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionChannelID, str)
        self.assertIsInstance(ColorSync.kColorSyncConversion3DLut, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionNDLut, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionInpChan, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionOutChan, str)
        self.assertIsInstance(ColorSync.kColorSyncConversionBPC, str)
        self.assertIsInstance(ColorSync.kColorSyncFixedPointRange, str)

        self.assertIsInstance(ColorSync.kColorSyncTransformCreator, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformSrcSpace, str)
        self.assertIsInstance(ColorSync.kColorSyncTransformDstSpace, str)

    @min_os_level("10.13")
    @max_os_level("10.13")
    def testConstants10_13_only(self):
        self.assertIsInstance(ColorSync.kColorSyncTranformInfo, str)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(ColorSync.kColorSyncTransformInfo, str)

    @min_os_level("10.15")
    def testConstants10_16(self):
        # XXX: Header says available in 10.16
        self.assertIsInstance(ColorSync.kColorSyncExtendedRange, str)
