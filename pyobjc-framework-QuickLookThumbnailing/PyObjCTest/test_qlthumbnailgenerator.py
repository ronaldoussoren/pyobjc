from PyObjCTools.TestSupport import TestCase, min_os_level

import QuickLookThumbnailing


class TestQLThumbnailGenerator(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsBlock(
            QuickLookThumbnailing.QLThumbnailGenerator.generateBestRepresentationForRequest_completionHandler_,  # noqa: B950
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            QuickLookThumbnailing.QLThumbnailGenerator.generateRepresentationsForRequest_updateHandler_,  # noqa: B950
            1,
            b"v@Q@",
        )
        self.assertArgIsBlock(
            QuickLookThumbnailing.QLThumbnailGenerator.saveBestRepresentationForRequest_toFileAtURL_withContentType_completionHandler_,  # noqa: B850
            3,
            b"v@",
        )
