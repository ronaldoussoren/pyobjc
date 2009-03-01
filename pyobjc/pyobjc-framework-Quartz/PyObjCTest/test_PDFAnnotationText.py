
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationText (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kPDFTextAnnotationIconComment, 0)
        self.failUnlessEqual(kPDFTextAnnotationIconKey, 1)
        self.failUnlessEqual(kPDFTextAnnotationIconNote, 2)
        self.failUnlessEqual(kPDFTextAnnotationIconHelp, 3)
        self.failUnlessEqual(kPDFTextAnnotationIconNewParagraph, 4)
        self.failUnlessEqual(kPDFTextAnnotationIconParagraph, 5)
        self.failUnlessEqual(kPDFTextAnnotationIconInsert, 6)

if __name__ == "__main__":
    main()
