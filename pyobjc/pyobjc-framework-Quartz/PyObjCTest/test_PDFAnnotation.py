
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotation (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(PDFAnnotation.shouldDisplay)
        self.failUnlessArgIsBOOL(PDFAnnotation.setShouldDisplay_, 0)
        self.failUnlessResultIsBOOL(PDFAnnotation.shouldPrint)
        self.failUnlessArgIsBOOL(PDFAnnotation.setShouldPrint_, 0)
        self.failUnlessResultIsBOOL(PDFAnnotation.hasAppearanceStream)

if __name__ == "__main__":
    main()
