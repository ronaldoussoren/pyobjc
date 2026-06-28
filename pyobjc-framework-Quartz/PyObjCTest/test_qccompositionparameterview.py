from PyObjCTools.TestSupport import TestCase
import Quartz


class TestQCCompositionParameterViewHelper(Quartz.NSObject):
    def compositionParameterView_shouldDisplayParameterWithKey_attributes_(
        self, pv, pk, pa
    ):
        return 1


class TestQCCompositionParameterView(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.QCCompositionParameterView.hasParameters)

        self.assertResultIsBOOL(Quartz.QCCompositionParameterView.drawsBackground)
        self.assertArgIsBOOL(Quartz.QCCompositionParameterView.setDrawsBackground_, 0)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestQCCompositionParameterViewHelper.compositionParameterView_shouldDisplayParameterWithKey_attributes_
        )
