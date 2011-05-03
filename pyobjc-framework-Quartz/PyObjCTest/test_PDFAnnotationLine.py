
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationLine (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFLineStyleNone, 0)
        self.assertEqual(kPDFLineStyleSquare, 1)
        self.assertEqual(kPDFLineStyleCircle, 2)
        self.assertEqual(kPDFLineStyleDiamond, 3)
        self.assertEqual(kPDFLineStyleOpenArrow, 4)
        self.assertEqual(kPDFLineStyleClosedArrow, 5)

if __name__ == "__main__":
    main()
