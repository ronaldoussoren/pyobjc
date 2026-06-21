from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFAnnotationChoiceWidget(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotationChoiceWidget.isListChoice)
        self.assertArgIsBOOL(Quartz.PDFAnnotationChoiceWidget.setIsListChoice_, 0)
