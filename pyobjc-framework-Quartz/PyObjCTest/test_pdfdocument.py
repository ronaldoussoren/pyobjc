from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Quartz
import objc


class TestPDFDocumentHelper(Quartz.NSObject):
    def classForPage(self):
        return 1

    def classForAnnotationType_(self, a):
        return 1

    def classForAnnotationClass_(self, a):
        return 1


class TestPDFDocument(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kPDFPrintPageScaleNone, 0)
        self.assertEqual(Quartz.kPDFPrintPageScaleToFit, 1)
        self.assertEqual(Quartz.kPDFPrintPageScaleDownToFit, 2)

        self.assertEqual(Quartz.kPDFDocumentPermissionsNone, 0)
        self.assertEqual(Quartz.kPDFDocumentPermissionsUser, 1)
        self.assertEqual(Quartz.kPDFDocumentPermissionsOwner, 2)

        self.assertIsInstance(Quartz.PDFDocumentDidUnlockNotification, str)
        self.assertIsInstance(Quartz.PDFDocumentDidBeginFindNotification, str)
        self.assertIsInstance(Quartz.PDFDocumentDidEndFindNotification, str)
        self.assertIsInstance(Quartz.PDFDocumentDidBeginPageFindNotification, str)
        self.assertIsInstance(Quartz.PDFDocumentDidEndPageFindNotification, str)
        self.assertIsInstance(Quartz.PDFDocumentDidFindMatchNotification, str)
        self.assertIsInstance(Quartz.PDFDocumentDidBeginWriteNotification, str)
        self.assertIsInstance(Quartz.PDFDocumentDidEndWriteNotification, str)
        self.assertIsInstance(Quartz.PDFDocumentDidBeginPageWriteNotification, str)
        self.assertIsInstance(Quartz.PDFDocumentDidEndPageWriteNotification, str)
        self.assertIsInstance(Quartz.PDFDocumentTitleAttribute, str)
        self.assertIsInstance(Quartz.PDFDocumentAuthorAttribute, str)
        self.assertIsInstance(Quartz.PDFDocumentSubjectAttribute, str)
        self.assertIsInstance(Quartz.PDFDocumentCreatorAttribute, str)
        self.assertIsInstance(Quartz.PDFDocumentProducerAttribute, str)
        self.assertIsInstance(Quartz.PDFDocumentCreationDateAttribute, str)
        self.assertIsInstance(Quartz.PDFDocumentModificationDateAttribute, str)
        self.assertIsInstance(Quartz.PDFDocumentKeywordsAttribute, str)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(Quartz.PDFDocumentOwnerPasswordOption, str)
        self.assertIsInstance(Quartz.PDFDocumentUserPasswordOption, str)

    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFDocument.isEncrypted)
        self.assertResultIsBOOL(Quartz.PDFDocument.isLocked)
        self.assertResultIsBOOL(Quartz.PDFDocument.unlockWithPassword_)
        self.assertResultIsBOOL(Quartz.PDFDocument.allowsPrinting)
        self.assertResultIsBOOL(Quartz.PDFDocument.allowsCopying)
        self.assertResultIsBOOL(Quartz.PDFDocument.writeToFile_)
        self.assertResultIsBOOL(Quartz.PDFDocument.writeToFile_withOptions_)
        self.assertResultIsBOOL(Quartz.PDFDocument.writeToURL_)
        self.assertResultIsBOOL(Quartz.PDFDocument.writeToURL_withOptions_)
        self.assertResultIsBOOL(Quartz.PDFDocument.isFinding)

        self.assertResultHasType(TestPDFDocumentHelper.classForPage, objc._C_CLASS)
        self.assertResultHasType(
            TestPDFDocumentHelper.classForAnnotationType_, objc._C_CLASS
        )
        self.assertResultHasType(
            TestPDFDocumentHelper.classForAnnotationClass_, objc._C_CLASS
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBOOL(
            Quartz.PDFDocument.printOperationForPrintInfo_scalingMode_autoRotate_, 2
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(Quartz.PDFDocument.allowsFormFieldEntry)
        self.assertResultIsBOOL(Quartz.PDFDocument.allowsDocumentChanges)
        self.assertResultIsBOOL(Quartz.PDFDocument.allowsDocumentAssembly)
        self.assertResultIsBOOL(Quartz.PDFDocument.allowsContentAccessibility)
        self.assertResultIsBOOL(Quartz.PDFDocument.allowsCommenting)

    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("PDFDocumentDelegate")
