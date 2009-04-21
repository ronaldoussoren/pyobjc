
from PyObjCTools.TestSupport import *
from Quartz.ImageKit import *

class TestIKImageBrowserViewHelper (NSObject):
    # IKImageBrowserDataSource
    def numberOfItemsInImageBrowser_(self, b): return 1
    def imageBrowser_itemAtIndex_(self, b, i): return None
    def imageBrowser_moveItemsAtIndexes_toIndex_(self, b, st, i): return False
    def imageBrowser_writeItemsAtIndexes_toPasteboard_(self, b, st, pb): return 44
    def numberOfGroupsInImageBrowser_(self, b): return 1
    def imageBrowser_groupAtIndex_(self, b, idx): return None

    # IKImageBrowserItem
    def imageVersion(self): return 1
    def isSelectable(self): return True

    # IKImageBrowserDelegate
    def imageBrowser_cellWasDoubleClickedAtIndex_(self, b, idx): pass
    def imageBrowser_cellWasRightClickedAtIndex_withEvent_(self, b, idx, e): pass


class TestIKImageBrowserView (TestCase):
    def testProtocols(self):
        self.failUnlessIsInstance(protocols.IKImageBrowserDataSource, objc.informal_protocol)

        self.failUnlessResultHasType(TestIKImageBrowserViewHelper.numberOfItemsInImageBrowser_, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIKImageBrowserViewHelper.imageBrowser_itemAtIndex_, 1, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestIKImageBrowserViewHelper.imageBrowser_moveItemsAtIndexes_toIndex_)
        self.failUnlessArgHasType(TestIKImageBrowserViewHelper.imageBrowser_moveItemsAtIndexes_toIndex_, 2, objc._C_NSUInteger)
        self.failUnlessResultHasType(TestIKImageBrowserViewHelper.imageBrowser_writeItemsAtIndexes_toPasteboard_, objc._C_NSUInteger)
        self.failUnlessResultHasType(TestIKImageBrowserViewHelper.numberOfGroupsInImageBrowser_, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIKImageBrowserViewHelper.imageBrowser_groupAtIndex_, 1, objc._C_NSUInteger)

        self.failUnlessIsInstance(protocols.IKImageBrowserItem, objc.informal_protocol)
        self.failUnlessResultHasType(TestIKImageBrowserViewHelper.imageVersion, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestIKImageBrowserViewHelper.isSelectable)

        self.failUnlessIsInstance(protocols.IKImageBrowserDelegate, objc.informal_protocol)
        self.failUnlessArgHasType(TestIKImageBrowserViewHelper.imageBrowser_cellWasDoubleClickedAtIndex_, 1, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIKImageBrowserViewHelper.imageBrowser_cellWasRightClickedAtIndex_withEvent_, 1, objc._C_NSUInteger)

    def testMethods(self):
        self.failUnlessResultIsBOOL(IKImageBrowserView.constrainsToOriginalSize)
        self.failUnlessArgIsBOOL(IKImageBrowserView.setConstrainsToOriginalSize_, 0)
        self.failUnlessArgIsBOOL(IKImageBrowserView.setSelectionIndexes_byExtendingSelection_, 1)
        self.failUnlessResultIsBOOL(IKImageBrowserView.allowsMultipleSelection)
        self.failUnlessArgIsBOOL(IKImageBrowserView.setAllowsMultipleSelection_, 0)
        self.failUnlessResultIsBOOL(IKImageBrowserView.allowsEmptySelection)
        self.failUnlessArgIsBOOL(IKImageBrowserView.setAllowsEmptySelection_, 0)
        self.failUnlessResultIsBOOL(IKImageBrowserView.allowsReordering)
        self.failUnlessArgIsBOOL(IKImageBrowserView.setAllowsReordering_, 0)
        self.failUnlessResultIsBOOL(IKImageBrowserView.animates)
        self.failUnlessArgIsBOOL(IKImageBrowserView.setAnimates_, 0)

        # Method does not exist?
        #view = IKImageBrowserView.alloc().init()
        #self.failUnlessResultIsBOOL(view.isGroupExpandedAtIndex_)

    def testConstants(self):
        self.failUnlessEqual(IKCellsStyleNone, 0)
        self.failUnlessEqual(IKCellsStyleShadowed, 1)
        self.failUnlessEqual(IKCellsStyleOutlined, 2)
        self.failUnlessEqual(IKCellsStyleTitled, 4)
        self.failUnlessEqual(IKCellsStyleSubtitled, 8)

        self.failUnlessIsInstance(IKImageBrowserPathRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserNSURLRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserNSImageRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserCGImageRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserCGImageSourceRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserNSDataRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserNSBitmapImageRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserQTMovieRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserQTMoviePathRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserQCCompositionRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserQCCompositionPathRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserQuickLookPathRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserIconRefPathRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserIconRefRepresentationType, unicode)
        self.failUnlessIsInstance(IKImageBrowserBackgroundColorKey, unicode)
        self.failUnlessIsInstance(IKImageBrowserSelectionColorKey, unicode)
        self.failUnlessIsInstance(IKImageBrowserCellsOutlineColorKey, unicode)
        self.failUnlessIsInstance(IKImageBrowserCellsTitleAttributesKey, unicode)
        self.failUnlessIsInstance(IKImageBrowserCellsHighlightedTitleAttributesKey, unicode)
        self.failUnlessIsInstance(IKImageBrowserCellsSubtitleAttributesKey, unicode)
        self.failUnlessIsInstance(IKImageBrowserGroupRangeKey, unicode)
        self.failUnlessIsInstance(IKImageBrowserGroupBackgroundColorKey, unicode)
        self.failUnlessIsInstance(IKImageBrowserGroupTitleKey, unicode)
        self.failUnlessIsInstance(IKImageBrowserGroupStyleKey, unicode)
                                                                                                       


if __name__ == "__main__":
    main()
