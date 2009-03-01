
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFBorder (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kPDFBorderStyleSolid, 0)
        self.failUnlessEqual(kPDFBorderStyleDashed, 1)
        self.failUnlessEqual(kPDFBorderStyleBeveled, 2)
        self.failUnlessEqual(kPDFBorderStyleInset, 3)
        self.failUnlessEqual(kPDFBorderStyleUnderline, 4)

if __name__ == "__main__":
    main()
