
from PyObjCTools.TestSupport import *
from LaunchServices import *

class TestLSSharedFileList (TestCase):
    def testIncomplete(self):
        self.fail("Add header tests for <LaunchServices/LSSharedFileList.h>")

    def testTypes(self):
        self.failUnlessIsCFType(LSSharedFileListRef)
        self.failUnlessIsCFType(LSSharedFileListItemRef)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(kLSSharedFileListFavoriteVolumes, unicode)
        self.failUnlessIsInstance(kLSSharedFileListFavoriteItems, unicode)
        self.failUnlessIsInstance(kLSSharedFileListRecentApplicationItems, unicode)
        self.failUnlessIsInstance(kLSSharedFileListRecentDocumentItems, unicode)
        self.failUnlessIsInstance(kLSSharedFileListRecentServerItems, unicode)
        self.failUnlessIsInstance(kLSSharedFileListSessionLoginItems, unicode)
        self.failUnlessIsInstance(kLSSharedFileListGlobalLoginItems, unicode)
        self.failUnlessIsInstance(kLSSharedFileListRecentItemsMaxAmount, unicode)
        self.failUnlessIsInstance(kLSSharedFileListVolumesComputerVisible, unicode)
        self.failUnlessIsInstance(kLSSharedFileListVolumesIDiskVisible, unicode)
        self.failUnlessIsInstance(kLSSharedFileListVolumesNetworkVisible, unicode)
        self.failUnlessIsInstance(kLSSharedFileListItemBeforeFirst, LSSharedFileListItemRef)
        self.failUnlessIsInstance(kLSSharedFileListItemLast, LSSharedFileListItemRef)
        self.failUnlessIsInstance(kLSSharedFileListItemHidden, unicode)

    def testConstants(self):
        self.failUnlessEqual(kLSSharedFileListNoUserInteraction, 1)
        self.failUnlessEqual(kLSSharedFileListDoNotMountVolumes, 2)

    def testFunctions(self):
        self.failUnlessIsInstance(LSSharedFileListGetTypeID(), (int, long))
        self.failUnlessIsInstance(LSSharedFileListItemGetTypeID(), (int, long))

        self.failUnlessResultIsCFRetained(LSSharedFileListCreate)
        lst = LSSharedFileListCreate(None, kLSSharedFileListFavoriteItems, None)
        self.failUnlessIsInstance(lst, LSSharedFileListRef)

        rl = CFRunLoopGetCurrent()


        self.failUnlessArgIsFunction(LSSharedFileListAddObserver, 3, 'v^{OpaqueLSSharedFileListRef=}^v', True)
        self.failUnlessArgHasType(LSSharedFileListAddObserver, 4, '^v')

        @objc.callbackFor(LSSharedFileListAddObserver)
        def callback(lst, ctxt):
            pass

        LSSharedFileListAddObserver(lst, rl, kCFRunLoopDefaultMode, callback, None)
        LSSharedFileListRemoveObserver(lst, rl, kCFRunLoopDefaultMode, callback, None)

        v = LSSharedFileListGetSeedValue(lst)
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultIsCFRetained(LSSharedFileListCopyProperty)
        self.failUnlessResultHasType(LSSharedFileListCopyProperty, '@')
        v = LSSharedFileListCopyProperty(lst, u"name")

        v = LSSharedFileListSetProperty(lst, u"pyobjc.name", u"value")
        self.failUnlessIsInstance(v, (int, long))
        v = LSSharedFileListCopyProperty(lst, u"name")
        self.failUnlessEqual(v, u"value")

        self.failUnlessArgIsOut(LSSharedFileListCopySnapshot, 1)
        v, seed = LSSharedFileListCopySnapshot(lst, None)
        self.failUnlessIsInstance(v, CFArrayRef)
        self.failUnlessIsInstance(seed, (int,long))

        self.failUnlessResultIsCFRetained(LSSharedFileListInsertItemURL)
        item = LSSharedFileListInsertItemURL(lst, kLSSharedFileListItemLast, "PyObjC.Test", None, 
                CFURLCreateWithString(None, "file:///etc/hosts", None), {}, [])
        self.failUnlessIsInstance(item, LSSharedFileListItemRef)

        v = LSSharedFileListItemGetID(item)
        self.failUnlessIsInstance(v, (int, long))

        v = LSSharedFileListItemCopyIconRef(item)
        self.failUnless(v is None)

        self.failUnlessResultIsCFRetained(LSSharedFileListItemCopyDisplayName)
        v = LSSharedFileListItemCopyDisplayName(item)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessArgIsOut(LSSharedFileListItemResolve, 2)
        self.failUnlessArgIsOut(LSSharedFileListItemResolve, 3)
        self.failUnlessArgIsCFRetained(LSSharedFileListItemResolve, 2)
        v, url, ref = LSSharedFileListItemResolve(item, 0, None, objc.NULL)
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessIsInstance(url, CFURLRef)

        v = LSSharedFileListItemSetProperty(item, u"name", u"pyobjc.test")
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultIsCFRetained(LSSharedFileListItemCopyProperty)
        v = LSSharedFileListItemCopyProperty(item, u"name")
        self.failUnlessEqual(v, "pyobjc.test")

        v = LSSharedFileListItemMove(lst, item, kLSSharedFileListItemBeforeFirst)
        self.failUnlessIsInstance(v, (int, long))

        v = LSSharedFileListItemRemove(lst, item)
        self.failUnlessIsInstance(v, (int, long))

        v = LSSharedFileListRemoveAllItems(lst)
        self.failUnlessIsInstance(v, (int, long))












    def testMissing(self):
        # Needs more infrastructure
        self.fail('LSSharedFileListSetAuthorization')

        # FSRef suckage
        self.fail('LSSharedFileListItemRef')










if __name__ == "__main__":
    main()
