
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSAttributedString (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSFontAttributeName, unicode)
        self.failUnlessIsInstance(NSParagraphStyleAttributeName, unicode)
        self.failUnlessIsInstance(NSForegroundColorAttributeName, unicode)
        self.failUnlessIsInstance(NSSuperscriptAttributeName, unicode)
        self.failUnlessIsInstance(NSBackgroundColorAttributeName, unicode)
        self.failUnlessIsInstance(NSLigatureAttributeName, unicode)
        self.failUnlessIsInstance(NSBaselineOffsetAttributeName, unicode)
        self.failUnlessIsInstance(NSKernAttributeName, unicode)
        self.failUnlessIsInstance(NSLinkAttributeName, unicode)

        self.failUnlessIsInstance(NSStrokeWidthAttributeName, unicode)
        self.failUnlessIsInstance(NSStrokeColorAttributeName, unicode)
        self.failUnlessIsInstance(NSUnderlineColorAttributeName, unicode)
        self.failUnlessIsInstance(NSStrikethroughStyleAttributeName, unicode)
        self.failUnlessIsInstance(NSStrikethroughColorAttributeName, unicode)
        self.failUnlessIsInstance(NSShadowAttributeName, unicode)
        self.failUnlessIsInstance(NSExpansionAttributeName, unicode)
        self.failUnlessIsInstance(NSToolTipAttributeName, unicode)

        self.failUnlessIsInstance(NSCharacterShapeAttributeName, unicode)
        self.failUnlessIsInstance(NSGlyphInfoAttributeName, unicode)
        self.failUnlessIsInstance(NSMarkedClauseSegmentAttributeName, unicode)

        self.failUnlessEqual(NSUnderlineStyleNone, 0x00)
        self.failUnlessEqual(NSUnderlineStyleSingle, 0x01)
        self.failUnlessEqual(NSUnderlineStyleThick, 0x02)
        self.failUnlessEqual(NSUnderlineStyleDouble, 0x09)

        self.failUnlessEqual(NSUnderlinePatternSolid, 0x0000)
        self.failUnlessEqual(NSUnderlinePatternDot, 0x0100)
        self.failUnlessEqual(NSUnderlinePatternDash, 0x0200)
        self.failUnlessEqual(NSUnderlinePatternDashDot, 0x0300)
        self.failUnlessEqual(NSUnderlinePatternDashDotDot, 0x0400)

        self.failUnlessIsInstance(NSUnderlineByWordMask, (int, long))

        self.failUnlessIsInstance(NSSpellingStateAttributeName, unicode)

        self.failUnlessEqual(NSSpellingStateSpellingFlag, (1 << 0))
        self.failUnlessEqual(NSSpellingStateGrammarFlag, (1 << 1))

        self.failUnlessIsInstance(NSPlainTextDocumentType, unicode)
        self.failUnlessIsInstance(NSRTFTextDocumentType, unicode)
        self.failUnlessIsInstance(NSRTFDTextDocumentType, unicode)
        self.failUnlessIsInstance(NSMacSimpleTextDocumentType, unicode)
        self.failUnlessIsInstance(NSHTMLTextDocumentType, unicode)
        self.failUnlessIsInstance(NSDocFormatTextDocumentType, unicode)
        self.failUnlessIsInstance(NSWordMLTextDocumentType, unicode)
        self.failUnlessIsInstance(NSWebArchiveTextDocumentType, unicode)
        self.failUnlessIsInstance(NSOfficeOpenXMLTextDocumentType, unicode)
        self.failUnlessIsInstance(NSOpenDocumentTextDocumentType, unicode)

        self.failUnlessIsInstance(NSPaperSizeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSLeftMarginDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSRightMarginDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSTopMarginDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSBottomMarginDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSViewSizeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSViewZoomDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSViewModeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSDocumentTypeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSReadOnlyDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSConvertedDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSCocoaVersionDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSBackgroundColorDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSHyphenationFactorDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSDefaultTabIntervalDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSCharacterEncodingDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSTitleDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSAuthorDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSKeywordsDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSCommentDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSCreationTimeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSModificationTimeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSExcludedElementsDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSTextEncodingNameDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSPrefixSpacesDocumentAttribute, unicode)

        self.failUnlessIsInstance(NSDocumentTypeDocumentOption, unicode)
        self.failUnlessIsInstance(NSDefaultAttributesDocumentOption, unicode)
        self.failUnlessIsInstance(NSCharacterEncodingDocumentOption, unicode)
        self.failUnlessIsInstance(NSTextEncodingNameDocumentOption, unicode)
        self.failUnlessIsInstance(NSBaseURLDocumentOption, unicode)
        self.failUnlessIsInstance(NSTimeoutDocumentOption, unicode)
        self.failUnlessIsInstance(NSWebPreferencesDocumentOption, unicode)
        self.failUnlessIsInstance(NSWebResourceLoadDelegateDocumentOption, unicode)
        self.failUnlessIsInstance(NSTextSizeMultiplierDocumentOption, unicode)

        self.failUnlessEqual(NSNoUnderlineStyle, 0)
        self.failUnlessEqual(NSSingleUnderlineStyle, 1)

        self.failUnlessIsInstance(NSUnderlineStrikethroughMask, (int, long))

    def testMethods(self):
        self.fail("- (id)initWithURL:(NSURL *)url options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error;")
        self.fail("- (id)initWithData:(NSData *)data options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error;")
        self.fail("- (id)initWithPath:(NSString *)path documentAttributes:(NSDictionary **)dict;")
        self.fail("- (id)initWithURL:(NSURL *)url documentAttributes:(NSDictionary **)dict;")
        self.fail("- (id)initWithRTF:(NSData *)data documentAttributes:(NSDictionary **)dict;")
        self.fail("- (id)initWithRTFD:(NSData *)data documentAttributes:(NSDictionary **)dict;")
        self.fail("- (id)initWithHTML:(NSData *)data documentAttributes:(NSDictionary **)dict;")
        self.fail("- (id)initWithHTML:(NSData *)data baseURL:(NSURL *)base documentAttributes:(NSDictionary **)dict;")
        self.fail("- (id)initWithDocFormat:(NSData *)data documentAttributes:(NSDictionary **)dict;")
        self.fail("- (id)initWithHTML:(NSData *)data options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict;")
        self.fail("- (id)initWithRTFDFileWrapper:(NSFileWrapper *)wrapper documentAttributes:(NSDictionary **)dict;")



        self.fail("- (BOOL)readFromURL:(NSURL *)url options:(NSDictionary *)opts documentAttributes:(NSDictionary **)dict error:(NSError **)error;")
        self.fail("- (BOOL)readFromData:(NSData *)data options:(NSDictionary *)opts documentAttributes:(NSDictionary **)dict error:(NSError **)error;")
        self.fail("- (BOOL)readFromURL:(NSURL *)url options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict;")
        self.fail("- (BOOL)readFromData:(NSData *)data options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict;")

        self.fail("- (NSURL *)URLAtIndex:(NSUInteger)location effectiveRange:(NSRangePointer)effectiveRange;")



if __name__ == "__main__":
    main()
