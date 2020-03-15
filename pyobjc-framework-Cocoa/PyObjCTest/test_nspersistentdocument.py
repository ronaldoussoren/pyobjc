import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersistentDocument(TestCase):
    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(
            AppKit.NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_modelConfiguration_storeOptions_error_  # noqa: B950
        )
        self.assertArgIsOut(
            AppKit.NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_modelConfiguration_storeOptions_error_,  # noqa: B950
            4,
        )

    def testMethods(self):
        self.assertResultIsBOOL(
            AppKit.NSPersistentDocument.writeToURL_ofType_forSaveOperation_originalContentsURL_error_  # noqa: B950
        )
        self.assertArgIsOut(
            AppKit.NSPersistentDocument.writeToURL_ofType_forSaveOperation_originalContentsURL_error_,  # noqa: B950
            4,
        )

        self.assertResultIsBOOL(AppKit.NSPersistentDocument.readFromURL_ofType_error_)
        self.assertArgIsOut(AppKit.NSPersistentDocument.readFromURL_ofType_error_, 2)

        self.assertResultIsBOOL(
            AppKit.NSPersistentDocument.revertToContentsOfURL_ofType_error_
        )
        self.assertArgIsOut(
            AppKit.NSPersistentDocument.revertToContentsOfURL_ofType_error_, 2
        )

        self.assertResultIsBOOL(
            AppKit.NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_error_
        )
        self.assertArgIsOut(
            AppKit.NSPersistentDocument.configurePersistentStoreCoordinatorForURL_ofType_error_,
            2,
        )
