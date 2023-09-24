import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestAVMetadataObject(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AVFoundation.AVMetadataObjectType, str)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVMetadataFaceObject.hasRollAngle)
        self.assertResultIsBOOL(AVFoundation.AVMetadataFaceObject.hasYawAngle)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeFace, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeUPCECode, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCode39Code, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCode39Mod43Code, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeEAN13Code, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeEAN8Code, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCode93Code, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCode128Code, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypePDF417Code, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeQRCode, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeAztecCode, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeInterleaved2of5Code, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeITF14Code, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeDataMatrixCode, str)

    @min_os_level("10.15")
    @expectedFailure
    def testConstants10_15_missing(self):
        with self.subTest("humanbody"):
            self.assertIsInstance(
                AVFoundation.AVFoundationAVMetadataObjectTypeHumanBody, str
            )  # noqa: B950
        with self.subTest("catbody"):
            self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCatBody, str)
        with self.subTest("dogbody"):
            self.assertIsInstance(AVFoundation.AVMetadataObjectTypeDogBody, str)
        with self.subTest("salientobject"):
            self.assertIsInstance(AVFoundation.AVMetadataObjectTypeSalientObject, str)

    @min_os_level("12.3")
    def testConstants12_3(self):
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCodabarCode, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeGS1DataBarCode, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataObjectTypeGS1DataBarExpandedCode, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataObjectTypeGS1DataBarLimitedCode, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeMicroQRCode, str)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeMicroPDF417Code, str)

    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeHumanFullBody, str)
