from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNTypes(TestCase):
    def testConstants(self):
        self.assertEqual(Vision.VNImageCropAndScaleOptionCenterCrop, 0)
        self.assertEqual(Vision.VNImageCropAndScaleOptionScaleFit, 1)
        self.assertEqual(Vision.VNImageCropAndScaleOptionScaleFill, 2)

        self.assertEqual(Vision.VNElementTypeUnknown, 0)
        self.assertEqual(Vision.VNElementTypeFloat, 1)
        self.assertEqual(Vision.VNElementTypeDouble, 2)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Vision.VNBarcodeSymbologyAztec, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyAztec, str)
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
