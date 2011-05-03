
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFDocument (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFPrintPageScaleNone, 0)
        self.assertEqual(kPDFPrintPageScaleToFit, 1)
        self.assertEqual(kPDFPrintPageScaleDownToFit, 2)

        self.assertIsInstance(PDFDocumentDidUnlockNotification, unicode)
        self.assertIsInstance(PDFDocumentDidBeginFindNotification, unicode)
        self.assertIsInstance(PDFDocumentDidEndFindNotification, unicode)
        self.assertIsInstance(PDFDocumentDidBeginPageFindNotification, unicode)
        self.assertIsInstance(PDFDocumentDidEndPageFindNotification, unicode)
        self.assertIsInstance(PDFDocumentDidFindMatchNotification, unicode)
        self.assertIsInstance(PDFDocumentDidBeginWriteNotification, unicode)
        self.assertIsInstance(PDFDocumentDidEndWriteNotification, unicode)
        self.assertIsInstance(PDFDocumentDidBeginPageWriteNotification, unicode)
        self.assertIsInstance(PDFDocumentDidEndPageWriteNotification, unicode)
        self.assertIsInstance(PDFDocumentTitleAttribute, unicode)
        self.assertIsInstance(PDFDocumentAuthorAttribute, unicode)
        self.assertIsInstance(PDFDocumentSubjectAttribute, unicode)
        self.assertIsInstance(PDFDocumentCreatorAttribute, unicode)
        self.assertIsInstance(PDFDocumentProducerAttribute, unicode)
        self.assertIsInstance(PDFDocumentCreationDateAttribute, unicode)
        self.assertIsInstance(PDFDocumentModificationDateAttribute, unicode)
        self.assertIsInstance(PDFDocumentKeywordsAttribute, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(PDFDocument.isEncrypted)
        self.assertResultIsBOOL(PDFDocument.isLocked)
        self.assertResultIsBOOL(PDFDocument.unlockWithPassword_)
        self.assertResultIsBOOL(PDFDocument.allowsPrinting)
        self.assertResultIsBOOL(PDFDocument.allowsCopying)
        self.assertResultIsBOOL(PDFDocument.writeToFile_)
        self.assertResultIsBOOL(PDFDocument.writeToFile_withOptions_)
        self.assertResultIsBOOL(PDFDocument.writeToURL_)
        self.assertResultIsBOOL(PDFDocument.writeToURL_withOptions_)
        self.assertResultIsBOOL(PDFDocument.isFinding)

    def testProtocols(self):
        self.assertIsInstance(protocols.PDFDocumentNotifications, objc.informal_protocol)
        self.assertIsInstance(protocols.PDFDocumentDelegate, objc.informal_protocol)


if __name__ == "__main__":
    main()
