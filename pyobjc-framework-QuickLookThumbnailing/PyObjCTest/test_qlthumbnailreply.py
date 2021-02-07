from PyObjCTools.TestSupport import TestCase, min_os_level

import QuickLookThumbnailing


class TestQLThumbnailReply(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsBlock(
            QuickLookThumbnailing.QLThumbnailReply.replyWithContextSize_drawingBlock_,  # noqa: B950
            1,
            b"Z^{CGContext=}",
        )
        self.assertArgIsBlock(
            QuickLookThumbnailing.QLThumbnailReply.replyWithContextSize_currentContextDrawingBlock_,  # noqa: B950
            1,
            b"Z",
        )
