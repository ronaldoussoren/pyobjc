
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFThumbnailView (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(PDFThumbnailView.allowsDragging)
        self.assertArgIsBOOL(PDFThumbnailView.setAllowsDragging_, 0)
        self.assertResultIsBOOL(PDFThumbnailView.allowsMultipleSelection)
        self.assertArgIsBOOL(PDFThumbnailView.setAllowsMultipleSelection_, 0)

if __name__ == "__main__":
    main()
