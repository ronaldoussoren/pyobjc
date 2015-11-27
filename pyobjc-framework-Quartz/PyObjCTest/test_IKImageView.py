
from PyObjCTools.TestSupport import *
from Quartz import *

class TestIKImageView (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(IKToolModeNone, unicode)
        self.assertIsInstance(IKToolModeMove, unicode)
        self.assertIsInstance(IKToolModeSelect, unicode)
        self.assertIsInstance(IKToolModeCrop, unicode)
        self.assertIsInstance(IKToolModeRotate, unicode)
        self.assertIsInstance(IKToolModeAnnotate, unicode)
        self.assertIsInstance(IKOverlayTypeBackground, unicode)
        self.assertIsInstance(IKOverlayTypeImage, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(IKToolModeSelectRect, unicode)
        self.assertIsInstance(IKToolModeSelectEllipse, unicode)
        self.assertIsInstance(IKToolModeSelectLasso, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(IKImageView.autoresizes)
        self.assertArgIsBOOL(IKImageView.setAutoresizes_, 0)

        self.assertResultIsBOOL(IKImageView.hasHorizontalScroller)
        self.assertArgIsBOOL(IKImageView.setHasHorizontalScroller_, 0)

        self.assertResultIsBOOL(IKImageView.hasVerticalScroller)
        self.assertArgIsBOOL(IKImageView.setHasVerticalScroller_, 0)

        self.assertResultIsBOOL(IKImageView.autohidesScrollers)
        self.assertArgIsBOOL(IKImageView.setAutohidesScrollers_, 0)

        self.assertResultIsBOOL(IKImageView.supportsDragAndDrop)
        self.assertArgIsBOOL(IKImageView.setSupportsDragAndDrop_, 0)

        self.assertResultIsBOOL(IKImageView.editable)
        self.assertArgIsBOOL(IKImageView.setEditable_, 0)

        self.assertResultIsBOOL(IKImageView.doubleClickOpensImageEditPanel)
        self.assertArgIsBOOL(IKImageView.setDoubleClickOpensImageEditPanel_, 0)



if __name__ == "__main__":
    main()
