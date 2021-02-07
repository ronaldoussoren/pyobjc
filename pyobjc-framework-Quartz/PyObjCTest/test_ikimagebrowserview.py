from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestIKImageBrowserViewHelper(Quartz.NSObject):
    # IKImageBrowserDataSource
    def numberOfItemsInImageBrowser_(self, b):
        return 1

    def imageBrowser_itemAtIndex_(self, b, i):
        return None

    def imageBrowser_moveItemsAtIndexes_toIndex_(self, b, st, i):
        return False

    def imageBrowser_writeItemsAtIndexes_toPasteboard_(self, b, st, pb):
        return 44

    def numberOfGroupsInImageBrowser_(self, b):
        return 1

    def imageBrowser_groupAtIndex_(self, b, idx):
        return None

    # IKImageBrowserItem
    def imageVersion(self):
        return 1

    def isSelectable(self):
        return True

    # IKImageBrowserDelegate
    def imageBrowser_cellWasDoubleClickedAtIndex_(self, b, idx):
        pass

    def imageBrowser_cellWasRightClickedAtIndex_withEvent_(self, b, idx, e):
        pass


class TestIKImageBrowserView(TestCase):
    @min_os_level("10.5")
    def testProtocols(self):
        # self.assertIsInstance(protocols.IKImageBrowserDataSource, objc.informal_protocol)

        self.assertResultHasType(
            TestIKImageBrowserViewHelper.numberOfItemsInImageBrowser_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestIKImageBrowserViewHelper.imageBrowser_itemAtIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestIKImageBrowserViewHelper.imageBrowser_moveItemsAtIndexes_toIndex_
        )
        self.assertArgHasType(
            TestIKImageBrowserViewHelper.imageBrowser_moveItemsAtIndexes_toIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestIKImageBrowserViewHelper.imageBrowser_writeItemsAtIndexes_toPasteboard_,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestIKImageBrowserViewHelper.numberOfGroupsInImageBrowser_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestIKImageBrowserViewHelper.imageBrowser_groupAtIndex_,
            1,
            objc._C_NSUInteger,
        )

        # self.assertIsInstance(protocols.IKImageBrowserItem, objc.informal_protocol)
        self.assertResultHasType(
            TestIKImageBrowserViewHelper.imageVersion, objc._C_NSUInteger
        )
        self.assertResultIsBOOL(TestIKImageBrowserViewHelper.isSelectable)

        # self.assertIsInstance(protocols.IKImageBrowserDelegate, objc.informal_protocol)
        self.assertArgHasType(
            TestIKImageBrowserViewHelper.imageBrowser_cellWasDoubleClickedAtIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestIKImageBrowserViewHelper.imageBrowser_cellWasRightClickedAtIndex_withEvent_,
            1,
            objc._C_NSUInteger,
        )

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.IKImageBrowserView.constrainsToOriginalSize)
        self.assertArgIsBOOL(Quartz.IKImageBrowserView.setConstrainsToOriginalSize_, 0)
        self.assertArgIsBOOL(
            Quartz.IKImageBrowserView.setSelectionIndexes_byExtendingSelection_, 1
        )
        self.assertResultIsBOOL(Quartz.IKImageBrowserView.allowsMultipleSelection)
        self.assertArgIsBOOL(Quartz.IKImageBrowserView.setAllowsMultipleSelection_, 0)
        self.assertResultIsBOOL(Quartz.IKImageBrowserView.allowsEmptySelection)
        self.assertArgIsBOOL(Quartz.IKImageBrowserView.setAllowsEmptySelection_, 0)
        self.assertResultIsBOOL(Quartz.IKImageBrowserView.allowsReordering)
        self.assertArgIsBOOL(Quartz.IKImageBrowserView.setAllowsReordering_, 0)
        self.assertResultIsBOOL(Quartz.IKImageBrowserView.animates)
        self.assertArgIsBOOL(Quartz.IKImageBrowserView.setAnimates_, 0)

    @min_os_level("10.10")
    def testMethods10_10(self):
        # Method does not exist?
        view = Quartz.IKImageBrowserView.alloc().init()
        self.assertResultIsBOOL(view.isGroupExpandedAtIndex_)

    @min_os_level("10.5")
    def testConstants(self):
        self.assertEqual(Quartz.IKCellsStyleNone, 0)
        self.assertEqual(Quartz.IKCellsStyleShadowed, 1)
        self.assertEqual(Quartz.IKCellsStyleOutlined, 2)
        self.assertEqual(Quartz.IKCellsStyleTitled, 4)
        self.assertEqual(Quartz.IKCellsStyleSubtitled, 8)
        self.assertEqual(Quartz.IKGroupBezelStyle, 0)
        self.assertEqual(Quartz.IKGroupDisclosureStyle, 1)

        self.assertIsInstance(Quartz.IKImageBrowserPathRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserNSURLRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserNSImageRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserCGImageRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserCGImageSourceRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserNSDataRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserNSBitmapImageRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserQTMovieRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserQTMoviePathRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserQCCompositionRepresentationType, str)
        self.assertIsInstance(
            Quartz.IKImageBrowserQCCompositionPathRepresentationType, str
        )
        self.assertIsInstance(Quartz.IKImageBrowserQuickLookPathRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserIconRefPathRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserIconRefRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserBackgroundColorKey, str)
        self.assertIsInstance(Quartz.IKImageBrowserSelectionColorKey, str)
        self.assertIsInstance(Quartz.IKImageBrowserCellsOutlineColorKey, str)
        self.assertIsInstance(Quartz.IKImageBrowserCellsTitleAttributesKey, str)
        self.assertIsInstance(
            Quartz.IKImageBrowserCellsHighlightedTitleAttributesKey, str
        )
        self.assertIsInstance(Quartz.IKImageBrowserCellsSubtitleAttributesKey, str)
        self.assertIsInstance(Quartz.IKImageBrowserGroupRangeKey, str)
        self.assertIsInstance(Quartz.IKImageBrowserGroupBackgroundColorKey, str)
        self.assertIsInstance(Quartz.IKImageBrowserGroupTitleKey, str)
        self.assertIsInstance(Quartz.IKImageBrowserGroupStyleKey, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Quartz.IKImageBrowserDropOn, 0)
        self.assertEqual(Quartz.IKImageBrowserDropBefore, 1)

        self.assertIsInstance(Quartz.IKImageBrowserPDFPageRepresentationType, str)
        self.assertIsInstance(Quartz.IKImageBrowserGroupHeaderLayer, str)
        self.assertIsInstance(Quartz.IKImageBrowserGroupHeaderLayer, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Quartz.IKImageBrowserView.canControlQuickLookPanel)
        self.assertArgIsBOOL(Quartz.IKImageBrowserView.setCanControlQuickLookPanel_, 0)
        self.assertResultIsBOOL(Quartz.IKImageBrowserView.allowsDroppingOnItems)
        self.assertArgIsBOOL(Quartz.IKImageBrowserView.setAllowsDroppingOnItems_, 0)
