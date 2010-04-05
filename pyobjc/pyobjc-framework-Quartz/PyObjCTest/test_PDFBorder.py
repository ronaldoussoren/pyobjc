
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFBorder (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFBorderStyleSolid, 0)
        self.assertEqual(kPDFBorderStyleDashed, 1)
        self.assertEqual(kPDFBorderStyleBeveled, 2)
        self.assertEqual(kPDFBorderStyleInset, 3)
        self.assertEqual(kPDFBorderStyleUnderline, 4)

if __name__ == "__main__":
    main()
