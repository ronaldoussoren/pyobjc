from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestIKImageView(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.IKToolModeNone, str)
        self.assertIsInstance(Quartz.IKToolModeMove, str)
        self.assertIsInstance(Quartz.IKToolModeSelect, str)
        self.assertIsInstance(Quartz.IKToolModeCrop, str)
        self.assertIsInstance(Quartz.IKToolModeRotate, str)
        self.assertIsInstance(Quartz.IKToolModeAnnotate, str)
        self.assertIsInstance(Quartz.IKOverlayTypeBackground, str)
        self.assertIsInstance(Quartz.IKOverlayTypeImage, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(Quartz.IKToolModeSelectRect, str)
        self.assertIsInstance(Quartz.IKToolModeSelectEllipse, str)
        self.assertIsInstance(Quartz.IKToolModeSelectLasso, str)

    def testMethods(self):
        self.assertResultIsBOOL(Quartz.IKImageView.autoresizes)
        self.assertArgIsBOOL(Quartz.IKImageView.setAutoresizes_, 0)

        self.assertResultIsBOOL(Quartz.IKImageView.hasHorizontalScroller)
        self.assertArgIsBOOL(Quartz.IKImageView.setHasHorizontalScroller_, 0)

        self.assertResultIsBOOL(Quartz.IKImageView.hasVerticalScroller)
        self.assertArgIsBOOL(Quartz.IKImageView.setHasVerticalScroller_, 0)

        self.assertResultIsBOOL(Quartz.IKImageView.autohidesScrollers)
        self.assertArgIsBOOL(Quartz.IKImageView.setAutohidesScrollers_, 0)

        self.assertResultIsBOOL(Quartz.IKImageView.supportsDragAndDrop)
        self.assertArgIsBOOL(Quartz.IKImageView.setSupportsDragAndDrop_, 0)

        self.assertResultIsBOOL(Quartz.IKImageView.editable)
        self.assertArgIsBOOL(Quartz.IKImageView.setEditable_, 0)

        self.assertResultIsBOOL(Quartz.IKImageView.doubleClickOpensImageEditPanel)
        self.assertArgIsBOOL(Quartz.IKImageView.setDoubleClickOpensImageEditPanel_, 0)
