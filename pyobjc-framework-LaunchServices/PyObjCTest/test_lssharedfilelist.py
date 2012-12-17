
from PyObjCTools.TestSupport import *
from LaunchServices import *

try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str

class TestLSSharedFileList (TestCase):
    def testTypes(self):
        self.assertIsCFType(LSSharedFileListRef)
        self.assertIsCFType(LSSharedFileListItemRef)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kLSSharedFileListFavoriteVolumes, unicode)
        self.assertIsInstance(kLSSharedFileListFavoriteItems, unicode)
        self.assertIsInstance(kLSSharedFileListRecentApplicationItems, unicode)
        self.assertIsInstance(kLSSharedFileListRecentDocumentItems, unicode)
        self.assertIsInstance(kLSSharedFileListRecentServerItems, unicode)
        self.assertIsInstance(kLSSharedFileListSessionLoginItems, unicode)
        self.assertIsInstance(kLSSharedFileListGlobalLoginItems, unicode)
        self.assertIsInstance(kLSSharedFileListRecentItemsMaxAmount, unicode)
        self.assertIsInstance(kLSSharedFileListVolumesComputerVisible, unicode)
        self.assertIsInstance(kLSSharedFileListVolumesIDiskVisible, unicode)
        self.assertIsInstance(kLSSharedFileListVolumesNetworkVisible, unicode)
        self.assertIsInstance(kLSSharedFileListItemHidden, unicode)

    @min_os_level('10.5')
    def testMagicConstants10_5(self):
        self.assertIsInstance(kLSSharedFileListItemBeforeFirst, LSSharedFileListItemRef)
        self.assertIsInstance(kLSSharedFileListItemLast, LSSharedFileListItemRef)

    def testConstants(self):
        self.assertEqual(kLSSharedFileListNoUserInteraction, 1)
        self.assertEqual(kLSSharedFileListDoNotMountVolumes, 2)

    def testFunctions(self):
        self.assertIsInstance(LSSharedFileListGetTypeID(), (int, long))
        self.assertIsInstance(LSSharedFileListItemGetTypeID(), (int, long))

        self.assertResultIsCFRetained(LSSharedFileListCreate)
        lst = LSSharedFileListCreate(None, kLSSharedFileListFavoriteItems, None)
        self.assertIsInstance(lst, LSSharedFileListRef)

        rl = CFRunLoopGetCurrent()


        self.assertArgIsFunction(LSSharedFileListAddObserver, 3, b'v^{OpaqueLSSharedFileListRef=}^v', True)
        self.assertArgHasType(LSSharedFileListAddObserver, 4, b'^v')

        @objc.callbackFor(LSSharedFileListAddObserver)
        def callback(lst, ctxt):
            pass

        LSSharedFileListAddObserver(lst, rl, kCFRunLoopDefaultMode, callback, None)
        LSSharedFileListRemoveObserver(lst, rl, kCFRunLoopDefaultMode, callback, None)

        v = LSSharedFileListGetSeedValue(lst)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(LSSharedFileListCopyProperty)
        self.assertResultHasType(LSSharedFileListCopyProperty, b'@')
        v = LSSharedFileListCopyProperty(lst, b"pyobjc.name".decode('latin1'))

        v = LSSharedFileListSetProperty(lst, b"pyobjc.name".decode('latin1'), b"value".decode('latin1'))
        self.assertIsInstance(v, (int, long))
        v = LSSharedFileListCopyProperty(lst, b"pyobjc.name".decode('latin1'))
        self.assertEqual(v, b"value".decode('latin1'))

        self.assertArgIsOut(LSSharedFileListCopySnapshot, 1)
        v, seed = LSSharedFileListCopySnapshot(lst, None)
        self.assertIsInstance(v, CFArrayRef)
        self.assertIsInstance(seed, (int,long))

        self.assertResultIsCFRetained(LSSharedFileListInsertItemURL)
        item = LSSharedFileListInsertItemURL(lst, kLSSharedFileListItemLast, b"PyObjC.Test".decode('latin1'), None,
                CFURLCreateWithString(None, "file:///etc/hosts", None), {}, [])
        self.assertIsInstance(item, LSSharedFileListItemRef)

        v = LSSharedFileListItemGetID(item)
        self.assertIsInstance(v, (int, long))

        v = LSSharedFileListItemCopyIconRef(item)
        if v is not None:
            self.assertIsInstance(v, IconRef)

        self.assertResultIsCFRetained(LSSharedFileListItemCopyDisplayName)
        v = LSSharedFileListItemCopyDisplayName(item)
        self.assertIsInstance(v, unicode)

        self.assertArgIsOut(LSSharedFileListItemResolve, 2)
        self.assertArgIsOut(LSSharedFileListItemResolve, 3)
        self.assertArgIsCFRetained(LSSharedFileListItemResolve, 2)
        v, url, ref = LSSharedFileListItemResolve(item, 0, None, objc.NULL)
        self.assertIsInstance(v, (int, long))
        if url is not None:
            self.assertIsInstance(url, CFURLRef)

        v = LSSharedFileListItemSetProperty(item, b"pyobjc.name".decode('latin1'), b"pyobjc.test".decode('latin1'))
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(LSSharedFileListItemCopyProperty)
        v = LSSharedFileListItemCopyProperty(item, b"pyobjc.name".decode('latin1'))
        if v is not None:
            self.assertEqual(v, "pyobjc.test")

        v = LSSharedFileListItemMove(lst, item, kLSSharedFileListItemBeforeFirst)
        self.assertIsInstance(v, (int, long))

        v = LSSharedFileListItemRemove(lst, item)
        self.assertIsInstance(v, (int, long))

        v = LSSharedFileListRemoveAllItems(lst)
        self.assertIsInstance(v, (int, long))




    @expectedFailure
    def testMissing(self):
        # Needs more infrastructure
        self.fail('LSSharedFileListSetAuthorization')

        # FSRef suckage
        self.fail('LSSharedFileListItemRef')










if __name__ == "__main__":
    main()
