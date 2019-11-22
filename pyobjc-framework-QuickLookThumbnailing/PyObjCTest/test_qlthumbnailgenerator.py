import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import QuickLookThumbnailing

    class TestQLThumbnailGenerator(TestCase):
        @min_os_level("10.15")
        def test_methods(self):
            self.assertArgIsBlock(
                QuickLookThumbnailing.QLThumbnailGenerator.generateBestRepresentationForRequest_completionHandler_,
                1,
                b"v@@",
            )
            self.assertArgIsBlock(
                QuickLookThumbnailing.QLThumbnailGenerator.generateRepresentationsForRequest_updateHandler_,
                1,
                b"v@Q@",
            )
            self.assertArgIsBlock(
                QuickLookThumbnailing.QLThumbnailGenerator.saveBestRepresentationForRequest_toFileAtURL_withContentType_completionHandler_,
                3,
                b"v@",
            )
