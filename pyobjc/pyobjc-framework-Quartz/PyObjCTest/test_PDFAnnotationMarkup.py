
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationMarkup (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kPDFMarkupTypeHighlight, 0)
        self.failUnlessEqual(kPDFMarkupTypeStrikeOut, 1)
        self.failUnlessEqual(kPDFMarkupTypeUnderline, 2)

if __name__ == "__main__":
    main()
