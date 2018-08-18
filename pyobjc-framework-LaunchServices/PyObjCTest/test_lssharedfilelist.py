
from PyObjCTools.TestSupport import *
import LaunchServices

import os

class TestLSSharedFileList (TestCase):
    def testTypes(self):
        self.assertIsCFType(LaunchServices.LSSharedFileListRef)
        self.assertIsCFType(LaunchServices.LSSharedFileListItemRef)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(LaunchServices.kLSSharedFileListFavoriteVolumes, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListFavoriteItems, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListRecentApplicationItems, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListRecentDocumentItems, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListRecentServerItems, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListSessionLoginItems, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListGlobalLoginItems, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListRecentItemsMaxAmount, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListVolumesComputerVisible, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListVolumesIDiskVisible, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListVolumesNetworkVisible, unicode)
        self.assertIsInstance(LaunchServices.kLSSharedFileListItemHidden, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(LaunchServices.kLSSharedFileListLoginItemHidden, unicode)

    @min_os_level('10.5')
    def testMagicConstants10_5(self):
        self.assertIsInstance(LaunchServices.kLSSharedFileListItemBeforeFirst, LaunchServices.LSSharedFileListItemRef)
        self.assertIsInstance(LaunchServices.kLSSharedFileListItemLast, LaunchServices.LSSharedFileListItemRef)

    def testConstants(self):
        self.assertEqual(LaunchServices.kLSSharedFileListNoUserInteraction, 1)
        self.assertEqual(LaunchServices.kLSSharedFileListDoNotMountVolumes, 2)

    def testFunctions(self):
        self.assertIsInstance(LaunchServices.LSSharedFileListGetTypeID(), (int, long))
        self.assertIsInstance(LaunchServices.LSSharedFileListItemGetTypeID(), (int, long))

        self.assertResultIsCFRetained(LaunchServices.LSSharedFileListCreate)
        lst = LaunchServices.LSSharedFileListCreate(None, LaunchServices.kLSSharedFileListRecentDocumentItems, None)
        self.assertIsInstance(lst, LaunchServices.LSSharedFileListRef)

        rl = LaunchServices.CFRunLoopGetCurrent()

        self.assertArgIsFunction(LaunchServices.LSSharedFileListAddObserver, 3, b'v^{OpaqueLSSharedFileListRef=}^v', True)
        self.assertArgHasType(LaunchServices.LSSharedFileListAddObserver, 4, b'^v')

        @objc.callbackFor(LaunchServices.LSSharedFileListAddObserver)
        def callback(lst, ctxt):
            pass

        LaunchServices.LSSharedFileListAddObserver(lst, rl, LaunchServices.kCFRunLoopDefaultMode, callback, None)
        LaunchServices.LSSharedFileListRemoveObserver(lst, rl, LaunchServices.kCFRunLoopDefaultMode, callback, None)

        v = LaunchServices.LSSharedFileListGetSeedValue(lst)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(LaunchServices.LSSharedFileListCopyProperty)
        self.assertResultHasType(LaunchServices.LSSharedFileListCopyProperty, b'@')
        v = LaunchServices.LSSharedFileListCopyProperty(lst, b"pyobjc.name".decode('latin1'))

        v = LaunchServices.LSSharedFileListSetProperty(lst, b"pyobjc.name".decode('latin1'), b"value".decode('latin1'))
        self.assertIsInstance(v, (int, long))
        v = LaunchServices.LSSharedFileListCopyProperty(lst, b"pyobjc.name".decode('latin1'))
        self.assertEqual(v, b"value".decode('latin1'))

        self.assertArgIsOut(LaunchServices.LSSharedFileListCopySnapshot, 1)
        v, seed = LaunchServices.LSSharedFileListCopySnapshot(lst, None)
        self.assertIsInstance(v, LaunchServices.CFArrayRef)
        self.assertIsInstance(seed, (int,long))

        self.assertResultIsCFRetained(LaunchServices.LSSharedFileListInsertItemURL)
        url = LaunchServices.CFURLCreateWithString(None, "file://" + os.path.expanduser('~'), None)
        title = b"PyObjC.Test".decode("latin1")
        item = LaunchServices.LSSharedFileListInsertItemFSRef(lst, LaunchServices.kLSSharedFileListItemLast, title, None, objc.FSRef.from_pathname(os.path.expanduser('~')), None, None)
        self.assertIsInstance(item, LaunchServices.LSSharedFileListItemRef)

        item = LaunchServices.LSSharedFileListInsertItemURL(lst, LaunchServices.kLSSharedFileListItemLast, title, None, url, None, None)
        self.assertIsInstance(item, LaunchServices.LSSharedFileListItemRef)

        v = LaunchServices.LSSharedFileListItemGetID(item)
        self.assertIsInstance(v, (int, long))

        v = LaunchServices.LSSharedFileListItemCopyIconRef(item)
        if v is not None:
            self.assertIsInstance(v, LaunchServices.IconRef)

        self.assertResultIsCFRetained(LaunchServices.LSSharedFileListItemCopyDisplayName)
        v = LaunchServices.LSSharedFileListItemCopyDisplayName(item)
        self.assertIsInstance(v, unicode)

        self.assertArgIsOut(LaunchServices.LSSharedFileListItemResolve, 2)
        self.assertArgIsOut(LaunchServices.LSSharedFileListItemResolve, 3)
        self.assertArgIsCFRetained(LaunchServices.LSSharedFileListItemResolve, 2)
        v, url, ref = LaunchServices.LSSharedFileListItemResolve(item, 0, None, objc.NULL)
        self.assertIsInstance(v, (int, long))
        if url is not None:
            self.assertIsInstance(url, LaunchServices.CFURLRef)

        v = LaunchServices.LSSharedFileListItemSetProperty(item, b"pyobjc.name".decode('latin1'), b"pyobjc.test".decode('latin1'))
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(LaunchServices.LSSharedFileListItemCopyProperty)
        v = LaunchServices.LSSharedFileListItemCopyProperty(item, b"pyobjc.name".decode('latin1'))
        if v is not None:
            self.assertEqual(v, "pyobjc.test")

        v = LaunchServices.LSSharedFileListItemMove(lst, item, LaunchServices.kLSSharedFileListItemBeforeFirst)
        self.assertIsInstance(v, (int, long))

        v = LaunchServices.LSSharedFileListItemRemove(lst, item)
        self.assertIsInstance(v, (int, long))

        LaunchServices.LSSharedFileListRemoveAllItems

    @expectedFailure
    def testMissing(self):
        # Needs more infrastructure
        self.fail('LSSharedFileListSetAuthorization')

        # FSRef suckage
        self.fail('LSSharedFileListItemRef')

    @min_os_level('10.10')
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(LaunchServices.LSSharedFileListItemCopyResolvedURL)
        self.assertArgIsOut(LaunchServices.LSSharedFileListItemCopyResolvedURL, 2)

if __name__ == "__main__":
    main()
