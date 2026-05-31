from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFThumbnailView(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFThumbnailView.allowsDragging)
        self.assertArgIsBOOL(Quartz.PDFThumbnailView.setAllowsDragging_, 0)
        self.assertResultIsBOOL(Quartz.PDFThumbnailView.allowsMultipleSelection)
        self.assertArgIsBOOL(Quartz.PDFThumbnailView.setAllowsMultipleSelection_, 0)
