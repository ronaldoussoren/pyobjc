
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationPopup (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(PDFAnnotationPopup.isOpen)
        self.assertArgIsBOOL(PDFAnnotationPopup.setIsOpen_, 0)

if __name__ == "__main__":
    main()
