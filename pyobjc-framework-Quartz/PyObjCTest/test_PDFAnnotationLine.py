
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationLine (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kPDFLineStyleNone, 0)
        self.failUnlessEqual(kPDFLineStyleSquare, 1)
        self.failUnlessEqual(kPDFLineStyleCircle, 2)
        self.failUnlessEqual(kPDFLineStyleDiamond, 3)
        self.failUnlessEqual(kPDFLineStyleOpenArrow, 4)
        self.failUnlessEqual(kPDFLineStyleClosedArrow, 5)

if __name__ == "__main__":
    main()
