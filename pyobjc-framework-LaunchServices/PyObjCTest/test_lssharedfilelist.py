
from PyObjCTools.TestSupport import *
from LaunchServices import *

import os

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

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kLSSharedFileListLoginItemHidden, unicode)

    @min_os_level('10.5')
    def testMagicConstants10_5(self):
        self.assertIsInstance(kLSSharedFileListItemBeforeFirst, LSSharedFileListItemRef)
        self.assertIsInstance(kLSSharedFileListItemLast, LSSharedFileListItemRef)

    def testConstants(self):
        self.assertEqual(kLSSharedFileListNoUserInteraction, 1)
        self.assertEqual(kLSSharedFileListDoNotMountVolumes, 2)

    def testFunctions(self):
        print(1)
        self.assertIsInstance(LSSharedFileListGetTypeID(), (int, long))
        print(2)
        self.assertIsInstance(LSSharedFileListItemGetTypeID(), (int, long))
        print(3)

        self.assertResultIsCFRetained(LSSharedFileListCreate)
        print(4)
        lst = LSSharedFileListCreate(None, kLSSharedFileListRecentDocumentItems, None)
        print(5)
        self.assertIsInstance(lst, LSSharedFileListRef)
        print(6)

        rl = CFRunLoopGetCurrent()
        print(7)


        self.assertArgIsFunction(LSSharedFileListAddObserver, 3, b'v^{OpaqueLSSharedFileListRef=}^v', True)
        print(8)
        self.assertArgHasType(LSSharedFileListAddObserver, 4, b'^v')
        print(9)

        @objc.callbackFor(LSSharedFileListAddObserver)
        def callback(lst, ctxt):
            pass
        print(10)

        print(11)
        LSSharedFileListAddObserver(lst, rl, kCFRunLoopDefaultMode, callback, None)
        print(12)
        LSSharedFileListRemoveObserver(lst, rl, kCFRunLoopDefaultMode, callback, None)
        print(13)

        v = LSSharedFileListGetSeedValue(lst)
        print(14)
        self.assertIsInstance(v, (int, long))
        print(15)

        self.assertResultIsCFRetained(LSSharedFileListCopyProperty)
        print(16)
        self.assertResultHasType(LSSharedFileListCopyProperty, b'@')
        print(17)
        v = LSSharedFileListCopyProperty(lst, b"pyobjc.name".decode('latin1'))
        print(18)

        v = LSSharedFileListSetProperty(lst, b"pyobjc.name".decode('latin1'), b"value".decode('latin1'))
        print(19)
        self.assertIsInstance(v, (int, long))
        v = LSSharedFileListCopyProperty(lst, b"pyobjc.name".decode('latin1'))
        print(20)
        self.assertEqual(v, b"value".decode('latin1'))

        self.assertArgIsOut(LSSharedFileListCopySnapshot, 1)
        v, seed = LSSharedFileListCopySnapshot(lst, None)
        print(21)
        self.assertIsInstance(v, CFArrayRef)
        self.assertIsInstance(seed, (int,long))

        self.assertResultIsCFRetained(LSSharedFileListInsertItemURL)
        url = CFURLCreateWithString(None, "file://" + os.path.expanduser('~'), None)
        print (22)
        title = b"PyObjC.Test".decode("latin1")
        item = LSSharedFileListInsertItemFSRef(lst, kLSSharedFileListItemLast, title, None, objc.FSRef.from_pathname(os.path.expanduser('~')), None, None)
        print(23)
        #self.assertIsInstance(item, LSSharedFileListItemRef)

        item = LSSharedFileListInsertItemURL(lst, kLSSharedFileListItemLast, title, None, url, None, None)
        self.assertIsInstance(item, LSSharedFileListItemRef)

        v = LSSharedFileListItemGetID(item)
        print (24)
        self.assertIsInstance(v, (int, long))

        v = LSSharedFileListItemCopyIconRef(item)
        print(25)
        if v is not None:
            self.assertIsInstance(v, IconRef)

        self.assertResultIsCFRetained(LSSharedFileListItemCopyDisplayName)
        v = LSSharedFileListItemCopyDisplayName(item)
        print(26)
        self.assertIsInstance(v, unicode)

        self.assertArgIsOut(LSSharedFileListItemResolve, 2)
        self.assertArgIsOut(LSSharedFileListItemResolve, 3)
        self.assertArgIsCFRetained(LSSharedFileListItemResolve, 2)
        print(27)
        v, url, ref = LSSharedFileListItemResolve(item, 0, None, objc.NULL)
        print(28)
        self.assertIsInstance(v, (int, long))
        if url is not None:
            self.assertIsInstance(url, CFURLRef)
        print(94)

        v = LSSharedFileListItemSetProperty(item, b"pyobjc.name".decode('latin1'), b"pyobjc.test".decode('latin1'))
        self.assertIsInstance(v, (int, long))
        print(95)

        self.assertResultIsCFRetained(LSSharedFileListItemCopyProperty)
        v = LSSharedFileListItemCopyProperty(item, b"pyobjc.name".decode('latin1'))
        if v is not None:
            self.assertEqual(v, "pyobjc.test")
        print(96)

        v = LSSharedFileListItemMove(lst, item, kLSSharedFileListItemBeforeFirst)
        self.assertIsInstance(v, (int, long))
        print(97)

        v = LSSharedFileListItemRemove(lst, item)
        self.assertIsInstance(v, (int, long))
        print(98)


        LSSharedFileListRemoveAllItems
        print(99)

    @expectedFailure
    def testMissing(self):
        # Needs more infrastructure
        self.fail('LSSharedFileListSetAuthorization')

        # FSRef suckage
        self.fail('LSSharedFileListItemRef')

    @min_os_level('10.10')
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(LSSharedFileListItemCopyResolvedURL)
        self.assertArgIsOut(LSSharedFileListItemCopyResolvedURL, 2)

if __name__ == "__main__":
    main()
