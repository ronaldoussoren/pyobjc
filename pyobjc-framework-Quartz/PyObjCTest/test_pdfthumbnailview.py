from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFThumbnailView(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.PDFThumbnailView.allowsDragging)
        self.assertArgIsBOOL(Quartz.PDFThumbnailView.setAllowsDragging_, 0)
        self.assertResultIsBOOL(Quartz.PDFThumbnailView.allowsMultipleSelection)
        self.assertArgIsBOOL(Quartz.PDFThumbnailView.setAllowsMultipleSelection_, 0)
