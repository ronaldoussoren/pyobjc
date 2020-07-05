import Quartz
from Foundation import NSMutableData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCGPDFContext(TestCase):
    def testFunctions(self):
        data = NSMutableData.data()
        self.assertIsInstance(data, Quartz.CFMutableDataRef)

        consumer = Quartz.CGDataConsumerCreateWithCFData(data)
        self.assertIsInstance(consumer, Quartz.CGDataConsumerRef)

        self.assertArgIsIn(Quartz.CGPDFContextCreate, 1)
        self.assertResultIsCFRetained(Quartz.CGPDFContextCreate)
        context = Quartz.CGPDFContextCreate(consumer, None, None)
        self.assertIsInstance(context, Quartz.CGContextRef)

        if hasattr(Quartz, "CGPDFContextClose"):
            Quartz.CGPDFContextClose(context)

        self.assertResultIsCFRetained(Quartz.CGPDFContextCreateWithURL)
        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertArgIsIn(Quartz.CGPDFContextCreateWithURL, 1)
        context = Quartz.CGPDFContextCreateWithURL(url, None, None)
        self.assertIsInstance(context, Quartz.CGContextRef)

        Quartz.CGPDFContextBeginPage(context, None)

        Quartz.CGPDFContextSetURLForRect(context, url, ((0, 0), (10, 10)))
        Quartz.CGPDFContextAddDestinationAtPoint(context, "target", (50, 50))

        Quartz.CGPDFContextSetDestinationForRect(
            context, "target", ((100, 120), (50, 60))
        )

        Quartz.CGPDFContextEndPage(context)

        if hasattr(Quartz, "CGPDFContextClose"):
            Quartz.CGPDFContextClose(context)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        # Note actual test is in the function below this one.
        Quartz.CGPDFContextClose

    @min_os_level("10.7")
    def testFunctions10_7(self):
        data = NSMutableData.data()
        consumer = Quartz.CGDataConsumerCreateWithCFData(data)
        context = Quartz.CGPDFContextCreate(consumer, None, None)

        metadata = (
            b"""<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?><?xpacket end='w'?>"""
        )
        Quartz.CGPDFContextAddDocumentMetadata(
            context, NSMutableData.dataWithBytes_length_(metadata, len(metadata))
        )

    @min_os_level("10.13")
    def testFunctions10_13(self):
        Quartz.CGPDFContextSetOutline

    @min_os_level("10.15")
    def testFunctions10_15(self):
        Quartz.CGPDFTagTypeGetName
        Quartz.CGPDFContextBeginTag
        Quartz.CGPDFContextEndTag

    def testConstants(self):
        self.assertIsInstance(Quartz.kCGPDFContextMediaBox, str)
        self.assertIsInstance(Quartz.kCGPDFContextCropBox, str)
        self.assertIsInstance(Quartz.kCGPDFContextBleedBox, str)
        self.assertIsInstance(Quartz.kCGPDFContextTrimBox, str)
        self.assertIsInstance(Quartz.kCGPDFContextArtBox, str)
        self.assertIsInstance(Quartz.kCGPDFContextTitle, str)
        self.assertIsInstance(Quartz.kCGPDFContextAuthor, str)
        self.assertIsInstance(Quartz.kCGPDFContextKeywords, str)
        self.assertIsInstance(Quartz.kCGPDFContextCreator, str)
        self.assertIsInstance(Quartz.kCGPDFContextOwnerPassword, str)
        self.assertIsInstance(Quartz.kCGPDFContextUserPassword, str)
        self.assertIsInstance(Quartz.kCGPDFContextEncryptionKeyLength, str)
        self.assertIsInstance(Quartz.kCGPDFContextAllowsPrinting, str)
        self.assertIsInstance(Quartz.kCGPDFContextAllowsCopying, str)
        self.assertIsInstance(Quartz.kCGPDFContextOutputIntent, str)
        self.assertIsInstance(Quartz.kCGPDFXOutputIntentSubtype, str)
        self.assertIsInstance(Quartz.kCGPDFXOutputConditionIdentifier, str)
        self.assertIsInstance(Quartz.kCGPDFXOutputCondition, str)
        self.assertIsInstance(Quartz.kCGPDFXRegistryName, str)
        self.assertIsInstance(Quartz.kCGPDFXInfo, str)
        self.assertIsInstance(Quartz.kCGPDFXDestinationOutputProfile, str)
        self.assertIsInstance(Quartz.kCGPDFContextOutputIntents, str)

        self.assertEqual(Quartz.CGPDFTagTypeDocument, 100)
        self.assertEqual(Quartz.CGPDFTagTypePart, 101)
        self.assertEqual(Quartz.CGPDFTagTypeArt, 102)
        self.assertEqual(Quartz.CGPDFTagTypeSection, 103)
        self.assertEqual(Quartz.CGPDFTagTypeDiv, 104)
        self.assertEqual(Quartz.CGPDFTagTypeBlockQuote, 105)
        self.assertEqual(Quartz.CGPDFTagTypeCaption, 106)
        self.assertEqual(Quartz.CGPDFTagTypeTOC, 107)
        self.assertEqual(Quartz.CGPDFTagTypeTOCI, 108)
        self.assertEqual(Quartz.CGPDFTagTypeIndex, 109)
        self.assertEqual(Quartz.CGPDFTagTypeNonStructure, 110)
        self.assertEqual(Quartz.CGPDFTagTypePrivate, 111)
        self.assertEqual(Quartz.CGPDFTagTypeParagraph, 200)
        self.assertEqual(Quartz.CGPDFTagTypeHeader, 201)
        self.assertEqual(Quartz.CGPDFTagTypeHeader1, 202)
        self.assertEqual(Quartz.CGPDFTagTypeHeader2, 203)
        self.assertEqual(Quartz.CGPDFTagTypeHeader3, 204)
        self.assertEqual(Quartz.CGPDFTagTypeHeader4, 205)
        self.assertEqual(Quartz.CGPDFTagTypeHeader5, 206)
        self.assertEqual(Quartz.CGPDFTagTypeHeader6, 207)
        self.assertEqual(Quartz.CGPDFTagTypeList, 300)
        self.assertEqual(Quartz.CGPDFTagTypeListItem, 301)
        self.assertEqual(Quartz.CGPDFTagTypeLabel, 302)
        self.assertEqual(Quartz.CGPDFTagTypeListBody, 303)
        self.assertEqual(Quartz.CGPDFTagTypeTable, 400)
        self.assertEqual(Quartz.CGPDFTagTypeTableRow, 401)
        self.assertEqual(Quartz.CGPDFTagTypeTableHeaderCell, 402)
        self.assertEqual(Quartz.CGPDFTagTypeTableDataCell, 403)
        self.assertEqual(Quartz.CGPDFTagTypeTableHeader, 404)
        self.assertEqual(Quartz.CGPDFTagTypeTableBody, 405)
        self.assertEqual(Quartz.CGPDFTagTypeTableFooter, 406)
        self.assertEqual(Quartz.CGPDFTagTypeSpan, 500)
        self.assertEqual(Quartz.CGPDFTagTypeQuote, 501)
        self.assertEqual(Quartz.CGPDFTagTypeNote, 502)
        self.assertEqual(Quartz.CGPDFTagTypeReference, 503)
        self.assertEqual(Quartz.CGPDFTagTypeBibliography, 504)
        self.assertEqual(Quartz.CGPDFTagTypeCode, 505)
        self.assertEqual(Quartz.CGPDFTagTypeLink, 506)
        self.assertEqual(Quartz.CGPDFTagTypeAnnotation, 507)
        self.assertEqual(Quartz.CGPDFTagTypeRuby, 600)
        self.assertEqual(Quartz.CGPDFTagTypeRubyBaseText, 601)
        self.assertEqual(Quartz.CGPDFTagTypeRubyAnnotationText, 602)
        self.assertEqual(Quartz.CGPDFTagTypeRubyPunctuation, 603)
        self.assertEqual(Quartz.CGPDFTagTypeWarichu, 604)
        self.assertEqual(Quartz.CGPDFTagTypeWarichuText, 605)
        self.assertEqual(Quartz.CGPDFTagTypeWarichuPunctiation, 606)
        self.assertEqual(Quartz.CGPDFTagTypeFigure, 700)
        self.assertEqual(Quartz.CGPDFTagTypeFormula, 701)
        self.assertEqual(Quartz.CGPDFTagTypeForm, 702)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(Quartz.kCGPDFContextSubject, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.kCGPDFContextAccessPermissions, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(Quartz.kCGPDFTagPropertyActualText, str)
        self.assertIsInstance(Quartz.kCGPDFTagPropertyAlternativeText, str)
        self.assertIsInstance(Quartz.kCGPDFTagPropertyTitleText, str)
        self.assertIsInstance(Quartz.kCGPDFTagPropertyLanguageText, str)

    @min_os_level("10.16")
    def testConstants10_16(self):
        self.assertIsInstance(Quartz.kCGPDFContextCreateLinearizedPDF, str)
        self.assertIsInstance(Quartz.kCGPDFContextCreatePDFA, str)
