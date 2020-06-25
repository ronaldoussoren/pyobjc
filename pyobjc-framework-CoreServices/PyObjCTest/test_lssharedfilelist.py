import os

import CoreServices
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import objc


class TestLSSharedFileList(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreServices.LSSharedFileListRef)
        self.assertIsCFType(CoreServices.LSSharedFileListItemRef)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(CoreServices.kLSSharedFileListFavoriteVolumes, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListFavoriteItems, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListRecentApplicationItems, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListRecentDocumentItems, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListRecentServerItems, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListSessionLoginItems, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListGlobalLoginItems, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListRecentItemsMaxAmount, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListVolumesComputerVisible, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListVolumesIDiskVisible, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListVolumesNetworkVisible, str)
        self.assertIsInstance(CoreServices.kLSSharedFileListItemHidden, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(CoreServices.kLSSharedFileListLoginItemHidden, str)

    @min_os_level("10.5")
    def testMagicConstants10_5(self):
        self.assertIsInstance(
            CoreServices.kLSSharedFileListItemBeforeFirst,
            CoreServices.LSSharedFileListItemRef,
        )
        self.assertIsInstance(
            CoreServices.kLSSharedFileListItemLast, CoreServices.LSSharedFileListItemRef
        )

    def testConstants(self):
        self.assertEqual(CoreServices.kLSSharedFileListNoUserInteraction, 1)
        self.assertEqual(CoreServices.kLSSharedFileListDoNotMountVolumes, 2)

    def testFunctions(self):
        self.assertIsInstance(CoreServices.LSSharedFileListGetTypeID(), int)
        self.assertIsInstance(CoreServices.LSSharedFileListItemGetTypeID(), int)

        self.assertResultIsCFRetained(CoreServices.LSSharedFileListCreate)
        lst = CoreServices.LSSharedFileListCreate(
            None, CoreServices.kLSSharedFileListRecentDocumentItems, None
        )
        self.assertIsInstance(lst, CoreServices.LSSharedFileListRef)

        rl = CoreServices.CFRunLoopGetCurrent()

        self.assertArgIsFunction(
            CoreServices.LSSharedFileListAddObserver,
            3,
            b"v^{OpaqueLSSharedFileListRef=}^v",
            True,
        )
        self.assertArgHasType(CoreServices.LSSharedFileListAddObserver, 4, b"^v")

        @objc.callbackFor(CoreServices.LSSharedFileListAddObserver)
        def callback(lst, ctxt):
            pass

        CoreServices.LSSharedFileListAddObserver(
            lst, rl, CoreServices.kCFRunLoopDefaultMode, callback, None
        )
        CoreServices.LSSharedFileListRemoveObserver(
            lst, rl, CoreServices.kCFRunLoopDefaultMode, callback, None
        )

        v = CoreServices.LSSharedFileListGetSeedValue(lst)
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(CoreServices.LSSharedFileListCopyProperty)
        self.assertResultHasType(CoreServices.LSSharedFileListCopyProperty, b"@")
        v = CoreServices.LSSharedFileListCopyProperty(lst, "pyobjc.name")

        v = CoreServices.LSSharedFileListSetProperty(lst, "pyobjc.name", "value")
        self.assertIsInstance(v, int)
        v = CoreServices.LSSharedFileListCopyProperty(lst, "pyobjc.name")
        self.assertEqual(v, "value")

        self.assertArgIsOut(CoreServices.LSSharedFileListCopySnapshot, 1)
        v, seed = CoreServices.LSSharedFileListCopySnapshot(lst, None)
        self.assertIsInstance(v, CoreServices.CFArrayRef)
        self.assertIsInstance(seed, int)

        self.assertResultIsCFRetained(CoreServices.LSSharedFileListInsertItemURL)
        url = CoreServices.CFURLCreateWithString(
            None, "file://" + os.path.expanduser("~"), None
        )
        title = "PyObjC.Test"
        item = CoreServices.LSSharedFileListInsertItemFSRef(
            lst,
            CoreServices.kLSSharedFileListItemLast,
            title,
            None,
            objc.FSRef.from_pathname(os.path.expanduser("~")),
            None,
            None,
        )
        self.assertIsInstance(item, CoreServices.LSSharedFileListItemRef)

        item = CoreServices.LSSharedFileListInsertItemURL(
            lst, CoreServices.kLSSharedFileListItemLast, title, None, url, None, None
        )
        self.assertIsInstance(item, CoreServices.LSSharedFileListItemRef)

        v = CoreServices.LSSharedFileListItemGetID(item)
        self.assertIsInstance(v, int)

        v = CoreServices.LSSharedFileListItemCopyIconRef(item)
        if v is not None:
            self.assertIsInstance(v, CoreServices.IconRef)

        self.assertResultIsCFRetained(CoreServices.LSSharedFileListItemCopyDisplayName)
        v = CoreServices.LSSharedFileListItemCopyDisplayName(item)
        self.assertIsInstance(v, str)

        self.assertArgIsOut(CoreServices.LSSharedFileListItemResolve, 2)
        self.assertArgIsOut(CoreServices.LSSharedFileListItemResolve, 3)
        self.assertArgIsCFRetained(CoreServices.LSSharedFileListItemResolve, 2)
        v, url, ref = CoreServices.LSSharedFileListItemResolve(item, 0, None, objc.NULL)
        self.assertIsInstance(v, int)
        if url is not None:
            self.assertIsInstance(url, CoreServices.CFURLRef)

        v = CoreServices.LSSharedFileListItemSetProperty(
            item, "pyobjc.name", "pyobjc.test"
        )
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(CoreServices.LSSharedFileListItemCopyProperty)
        v = CoreServices.LSSharedFileListItemCopyProperty(item, "pyobjc.name")
        if v is not None:
            self.assertEqual(v, "pyobjc.test")

        v = CoreServices.LSSharedFileListItemMove(
            lst, item, CoreServices.kLSSharedFileListItemBeforeFirst
        )
        self.assertIsInstance(v, int)

        v = CoreServices.LSSharedFileListItemRemove(lst, item)
        self.assertIsInstance(v, int)

        CoreServices.LSSharedFileListRemoveAllItems

    @expectedFailure
    def testMissing(self):
        # Needs more infrastructure
        self.fail("LSSharedFileListSetAuthorization")

        # FSRef suckage
        self.fail("LSSharedFileListItemRef")

    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(CoreServices.LSSharedFileListItemCopyResolvedURL)
        self.assertArgIsOut(CoreServices.LSSharedFileListItemCopyResolvedURL, 2)
