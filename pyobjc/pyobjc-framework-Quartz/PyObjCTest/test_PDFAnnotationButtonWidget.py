
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationButtonWidget (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kPDFWidgetUnknownControl, -1)
        self.failUnlessEqual(kPDFWidgetPushButtonControl, 0) 
        self.failUnlessEqual(kPDFWidgetRadioButtonControl, 1)
        self.failUnlessEqual(kPDFWidgetCheckBoxControl, 2)

    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessResultIsBOOL(PDFAnnotationButtonWidget.isHighlighted)
        self.failUnlessResultIsBOOL(PDFAnnotationButtonWidget.allowsToggleToOff)

if __name__ == "__main__":
    main()
