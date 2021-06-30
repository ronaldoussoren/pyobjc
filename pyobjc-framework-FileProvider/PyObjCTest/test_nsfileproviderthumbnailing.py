import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderThumbnailing(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.fetchThumbnailsForItemIdentifiers_requestedSize_perThumbnailCompletionHandler_completionHandler_,  # noqa: B950
            2,
            b"v@@@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.fetchThumbnailsForItemIdentifiers_requestedSize_perThumbnailCompletionHandler_completionHandler_,  # noqa: B950
            3,
            b"v@",
        )
