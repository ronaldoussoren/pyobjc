import objc
from PyObjCTools.TestSupport import TestCase, min_os_level
import FinderSync


class TestFinderSyncHelper(FinderSync.NSObject):
    def valuesForAttributes_forItemWithURL_completion_(self, at, iu, com):
        pass

    def makeListenerEndpointForServiceName_itemURL_andReturnError_(self, a, b, c):
        pass


class TestFinderSync(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(FinderSync.FIMenuKind)

    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(FinderSync.FIFinderSyncController, objc.objc_class)
        self.assertIsInstance(FinderSync.FIFinderSync, objc.objc_class)

    @min_os_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("FIFinderSync")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestFinderSyncHelper.valuesForAttributes_forItemWithURL_completion_,
            2,
            b"v@@",
        )

        self.assertArgIsOut(
            TestFinderSyncHelper.makeListenerEndpointForServiceName_itemURL_andReturnError_,
            2,
        )

    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(FinderSync.FIMenuKindContextualMenuForItems, 0)
        self.assertEqual(FinderSync.FIMenuKindContextualMenuForContainer, 1)
        self.assertEqual(FinderSync.FIMenuKindContextualMenuForSidebar, 2)
        self.assertEqual(FinderSync.FIMenuKindToolbarItemMenu, 3)

    @min_os_level("10.13")
    def testMethods(self):
        self.assertArgIsBlock(
            FinderSync.FIFinderSyncController.setLastUsedDate_forItemWithURL_completion_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            FinderSync.FIFinderSyncController.setTagData_forItemWithURL_completion_,
            2,
            b"v@",
        )

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertResultIsBOOL(FinderSync.FIFinderSyncController.isExtensionEnabled)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(FinderSync)
