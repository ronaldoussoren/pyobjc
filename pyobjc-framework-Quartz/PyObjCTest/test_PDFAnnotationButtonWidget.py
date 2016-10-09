
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationButtonWidget (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFWidgetUnknownControl, -1)
        self.assertEqual(kPDFWidgetPushButtonControl, 0)
        self.assertEqual(kPDFWidgetRadioButtonControl, 1)
        self.assertEqual(kPDFWidgetCheckBoxControl, 2)

        self.assertEqual(kPDFWidgetMixedState, -1)
        self.assertEqual(kPDFWidgetOffState, 0)
        self.assertEqual(kPDFWidgetOnState, 1)


    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(PDFAnnotationButtonWidget.isHighlighted)
        self.assertArgIsBOOL(PDFAnnotationButtonWidget.setHighlighted_, 0)
        self.assertResultIsBOOL(PDFAnnotationButtonWidget.allowsToggleToOff)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBOOL(PDFAnnotationButtonWidget.setAllowsToggleToOff_, 0)

if __name__ == "__main__":
    main()
