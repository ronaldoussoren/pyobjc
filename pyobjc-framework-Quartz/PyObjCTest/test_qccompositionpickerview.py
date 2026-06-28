from PyObjCTools.TestSupport import TestCase
import Quartz


class TestQCCompositionPickerView(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            Quartz.QCCompositionPickerViewDidSelectCompositionNotification, str
        )

    def test_methods(self):
        self.assertResultIsBOOL(Quartz.QCCompositionPickerView.showsCompositionNames)
        self.assertArgIsBOOL(
            Quartz.QCCompositionPickerView.setShowsCompositionNames_, 0
        )

        self.assertResultIsBOOL(Quartz.QCCompositionPickerView.allowsEmptySelection)
        self.assertArgIsBOOL(Quartz.QCCompositionPickerView.setAllowsEmptySelection_, 0)

        self.assertResultIsBOOL(Quartz.QCCompositionPickerView.isAnimating)

        self.assertResultIsBOOL(Quartz.QCCompositionPickerView.drawsBackground)
        self.assertArgIsBOOL(Quartz.QCCompositionPickerView.setDrawsBackground_, 0)
