import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import ColorSync

    class TestColorSyncProfile (TestCase):
        @min_os_level('10.13')
        def testCFType(self):
            self.assertIsCFType(ColorSync.ColorSyncProfileRef)
            self.assertIsCFType(ColorSync.ColorSyncMutableProfileRef)

        @min_os_level('10.13')
        def testFunctions(self):
            self.assertIsInstance(ColorSync.ColorSyncProfileGetTypeID(), (int, long))

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

            self.assertArgIsOut(ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 1)
            self.assertArgIsOut(ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 2)
            self.assertArgIsOut(ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 3)
            self.assertArgIsOut(ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 4)
            self.assertArgIsOut(ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 5)
            self.assertArgIsOut(ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 6)
            self.assertArgIsOut(ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 7)
            self.assertArgIsOut(ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 8)
            self.assertArgIsOut(ColorSync.ColorSyncProfileGetDisplayTransferFormulaFromVCGT, 9)

            self.assertArgIsIn(ColorSync.ColorSyncProfileCreateDisplayTransferTablesFromVCGT, 1)

            self.assertArgIsFunction(ColorSync.ColorSyncIterateInstalledProfiles, 0, objc._C_BOOL + b'^{__CFDictionary=}^v', False)
            self.assertArgIsInOut(ColorSync.ColorSyncIterateInstalledProfiles, 1)
            self.assertArgIsOut(ColorSync.ColorSyncIterateInstalledProfiles, 3)

            self.assertArgIsOut(ColorSync.ColorSyncProfileInstall, 3)
            self.assertArgIsOut(ColorSync.ColorSyncProfileUninstall, 1)


        @min_os_level('10.13')
        def testConstants(self):
            self.assertIsInstance(ColorSync.kColorSyncGenericGrayProfile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncGenericGrayGamma22Profile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncGenericRGBProfile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncGenericCMYKProfile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDisplayP3Profile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSRGBProfile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncAdobeRGB1998Profile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncGenericLabProfile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncGenericXYZProfile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncACESCGLinearProfile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDCIP3Profile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncITUR709Profile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncITUR2020Profile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncROMMRGBProfile, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileHeader, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileColorSpace, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfilePCS, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileURL, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileDescription, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileMD5Digest, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigAToB0Tag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigAToB1Tag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigAToB2Tag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigBToA0Tag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigBToA1Tag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigBToA2Tag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigCmykData, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigGrayData, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigLabData, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigRgbData, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigXYZData, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigAbstractClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigBlueTRCTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigBlueColorantTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigMediaBlackPointTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigCopyrightTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigProfileDescriptionTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigDeviceModelDescTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigDeviceMfgDescTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigGreenTRCTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigGreenColorantTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigGamutTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigGrayTRCTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigLinkClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigDisplayClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigNamedColor2Tag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigNamedColorClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigPreview0Tag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigPreview1Tag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigPreview2Tag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigOutputClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigProfileSequenceDescTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigRedTRCTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigRedColorantTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigInputClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigColorSpaceClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigTechnologyTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigViewingConditionsTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigViewingCondDescTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncSigMediaWhitePointTag, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileComputerDomain, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileUserDomain, unicode)

            self.assertEqual(ColorSync.COLORSYNC_PROFILE_INSTALL_ENTITLEMENT, b"com.apple.developer.ColorSync.profile.install")
            self.assertEqual(ColorSync.COLORSYNC_MD5_LENGTH, 16)

        def testStructs(self):
            v = ColorSync.ColorSyncMD5()
            self.assertTrue(hasattr(v, 'digest'))


if __name__ == "__main__":
    main()
