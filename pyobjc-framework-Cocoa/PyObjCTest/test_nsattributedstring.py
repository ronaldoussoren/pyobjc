from PyObjCTools.TestSupport import *

from Foundation import *
from AppKit import *
import Foundation

class TestNSAttributedString (TestCase):
    def testOutput(self):
        self.assertArgIsOut(NSAttributedString.attributesAtIndex_effectiveRange_, 1)
        self.assertArgIsOut(NSAttributedString.attribute_atIndex_effectiveRange_, 2)
        self.assertArgIsOut(NSAttributedString.attributesAtIndex_longestEffectiveRange_inRange_, 1)
        self.assertArgIsOut(NSAttributedString.attribute_atIndex_longestEffectiveRange_inRange_, 2)

        self.assertResultIsBOOL(NSAttributedString.isEqualToAttributedString_)

    def testConstantsAppKit(self):
        self.assertIsInstance(NSFontAttributeName, unicode)
        self.assertIsInstance(NSParagraphStyleAttributeName, unicode)
        self.assertIsInstance(NSForegroundColorAttributeName, unicode)
        self.assertIsInstance(NSUnderlineStyleAttributeName, unicode)
        self.assertIsInstance(NSSuperscriptAttributeName, unicode)
        self.assertIsInstance(NSBackgroundColorAttributeName, unicode)
        self.assertIsInstance(NSAttachmentAttributeName, unicode)
        self.assertIsInstance(NSLigatureAttributeName, unicode)
        self.assertIsInstance(NSBaselineOffsetAttributeName, unicode)
        self.assertIsInstance(NSKernAttributeName, unicode)
        self.assertIsInstance(NSLinkAttributeName, unicode)
        self.assertIsInstance(NSStrokeWidthAttributeName, unicode)
        self.assertIsInstance(NSStrokeColorAttributeName, unicode)
        self.assertIsInstance(NSUnderlineColorAttributeName, unicode)
        self.assertIsInstance(NSStrikethroughStyleAttributeName, unicode)
        self.assertIsInstance(NSStrikethroughColorAttributeName, unicode)
        self.assertIsInstance(NSShadowAttributeName, unicode)
        self.assertIsInstance(NSObliquenessAttributeName, unicode)
        self.assertIsInstance(NSExpansionAttributeName, unicode)
        self.assertIsInstance(NSCursorAttributeName, unicode)
        self.assertIsInstance(NSToolTipAttributeName, unicode)
        self.assertIsInstance(NSCharacterShapeAttributeName, unicode)
        self.assertIsInstance(NSGlyphInfoAttributeName, unicode)
        self.assertIsInstance(NSMarkedClauseSegmentAttributeName, unicode)
        self.assertIsInstance(NSSpellingStateAttributeName, unicode)

        self.assertEqual(NSUnderlineStyleNone, 0x00)
        self.assertEqual(NSUnderlineStyleSingle, 0x01)
        self.assertEqual(NSUnderlineStyleThick, 0x02)
        self.assertEqual(NSUnderlineStyleDouble, 0x09)
        self.assertEqual(NSUnderlinePatternSolid, 0x0000)
        self.assertEqual(NSUnderlinePatternDot, 0x0100)
        self.assertEqual(NSUnderlinePatternDash, 0x0200)
        self.assertEqual(NSUnderlinePatternDashDot, 0x0300)
        self.assertEqual(NSUnderlinePatternDashDotDot, 0x0400)

        self.assertEqual(NSSpellingStateSpellingFlag, 1)
        self.assertEqual(NSSpellingStateGrammarFlag, 2)

        self.assertIsInstance(NSPlainTextDocumentType, unicode)
        self.assertIsInstance(NSRTFTextDocumentType, unicode)
        self.assertIsInstance(NSRTFDTextDocumentType, unicode)
        self.assertIsInstance(NSMacSimpleTextDocumentType, unicode)
        self.assertIsInstance(NSHTMLTextDocumentType, unicode)
        self.assertIsInstance(NSDocFormatTextDocumentType, unicode)
        self.assertIsInstance(NSWordMLTextDocumentType, unicode)
        self.assertIsInstance(NSWebArchiveTextDocumentType, unicode)
        self.assertIsInstance(NSOfficeOpenXMLTextDocumentType, unicode)
        self.assertIsInstance(NSOpenDocumentTextDocumentType, unicode)
        self.assertIsInstance(NSPaperSizeDocumentAttribute, unicode)
        self.assertIsInstance(NSLeftMarginDocumentAttribute, unicode)
        self.assertIsInstance(NSRightMarginDocumentAttribute, unicode)
        self.assertIsInstance(NSTopMarginDocumentAttribute, unicode)
        self.assertIsInstance(NSBottomMarginDocumentAttribute, unicode)
        self.assertIsInstance(NSViewSizeDocumentAttribute, unicode)
        self.assertIsInstance(NSViewZoomDocumentAttribute, unicode)
        self.assertIsInstance(NSViewModeDocumentAttribute, unicode)
        self.assertIsInstance(NSDocumentTypeDocumentAttribute, unicode)
        self.assertIsInstance(NSReadOnlyDocumentAttribute, unicode)
        self.assertIsInstance(NSConvertedDocumentAttribute, unicode)
        self.assertIsInstance(NSCocoaVersionDocumentAttribute, unicode)
        self.assertIsInstance(NSBackgroundColorDocumentAttribute, unicode)
        self.assertIsInstance(NSHyphenationFactorDocumentAttribute, unicode)
        self.assertIsInstance(NSDefaultTabIntervalDocumentAttribute, unicode)
        self.assertIsInstance(NSCharacterEncodingDocumentAttribute, unicode)
        self.assertIsInstance(NSTitleDocumentAttribute, unicode)
        self.assertIsInstance(NSCompanyDocumentAttribute, unicode)
        self.assertIsInstance(NSCopyrightDocumentAttribute, unicode)
        self.assertIsInstance(NSSubjectDocumentAttribute, unicode)
        self.assertIsInstance(NSAuthorDocumentAttribute, unicode)
        self.assertIsInstance(NSKeywordsDocumentAttribute, unicode)
        self.assertIsInstance(NSCommentDocumentAttribute, unicode)
        self.assertIsInstance(NSEditorDocumentAttribute, unicode)
        self.assertIsInstance(NSCreationTimeDocumentAttribute, unicode)
        self.assertIsInstance(NSModificationTimeDocumentAttribute, unicode)
        self.assertIsInstance(NSExcludedElementsDocumentAttribute, unicode)
        self.assertIsInstance(NSTextEncodingNameDocumentAttribute, unicode)
        self.assertIsInstance(NSPrefixSpacesDocumentAttribute, unicode)
        self.assertIsInstance(NSDocumentTypeDocumentOption, unicode)
        self.assertIsInstance(NSDefaultAttributesDocumentOption, unicode)
        self.assertIsInstance(NSCharacterEncodingDocumentOption, unicode)
        self.assertIsInstance(NSTextEncodingNameDocumentOption, unicode)
        self.assertIsInstance(NSBaseURLDocumentOption, unicode)
        self.assertIsInstance(NSTimeoutDocumentOption, unicode)
        self.assertIsInstance(NSWebPreferencesDocumentOption, unicode)
        self.assertIsInstance(NSWebResourceLoadDelegateDocumentOption, unicode)
        self.assertIsInstance(NSTextSizeMultiplierDocumentOption, unicode)

        self.assertEqual(NSNoUnderlineStyle, 0)
        self.assertEqual(NSSingleUnderlineStyle, 1)
        self.assertIsInstance(NSUnderlineStrikethroughMask, (int, long))

    def testMethodsAppKit(self):
        self.assertResultIsBOOL(NSAttributedString.containsAttachments)

        self.assertArgIsOut(NSAttributedString.initWithURL_options_documentAttributes_error_, 2)
        self.assertArgIsOut(NSAttributedString.initWithURL_options_documentAttributes_error_, 3)

        self.assertArgIsOut(NSAttributedString.initWithData_options_documentAttributes_error_, 2)
        self.assertArgIsOut(NSAttributedString.initWithData_options_documentAttributes_error_, 3)

        self.assertArgIsOut(NSAttributedString.initWithPath_documentAttributes_, 1)
        self.assertArgIsOut(NSAttributedString.initWithURL_documentAttributes_, 1)
        self.assertArgIsOut(NSAttributedString.initWithRTF_documentAttributes_, 1)
        self.assertArgIsOut(NSAttributedString.initWithRTFD_documentAttributes_, 1)
        self.assertArgIsOut(NSAttributedString.initWithHTML_documentAttributes_, 1)
        self.assertArgIsOut(NSAttributedString.initWithHTML_baseURL_documentAttributes_, 2)
        self.assertArgIsOut(NSAttributedString.initWithRTFDFileWrapper_documentAttributes_, 1)

        self.assertArgIsOut(NSAttributedString.dataFromRange_documentAttributes_error_, 2)
        self.assertArgIsOut(NSAttributedString.fileWrapperFromRange_documentAttributes_error_, 2)
        
        self.assertResultIsBOOL(NSMutableAttributedString.readFromURL_options_documentAttributes_error_)
        self.assertArgIsOut(NSMutableAttributedString.readFromURL_options_documentAttributes_error_, 2)
        self.assertArgIsOut(NSMutableAttributedString.readFromURL_options_documentAttributes_error_, 3)

        self.assertResultIsBOOL(NSMutableAttributedString.readFromData_options_documentAttributes_error_)
        self.assertArgIsOut(NSMutableAttributedString.readFromData_options_documentAttributes_error_, 2)
        self.assertArgIsOut(NSMutableAttributedString.readFromData_options_documentAttributes_error_, 3)

        self.assertResultIsBOOL(NSMutableAttributedString.readFromURL_options_documentAttributes_)
        self.assertArgIsOut(NSMutableAttributedString.readFromURL_options_documentAttributes_, 2)

        self.assertResultIsBOOL(NSMutableAttributedString.readFromData_options_documentAttributes_)
        self.assertArgIsOut(NSMutableAttributedString.readFromData_options_documentAttributes_, 2)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSAttributedStringEnumerationReverse, 1<<1)
        self.assertEqual(NSAttributedStringEnumerationLongestEffectiveRangeNotRequired, 1<<20)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgHasType(NSAttributedString.enumerateAttributesInRange_options_usingBlock_, 0, NSRange.__typestr__)
        self.assertArgIsBlock(NSAttributedString.enumerateAttributesInRange_options_usingBlock_, 2, b'v@'+NSRange.__typestr__+b'o^'+objc._C_NSBOOL)

        self.assertArgHasType(NSAttributedString.enumerateAttribute_inRange_options_usingBlock_, 1, NSRange.__typestr__)
        self.assertArgIsBlock(NSAttributedString.enumerateAttribute_inRange_options_usingBlock_, 3, b'v@'+NSRange.__typestr__+b'o^'+objc._C_NSBOOL)

if __name__ == '__main__':
    main()
