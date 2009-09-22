from Quartz import *
from PyObjCTools.TestSupport import *

class TestIKImageBrowserCell (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(IKImageStateNoImage, 0)
        self.failUnlessEqual(IKImageStateInvalid, 1)
        self.failUnlessEqual(IKImageStateReady, 2)

        self.failUnlessIsInstance(IKImageBrowserCellBackgroundLayer, unicode)
        self.failUnlessIsInstance(IKImageBrowserCellForegroundLayer, unicode)
        self.failUnlessIsInstance(IKImageBrowserCellSelectionLayer, unicode)
        self.failUnlessIsInstance(IKImageBrowserCellPlaceHolderLayer, unicode)


    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultHasType(IKImageBrowserCell.frame, NSRect.__typestr__)
        self.failUnlessResultHasType(IKImageBrowserCell.imageContainerFrame, NSRect.__typestr__)
        self.failUnlessResultHasType(IKImageBrowserCell.imageFrame, NSRect.__typestr__)
        self.failUnlessResultHasType(IKImageBrowserCell.selectionFrame, NSRect.__typestr__)
        self.failUnlessResultHasType(IKImageBrowserCell.titleFrame, NSRect.__typestr__)
        self.failUnlessResultHasType(IKImageBrowserCell.subtitleFrame, NSRect.__typestr__)
        self.failUnlessResultIsBOOL(IKImageBrowserCell.isSelected)

if __name__ == "__main__":
    main()

