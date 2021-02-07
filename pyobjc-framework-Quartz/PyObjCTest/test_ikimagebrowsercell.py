from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestIKImageBrowserCell(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Quartz.IKImageStateNoImage, 0)
        self.assertEqual(Quartz.IKImageStateInvalid, 1)
        self.assertEqual(Quartz.IKImageStateReady, 2)

        self.assertIsInstance(Quartz.IKImageBrowserCellBackgroundLayer, str)
        self.assertIsInstance(Quartz.IKImageBrowserCellForegroundLayer, str)
        self.assertIsInstance(Quartz.IKImageBrowserCellSelectionLayer, str)
        self.assertIsInstance(Quartz.IKImageBrowserCellPlaceHolderLayer, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultHasType(
            Quartz.IKImageBrowserCell.frame, Quartz.NSRect.__typestr__
        )
        self.assertResultHasType(
            Quartz.IKImageBrowserCell.imageContainerFrame, Quartz.NSRect.__typestr__
        )
        self.assertResultHasType(
            Quartz.IKImageBrowserCell.imageFrame, Quartz.NSRect.__typestr__
        )
        self.assertResultHasType(
            Quartz.IKImageBrowserCell.selectionFrame, Quartz.NSRect.__typestr__
        )
        self.assertResultHasType(
            Quartz.IKImageBrowserCell.titleFrame, Quartz.NSRect.__typestr__
        )
        self.assertResultHasType(
            Quartz.IKImageBrowserCell.subtitleFrame, Quartz.NSRect.__typestr__
        )
        self.assertResultIsBOOL(Quartz.IKImageBrowserCell.isSelected)
