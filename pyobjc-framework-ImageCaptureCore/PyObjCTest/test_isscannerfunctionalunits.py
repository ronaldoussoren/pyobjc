import ImageCaptureCore
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestICScannerFunctionalUnits(TestCase):
    def testConstants(self):
        self.assertEqual(ImageCaptureCore.ICScannerFunctionalUnitTypeFlatbed, 0)
        self.assertEqual(
            ImageCaptureCore.ICScannerFunctionalUnitTypePositiveTransparency, 1
        )
        self.assertEqual(
            ImageCaptureCore.ICScannerFunctionalUnitTypeNegativeTransparency, 2
        )
        self.assertEqual(ImageCaptureCore.ICScannerFunctionalUnitTypeDocumentFeeder, 3)

        self.assertEqual(ImageCaptureCore.ICScannerMeasurementUnitInches, 0)
        self.assertEqual(ImageCaptureCore.ICScannerMeasurementUnitCentimeters, 1)
        self.assertEqual(ImageCaptureCore.ICScannerMeasurementUnitPicas, 2)
        self.assertEqual(ImageCaptureCore.ICScannerMeasurementUnitPoints, 3)
        self.assertEqual(ImageCaptureCore.ICScannerMeasurementUnitTwips, 4)
        self.assertEqual(ImageCaptureCore.ICScannerMeasurementUnitPixels, 5)

        self.assertEqual(ImageCaptureCore.ICScannerBitDepth1Bit, 1)
        self.assertEqual(ImageCaptureCore.ICScannerBitDepth8Bits, 8)
        self.assertEqual(ImageCaptureCore.ICScannerBitDepth16Bits, 16)

        self.assertEqual(ImageCaptureCore.ICScannerColorDataFormatTypeChunky, 0)
        self.assertEqual(ImageCaptureCore.ICScannerColorDataFormatTypePlanar, 1)

        self.assertEqual(ImageCaptureCore.ICScannerPixelDataTypeBW, 0)
        self.assertEqual(ImageCaptureCore.ICScannerPixelDataTypeGray, 1)
        self.assertEqual(ImageCaptureCore.ICScannerPixelDataTypeRGB, 2)
        self.assertEqual(ImageCaptureCore.ICScannerPixelDataTypePalette, 3)
        self.assertEqual(ImageCaptureCore.ICScannerPixelDataTypeCMY, 4)
        self.assertEqual(ImageCaptureCore.ICScannerPixelDataTypeCMYK, 5)
        self.assertEqual(ImageCaptureCore.ICScannerPixelDataTypeYUV, 6)
        self.assertEqual(ImageCaptureCore.ICScannerPixelDataTypeYUVK, 7)
        self.assertEqual(ImageCaptureCore.ICScannerPixelDataTypeCIEXYZ, 8)

        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeDefault, 0)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeA4, 1)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeB5, 2)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeUSLetter, 3)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeUSLegal, 4)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeA5, 5)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB4, 6)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB6, 7)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeUSLedger, 9)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeUSExecutive, 10)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeA3, 11)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB3, 12)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeA6, 13)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC4, 14)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC5, 15)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC6, 16)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType4A0, 17)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType2A0, 18)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeA0, 19)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeA1, 20)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeA2, 21)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeA7, 22)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeA8, 23)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeA9, 24)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType10, 25)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB0, 26)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB1, 27)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB2, 28)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB5, 29)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB7, 30)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB8, 31)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB9, 32)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeISOB10, 33)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeJISB0, 34)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeJISB1, 35)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeJISB2, 36)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeJISB3, 37)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeJISB4, 38)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeJISB6, 39)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeJISB7, 40)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeJISB8, 41)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeJISB9, 42)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeJISB10, 43)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC0, 44)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC1, 45)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC2, 46)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC3, 47)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC7, 48)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC8, 49)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC9, 50)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeC10, 51)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeUSStatement, 52)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeBusinessCard, 53)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeE, 60)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType3R, 61)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType4R, 62)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType5R, 63)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType6R, 64)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType8R, 65)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeS8R, 66)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType10R, 67)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeS10R, 68)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType11R, 69)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType12R, 70)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeS12R, 71)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType110, 72)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeAPSH, 73)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeAPSC, 74)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeAPSP, 75)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentType135, 76)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeMF, 77)
        self.assertEqual(ImageCaptureCore.ICScannerDocumentTypeLF, 78)

        self.assertEqual(ImageCaptureCore.ICScannerFunctionalUnitStateReady, 1 << 0)
        self.assertEqual(
            ImageCaptureCore.ICScannerFunctionalUnitStateScanInProgress, 1 << 1
        )
        self.assertEqual(
            ImageCaptureCore.ICScannerFunctionalUnitStateOverviewScanInProgress, 1 << 2
        )

        self.assertEqual(ImageCaptureCore.ICScannerFeatureTypeEnumeration, 0)
        self.assertEqual(ImageCaptureCore.ICScannerFeatureTypeRange, 1)
        self.assertEqual(ImageCaptureCore.ICScannerFeatureTypeBoolean, 2)
        self.assertEqual(ImageCaptureCore.ICScannerFeatureTypeTemplate, 3)

    def testMethods(self):
        self.assertResultIsBOOL(ImageCaptureCore.ICScannerFeatureBoolean.value)
        self.assertArgIsBOOL(ImageCaptureCore.ICScannerFeatureBoolean.setValue_, 0)

        self.assertResultIsBOOL(
            ImageCaptureCore.ICScannerFunctionalUnit.acceptsThresholdForBlackAndWhiteScanning
        )
        self.assertResultIsBOOL(
            ImageCaptureCore.ICScannerFunctionalUnit.usesThresholdForBlackAndWhiteScanning
        )
        self.assertArgIsBOOL(
            ImageCaptureCore.ICScannerFunctionalUnit.setUsesThresholdForBlackAndWhiteScanning_,
            0,
        )
        self.assertResultIsBOOL(ImageCaptureCore.ICScannerFunctionalUnit.scanInProgress)
        self.assertResultIsBOOL(
            ImageCaptureCore.ICScannerFunctionalUnit.canPerformOverviewScan
        )
        self.assertResultIsBOOL(
            ImageCaptureCore.ICScannerFunctionalUnit.overviewScanInProgress
        )
        self.assertResultIsBOOL(
            ImageCaptureCore.ICScannerFunctionalUnitDocumentFeeder.supportsDuplexScanning
        )
        self.assertResultIsBOOL(
            ImageCaptureCore.ICScannerFunctionalUnitDocumentFeeder.duplexScanningEnabled
        )
        self.assertArgIsBOOL(
            ImageCaptureCore.ICScannerFunctionalUnitDocumentFeeder.setDuplexScanningEnabled_,
            0,
        )
        self.assertResultIsBOOL(
            ImageCaptureCore.ICScannerFunctionalUnitDocumentFeeder.documentLoaded
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(
            ImageCaptureCore.ICScannerFunctionalUnitDocumentFeeder.reverseFeederPageOrder
        )
