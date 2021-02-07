import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSFileProviderEnumerationHelper(FileProvider.NSObject):
    def finishEnumeratingChangesUpToSyncAnchor_moreComing_(self, a, b):
        pass

    def currentSyncAnchorWithCompletionHandler_(self, a):
        pass

    def suggestedPageSize(self):
        return 1

    def suggestedBatchSize(self):
        return 1


class TestNSFileProviderEnumeration(TestCase):
    @min_os_level("10.16")
    def test_constants(self):
        self.assertIsInstance(
            FileProvider.NSFileProviderInitialPageSortedByDate, FileProvider.NSData
        )
        self.assertIsInstance(
            FileProvider.NSFileProviderInitialPageSortedByName, FileProvider.NSData
        )

    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("NSFileProviderEnumerationObserver")
        objc.protocolNamed("NSFileProviderChangeObserver")
        objc.protocolNamed("NSFileProviderEnumerator")

    def test_methods(self):
        self.assertArgIsBOOL(
            TestNSFileProviderEnumerationHelper.finishEnumeratingChangesUpToSyncAnchor_moreComing_,  # noqa: B950
            1,
        )
        self.assertArgIsBlock(
            TestNSFileProviderEnumerationHelper.currentSyncAnchorWithCompletionHandler_,
            0,
            b"v",
        )
        self.assertResultHasType(
            TestNSFileProviderEnumerationHelper.suggestedPageSize, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestNSFileProviderEnumerationHelper.suggestedBatchSize, objc._C_NSUInteger
        )

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsOut(
            FileProvider.NSFileProviderExtension.enumeratorForContainerItemIdentifier_error_,
            1,
        )
