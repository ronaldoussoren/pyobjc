
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFDocument (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kPDFPrintPageScaleNone, 0)
        self.failUnlessEqual(kPDFPrintPageScaleToFit, 1)
        self.failUnlessEqual(kPDFPrintPageScaleDownToFit, 2)

        self.failUnlessIsInstance(PDFDocumentDidUnlockNotification, unicode)
        self.failUnlessIsInstance(PDFDocumentDidBeginFindNotification, unicode)
        self.failUnlessIsInstance(PDFDocumentDidEndFindNotification, unicode)
        self.failUnlessIsInstance(PDFDocumentDidBeginPageFindNotification, unicode)
        self.failUnlessIsInstance(PDFDocumentDidEndPageFindNotification, unicode)
        self.failUnlessIsInstance(PDFDocumentDidFindMatchNotification, unicode)
        self.failUnlessIsInstance(PDFDocumentDidBeginWriteNotification, unicode)
        self.failUnlessIsInstance(PDFDocumentDidEndWriteNotification, unicode)
        self.failUnlessIsInstance(PDFDocumentDidBeginPageWriteNotification, unicode)
        self.failUnlessIsInstance(PDFDocumentDidEndPageWriteNotification, unicode)
        self.failUnlessIsInstance(PDFDocumentTitleAttribute, unicode)
        self.failUnlessIsInstance(PDFDocumentAuthorAttribute, unicode)
        self.failUnlessIsInstance(PDFDocumentSubjectAttribute, unicode)
        self.failUnlessIsInstance(PDFDocumentCreatorAttribute, unicode)
        self.failUnlessIsInstance(PDFDocumentProducerAttribute, unicode)
        self.failUnlessIsInstance(PDFDocumentCreationDateAttribute, unicode)
        self.failUnlessIsInstance(PDFDocumentModificationDateAttribute, unicode)
        self.failUnlessIsInstance(PDFDocumentKeywordsAttribute, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(PDFDocument.isEncrypted)
        self.failUnlessResultIsBOOL(PDFDocument.isLocked)
        self.failUnlessResultIsBOOL(PDFDocument.unlockWithPassword_)
        self.failUnlessResultIsBOOL(PDFDocument.allowsPrinting)
        self.failUnlessResultIsBOOL(PDFDocument.allowsCopying)
        self.failUnlessResultIsBOOL(PDFDocument.writeToFile_)
        self.failUnlessResultIsBOOL(PDFDocument.writeToFile_withOptions_)
        self.failUnlessResultIsBOOL(PDFDocument.writeToURL_)
        self.failUnlessResultIsBOOL(PDFDocument.writeToURL_withOptions_)
        self.failUnlessResultIsBOOL(PDFDocument.isFinding)

    def testProtocols(self):
        self.failUnlessIsInstance(protocols.PDFDocumentNotifications, objc.informal_protocol)
        self.failUnlessIsInstance(protocols.PDFDocumentDelegate, objc.informal_protocol)


if __name__ == "__main__":
    main()
