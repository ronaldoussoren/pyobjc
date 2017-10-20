from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIBarcodeDescriptor (TestCase):
    def testConstants(self):
        self.assertEqual(CIQRCodeErrorCorrectionLevelL, ord('L'))
        self.assertEqual(CIQRCodeErrorCorrectionLevelM, ord('M'))
        self.assertEqual(CIQRCodeErrorCorrectionLevelQ, ord('Q'))
        self.assertEqual(CIQRCodeErrorCorrectionLevelH, ord('H'))

        self.assertEqual(CIDataMatrixCodeECCVersion000,   0)
        self.assertEqual(CIDataMatrixCodeECCVersion050,  50)
        self.assertEqual(CIDataMatrixCodeECCVersion080,  80)
        self.assertEqual(CIDataMatrixCodeECCVersion100, 100)
        self.assertEqual(CIDataMatrixCodeECCVersion140, 140)
        self.assertEqual(CIDataMatrixCodeECCVersion200, 200)

    @min_os_level('10.13')
    def testMethods(self):
        self.assertResultIsBOOL(CIAztecCodeDescriptor.isCompact)
        self.assertResultIsBOOL(CIPDF417CodeDescriptor.isCompact)

if __name__ == "__main__":
    main()
