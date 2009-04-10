from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestXMLParser (TestCase):
    # Note: This doesn't actually test the API

    def testTypes(self):
        self.failUnlessIsCFType(CFXMLParserRef)

    def testTypeID(self):
        self.failUnless(isinstance(CFXMLParserGetTypeID(), (int, long)))

        

    def testConstants(self):
        self.failUnless( kCFXMLParserValidateDocument == (1 << 0) )
        self.failUnless( kCFXMLParserSkipMetaData == (1 << 1) )
        self.failUnless( kCFXMLParserReplacePhysicalEntities == (1 << 2) )
        self.failUnless( kCFXMLParserSkipWhitespace == (1 << 3) )
        self.failUnless( kCFXMLParserResolveExternalEntities == (1 << 4) )
        self.failUnless( kCFXMLParserAddImpliedAttributes == (1 << 5) )
        self.failUnless( kCFXMLParserAllOptions == 0x00FFFFFF )
        self.failUnless( kCFXMLParserNoOptions == 0 )

        self.failUnless( kCFXMLStatusParseNotBegun == -2 )
        self.failUnless( kCFXMLStatusParseInProgress == -1 )
        self.failUnless( kCFXMLStatusParseSuccessful == 0 )
        self.failUnless( kCFXMLErrorUnexpectedEOF == 1 )
        self.failUnless( kCFXMLErrorUnknownEncoding == 2 )
        self.failUnless( kCFXMLErrorEncodingConversionFailure == 3 )
        self.failUnless( kCFXMLErrorMalformedProcessingInstruction == 4)
        self.failUnless( kCFXMLErrorMalformedDTD == 5 )
        self.failUnless( kCFXMLErrorMalformedName == 6 )
        self.failUnless( kCFXMLErrorMalformedCDSect == 7 )
        self.failUnless( kCFXMLErrorMalformedCloseTag == 8 )
        self.failUnless( kCFXMLErrorMalformedStartTag == 9 )
        self.failUnless( kCFXMLErrorMalformedDocument == 10 )
        self.failUnless( kCFXMLErrorElementlessDocument == 11 )
        self.failUnless( kCFXMLErrorMalformedComment == 12 )
        self.failUnless( kCFXMLErrorMalformedCharacterReference == 13 )
        self.failUnless( kCFXMLErrorMalformedParsedCharacterData == 14 )
        self.failUnless( kCFXMLErrorNoData == 15 )

        self.failUnless( isinstance(kCFXMLTreeErrorDescription, unicode) )
        self.failUnless( isinstance(kCFXMLTreeErrorLineNumber, unicode) )
        self.failUnless( isinstance(kCFXMLTreeErrorLocation, unicode) )
        self.failUnless( isinstance(kCFXMLTreeErrorStatusCode, unicode) )


if __name__ == "__main__":
    main()
