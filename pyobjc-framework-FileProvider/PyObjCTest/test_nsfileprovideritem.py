from PyObjCTools.TestSupport import *

import FileProvider


class TestNSFileProviderItemHelper(FileProvider.NSObject):
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
            | FileProvider.NSFileProviderItemCapabilitiesAllowsDeleting,
        )

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("NSFileProviderItemFlags")
        objc.protocolNamed("NSFileProviderItem")

    def test_methods(self):
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
