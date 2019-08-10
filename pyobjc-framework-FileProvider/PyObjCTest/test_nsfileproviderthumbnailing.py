from PyObjCTools.TestSupport import *

import FileProvider


class TestNSFileProviderThumbnailing(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.fetchThumbnailsForItemIdentifiers_requestedSize_perThumbnailCompletionHandler_completionHandler_,
            2,
            b"v@@@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.fetchThumbnailsForItemIdentifiers_requestedSize_perThumbnailCompletionHandler_completionHandler_,
            3,
            b"v@",
        )
