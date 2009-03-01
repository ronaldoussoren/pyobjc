
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFSelection (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(PDFSelection.drawForPage_withBox_active_, 2)

if __name__ == "__main__":
    main()
