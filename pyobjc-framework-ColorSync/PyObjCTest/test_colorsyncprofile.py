from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import ColorSync


class TestColorSyncProfile(TestCase):
    @min_os_level("10.13")
    def testCFType(self):
        self.assertIsCFType(ColorSync.ColorSyncProfileRef)
        self.assertIsCFType(ColorSync.ColorSyncMutableProfileRef)

    @min_os_level("10.4")
    def testFunctions10_4(self):
        self.assertResultHasType(ColorSync.ColorSyncProfileIsWideGamut, objc._C_BOOL)

    @min_os_level("10.13")
    def testFunctions10_13(self):
        self.assertIsInstance(ColorSync.ColorSyncProfileGetTypeID(), int)

        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCreate)
        self.assertArgIsOut(ColorSync.ColorSyncProfileCreate, 1)

        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCreateWithURL)
        self.assertArgIsOut(ColorSync.ColorSyncProfileCreateWithURL, 1)

        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCreateWithName)
        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCreateWithName)
        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCreateDeviceProfile)
        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCreateMutable)
        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCreateMutableCopy)
        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCreateLink)

        self.assertArgIsOut(ColorSync.ColorSyncProfileVerify, 1)
        self.assertArgIsOut(ColorSync.ColorSyncProfileVerify, 2)

        self.assertArgIsOut(ColorSync.ColorSyncProfileEstimateGammaWithDisplayID, 1)
        self.assertArgIsOut(ColorSync.ColorSyncProfileEstimateGamma, 1)

        ColorSync.ColorSyncProfileGetMD5

        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCopyData)
        self.assertArgIsOut(ColorSync.ColorSyncProfileCopyData, 1)

        ColorSync.ColorSyncProfileGetURL

        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCopyHeader)

        ColorSync.ColorSyncProfileSetHeader

        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCopyDescriptionString)
        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCopyTagSignatures)

        ColorSync.ColorSyncProfileContainsTag

        self.assertResultIsCFRetained(ColorSync.ColorSyncProfileCopyTag)

        ColorSync.ColorSyncProfileSetTag
        ColorSync.ColorSyncProfileRemoveTag

        self.assertArgIsOut(
            ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 1
        )
        self.assertArgIsOut(
            ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 2
        )
        self.assertArgIsOut(
            ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 3
        )
        self.assertArgIsOut(
            ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 4
        )
        self.assertArgIsOut(
            ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 5
        )
        self.assertArgIsOut(
            ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 6
        )
        self.assertArgIsOut(
            ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 7
        )
        self.assertArgIsOut(
            ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 8
        )
        self.assertArgIsOut(
            ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 9
        )

        self.assertArgIsIn(
            ColorSync.ColorSyncProfileCreateDisplayTransferTablesFromVCGT, 1
        )

        self.assertArgIsFunction(
            ColorSync.ColorSyncIterateInstalledProfiles,
            0,
            objc._C_BOOL + b"^{__CFDictionary=}^v",
            False,
        )
        self.assertArgIsInOut(ColorSync.ColorSyncIterateInstalledProfiles, 1)
        self.assertArgIsOut(ColorSync.ColorSyncIterateInstalledProfiles, 3)

        self.assertArgIsInOut(ColorSync.ColorSyncIterateInstalledProfilesWithOptions, 1)
        self.assertArgIsOut(ColorSync.ColorSyncIterateInstalledProfilesWithOptions, 4)

        self.assertArgIsOut(ColorSync.ColorSyncProfileInstall, 3)
        self.assertArgIsOut(ColorSync.ColorSyncProfileUninstall, 1)

        self.assertArgIsInOut(ColorSync.ColorSyncIterateInstalledProfiles, 1)
        self.assertArgIsOut(ColorSync.ColorSyncIterateInstalledProfiles, 3)

        self.assertArgIsInOut(ColorSync.ColorSyncIterateInstalledProfilesWithOptions, 1)
        self.assertArgIsOut(ColorSync.ColorSyncIterateInstalledProfilesWithOptions, 4)

    @min_os_level("11.0")
    def testFunctions11_0(self):
        self.assertResultHasType(ColorSync.ColorSyncProfileIsMatrixBased, objc._C_BOOL)

    @min_os_level("12.0")
    def testFunctions12_0(self):
        self.assertResultHasType(ColorSync.ColorSyncProfileIsPQBased, objc._C_BOOL)
        self.assertResultHasType(ColorSync.ColorSyncProfileIsHLGBased, objc._C_BOOL)

    @min_os_level("10.13")
    def testConstants(self):
        self.assertEqual(ColorSync.icVersion4Number, 0x04000000)
        self.assertIsInstance(ColorSync.kColorSyncGenericGrayProfile, str)
        self.assertIsInstance(ColorSync.kColorSyncGenericGrayGamma22Profile, str)
        self.assertIsInstance(ColorSync.kColorSyncGenericRGBProfile, str)
        self.assertIsInstance(ColorSync.kColorSyncGenericCMYKProfile, str)
        self.assertIsInstance(ColorSync.kColorSyncDisplayP3Profile, str)
        self.assertIsInstance(ColorSync.kColorSyncSRGBProfile, str)
        self.assertIsInstance(ColorSync.kColorSyncAdobeRGB1998Profile, str)
        self.assertIsInstance(ColorSync.kColorSyncGenericLabProfile, str)
        self.assertIsInstance(ColorSync.kColorSyncGenericXYZProfile, str)
        self.assertIsInstance(ColorSync.kColorSyncACESCGLinearProfile, str)
        self.assertIsInstance(ColorSync.kColorSyncDCIP3Profile, str)
        self.assertIsInstance(ColorSync.kColorSyncITUR709Profile, str)
        self.assertIsInstance(ColorSync.kColorSyncITUR2020Profile, str)
        self.assertIsInstance(ColorSync.kColorSyncROMMRGBProfile, str)
        self.assertIsInstance(ColorSync.kColorSyncProfileHeader, str)
        self.assertIsInstance(ColorSync.kColorSyncProfileClass, str)
        self.assertIsInstance(ColorSync.kColorSyncProfileColorSpace, str)
        self.assertIsInstance(ColorSync.kColorSyncProfilePCS, str)
        self.assertIsInstance(ColorSync.kColorSyncProfileURL, str)
        self.assertIsInstance(ColorSync.kColorSyncProfileDescription, str)
        self.assertIsInstance(ColorSync.kColorSyncProfileMD5Digest, str)
        self.assertIsInstance(ColorSync.kColorSyncSigAToB0Tag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigAToB1Tag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigAToB2Tag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigBToA0Tag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigBToA1Tag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigBToA2Tag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigCmykData, str)
        self.assertIsInstance(ColorSync.kColorSyncSigGrayData, str)
        self.assertIsInstance(ColorSync.kColorSyncSigLabData, str)
        self.assertIsInstance(ColorSync.kColorSyncSigRgbData, str)
        self.assertIsInstance(ColorSync.kColorSyncSigXYZData, str)
        self.assertIsInstance(ColorSync.kColorSyncSigAbstractClass, str)
        self.assertIsInstance(ColorSync.kColorSyncSigBlueTRCTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigBlueColorantTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigMediaBlackPointTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigCopyrightTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigProfileDescriptionTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigDeviceModelDescTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigDeviceMfgDescTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigGreenTRCTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigGreenColorantTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigGamutTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigGrayTRCTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigLinkClass, str)
        self.assertIsInstance(ColorSync.kColorSyncSigDisplayClass, str)
        self.assertIsInstance(ColorSync.kColorSyncSigNamedColor2Tag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigNamedColorClass, str)
        self.assertIsInstance(ColorSync.kColorSyncSigPreview0Tag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigPreview1Tag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigPreview2Tag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigOutputClass, str)
        self.assertIsInstance(ColorSync.kColorSyncSigProfileSequenceDescTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigRedTRCTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigRedColorantTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigInputClass, str)
        self.assertIsInstance(ColorSync.kColorSyncSigColorSpaceClass, str)
        self.assertIsInstance(ColorSync.kColorSyncSigTechnologyTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigViewingConditionsTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigViewingCondDescTag, str)
        self.assertIsInstance(ColorSync.kColorSyncSigMediaWhitePointTag, str)
        self.assertIsInstance(ColorSync.kColorSyncProfileComputerDomain, str)
        self.assertIsInstance(ColorSync.kColorSyncProfileUserDomain, str)

        self.assertEqual(
            ColorSync.COLORSYNC_PROFILE_INSTALL_ENTITLEMENT,
            b"com.apple.developer.ColorSync.profile.install",
        )
        self.assertEqual(ColorSync.COLORSYNC_MD5_LENGTH, 16)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(ColorSync.kColorSyncProfileCacheSeed, str)
        self.assertIsInstance(ColorSync.kColorSyncWaitForCacheReply, str)
        self.assertIsInstance(ColorSync.kColorSyncWaitForCacheReply, str)

    @min_os_level("13.0")
    def testConstants13_0(self):
        self.assertIsInstance(ColorSync.kColorSyncProfileIsValid, str)
        self.assertIsInstance(ColorSync.kColorSyncWebSafeColorsProfile, str)

    def testStructs(self):
        v = ColorSync.ColorSyncMD5()
        self.assertTrue(hasattr(v, "digest"))
        self.assertPickleRoundTrips(v)
