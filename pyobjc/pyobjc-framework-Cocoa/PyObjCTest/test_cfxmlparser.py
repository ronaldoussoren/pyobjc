from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestXMLParser (TestCase):
    # Note: This doesn't actually test the API

    def testTypes(self):
        self.assertIsCFType(CFXMLParserRef)

    def testTypeID(self):
        self.assertIsInstance(CFXMLParserGetTypeID(), (int, long))
    def testConstants(self):
        self.assertEqual(kCFXMLParserValidateDocument , (1 << 0) )
        self.assertEqual(kCFXMLParserSkipMetaData , (1 << 1) )
        self.assertEqual(kCFXMLParserReplacePhysicalEntities , (1 << 2) )
        self.assertEqual(kCFXMLParserSkipWhitespace , (1 << 3) )
        self.assertEqual(kCFXMLParserResolveExternalEntities , (1 << 4) )
        self.assertEqual(kCFXMLParserAddImpliedAttributes , (1 << 5) )
        self.assertEqual(kCFXMLParserAllOptions , 0x00FFFFFF )
        self.assertEqual(kCFXMLParserNoOptions , 0 )
        self.assertEqual(kCFXMLStatusParseNotBegun , -2 )
        self.assertEqual(kCFXMLStatusParseInProgress , -1 )
        self.assertEqual(kCFXMLStatusParseSuccessful , 0 )
        self.assertEqual(kCFXMLErrorUnexpectedEOF , 1 )
        self.assertEqual(kCFXMLErrorUnknownEncoding , 2 )
        self.assertEqual(kCFXMLErrorEncodingConversionFailure , 3 )
        self.assertEqual(kCFXMLErrorMalformedProcessingInstruction , 4)
        self.assertEqual(kCFXMLErrorMalformedDTD , 5 )
        self.assertEqual(kCFXMLErrorMalformedName , 6 )
        self.assertEqual(kCFXMLErrorMalformedCDSect , 7 )
        self.assertEqual(kCFXMLErrorMalformedCloseTag , 8 )
        self.assertEqual(kCFXMLErrorMalformedStartTag , 9 )
        self.assertEqual(kCFXMLErrorMalformedDocument , 10 )
        self.assertEqual(kCFXMLErrorElementlessDocument , 11 )
        self.assertEqual(kCFXMLErrorMalformedComment , 12 )
        self.assertEqual(kCFXMLErrorMalformedCharacterReference , 13 )
        self.assertEqual(kCFXMLErrorMalformedParsedCharacterData , 14 )
        self.assertEqual(kCFXMLErrorNoData , 15 )
        self.assertIsInstance(kCFXMLTreeErrorDescription, unicode)
        self.assertIsInstance(kCFXMLTreeErrorLineNumber, unicode)
        self.assertIsInstance(kCFXMLTreeErrorLocation, unicode)
        self.assertIsInstance(kCFXMLTreeErrorStatusCode, unicode)
if __name__ == "__main__":
    main()
