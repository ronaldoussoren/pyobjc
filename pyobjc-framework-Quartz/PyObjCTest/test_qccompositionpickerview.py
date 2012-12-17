
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

try:
    unicode
except NameError:
    unicode = str

class TestQCCompositionPickerView (TestCase):

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(QCCompositionPickerViewDidSelectCompositionNotification, unicode)

    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(QCCompositionPickerView.showsCompositionNames)
        self.assertArgIsBOOL(QCCompositionPickerView.setShowsCompositionNames_, 0)

        self.assertResultIsBOOL(QCCompositionPickerView.allowsEmptySelection)
        self.assertArgIsBOOL(QCCompositionPickerView.setAllowsEmptySelection_, 0)

        self.assertResultIsBOOL(QCCompositionPickerView.isAnimating)

        self.assertResultIsBOOL(QCCompositionPickerView.drawsBackground)
        self.assertArgIsBOOL(QCCompositionPickerView.setDrawsBackground_, 0)


if __name__ == "__main__":
    main()
