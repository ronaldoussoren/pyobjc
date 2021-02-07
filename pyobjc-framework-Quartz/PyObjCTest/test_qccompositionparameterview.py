from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestQCCompositionParameterViewHelper(Quartz.NSObject):
    def compositionParameterView_shouldDisplayParameterWithKey_attributes_(
        self, pv, pk, pa
    ):
        return 1


class TestQCCompositionParameterView(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.QCCompositionParameterView.hasParameters)

        self.assertResultIsBOOL(Quartz.QCCompositionParameterView.drawsBackground)
        self.assertArgIsBOOL(Quartz.QCCompositionParameterView.setDrawsBackground_, 0)

        self.assertResultIsBOOL(
            TestQCCompositionParameterViewHelper.compositionParameterView_shouldDisplayParameterWithKey_attributes_
        )
