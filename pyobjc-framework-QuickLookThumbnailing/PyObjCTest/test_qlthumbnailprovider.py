import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import QuickLookThumbnailing

    class TestQLThumbnailProvider(TestCase):
        @min_os_level("10.15")
        def test_methods(self):
            self.assertArgIsBlock(
                QuickLookThumbnailing.QLThumbnailProvider.provideThumbnailForFileRequest_completionHandler_,
                1,
                b"v@@",
            )
