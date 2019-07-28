from PyObjCTools.TestSupport import *

import FileProvider

class TestNSFileProviderManager (TestCase):
    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderDownloadPolicyDefault, 0)
        self.assertEqual(FileProvider.NSFileProviderDownloadPolicySpeculative, 1)
        self.assertEqual(FileProvider.NSFileProviderDownloadPolicyKeepDownloaded, 2)

    @min_os_level('10.15')
    def test_methods10_15(self):
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.signalEnumeratorForContainerItemIdentifier_completionHandler_, 1, b'v@')
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.registerURLSessionTask_forItemWithIdentifier_completionHandler_, 2, b'v@')
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.getUserVisibleURLForItemIdentifier_completionHandler_, 1, b'v@@')
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.getIdentifierForUserVisibleFileAtURL_completionHandler_, 1, b'v@@@')

        self.assertResultIsBOOL(FileProvider.NSFileProviderManager.writePlaceholderAtURL_withMetadata_error_)
        self.assertArgIsOut(FileProvider.NSFileProviderManager.writePlaceholderAtURL_withMetadata_error_, 2)

        self.assertArgIsBlock(FileProvider.NSFileProviderManager.addDomain_completionHandler_, 1, b'v@')
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.removeDomain_completionHandler_, 1, b'v@')
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.getDomainsWithCompletionHandler_, 0, b'v@@')
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.removeAllDomainsWithCompletionHandler_, 0, b'v@')
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.importDomain_fromDirectoryAtURL_completionHandler_, 2, b'v@')
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.reimportItemsBelowItemWithIdentifier_completionHandler_, 1, b'v@')
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.setDownloadPolicy_forItemWithIdentifier_completionHandler_, 2, b'v@')
        self.assertArgIsBlock(FileProvider.NSFileProviderManager.evictItemWithIdentifier_completionHandler_, 1, b'v@')
