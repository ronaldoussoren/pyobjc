import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSPrinter(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSPrinterTableOK, 0)
        self.assertEqual(AppKit.NSPrinterTableNotFound, 1)
        self.assertEqual(AppKit.NSPrinterTableError, 2)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSPrinter.isKey_inTable_)
        self.assertResultIsBOOL(AppKit.NSPrinter.booleanForKey_inTable_)
        self.assertResultIsBOOL(AppKit.NSPrinter.acceptsBinary)
        self.assertResultIsBOOL(AppKit.NSPrinter.isColor)
        self.assertResultIsBOOL(AppKit.NSPrinter.isFontAvailable_)
        self.assertResultIsBOOL(AppKit.NSPrinter.isOutputStackInReverseOrder)
        self.assertArgIsBOOL(
            AppKit.NSPrinter.printerWithName_domain_includeUnavailable_, 2
        )
