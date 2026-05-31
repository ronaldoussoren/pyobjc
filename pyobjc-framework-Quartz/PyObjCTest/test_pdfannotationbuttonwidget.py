from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFAnnotationButtonWidget(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kPDFWidgetUnknownControl, -1)
        self.assertEqual(Quartz.kPDFWidgetPushButtonControl, 0)
        self.assertEqual(Quartz.kPDFWidgetRadioButtonControl, 1)
        self.assertEqual(Quartz.kPDFWidgetCheckBoxControl, 2)

        self.assertEqual(Quartz.kPDFWidgetMixedState, -1)
        self.assertEqual(Quartz.kPDFWidgetOffState, 0)
        self.assertEqual(Quartz.kPDFWidgetOnState, 1)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotationButtonWidget.isHighlighted)
        self.assertArgIsBOOL(Quartz.PDFAnnotationButtonWidget.setHighlighted_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotationButtonWidget.allowsToggleToOff)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBOOL(Quartz.PDFAnnotationButtonWidget.setAllowsToggleToOff_, 0)
