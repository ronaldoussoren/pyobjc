
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationButtonStamp (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultIsBOOL(PDFAnnotationStamp.isSignature)

if __name__ == "__main__":
    main()
