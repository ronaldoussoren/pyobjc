from PyObjCTools.TestSupport import TestCase, min_os_level

import Quartz


class TestQLPreviewReply(TestCase):
    @min_os_level("12.0")
    def testMethods(self):
        self.assertArgIsBOOL(
            Quartz.QLPreviewReply.initWithContextSize_isBitmap_drawingBlock_, 1
        )
        self.assertArgIsBlock(
            Quartz.QLPreviewReply.initWithContextSize_isBitmap_drawingBlock_,
            2,
            b"Z^{CGContext=}@o^@",
        )

        self.assertArgIsBlock(
            Quartz.QLPreviewReply.initWithDataOfContentType_contentSize_dataCreationBlock_,
            2,
            b"@@o^@",
        )

        self.assertArgIsBlock(
            Quartz.QLPreviewReply.initForPDFWithPageSize_documentCreationBlock_,
            1,
            b"@@o^@",
        )
