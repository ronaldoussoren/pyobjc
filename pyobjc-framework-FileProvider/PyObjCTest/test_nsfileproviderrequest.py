import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderRequest(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(FileProvider.NSFileProviderRequest.isSystemRequest)
        self.assertResultIsBOOL(FileProvider.NSFileProviderRequest.isFileViewerRequest)

        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.lookupRequestingApplicationIdentifier_reason_completionHandler_,
            2,
            b"v@@",
        )
