import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderRequest(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(FileProvider.NSFileProviderRequest.isSystemRequest)
        self.assertResultIsBOOL(FileProvider.NSFileProviderRequest.isFileViewerRequest)

        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.lookupRequestingApplicationIdentifier_reason_completionHandler_,
            2,
            b"v@@",
        )
