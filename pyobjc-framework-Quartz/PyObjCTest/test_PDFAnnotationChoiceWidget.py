
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationChoiceWidget (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(PDFAnnotationChoiceWidget.isListChoice)
        self.assertArgIsBOOL(PDFAnnotationChoiceWidget.setIsListChoice_, 0)

if __name__ == "__main__":
    main()
