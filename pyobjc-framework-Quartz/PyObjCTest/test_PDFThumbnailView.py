
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFThumbnailView (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(PDFThumbnailView.allowsDragging)
        self.failUnlessArgIsBOOL(PDFThumbnailView.setAllowsDragging_, 0)
        self.failUnlessResultIsBOOL(PDFThumbnailView.allowsMultipleSelection)
        self.failUnlessArgIsBOOL(PDFThumbnailView.setAllowsMultipleSelection_, 0)

if __name__ == "__main__":
    main()
