
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPrinter (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSPrinterTableOK, 0)
        self.failUnlessEqual(NSPrinterTableNotFound, 1)
        self.failUnlessEqual(NSPrinterTableError, 2)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPrinter.isKey_inTable_)
        self.failUnlessResultIsBOOL(NSPrinter.booleanForKey_inTable_)
        self.failUnlessResultIsBOOL(NSPrinter.acceptsBinary)
        self.failUnlessResultIsBOOL(NSPrinter.isColor)
        self.failUnlessResultIsBOOL(NSPrinter.isFontAvailable_)
        self.failUnlessResultIsBOOL(NSPrinter.isOutputStackInReverseOrder)
        self.failUnlessArgIsBOOL(NSPrinter.printerWithName_domain_includeUnavailable_, 2)


if __name__ == "__main__":
    main()
