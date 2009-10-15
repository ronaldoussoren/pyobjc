
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFOutline (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessResultIsBOOL(PDFOutline.isOpen)
        self.failUnlessArgIsBOOL(PDFOutline.setIsOpen_, 0)

if __name__ == "__main__":
    main()
