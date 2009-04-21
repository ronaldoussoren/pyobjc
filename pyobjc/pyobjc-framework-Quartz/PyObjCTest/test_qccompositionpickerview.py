
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

class TestQCCompositionPickerView (TestCase):

    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(QCCompositionPickerViewDidSelectCompositionNotification, unicode)

    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessResultIsBOOL(QCCompositionPickerView.showsCompositionNames)
        self.failUnlessArgIsBOOL(QCCompositionPickerView.setShowsCompositionNames_, 0)

        self.failUnlessResultIsBOOL(QCCompositionPickerView.allowsEmptySelection)
        self.failUnlessArgIsBOOL(QCCompositionPickerView.setAllowsEmptySelection_, 0)

        self.failUnlessResultIsBOOL(QCCompositionPickerView.isAnimating)

        self.failUnlessResultIsBOOL(QCCompositionPickerView.drawsBackground)
        self.failUnlessArgIsBOOL(QCCompositionPickerView.setDrawsBackground_, 0)
        

if __name__ == "__main__":
    main()
