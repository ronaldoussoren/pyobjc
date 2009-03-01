
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationPopup (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(PDFAnnotationPopup.isOpen)
        self.failUnlessArgIsBOOL(PDFAnnotationPopup.setIsOpen_, 0)

if __name__ == "__main__":
    main()
