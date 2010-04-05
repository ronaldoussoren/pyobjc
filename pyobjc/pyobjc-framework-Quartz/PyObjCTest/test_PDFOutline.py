
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFOutline (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(PDFOutline.isOpen)
        self.assertArgIsBOOL(PDFOutline.setIsOpen_, 0)

if __name__ == "__main__":
    main()
