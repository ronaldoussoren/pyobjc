
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFDocumentHelper (NSObject):
    def classForPage(self): return 1
    def classForAnnotationType_(self, a): return 1
    def classForAnnotationClass_(self, a): return 1

class TestPDFDocument (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFPrintPageScaleNone, 0)
        self.assertEqual(kPDFPrintPageScaleToFit, 1)
        self.assertEqual(kPDFPrintPageScaleDownToFit, 2)

        self.assertEqual(kPDFDocumentPermissionsNone, 0)
        self.assertEqual(kPDFDocumentPermissionsUser, 1)
        self.assertEqual(kPDFDocumentPermissionsOwner, 2)

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
        self.assertResultIsBOOL(PDFDocument.allowsFormFieldEntry)
        self.assertResultIsBOOL(PDFDocument.writeToFile_)
        self.assertResultIsBOOL(PDFDocument.writeToFile_withOptions_)
        self.assertResultIsBOOL(PDFDocument.writeToURL_)
        self.assertResultIsBOOL(PDFDocument.writeToURL_withOptions_)
        self.assertResultIsBOOL(PDFDocument.isFinding)

        self.assertResultIsBOOL(PDFDocument.allowsDocumentChanges)
        self.assertResultIsBOOL(PDFDocument.allowsDocumentAssembly)
        self.assertResultIsBOOL(PDFDocument.allowsContentAccessibility)
        self.assertResultIsBOOL(PDFDocument.allowsCommenting)

        self.assertResultHasType(TestPDFDocumentHelper.classForPage, objc._C_CLASS)
        self.assertResultHasType(TestPDFDocumentHelper.classForAnnotationType_, objc._C_CLASS)
        self.assertResultHasType(TestPDFDocumentHelper.classForAnnotationClass_, objc._C_CLASS)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertArgIsBOOL(PDFDocument.printOperationForPrintInfo_scalingMode_autoRotate_, 2)

    def testProtocols(self):
        #self.assertIsInstance(protocols.PDFDocumentNotifications, objc.informal_protocol)
        #self.assertIsInstance(protocols.PDFDocumentDelegate, objc.informal_protocol)
        pass


if __name__ == "__main__":
    main()
