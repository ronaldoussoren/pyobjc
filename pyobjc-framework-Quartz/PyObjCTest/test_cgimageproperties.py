import Quartz
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    os_level_key,
    expectedFailureIf,
)


class TestCGImageProperties(TestCase):
    @min_os_level("10.14")
    def testFunctions(self):
        Quartz.CGImageSourceGetPrimaryImageIndex

    def testConstants(self):
        self.assertEqual(Quartz.IMAGEIO_PNG_NO_FILTERS, 0x00)
        self.assertEqual(Quartz.IMAGEIO_PNG_FILTER_NONE, 0x08)
        self.assertEqual(Quartz.IMAGEIO_PNG_FILTER_SUB, 0x10)
        self.assertEqual(Quartz.IMAGEIO_PNG_FILTER_UP, 0x20)
        self.assertEqual(Quartz.IMAGEIO_PNG_FILTER_AVG, 0x40)
        self.assertEqual(Quartz.IMAGEIO_PNG_FILTER_PAETH, 0x80)
        self.assertEqual(
            Quartz.IMAGEIO_PNG_ALL_FILTERS,
            Quartz.IMAGEIO_PNG_FILTER_NONE
            | Quartz.IMAGEIO_PNG_FILTER_SUB
            | Quartz.IMAGEIO_PNG_FILTER_UP
            | Quartz.IMAGEIO_PNG_FILTER_AVG
            | Quartz.IMAGEIO_PNG_FILTER_PAETH,
        )

        self.assertIsInstance(Quartz.kCGImagePropertyTIFFDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGIFDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyJFIFDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyRawDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFDictionary, str)

        self.assertIsInstance(Quartz.kCGImagePropertyFileSize, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPixelHeight, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPixelWidth, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDPIHeight, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDPIWidth, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDepth, str)
        self.assertIsInstance(Quartz.kCGImagePropertyOrientation, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIsFloat, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIsIndexed, str)
        self.assertIsInstance(Quartz.kCGImagePropertyHasAlpha, str)
        self.assertIsInstance(Quartz.kCGImagePropertyColorModel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyProfileName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyColorModelRGB, str)
        self.assertIsInstance(Quartz.kCGImagePropertyColorModelGray, str)
        self.assertIsInstance(Quartz.kCGImagePropertyColorModelCMYK, str)
        self.assertIsInstance(Quartz.kCGImagePropertyColorModelLab, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFCompression, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFPhotometricInterpretation, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFDocumentName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFImageDescription, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFMake, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFModel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFOrientation, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFXResolution, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFYResolution, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFResolutionUnit, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFSoftware, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFTransferFunction, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFDateTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFArtist, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFHostComputer, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFCopyright, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFWhitePoint, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFPrimaryChromaticities, str)
        self.assertIsInstance(Quartz.kCGImagePropertyJFIFVersion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyJFIFXDensity, str)
        self.assertIsInstance(Quartz.kCGImagePropertyJFIFYDensity, str)
        self.assertIsInstance(Quartz.kCGImagePropertyJFIFDensityUnit, str)
        self.assertIsInstance(Quartz.kCGImagePropertyJFIFIsProgressive, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifExposureTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifFNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifExposureProgram, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSpectralSensitivity, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifISOSpeedRatings, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifOECF, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifVersion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifDateTimeOriginal, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifDateTimeDigitized, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifComponentsConfiguration, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifCompressedBitsPerPixel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifShutterSpeedValue, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifApertureValue, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifBrightnessValue, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifExposureBiasValue, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifMaxApertureValue, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSubjectDistance, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifMeteringMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifLightSource, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifFlash, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifFocalLength, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSubjectArea, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifMakerNote, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifUserComment, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSubsecTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSubsecTimeOrginal, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSubsecTimeDigitized, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifFlashPixVersion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifColorSpace, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifPixelXDimension, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifPixelYDimension, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifRelatedSoundFile, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifFlashEnergy, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSpatialFrequencyResponse, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifFocalPlaneXResolution, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifFocalPlaneYResolution, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifFocalPlaneResolutionUnit, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSubjectLocation, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifExposureIndex, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSensingMethod, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifFileSource, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSceneType, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifCFAPattern, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifCustomRendered, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifExposureMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifWhiteBalance, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifDigitalZoomRatio, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifFocalLenIn35mmFilm, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSceneCaptureType, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifGainControl, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifContrast, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSaturation, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSharpness, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifDeviceSettingDescription, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSubjectDistRange, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifImageUniqueID, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifGamma, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGIFLoopCount, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGIFDelayTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGIFImageColorMap, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGIFHasGlobalColorMap, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGGamma, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGInterlaceType, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGXPixelsPerMeter, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGYPixelsPerMeter, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGsRGBIntent, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGChromaticities, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSVersion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSLatitudeRef, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSLatitude, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSLongitudeRef, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSLongitude, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSAltitudeRef, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSAltitude, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSTimeStamp, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSSatellites, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSStatus, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSMeasureMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDOP, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSSpeedRef, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSSpeed, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSTrackRef, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSTrack, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSImgDirectionRef, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSImgDirection, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSMapDatum, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDestLatitudeRef, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDestLatitude, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDestLongitudeRef, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDestLongitude, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDestBearingRef, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDestBearing, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDestDistanceRef, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDestDistance, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSProcessingMethod, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSAreaInformation, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDateStamp, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSDifferental, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCObjectTypeReference, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCObjectAttributeReference, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCObjectName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCEditStatus, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCEditorialUpdate, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCUrgency, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCSubjectReference, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCCategory, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCSupplementalCategory, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCFixtureIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCKeywords, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContentLocationCode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContentLocationName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCReleaseDate, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCReleaseTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExpirationDate, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExpirationTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCSpecialInstructions, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCActionAdvised, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCReferenceService, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCReferenceDate, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCReferenceNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCDateCreated, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCTimeCreated, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCDigitalCreationDate, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCDigitalCreationTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCOriginatingProgram, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCProgramVersion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCObjectCycle, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCByline, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCBylineTitle, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCCity, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCSubLocation, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCProvinceState, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCCountryPrimaryLocationCode, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCCountryPrimaryLocationName, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCOriginalTransmissionReference, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCHeadline, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCCredit, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCSource, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCCopyrightNotice, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContact, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCCaptionAbstract, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCWriterEditor, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCImageType, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCImageOrientation, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCLanguageIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCStarRating, str)

        self.assertEqual(Quartz.kCGImagePropertyOrientationUp, 1)
        self.assertEqual(Quartz.kCGImagePropertyOrientationUpMirrored, 2)
        self.assertEqual(Quartz.kCGImagePropertyOrientationDown, 3)
        self.assertEqual(Quartz.kCGImagePropertyOrientationDownMirrored, 4)
        self.assertEqual(Quartz.kCGImagePropertyOrientationLeftMirrored, 5)
        self.assertEqual(Quartz.kCGImagePropertyOrientationRight, 6)
        self.assertEqual(Quartz.kCGImagePropertyOrientationRightMirrored, 7)
        self.assertEqual(Quartz.kCGImagePropertyOrientationLeft, 8)

        self.assertEqual(Quartz.kCGImageTGACompressionNone, 0)
        self.assertEqual(Quartz.kCGImageTGACompressionRLE, 1)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(Quartz.kCGImagePropertyMakerCanonDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonDictionary, str)
        self.assertIsInstance(Quartz.kCGImageProperty8BIMDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGDictionary, str)
        self.assertIsInstance(Quartz.kCGImageProperty8BIMLayerNames, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGVersion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBackwardVersion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGUniqueCameraModel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGLocalizedCameraModel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGCameraSerialNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGLensInfo, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFDescription, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFFirmware, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFOwnerName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFImageName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFImageFileName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFReleaseMethod, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFReleaseTiming, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFRecordID, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFSelfTimingTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFCameraSerialNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFImageSerialNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFContinuousDrive, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFFocusMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFMeteringMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFShootingMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFLensModel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFLensMaxMM, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFLensMinMM, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFWhiteBalanceIndex, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFFlashExposureComp, str)
        self.assertIsInstance(Quartz.kCGImagePropertyCIFFMeasuredEV, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonISOSetting, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonColorMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonQuality, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonWhiteBalanceMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonSharpenMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonFocusMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonFlashSetting, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonISOSelection, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonFlashExposureComp, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonImageAdjustment, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonLensAdapter, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonLensType, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonLensInfo, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonFocusDistance, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonDigitalZoom, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonShootingMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonCameraSerialNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerNikonShutterCount, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerCanonOwnerName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerCanonCameraSerialNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerCanonImageSerialNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerCanonFlashExposureComp, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerCanonContinuousDrive, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerCanonLensModel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifAuxDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerCanonFirmware, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerCanonAspectRatioInfo, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifAuxLensInfo, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifAuxLensModel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifAuxSerialNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifAuxLensID, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifAuxLensSerialNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifAuxImageNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifAuxFlashCompensation, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifAuxOwnerName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifAuxFirmware, str)

    @min_os_level("10.5")
    @expectedFailureIf(os_release().rsplit(".", 1)[0] == "10.6")
    def testConstants10_5_bad_on_10_6(self):
        self.assertTrue(hasattr(Quartz, "kCGImagePropertyMakerMinoltaDictionary"))
        self.assertTrue(hasattr(Quartz, "kCGImagePropertyMakerFujiDictionary"))
        self.assertTrue(hasattr(Quartz, "kCGImagePropertyMakerOlympusDictionary"))
        self.assertTrue(hasattr(Quartz, "kCGImagePropertyMakerPentaxDictionary"))

        self.assertIsInstance(Quartz.kCGImagePropertyMakerMinoltaDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerFujiDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerOlympusDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyMakerPentaxDictionary, str)

    @min_os_level("10.7")
    def testConstants10_6(self):
        # Contants aren't actually available on OSX 10.6
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCCreatorContactInfo, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCRightsUsageTerms, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCScene, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContactInfoCity, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContactInfoCountry, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContactInfoAddress, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContactInfoPostalCode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContactInfoStateProvince, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContactInfoEmails, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContactInfoPhones, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCContactInfoWebURLs, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(Quartz.kCGImagePropertyGIFUnclampedDelayTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGAuthor, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGCopyright, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGCreationTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGDescription, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGModificationTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGSoftware, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGTitle, str)

    @min_os_level("10.7")
    @expectedFailureIf(os_level_key(os_release()) <= os_level_key("10.9"))
    def testConstants10_7_broken(self):
        # The constants in this testcase are defined in headers and documentation,
        # but aren't exported by the framework...
        self.assertIsInstance(Quartz.kCGImagePropertyExifCameraOwnerName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifBodySerialNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifLensSpecification, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifLensMake, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifLensModel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifLensSerialNumber, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Quartz.kCGImagePropertyOpenEXRDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyOpenEXRAspectRatio, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSensitivityType, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifStandardOutputSensitivity, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifRecommendedExposureIndex, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifISOSpeed, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifISOSpeedLatitudeyyy, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifISOSpeedLatitudezzz, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Quartz.kCGImagePropertyMakerAppleDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyAPNGLoopCount, str)
        self.assertIsInstance(Quartz.kCGImagePropertyAPNGDelayTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyAPNGUnclampedDelayTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGPSHPositioningError, str)
        self.assertIsInstance(Quartz.kCGImageProperty8BIMVersion, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFTileWidth, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFTileLength, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGCompressionFilter, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifSubsecTimeOriginal, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBlackLevel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGWhiteLevel, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGCalibrationIlluminant1, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGCalibrationIlluminant2, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGColorMatrix1, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGColorMatrix2, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGCameraCalibration1, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGCameraCalibration2, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGAsShotNeutral, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGAsShotWhiteXY, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBaselineExposure, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBaselineNoise, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBaselineSharpness, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGPrivateData, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGCameraCalibrationSignature, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyDNGProfileCalibrationSignature, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyDNGNoiseProfile, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGWarpRectilinear, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGWarpFisheye, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGFixVignetteRadial, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.kCGImagePropertyFileContentsDictionary, str)
        self.assertIsInstance(Quartz.kCGImageAuxiliaryDataTypeDepth, str)
        self.assertIsInstance(Quartz.kCGImageAuxiliaryDataTypeDisparity, str)

        self.assertIsInstance(Quartz.kCGImageAuxiliaryDataInfoData, str)
        self.assertIsInstance(Quartz.kCGImageAuxiliaryDataInfoDataDescription, str)
        self.assertIsInstance(Quartz.kCGImageAuxiliaryDataInfoMetadata, str)
        self.assertIsInstance(Quartz.kCGImagePropertyImageCount, str)
        self.assertIsInstance(Quartz.kCGImagePropertyWidth, str)
        self.assertIsInstance(Quartz.kCGImagePropertyHeight, str)
        self.assertIsInstance(Quartz.kCGImagePropertyBytesPerRow, str)
        self.assertIsInstance(Quartz.kCGImagePropertyNamedColorSpace, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPixelFormat, str)
        self.assertIsInstance(Quartz.kCGImagePropertyImages, str)
        self.assertIsInstance(Quartz.kCGImagePropertyThumbnailImages, str)
        self.assertIsInstance(Quartz.kCGImagePropertyAuxiliaryData, str)
        self.assertIsInstance(Quartz.kCGImagePropertyAuxiliaryDataType, str)

        # New definition in Xcode 10.14 SDK
        self.assertIsInstance(Quartz.kCGImagePropertyPrimaryImage, str)

        # New definition in Xcode 12.5 SDK
        self.assertIsInstance(Quartz.kCGImagePropertyPNGTransparency, str)

    @min_os_level("10.13.4")
    def testConstants10_13_4(self):
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtAboutCvTerm, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtAboutCvTermCvId, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtAboutCvTermId, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtAboutCvTermName, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtAboutCvTermRefinedAbout, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtAddlModelInfo, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkOrObject, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtArtworkCircaDateCreated, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtArtworkContentDescription, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtArtworkContributionDescription, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkCopyrightNotice, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkCreator, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkCreatorID, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtArtworkCopyrightOwnerID, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtArtworkCopyrightOwnerName, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkLicensorID, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkLicensorName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkDateCreated, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtArtworkPhysicalDescription, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkSource, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtArtworkSourceInventoryNo, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkSourceInvURL, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkStylePeriod, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtArtworkTitle, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtAudioBitrate, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtAudioBitrateMode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtAudioChannelCount, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtCircaDateCreated, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtContainerFormat, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtContainerFormatIdentifier, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtContainerFormatName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtContributor, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtContributorIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtContributorName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtContributorRole, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtCopyrightYear, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtCreator, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtCreatorIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtCreatorName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtCreatorRole, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtControlledVocabularyTerm, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDataOnScreen, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDataOnScreenRegion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDataOnScreenRegionD, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDataOnScreenRegionH, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDataOnScreenRegionText, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDataOnScreenRegionUnit, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDataOnScreenRegionW, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDataOnScreenRegionX, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDataOnScreenRegionY, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDigitalImageGUID, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDigitalSourceFileType, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDigitalSourceType, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDopesheet, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDopesheetLink, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtDopesheetLinkLink, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtDopesheetLinkLinkQualifier, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtEmbdEncRightsExpr, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtEmbeddedEncodedRightsExpr, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtEmbeddedEncodedRightsExprType, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtEmbeddedEncodedRightsExprLangID, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtEpisode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtEpisodeIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtEpisodeName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtEpisodeNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtEvent, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtShownEvent, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtShownEventIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtShownEventName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtExternalMetadataLink, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtFeedIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtGenre, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtGenreCvId, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtGenreCvTermId, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtGenreCvTermName, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtGenreCvTermRefinedAbout, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtHeadline, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtIPTCLastEdited, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLinkedEncRightsExpr, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtLinkedEncodedRightsExpr, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtLinkedEncodedRightsExprType, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtLinkedEncodedRightsExprLangID, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationCreated, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationCity, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationCountryCode, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationCountryName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationGPSAltitude, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationGPSLatitude, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationGPSLongitude, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationLocationId, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationLocationName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationProvinceState, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationSublocation, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationWorldRegion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtLocationShown, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtMaxAvailHeight, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtMaxAvailWidth, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtModelAge, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtOrganisationInImageCode, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtOrganisationInImageName, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPersonHeard, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPersonHeardIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPersonHeardName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPersonInImage, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPersonInImageWDetails, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtPersonInImageCharacteristic, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtPersonInImageCvTermCvId, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPersonInImageCvTermId, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtPersonInImageCvTermName, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtPersonInImageCvTermRefinedAbout, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtPersonInImageDescription, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPersonInImageId, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPersonInImageName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtProductInImage, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtProductInImageDescription, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtProductInImageGTIN, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtProductInImageName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPublicationEvent, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPublicationEventDate, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtPublicationEventIdentifier, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtPublicationEventName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRating, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRatingRatingRegion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRatingRegionCity, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtRatingRegionCountryCode, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtRatingRegionCountryName, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtRatingRegionGPSAltitude, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtRatingRegionGPSLatitude, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtRatingRegionGPSLongitude, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRatingRegionIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRatingRegionLocationId, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtRatingRegionLocationName, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtRatingRegionProvinceState, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtRatingRegionSublocation, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtRatingRegionWorldRegion, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRatingScaleMaxValue, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRatingScaleMinValue, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRatingSourceLink, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRatingValue, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRatingValueLogoLink, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRegistryID, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRegistryEntryRole, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRegistryItemID, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtRegistryOrganisationID, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtReleaseReady, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtSeason, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtSeasonIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtSeasonName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtSeasonNumber, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtSeries, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtSeriesIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtSeriesName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtStorylineIdentifier, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtStreamReady, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtStylePeriod, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtSupplyChainSource, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtSupplyChainSourceIdentifier, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtSupplyChainSourceName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtTemporalCoverage, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtTemporalCoverageFrom, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtTemporalCoverageTo, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtTranscript, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtTranscriptLink, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtTranscriptLinkLink, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtTranscriptLinkLinkQualifier, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtVideoBitrate, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtVideoBitrateMode, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtVideoDisplayAspectRatio, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtVideoEncodingProfile, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtVideoShotType, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtVideoShotTypeIdentifier, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtVideoShotTypeName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtVideoStreamsCount, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtVisualColor, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtWorkflowTag, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtWorkflowTagCvId, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtWorkflowTagCvTermId, str)
        self.assertIsInstance(Quartz.kCGImagePropertyIPTCExtWorkflowTagCvTermName, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyIPTCExtWorkflowTagCvTermRefinedAbout, str
        )

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(Quartz.kCGImagePropertyDNGActiveArea, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGAnalogBalance, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGAntiAliasStrength, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGAsShotICCProfile, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGAsShotPreProfileMatrix, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGAsShotProfileName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBaselineExposureOffset, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBayerGreenSplit, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBestQualityScale, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBlackLevelDeltaH, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBlackLevelDeltaV, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGBlackLevelRepeatDim, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGCFALayout, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGCFAPlaneColor, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGChromaBlurRadius, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGColorimetricReference, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGCurrentICCProfile, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGCurrentPreProfileMatrix, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGDefaultBlackRender, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGDefaultCropOrigin, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGDefaultCropSize, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGDefaultScale, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGDefaultUserCrop, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGExtraCameraProfiles, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGForwardMatrix1, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGForwardMatrix2, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGLinearizationTable, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGLinearResponseLimit, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGMakerNoteSafety, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGMaskedAreas, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGNewRawImageDigest, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGNoiseReductionApplied, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGOpcodeList1, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGOpcodeList2, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGOpcodeList3, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyDNGOriginalBestQualityFinalSize, str
        )
        self.assertIsInstance(Quartz.kCGImagePropertyDNGOriginalDefaultCropSize, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGOriginalDefaultFinalSize, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGOriginalRawFileData, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGOriginalRawFileDigest, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGOriginalRawFileName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGPreviewApplicationName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGPreviewApplicationVersion, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGPreviewColorSpace, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGPreviewDateTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGPreviewSettingsDigest, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGPreviewSettingsName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileCopyright, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileEmbedPolicy, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileHueSatMapData1, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileHueSatMapData2, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileHueSatMapDims, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileHueSatMapEncoding, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileLookTableData, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileLookTableDims, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileLookTableEncoding, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileName, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGProfileToneCurve, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGRawDataUniqueID, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGRawImageDigest, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGRawToPreviewGain, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGReductionMatrix1, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGReductionMatrix2, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGRowInterleaveFactor, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGShadowScale, str)
        self.assertIsInstance(Quartz.kCGImagePropertyDNGSubTileBlockSize, str)

        self.assertIsInstance(Quartz.kCGImageAuxiliaryDataTypePortraitEffectsMatte, str)

        self.assertIsInstance(Quartz.kCGImagePropertyPNGComment, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGDisclaimer, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGSource, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGWarning, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(Quartz.kCGImagePropertyHEICSDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyHEICSLoopCount, str)
        self.assertIsInstance(Quartz.kCGImagePropertyHEICSDelayTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyHEICSUnclampedDelayTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyHEICSCanvasPixelWidth, str)
        self.assertIsInstance(Quartz.kCGImagePropertyHEICSCanvasPixelHeight, str)
        self.assertIsInstance(Quartz.kCGImagePropertyHEICSFrameInfoArray, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifOffsetTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifOffsetTimeOriginal, str)
        self.assertIsInstance(Quartz.kCGImagePropertyExifOffsetTimeDigitized, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGIFCanvasPixelWidth, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGIFCanvasPixelHeight, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGIFFrameInfoArray, str)
        self.assertIsInstance(Quartz.kCGImagePropertyAPNGFrameInfoArray, str)
        self.assertIsInstance(Quartz.kCGImagePropertyAPNGCanvasPixelWidth, str)
        self.assertIsInstance(Quartz.kCGImagePropertyAPNGCanvasPixelHeight, str)
        self.assertIsInstance(
            Quartz.kCGImageAuxiliaryDataTypeSemanticSegmentationSkinMatte, str
        )
        self.assertIsInstance(
            Quartz.kCGImageAuxiliaryDataTypeSemanticSegmentationHairMatte, str
        )
        self.assertIsInstance(
            Quartz.kCGImageAuxiliaryDataTypeSemanticSegmentationTeethMatte, str
        )

    @min_os_level("10.15.1")
    def testConstants10_15_1(self):
        self.assertIsInstance(Quartz.kCGImagePropertyExifCompositeImage, str)
        self.assertIsInstance(
            Quartz.kCGImagePropertyExifSourceImageNumberOfCompositeImage, str
        )
        self.assertIsInstance(
            Quartz.kCGImagePropertyExifSourceExposureTimesOfCompositeImage, str
        )

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(Quartz.kCGImagePropertyWebPDictionary, str)

        self.assertIsInstance(Quartz.kCGImagePropertyWebPLoopCount, str)
        self.assertIsInstance(Quartz.kCGImagePropertyWebPDelayTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyWebPUnclampedDelayTime, str)
        self.assertIsInstance(Quartz.kCGImagePropertyWebPFrameInfoArray, str)
        self.assertIsInstance(Quartz.kCGImagePropertyWebPCanvasPixelWidth, str)
        self.assertIsInstance(Quartz.kCGImagePropertyWebPCanvasPixelHeight, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTGADictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTGACompression, str)

        self.assertIsInstance(
            Quartz.kCGImageAuxiliaryDataTypeSemanticSegmentationGlassesMatte, str
        )
        self.assertIsInstance(Quartz.kCGImageAuxiliaryDataTypeHDRGainMap, str)
        self.assertIsInstance(
            Quartz.kCGImageAuxiliaryDataTypeSemanticSegmentationSkyMatte, str
        )

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(Quartz.kCGImagePropertyImageIndex, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroups, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupIndex, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupType, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupTypeStereoPair, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupTypeAlternate, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupImagesAlternate, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupImageIndexLeft, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupImageIndexRight, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupImageIsLeftImage, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupImageIsRightImage, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupImageIsAlternateImage, str)
        self.assertIsInstance(Quartz.kCGImagePropertyPNGPixelsAspectRatio, str)

    @min_os_level("13.0")
    def testConstants13_0(self):
        self.assertTrue(not hasattr(Quartz, "kCGImagePropertyHorizontalFOV"))

        self.assertIsInstance(Quartz.kCGImagePropertyHEIFDictionary, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupImageBaseline, str)
        self.assertIsInstance(Quartz.kCGImagePropertyGroupImageDisparityAdjustment, str)
        self.assertIsInstance(Quartz.kIIOMetadata_CameraExtrinsicsKey, str)
        self.assertIsInstance(Quartz.kIIOCameraExtrinsics_CoordinateSystemID, str)
        self.assertIsInstance(Quartz.kIIOCameraExtrinsics_Position, str)
        self.assertIsInstance(Quartz.kIIOCameraExtrinsics_Rotation, str)
        self.assertIsInstance(Quartz.kIIOMetadata_CameraModelKey, str)
        self.assertIsInstance(Quartz.kIIOCameraModel_ModelType, str)
        self.assertIsInstance(Quartz.kIIOCameraModelType_SimplifiedPinhole, str)
        self.assertIsInstance(Quartz.kIIOCameraModelType_GenericPinhole, str)
        self.assertIsInstance(Quartz.kIIOCameraModel_Intrinsics, str)

    @min_os_level("13.3")
    def testConstants13_3(self):
        # kCGImagePropertyOpenEXRCompression is no longer present in the 14.0 SDK,
        # but wasn't deprecated?
        self.assertIsInstance(Quartz.kCGImagePropertyOpenEXRCompression, str)
        self.assertIsInstance(Quartz.kCGImagePropertyAVISDictionary, str)

    @min_os_level("14.4")
    def testConstants14_4(self):
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFXPosition, str)
        self.assertIsInstance(Quartz.kCGImagePropertyTIFFYPosition, str)
