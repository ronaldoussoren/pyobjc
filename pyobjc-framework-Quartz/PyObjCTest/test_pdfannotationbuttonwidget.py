from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFAnnotationButtonWidget(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Quartz.PDFWidgetControlType)
        self.assertEqual(Quartz.kPDFWidgetUnknownControl, -1)
        self.assertEqual(Quartz.kPDFWidgetPushButtonControl, 0)
        self.assertEqual(Quartz.kPDFWidgetRadioButtonControl, 1)
        self.assertEqual(Quartz.kPDFWidgetCheckBoxControl, 2)

        self.assertIsEnumType(Quartz.PDFWidgetCellState)
        self.assertEqual(Quartz.kPDFWidgetMixedState, -1)
        self.assertEqual(Quartz.kPDFWidgetOffState, 0)
        self.assertEqual(Quartz.kPDFWidgetOnState, 1)

    def test_methods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotationButtonWidget.isHighlighted)
        self.assertArgIsBOOL(Quartz.PDFAnnotationButtonWidget.setHighlighted_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotationButtonWidget.allowsToggleToOff)

        self.assertArgIsBOOL(Quartz.PDFAnnotationButtonWidget.setAllowsToggleToOff_, 0)
