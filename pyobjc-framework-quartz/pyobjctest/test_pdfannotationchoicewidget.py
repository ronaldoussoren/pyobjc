from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFAnnotationChoiceWidget(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotationChoiceWidget.isListChoice)
        self.assertArgIsBOOL(Quartz.PDFAnnotationChoiceWidget.setIsListChoice_, 0)
