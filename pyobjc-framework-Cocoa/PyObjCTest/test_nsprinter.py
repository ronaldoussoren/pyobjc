
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPrinter (TestCase):
    def testConstants(self):
        self.assertEqual(NSPrinterTableOK, 0)
        self.assertEqual(NSPrinterTableNotFound, 1)
        self.assertEqual(NSPrinterTableError, 2)

    def testMethods(self):
        self.assertResultIsBOOL(NSPrinter.isKey_inTable_)
        self.assertResultIsBOOL(NSPrinter.booleanForKey_inTable_)
        self.assertResultIsBOOL(NSPrinter.acceptsBinary)
        self.assertResultIsBOOL(NSPrinter.isColor)
        self.assertResultIsBOOL(NSPrinter.isFontAvailable_)
        self.assertResultIsBOOL(NSPrinter.isOutputStackInReverseOrder)
        self.assertArgIsBOOL(NSPrinter.printerWithName_domain_includeUnavailable_, 2)


if __name__ == "__main__":
    main()
