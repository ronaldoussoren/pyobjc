
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPrinter (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSPrinterTableOK, 0)
        self.failUnlessEqual(NSPrinterTableNotFound, 1)
        self.failUnlessEqual(NSPrinterTableError, 2)


if __name__ == "__main__":
    main()
