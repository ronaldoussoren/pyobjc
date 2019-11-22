from PyObjCTools.TestSupport import *
from Quartz import *
import Quartz
from Foundation import NSMutableData


class TestCGPDFContext(TestCase):
    def testFunctions(self):
        data = NSMutableData.data()
        self.assertIsInstance(data, CFMutableDataRef)

        consumer = CGDataConsumerCreateWithCFData(data)
        self.assertIsInstance(consumer, CGDataConsumerRef)

        self.assertArgIsIn(CGPDFContextCreate, 1)
        self.assertResultIsCFRetained(CGPDFContextCreate)
        context = CGPDFContextCreate(consumer, None, None)
        self.assertIsInstance(context, CGContextRef)

        if hasattr(Quartz, "CGPDFContextClose"):
            CGPDFContextClose(context)

        self.assertResultIsCFRetained(CGPDFContextCreateWithURL)
        url = CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False
        )
        self.assertArgIsIn(CGPDFContextCreateWithURL, 1)
        context = CGPDFContextCreateWithURL(url, None, None)
        self.assertIsInstance(context, CGContextRef)

        CGPDFContextBeginPage(context, None)

        CGPDFContextSetURLForRect(context, url, ((0, 0), (10, 10)))
        CGPDFContextAddDestinationAtPoint(context, "target", (50, 50))

        CGPDFContextSetDestinationForRect(context, "target", ((100, 120), (50, 60)))

        CGPDFContextEndPage(context)

        if hasattr(Quartz, "CGPDFContextClose"):
            CGPDFContextClose(context)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        # Note actual test is in the function below this one.
        CGPDFContextClose

    @min_os_level("10.7")
    def testFunctions10_7(self):
        data = NSMutableData.data()
        consumer = CGDataConsumerCreateWithCFData(data)
        context = CGPDFContextCreate(consumer, None, None)

        metadata = (
            b"""<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?><?xpacket end='w'?>"""
        )
        CGPDFContextAddDocumentMetadata(
            context, NSMutableData.dataWithBytes_length_(metadata, len(metadata))
        )

    @min_os_level("10.13")
    def testFunctions10_13(self):
        CGPDFContextSetOutline

    @min_os_level("10.15")
    def testFunctions10_15(self):
        CGPDFTagTypeGetName
        CGPDFContextBeginTag
        CGPDFContextEndTag

    def testConstants(self):
        self.assertIsInstance(kCGPDFContextMediaBox, unicode)
        self.assertIsInstance(kCGPDFContextCropBox, unicode)
        self.assertIsInstance(kCGPDFContextBleedBox, unicode)
        self.assertIsInstance(kCGPDFContextTrimBox, unicode)
        self.assertIsInstance(kCGPDFContextArtBox, unicode)
        self.assertIsInstance(kCGPDFContextTitle, unicode)
        self.assertIsInstance(kCGPDFContextAuthor, unicode)
        self.assertIsInstance(kCGPDFContextKeywords, unicode)
        self.assertIsInstance(kCGPDFContextCreator, unicode)
        self.assertIsInstance(kCGPDFContextOwnerPassword, unicode)
        self.assertIsInstance(kCGPDFContextUserPassword, unicode)
        self.assertIsInstance(kCGPDFContextEncryptionKeyLength, unicode)
        self.assertIsInstance(kCGPDFContextAllowsPrinting, unicode)
        self.assertIsInstance(kCGPDFContextAllowsCopying, unicode)
        self.assertIsInstance(kCGPDFContextOutputIntent, unicode)
        self.assertIsInstance(kCGPDFXOutputIntentSubtype, unicode)
        self.assertIsInstance(kCGPDFXOutputConditionIdentifier, unicode)
        self.assertIsInstance(kCGPDFXOutputCondition, unicode)
        self.assertIsInstance(kCGPDFXRegistryName, unicode)
        self.assertIsInstance(kCGPDFXInfo, unicode)
        self.assertIsInstance(kCGPDFXDestinationOutputProfile, unicode)
        self.assertIsInstance(kCGPDFContextOutputIntents, unicode)

        self.assertEqual(CGPDFTagTypeDocument, 100)
        self.assertEqual(CGPDFTagTypePart, 101)
        self.assertEqual(CGPDFTagTypeArt, 102)
        self.assertEqual(CGPDFTagTypeSection, 103)
        self.assertEqual(CGPDFTagTypeDiv, 104)
        self.assertEqual(CGPDFTagTypeBlockQuote, 105)
        self.assertEqual(CGPDFTagTypeCaption, 106)
        self.assertEqual(CGPDFTagTypeTOC, 107)
        self.assertEqual(CGPDFTagTypeTOCI, 108)
        self.assertEqual(CGPDFTagTypeIndex, 109)
        self.assertEqual(CGPDFTagTypeNonStructure, 110)
        self.assertEqual(CGPDFTagTypePrivate, 111)
        self.assertEqual(CGPDFTagTypeParagraph, 200)
        self.assertEqual(CGPDFTagTypeHeader, 201)
        self.assertEqual(CGPDFTagTypeHeader1, 202)
        self.assertEqual(CGPDFTagTypeHeader2, 203)
        self.assertEqual(CGPDFTagTypeHeader3, 204)
        self.assertEqual(CGPDFTagTypeHeader4, 205)
        self.assertEqual(CGPDFTagTypeHeader5, 206)
        self.assertEqual(CGPDFTagTypeHeader6, 207)
        self.assertEqual(CGPDFTagTypeList, 300)
        self.assertEqual(CGPDFTagTypeListItem, 301)
        self.assertEqual(CGPDFTagTypeLabel, 302)
        self.assertEqual(CGPDFTagTypeListBody, 303)
        self.assertEqual(CGPDFTagTypeTable, 400)
        self.assertEqual(CGPDFTagTypeTableRow, 401)
        self.assertEqual(CGPDFTagTypeTableHeaderCell, 402)
        self.assertEqual(CGPDFTagTypeTableDataCell, 403)
        self.assertEqual(CGPDFTagTypeTableHeader, 404)
        self.assertEqual(CGPDFTagTypeTableBody, 405)
        self.assertEqual(CGPDFTagTypeTableFooter, 406)
        self.assertEqual(CGPDFTagTypeSpan, 500)
        self.assertEqual(CGPDFTagTypeQuote, 501)
        self.assertEqual(CGPDFTagTypeNote, 502)
        self.assertEqual(CGPDFTagTypeReference, 503)
        self.assertEqual(CGPDFTagTypeBibliography, 504)
        self.assertEqual(CGPDFTagTypeCode, 505)
        self.assertEqual(CGPDFTagTypeLink, 506)
        self.assertEqual(CGPDFTagTypeAnnotation, 507)
        self.assertEqual(CGPDFTagTypeRuby, 600)
        self.assertEqual(CGPDFTagTypeRubyBaseText, 601)
        self.assertEqual(CGPDFTagTypeRubyAnnotationText, 602)
        self.assertEqual(CGPDFTagTypeRubyPunctuation, 603)
        self.assertEqual(CGPDFTagTypeWarichu, 604)
        self.assertEqual(CGPDFTagTypeWarichuText, 605)
        self.assertEqual(CGPDFTagTypeWarichuPunctiation, 606)
        self.assertEqual(CGPDFTagTypeFigure, 700)
        self.assertEqual(CGPDFTagTypeFormula, 701)
        self.assertEqual(CGPDFTagTypeForm, 702)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(kCGPDFContextSubject, unicode)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(kCGPDFContextAccessPermissions, unicode)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(kCGPDFTagPropertyActualText, unicode)
        self.assertIsInstance(kCGPDFTagPropertyAlternativeText, unicode)
        self.assertIsInstance(kCGPDFTagPropertyTitleText, unicode)
        self.assertIsInstance(kCGPDFTagPropertyLanguageText, unicode)


if __name__ == "__main__":
    main()
