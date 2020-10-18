import FileProvider
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSFileProviderItemHelper(FileProvider.NSObject):
    def capabilities(self):
        return 1

    def fileSystemFlags(self):
        return 1

    def isUserReadable(self):
        return 1

    def isUserWritable(self):
        return 1

    def isHidden(self):
        return 1

    def isPathExtensionHidden(self):
        return 1

    def isTrashed(self):
        return 1

    def isUploaded(self):
        return 1

    def isUploading(self):
        return 1

    def isDownloaded(self):
        return 1

    def isDownloading(self):
        return 1

    def isExcludedFromSync(self):
        return 1

    def isMostRecentVersionDownloaded(self):
        return 1

    def isShared(self):
        return 1

    def isSharedByCurrentUser(self):
        return 1


class TestNSFileProviderItem(TestCase):
    def test_constants(self):
        self.assertEqual(
            FileProvider.NSFileProviderItemCapabilitiesAllowsReading, 1 << 0
        )
        self.assertEqual(
            FileProvider.NSFileProviderItemCapabilitiesAllowsWriting, 1 << 1
        )
        self.assertEqual(
            FileProvider.NSFileProviderItemCapabilitiesAllowsReparenting, 1 << 2
        )
        self.assertEqual(
            FileProvider.NSFileProviderItemCapabilitiesAllowsRenaming, 1 << 3
        )
        self.assertEqual(
            FileProvider.NSFileProviderItemCapabilitiesAllowsTrashing, 1 << 4
        )
        self.assertEqual(
            FileProvider.NSFileProviderItemCapabilitiesAllowsDeleting, 1 << 5
        )
        self.assertEqual(
            FileProvider.NSFileProviderItemCapabilitiesAllowsEvicting, 1 << 6
        )
        self.assertEqual(
            FileProvider.NSFileProviderItemCapabilitiesAllowsAddingSubItems,
            FileProvider.NSFileProviderItemCapabilitiesAllowsWriting,
        )
        self.assertEqual(
            FileProvider.NSFileProviderItemCapabilitiesAllowsContentEnumerating,
            FileProvider.NSFileProviderItemCapabilitiesAllowsReading,
        )
        self.assertEqual(
            FileProvider.NSFileProviderItemCapabilitiesAllowsAll,
            FileProvider.NSFileProviderItemCapabilitiesAllowsReading
            | FileProvider.NSFileProviderItemCapabilitiesAllowsWriting
            | FileProvider.NSFileProviderItemCapabilitiesAllowsReparenting
            | FileProvider.NSFileProviderItemCapabilitiesAllowsRenaming
            | FileProvider.NSFileProviderItemCapabilitiesAllowsTrashing
            | FileProvider.NSFileProviderItemCapabilitiesAllowsDeleting
            | FileProvider.NSFileProviderItemCapabilitiesAllowsEvicting,
        )

        self.assertEqual(FileProvider.NSFileProviderFileSystemUserExecutable, 1 << 0)
        self.assertEqual(FileProvider.NSFileProviderFileSystemUserReadable, 1 << 1)
        self.assertEqual(FileProvider.NSFileProviderFileSystemUserWritable, 1 << 2)
        self.assertEqual(FileProvider.NSFileProviderFileSystemHidden, 1 << 3)
        self.assertEqual(
            FileProvider.NSFileProviderFileSystemPathExtensionHidden, 1 << 4
        )

        self.assertIsInstance(
            FileProvider.NSFileProviderRootContainerItemIdentifier, str
        )
        self.assertIsInstance(
            FileProvider.NSFileProviderWorkingSetContainerItemIdentifier, str
        )
        self.assertIsInstance(
            FileProvider.NSFileProviderTrashContainerItemIdentifier, str
        )

    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("NSFileProviderItem")

    def test_methods(self):
        self.assertResultHasType(
            TestNSFileProviderItemHelper.capabilities, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestNSFileProviderItemHelper.fileSystemFlags, objc._C_NSUInteger
        )
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isUserReadable)
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isUserWritable)
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isHidden)
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isPathExtensionHidden)
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isTrashed)
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isUploaded)
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isUploading)
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isDownloaded)
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isDownloading)
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isExcludedFromSync)
        self.assertResultIsBOOL(
            TestNSFileProviderItemHelper.isMostRecentVersionDownloaded
        )
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isShared)
        self.assertResultIsBOOL(TestNSFileProviderItemHelper.isSharedByCurrentUser)
