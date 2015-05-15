
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationTextWidget (TestCase):
    @min_os_level('10.9')
    def testMethods(self):
        self.assertResultIsBOOL(PDFAnnotationTextWidget.isMultiline)
        self.assertArgIsBOOL(PDFAnnotationTextWidget.setIsMultiline_, 0)

if __name__ == "__main__":
    main()
