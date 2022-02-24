from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNTypes(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Vision.VNBarcodeSymbology, str)
        self.assertIsTypedEnum(Vision.VNVideoProcessingOption, str)

    def test_enum_types(self):
        self.assertIsEnumType(Vision.VNElementType)
        self.assertIsEnumType(Vision.VNImageCropAndScaleOption)

    def testConstants(self):
        self.assertEqual(Vision.VNImageCropAndScaleOptionCenterCrop, 0)
        self.assertEqual(Vision.VNImageCropAndScaleOptionScaleFit, 1)
        self.assertEqual(Vision.VNImageCropAndScaleOptionScaleFill, 2)

        self.assertEqual(Vision.VNElementTypeUnknown, 0)
        self.assertEqual(Vision.VNElementTypeFloat, 1)
        self.assertEqual(Vision.VNElementTypeDouble, 2)

        self.assertEqual(Vision.VNChiralityUnknown, 0)
        self.assertEqual(Vision.VNChiralityLeft, -1)
        self.assertEqual(Vision.VNChiralityRight, 1)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Vision.VNBarcodeSymbologyAztec, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode39, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode39Checksum, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode39FullASCII, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode39FullASCIIChecksum, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode93, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode93i, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode128, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyDataMatrix, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyEAN8, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyEAN13, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyI2of5, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyI2of5Checksum, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyITF14, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyPDF417, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyQR, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyUPCE, str)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(Vision.VNVideoProcessingOptionFrameCadence, str)
        self.assertIsInstance(Vision.VNVideoProcessingOptionTimeInterval, str)

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(Vision.VNBarcodeSymbologyCodabar, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyGS1DataBar, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyGS1DataBarExpanded, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyGS1DataBarLimited, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyMicroPDF417, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyMicroQR, str)
