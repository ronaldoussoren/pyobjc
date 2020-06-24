from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCIBarcodeDescriptor(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.CIQRCodeErrorCorrectionLevelL, ord("L"))
        self.assertEqual(Quartz.CIQRCodeErrorCorrectionLevelM, ord("M"))
        self.assertEqual(Quartz.CIQRCodeErrorCorrectionLevelQ, ord("Q"))
        self.assertEqual(Quartz.CIQRCodeErrorCorrectionLevelH, ord("H"))

        self.assertEqual(Quartz.CIDataMatrixCodeECCVersion000, 0)
        self.assertEqual(Quartz.CIDataMatrixCodeECCVersion050, 50)
        self.assertEqual(Quartz.CIDataMatrixCodeECCVersion080, 80)
        self.assertEqual(Quartz.CIDataMatrixCodeECCVersion100, 100)
        self.assertEqual(Quartz.CIDataMatrixCodeECCVersion140, 140)
        self.assertEqual(Quartz.CIDataMatrixCodeECCVersion200, 200)

    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.CIAztecCodeDescriptor.isCompact)
        self.assertResultIsBOOL(Quartz.CIPDF417CodeDescriptor.isCompact)
