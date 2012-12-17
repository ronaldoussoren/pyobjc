
from PyObjCTools.TestSupport import *
from Quartz import *

try:
    unicode
except NameError:
    unicode = str

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
    @min_os_level('10.5')
    def testProtocols(self):
        self.assertIsInstance(protocols.IKImageBrowserDataSource, objc.informal_protocol)

        self.assertResultHasType(TestIKImageBrowserViewHelper.numberOfItemsInImageBrowser_, objc._C_NSUInteger)
        self.assertArgHasType(TestIKImageBrowserViewHelper.imageBrowser_itemAtIndex_, 1, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestIKImageBrowserViewHelper.imageBrowser_moveItemsAtIndexes_toIndex_)
        self.assertArgHasType(TestIKImageBrowserViewHelper.imageBrowser_moveItemsAtIndexes_toIndex_, 2, objc._C_NSUInteger)
        self.assertResultHasType(TestIKImageBrowserViewHelper.imageBrowser_writeItemsAtIndexes_toPasteboard_, objc._C_NSUInteger)
        self.assertResultHasType(TestIKImageBrowserViewHelper.numberOfGroupsInImageBrowser_, objc._C_NSUInteger)
        self.assertArgHasType(TestIKImageBrowserViewHelper.imageBrowser_groupAtIndex_, 1, objc._C_NSUInteger)

        self.assertIsInstance(protocols.IKImageBrowserItem, objc.informal_protocol)
        self.assertResultHasType(TestIKImageBrowserViewHelper.imageVersion, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestIKImageBrowserViewHelper.isSelectable)

        self.assertIsInstance(protocols.IKImageBrowserDelegate, objc.informal_protocol)
        self.assertArgHasType(TestIKImageBrowserViewHelper.imageBrowser_cellWasDoubleClickedAtIndex_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestIKImageBrowserViewHelper.imageBrowser_cellWasRightClickedAtIndex_withEvent_, 1, objc._C_NSUInteger)

    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(IKImageBrowserView.constrainsToOriginalSize)
        self.assertArgIsBOOL(IKImageBrowserView.setConstrainsToOriginalSize_, 0)
        self.assertArgIsBOOL(IKImageBrowserView.setSelectionIndexes_byExtendingSelection_, 1)
        self.assertResultIsBOOL(IKImageBrowserView.allowsMultipleSelection)
        self.assertArgIsBOOL(IKImageBrowserView.setAllowsMultipleSelection_, 0)
        self.assertResultIsBOOL(IKImageBrowserView.allowsEmptySelection)
        self.assertArgIsBOOL(IKImageBrowserView.setAllowsEmptySelection_, 0)
        self.assertResultIsBOOL(IKImageBrowserView.allowsReordering)
        self.assertArgIsBOOL(IKImageBrowserView.setAllowsReordering_, 0)
        self.assertResultIsBOOL(IKImageBrowserView.animates)
        self.assertArgIsBOOL(IKImageBrowserView.setAnimates_, 0)

        # Method does not exist?
        #view = IKImageBrowserView.alloc().init()
        #self.assertResultIsBOOL(view.isGroupExpandedAtIndex_)

    @min_os_level('10.5')
    def testConstants(self):
        self.assertEqual(IKCellsStyleNone, 0)
        self.assertEqual(IKCellsStyleShadowed, 1)
        self.assertEqual(IKCellsStyleOutlined, 2)
        self.assertEqual(IKCellsStyleTitled, 4)
        self.assertEqual(IKCellsStyleSubtitled, 8)
        self.assertEqual(IKGroupBezelStyle, 0)
        self.assertEqual(IKGroupDisclosureStyle, 1)

        self.assertIsInstance(IKImageBrowserPathRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserNSURLRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserNSImageRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserCGImageRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserCGImageSourceRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserNSDataRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserNSBitmapImageRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserQTMovieRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserQTMoviePathRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserQCCompositionRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserQCCompositionPathRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserQuickLookPathRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserIconRefPathRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserIconRefRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserBackgroundColorKey, unicode)
        self.assertIsInstance(IKImageBrowserSelectionColorKey, unicode)
        self.assertIsInstance(IKImageBrowserCellsOutlineColorKey, unicode)
        self.assertIsInstance(IKImageBrowserCellsTitleAttributesKey, unicode)
        self.assertIsInstance(IKImageBrowserCellsHighlightedTitleAttributesKey, unicode)
        self.assertIsInstance(IKImageBrowserCellsSubtitleAttributesKey, unicode)
        self.assertIsInstance(IKImageBrowserGroupRangeKey, unicode)
        self.assertIsInstance(IKImageBrowserGroupBackgroundColorKey, unicode)
        self.assertIsInstance(IKImageBrowserGroupTitleKey, unicode)
        self.assertIsInstance(IKImageBrowserGroupStyleKey, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(IKImageBrowserDropOn, 0)
        self.assertEqual(IKImageBrowserDropBefore, 1)

        self.assertIsInstance(IKImageBrowserPDFPageRepresentationType, unicode)
        self.assertIsInstance(IKImageBrowserGroupHeaderLayer, unicode)
        self.assertIsInstance(IKImageBrowserGroupHeaderLayer, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(IKImageBrowserView.canControlQuickLookPanel)
        self.assertArgIsBOOL(IKImageBrowserView.setCanControlQuickLookPanel_, 0)
        self.assertResultIsBOOL(IKImageBrowserView.allowsDroppingOnItems)
        self.assertArgIsBOOL(IKImageBrowserView.setAllowsDroppingOnItems_, 0)

if __name__ == "__main__":
    main()
