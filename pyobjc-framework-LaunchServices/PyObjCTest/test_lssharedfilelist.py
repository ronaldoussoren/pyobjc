import os
import warnings

from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import objc

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import LaunchServices


class TestLSSharedFileList(TestCase):
    def testTypes(self):
        self.assertIsCFType(LaunchServices.LSSharedFileListRef)
        self.assertIsCFType(LaunchServices.LSSharedFileListItemRef)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(LaunchServices.kLSSharedFileListFavoriteVolumes, str)
        self.assertIsInstance(LaunchServices.kLSSharedFileListFavoriteItems, str)
        self.assertIsInstance(
            LaunchServices.kLSSharedFileListRecentApplicationItems, str
        )
        self.assertIsInstance(LaunchServices.kLSSharedFileListRecentDocumentItems, str)
        self.assertIsInstance(LaunchServices.kLSSharedFileListRecentServerItems, str)
        self.assertIsInstance(LaunchServices.kLSSharedFileListSessionLoginItems, str)
        self.assertIsInstance(LaunchServices.kLSSharedFileListGlobalLoginItems, str)
        self.assertIsInstance(LaunchServices.kLSSharedFileListRecentItemsMaxAmount, str)
        self.assertIsInstance(
            LaunchServices.kLSSharedFileListVolumesComputerVisible, str
        )
        self.assertIsInstance(LaunchServices.kLSSharedFileListVolumesIDiskVisible, str)
        self.assertIsInstance(
            LaunchServices.kLSSharedFileListVolumesNetworkVisible, str
        )
        self.assertIsInstance(LaunchServices.kLSSharedFileListItemHidden, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(LaunchServices.kLSSharedFileListLoginItemHidden, str)

    @min_os_level("10.5")
    def testMagicConstants10_5(self):
        self.assertIsInstance(
            LaunchServices.kLSSharedFileListItemBeforeFirst,
            LaunchServices.LSSharedFileListItemRef,
        )
        self.assertIsInstance(
            LaunchServices.kLSSharedFileListItemLast,
            LaunchServices.LSSharedFileListItemRef,
        )

    def testConstants(self):
        self.assertEqual(LaunchServices.kLSSharedFileListNoUserInteraction, 1)
        self.assertEqual(LaunchServices.kLSSharedFileListDoNotMountVolumes, 2)

    def testFunctions(self):
        self.assertIsInstance(LaunchServices.LSSharedFileListGetTypeID(), int)
        self.assertIsInstance(LaunchServices.LSSharedFileListItemGetTypeID(), int)

        self.assertResultIsCFRetained(LaunchServices.LSSharedFileListCreate)
        lst = LaunchServices.LSSharedFileListCreate(
            None, LaunchServices.kLSSharedFileListRecentDocumentItems, None
        )
        self.assertIsInstance(lst, LaunchServices.LSSharedFileListRef)

        rl = LaunchServices.CFRunLoopGetCurrent()

        self.assertArgIsFunction(
            LaunchServices.LSSharedFileListAddObserver,
            3,
            b"v^{OpaqueLSSharedFileListRef=}^v",
            True,
        )
        self.assertArgHasType(LaunchServices.LSSharedFileListAddObserver, 4, b"^v")

        @objc.callbackFor(LaunchServices.LSSharedFileListAddObserver)
        def callback(lst, ctxt):
            pass

        LaunchServices.LSSharedFileListAddObserver(
            lst, rl, LaunchServices.kCFRunLoopDefaultMode, callback, None
        )
        LaunchServices.LSSharedFileListRemoveObserver(
            lst, rl, LaunchServices.kCFRunLoopDefaultMode, callback, None
        )

        v = LaunchServices.LSSharedFileListGetSeedValue(lst)
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(LaunchServices.LSSharedFileListCopyProperty)
        self.assertResultHasType(LaunchServices.LSSharedFileListCopyProperty, b"@")
        v = LaunchServices.LSSharedFileListCopyProperty(lst, "pyobjc.name")

        v = LaunchServices.LSSharedFileListSetProperty(lst, "pyobjc.name", "value")
        self.assertIsInstance(v, int)
        v = LaunchServices.LSSharedFileListCopyProperty(lst, "pyobjc.name")
        self.assertEqual(v, "value")

        self.assertArgIsOut(LaunchServices.LSSharedFileListCopySnapshot, 1)
        v, seed = LaunchServices.LSSharedFileListCopySnapshot(lst, None)
        self.assertIsInstance(v, LaunchServices.CFArrayRef)
        self.assertIsInstance(seed, int)

        self.assertResultIsCFRetained(LaunchServices.LSSharedFileListInsertItemURL)
        url = LaunchServices.CFURLCreateWithString(
            None, "file://" + os.path.expanduser("~"), None
        )
        title = "PyObjC.Test"
        item = LaunchServices.LSSharedFileListInsertItemFSRef(
            lst,
            LaunchServices.kLSSharedFileListItemLast,
            title,
            None,
            objc.FSRef.from_pathname(os.path.expanduser("~")),
            None,
            None,
        )
        self.assertIsInstance(item, LaunchServices.LSSharedFileListItemRef)

        item = LaunchServices.LSSharedFileListInsertItemURL(
            lst, LaunchServices.kLSSharedFileListItemLast, title, None, url, None, None
        )
        self.assertIsInstance(item, LaunchServices.LSSharedFileListItemRef)

        v = LaunchServices.LSSharedFileListItemGetID(item)
        self.assertIsInstance(v, int)

        v = LaunchServices.LSSharedFileListItemCopyIconRef(item)
        if v is not None:
            self.assertIsInstance(v, LaunchServices.IconRef)

        self.assertResultIsCFRetained(
            LaunchServices.LSSharedFileListItemCopyDisplayName
        )
        v = LaunchServices.LSSharedFileListItemCopyDisplayName(item)
        self.assertIsInstance(v, str)

        self.assertArgIsOut(LaunchServices.LSSharedFileListItemResolve, 2)
        self.assertArgIsOut(LaunchServices.LSSharedFileListItemResolve, 3)
        self.assertArgIsCFRetained(LaunchServices.LSSharedFileListItemResolve, 2)
        v, url, ref = LaunchServices.LSSharedFileListItemResolve(
            item, 0, None, objc.NULL
        )
        self.assertIsInstance(v, int)
        if url is not None:
            self.assertIsInstance(url, LaunchServices.CFURLRef)

        v = LaunchServices.LSSharedFileListItemSetProperty(
            item, "pyobjc.name", "pyobjc.test"
        )
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(LaunchServices.LSSharedFileListItemCopyProperty)
        v = LaunchServices.LSSharedFileListItemCopyProperty(item, "pyobjc.name")
        if v is not None:
            self.assertEqual(v, "pyobjc.test")

        v = LaunchServices.LSSharedFileListItemMove(
            lst, item, LaunchServices.kLSSharedFileListItemBeforeFirst
        )
        self.assertIsInstance(v, int)

        v = LaunchServices.LSSharedFileListItemRemove(lst, item)
        self.assertIsInstance(v, int)

        LaunchServices.LSSharedFileListRemoveAllItems

    @expectedFailure
    def testMissing(self):
        # Needs more infrastructure
        self.fail("LSSharedFileListSetAuthorization")

        # FSRef suckage
        self.fail("LSSharedFileListItemRef")

    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(
            LaunchServices.LSSharedFileListItemCopyResolvedURL
        )
        self.assertArgIsOut(LaunchServices.LSSharedFileListItemCopyResolvedURL, 2)
