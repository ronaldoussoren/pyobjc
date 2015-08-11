from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPDFInfo (TestCase):
    @min_os_level('10.9')
    def testMethods(self):
        self.assertResultIsBOOL(NSPDFInfo.isFileExtensionHidden)
        self.assertArgIsBOOL(NSPDFInfo.setFileExtensionHidden_, 0)

if __name__ == "__main__":
    main()
