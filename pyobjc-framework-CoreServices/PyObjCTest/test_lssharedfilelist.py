
from PyObjCTools.TestSupport import *
import CoreServices

import os

class TestLSSharedFileList (TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreServices.LSSharedFileListRef)
        self.assertIsCFType(CoreServices.LSSharedFileListItemRef)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(CoreServices.kLSSharedFileListFavoriteVolumes, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListFavoriteItems, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListRecentApplicationItems, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListRecentDocumentItems, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListRecentServerItems, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListSessionLoginItems, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListGlobalLoginItems, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListRecentItemsMaxAmount, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListVolumesComputerVisible, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListVolumesIDiskVisible, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListVolumesNetworkVisible, unicode)
        self.assertIsInstance(CoreServices.kLSSharedFileListItemHidden, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(CoreServices.kLSSharedFileListLoginItemHidden, unicode)

    @min_os_level('10.5')
    def testMagicConstants10_5(self):
        self.assertIsInstance(CoreServices.kLSSharedFileListItemBeforeFirst, CoreServices.LSSharedFileListItemRef)
        self.assertIsInstance(CoreServices.kLSSharedFileListItemLast, CoreServices.LSSharedFileListItemRef)

    def testConstants(self):
        self.assertEqual(CoreServices.kLSSharedFileListNoUserInteraction, 1)
        self.assertEqual(CoreServices.kLSSharedFileListDoNotMountVolumes, 2)

    def testFunctions(self):
        self.assertIsInstance(CoreServices.LSSharedFileListGetTypeID(), (int, long))
        self.assertIsInstance(CoreServices.LSSharedFileListItemGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CoreServices.LSSharedFileListCreate)
        lst = CoreServices.LSSharedFileListCreate(None, CoreServices.kLSSharedFileListRecentDocumentItems, None)
        self.assertIsInstance(lst, CoreServices.LSSharedFileListRef)

        rl = CoreServices.CFRunLoopGetCurrent()

        self.assertArgIsFunction(CoreServices.LSSharedFileListAddObserver, 3, b'v^{OpaqueLSSharedFileListRef=}^v', True)
        self.assertArgHasType(CoreServices.LSSharedFileListAddObserver, 4, b'^v')

        @objc.callbackFor(CoreServices.LSSharedFileListAddObserver)
        def callback(lst, ctxt):
            pass

        CoreServices.LSSharedFileListAddObserver(lst, rl, CoreServices.kCFRunLoopDefaultMode, callback, None)
        CoreServices.LSSharedFileListRemoveObserver(lst, rl, CoreServices.kCFRunLoopDefaultMode, callback, None)

        v = CoreServices.LSSharedFileListGetSeedValue(lst)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(CoreServices.LSSharedFileListCopyProperty)
        self.assertResultHasType(CoreServices.LSSharedFileListCopyProperty, b'@')
        v = CoreServices.LSSharedFileListCopyProperty(lst, b"pyobjc.name".decode('latin1'))

        v = CoreServices.LSSharedFileListSetProperty(lst, b"pyobjc.name".decode('latin1'), b"value".decode('latin1'))
        self.assertIsInstance(v, (int, long))
        v = CoreServices.LSSharedFileListCopyProperty(lst, b"pyobjc.name".decode('latin1'))
        self.assertEqual(v, b"value".decode('latin1'))

        self.assertArgIsOut(CoreServices.LSSharedFileListCopySnapshot, 1)
        v, seed = CoreServices.LSSharedFileListCopySnapshot(lst, None)
        self.assertIsInstance(v, CoreServices.CFArrayRef)
        self.assertIsInstance(seed, (int,long))

        self.assertResultIsCFRetained(CoreServices.LSSharedFileListInsertItemURL)
        url = CoreServices.CFURLCreateWithString(None, "file://" + os.path.expanduser('~'), None)
        title = b"PyObjC.Test".decode("latin1")
        item = CoreServices.LSSharedFileListInsertItemFSRef(lst, CoreServices.kLSSharedFileListItemLast, title, None, objc.FSRef.from_pathname(os.path.expanduser('~')), None, None)
        self.assertIsInstance(item, CoreServices.LSSharedFileListItemRef)

        item = CoreServices.LSSharedFileListInsertItemURL(lst, CoreServices.kLSSharedFileListItemLast, title, None, url, None, None)
        self.assertIsInstance(item, CoreServices.LSSharedFileListItemRef)

        v = CoreServices.LSSharedFileListItemGetID(item)
        self.assertIsInstance(v, (int, long))

        v = CoreServices.LSSharedFileListItemCopyIconRef(item)
        if v is not None:
            self.assertIsInstance(v, CoreServices.IconRef)

        self.assertResultIsCFRetained(CoreServices.LSSharedFileListItemCopyDisplayName)
        v = CoreServices.LSSharedFileListItemCopyDisplayName(item)
        self.assertIsInstance(v, unicode)

        self.assertArgIsOut(CoreServices.LSSharedFileListItemResolve, 2)
        self.assertArgIsOut(CoreServices.LSSharedFileListItemResolve, 3)
        self.assertArgIsCFRetained(CoreServices.LSSharedFileListItemResolve, 2)
        v, url, ref = CoreServices.LSSharedFileListItemResolve(item, 0, None, objc.NULL)
        self.assertIsInstance(v, (int, long))
        if url is not None:
            self.assertIsInstance(url, CoreServices.CFURLRef)

        v = CoreServices.LSSharedFileListItemSetProperty(item, b"pyobjc.name".decode('latin1'), b"pyobjc.test".decode('latin1'))
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(CoreServices.LSSharedFileListItemCopyProperty)
        v = CoreServices.LSSharedFileListItemCopyProperty(item, b"pyobjc.name".decode('latin1'))
        if v is not None:
            self.assertEqual(v, "pyobjc.test")

        v = CoreServices.LSSharedFileListItemMove(lst, item, CoreServices.kLSSharedFileListItemBeforeFirst)
        self.assertIsInstance(v, (int, long))

        v = CoreServices.LSSharedFileListItemRemove(lst, item)
        self.assertIsInstance(v, (int, long))

        CoreServices.LSSharedFileListRemoveAllItems

    @expectedFailure
    def testMissing(self):
        # Needs more infrastructure
        self.fail('LSSharedFileListSetAuthorization')

        # FSRef suckage
        self.fail('LSSharedFileListItemRef')

    @min_os_level('10.10')
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(CoreServices.LSSharedFileListItemCopyResolvedURL)
        self.assertArgIsOut(CoreServices.LSSharedFileListItemCopyResolvedURL, 2)

if __name__ == "__main__":
    main()
