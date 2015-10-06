from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationLink (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(PDFAnnotationLink.setHighlighted_, 0)

if __name__ == "__main__":
    main()
