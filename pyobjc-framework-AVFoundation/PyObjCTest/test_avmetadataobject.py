from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVMetadataObject(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVMetadataFaceObject.hasRollAngle)
        self.assertResultIsBOOL(AVFoundation.AVMetadataFaceObject.hasYawAngle)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeFace, unicode)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeUPCECode, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCode39Code, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCode39Mod43Code, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeEAN13Code, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeEAN8Code, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCode93Code, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCode128Code, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypePDF417Code, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeQRCode, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeAztecCode, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataObjectTypeInterleaved2of5Code, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeITF14Code, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeDataMatrixCode, unicode)

    @min_os_level("10.15")
    @expectedFailure
    def testConstants10_15_missing(self):
        with self.subTest("humanbody"):
            self.assertIsInstance(AVFoundationAVMetadataObjectTypeHumanBody, unicode)
        with self.subTest("catbody"):
            self.assertIsInstance(AVFoundation.AVMetadataObjectTypeCatBody, unicode)
        with self.subTest("dogbody"):
            self.assertIsInstance(AVFoundation.AVMetadataObjectTypeDogBody, unicode)
        with self.subTest("salientobject"):
            self.assertIsInstance(
                AVFoundation.AVMetadataObjectTypeSalientObject, unicode
            )


if __name__ == "__main__":
    main()
