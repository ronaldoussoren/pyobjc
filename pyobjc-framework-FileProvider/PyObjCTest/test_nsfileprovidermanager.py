import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSFileProviderManagerHelper(FileProvider.NSObject):
    def refreshInterval(self):
        return 1


class TestNSFileProviderManager(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(FileProvider.NSFileProviderDomainRemovalMode)
        self.assertIsEnumType(FileProvider.NSFileProviderManagerDisconnectionOptions)

    def test_constants(self):
        self.assertEqual(
            FileProvider.NSFileProviderManagerDisconnectionOptionsTemporary, 1 << 0
        )

        self.assertEqual(FileProvider.NSFileProviderDomainRemovalModeRemoveAll, 0)
        self.assertEqual(
            FileProvider.NSFileProviderDomainRemovalModePreserveDirtyUserData, 1
        )
        self.assertEqual(
            FileProvider.NSFileProviderDomainRemovalModePreserveDownloadedUserData, 2
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.signalEnumeratorForContainerItemIdentifier_completionHandler_,  # noqa:  B950
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.getUserVisibleURLForItemIdentifier_completionHandler_,  # noqa: B950
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.getIdentifierForUserVisibleFileAtURL_completionHandler_,  # noqa: B950
            1,
            b"v@@@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.registerURLSessionTask_forItemWithIdentifier_completionHandler_,  # noqa: B950
            2,
            b"v@",
        )
        self.assertArgIsOut(
            FileProvider.NSFileProviderManager.temporaryDirectoryURLWithError_,
            0,
        )

        self.assertResultIsBOOL(
            FileProvider.NSFileProviderManager.writePlaceholderAtURL_withMetadata_error_
        )
        self.assertArgIsOut(
            FileProvider.NSFileProviderManager.writePlaceholderAtURL_withMetadata_error_,
            2,
        )

        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.addDomain_completionHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.removeDomain_completionHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.getDomainsWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.removeAllDomainsWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.importDomain_fromDirectoryAtURL_completionHandler_,  # noqa: B950
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.signalErrorResolved_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.reimportItemsBelowItemWithIdentifier_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.evictItemWithIdentifier_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.waitForChangesOnItemsBelowItemWithIdentifier_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.waitForStabilizationWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.disconnectWithReason_options_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.reconnectWithCompletionHandler_,
            0,
            b"v@",
        )

        self.assertResultHasType(
            TestNSFileProviderManagerHelper.refreshInterval, objc._C_DBL
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.removeDomain_mode_completionHandler_,  # noqa:  B950
            2,
            b"v@@",
        )

    @min_sdk_level("11.3")
    def test_protocols(self):
        objc.protocolNamed("NSFileProviderPendingSetEnumerator")
