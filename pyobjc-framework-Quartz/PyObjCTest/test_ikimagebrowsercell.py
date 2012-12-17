from Quartz import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str

class TestIKImageBrowserCell (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(IKImageStateNoImage, 0)
        self.assertEqual(IKImageStateInvalid, 1)
        self.assertEqual(IKImageStateReady, 2)

        self.assertIsInstance(IKImageBrowserCellBackgroundLayer, unicode)
        self.assertIsInstance(IKImageBrowserCellForegroundLayer, unicode)
        self.assertIsInstance(IKImageBrowserCellSelectionLayer, unicode)
        self.assertIsInstance(IKImageBrowserCellPlaceHolderLayer, unicode)


    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultHasType(IKImageBrowserCell.frame, NSRect.__typestr__)
        self.assertResultHasType(IKImageBrowserCell.imageContainerFrame, NSRect.__typestr__)
        self.assertResultHasType(IKImageBrowserCell.imageFrame, NSRect.__typestr__)
        self.assertResultHasType(IKImageBrowserCell.selectionFrame, NSRect.__typestr__)
        self.assertResultHasType(IKImageBrowserCell.titleFrame, NSRect.__typestr__)
        self.assertResultHasType(IKImageBrowserCell.subtitleFrame, NSRect.__typestr__)
        self.assertResultIsBOOL(IKImageBrowserCell.isSelected)

if __name__ == "__main__":
    main()
