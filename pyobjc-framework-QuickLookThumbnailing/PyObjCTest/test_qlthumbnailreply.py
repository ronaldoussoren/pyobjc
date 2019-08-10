import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import QuickLookThumbnailing

    class TestQLThumbnailReply(TestCase):
        @min_os_level("10.15")
        def test_methods(self):
            self.assertArgIsBlock(
                QuickLookThumbnailing.QLThumbnailReply.replyWithContextSize_drawingBlock_,
                1,
                b"Z^{CGContext=}",
            )
            self.assertArgIsBlock(
                QuickLookThumbnailing.QLThumbnailReply.replyWithContextSize_currentContextDrawingBlock_,
                1,
                b"Z",
            )
