
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationChoiceWidget (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(PDFAnnotationChoiceWidget.isListChoice)
        self.failUnlessArgIsBOOL(PDFAnnotationChoiceWidget.setIsListChoice_, 0)

if __name__ == "__main__":
    main()
