from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestQCCompositionPickerView(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(
            Quartz.QCCompositionPickerViewDidSelectCompositionNotification, str
        )

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.QCCompositionPickerView.showsCompositionNames)
        self.assertArgIsBOOL(
            Quartz.QCCompositionPickerView.setShowsCompositionNames_, 0
        )

        self.assertResultIsBOOL(Quartz.QCCompositionPickerView.allowsEmptySelection)
        self.assertArgIsBOOL(Quartz.QCCompositionPickerView.setAllowsEmptySelection_, 0)

        self.assertResultIsBOOL(Quartz.QCCompositionPickerView.isAnimating)

        self.assertResultIsBOOL(Quartz.QCCompositionPickerView.drawsBackground)
        self.assertArgIsBOOL(Quartz.QCCompositionPickerView.setDrawsBackground_, 0)
