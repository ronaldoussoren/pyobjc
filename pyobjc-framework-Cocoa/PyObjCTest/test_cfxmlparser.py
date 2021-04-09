import CoreFoundation
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestXMLParser(TestCase):
    # Note: This doesn't actually test the API

    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFXMLParserRef)

    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFXMLParserGetTypeID(), int)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFXMLParserValidateDocument, (1 << 0))
        self.assertEqual(CoreFoundation.kCFXMLParserSkipMetaData, (1 << 1))
        self.assertEqual(CoreFoundation.kCFXMLParserReplacePhysicalEntities, (1 << 2))
        self.assertEqual(CoreFoundation.kCFXMLParserSkipWhitespace, (1 << 3))
        self.assertEqual(CoreFoundation.kCFXMLParserResolveExternalEntities, (1 << 4))
        self.assertEqual(CoreFoundation.kCFXMLParserAddImpliedAttributes, (1 << 5))
        self.assertEqual(CoreFoundation.kCFXMLParserAllOptions, 0x00FFFFFF)
        self.assertEqual(CoreFoundation.kCFXMLParserNoOptions, 0)
        self.assertEqual(CoreFoundation.kCFXMLStatusParseNotBegun, -2)
        self.assertEqual(CoreFoundation.kCFXMLStatusParseInProgress, -1)
        self.assertEqual(CoreFoundation.kCFXMLStatusParseSuccessful, 0)
        self.assertEqual(CoreFoundation.kCFXMLErrorUnexpectedEOF, 1)
        self.assertEqual(CoreFoundation.kCFXMLErrorUnknownEncoding, 2)
        self.assertEqual(CoreFoundation.kCFXMLErrorEncodingConversionFailure, 3)
        self.assertEqual(CoreFoundation.kCFXMLErrorMalformedProcessingInstruction, 4)
        self.assertEqual(CoreFoundation.kCFXMLErrorMalformedDTD, 5)
        self.assertEqual(CoreFoundation.kCFXMLErrorMalformedName, 6)
        self.assertEqual(CoreFoundation.kCFXMLErrorMalformedCDSect, 7)
        self.assertEqual(CoreFoundation.kCFXMLErrorMalformedCloseTag, 8)
        self.assertEqual(CoreFoundation.kCFXMLErrorMalformedStartTag, 9)
        self.assertEqual(CoreFoundation.kCFXMLErrorMalformedDocument, 10)
        self.assertEqual(CoreFoundation.kCFXMLErrorElementlessDocument, 11)
        self.assertEqual(CoreFoundation.kCFXMLErrorMalformedComment, 12)
        self.assertEqual(CoreFoundation.kCFXMLErrorMalformedCharacterReference, 13)
        self.assertEqual(CoreFoundation.kCFXMLErrorMalformedParsedCharacterData, 14)
        self.assertEqual(CoreFoundation.kCFXMLErrorNoData, 15)
        self.assertIsInstance(CoreFoundation.kCFXMLTreeErrorDescription, str)
        self.assertIsInstance(CoreFoundation.kCFXMLTreeErrorLineNumber, str)
        self.assertIsInstance(CoreFoundation.kCFXMLTreeErrorLocation, str)
        self.assertIsInstance(CoreFoundation.kCFXMLTreeErrorStatusCode, str)

    @expectedFailure
    def testMissingWrappers(self):
        self.fail("Missing manual wrappers for CoreFoundation.CFXMLParser (low prio)")
