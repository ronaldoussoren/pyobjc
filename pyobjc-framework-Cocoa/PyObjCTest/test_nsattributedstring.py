import objc
import Foundation
import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSAttributedString(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Foundation.NSAttributedStringKey, str)
        self.assertIsTypedEnum(AppKit.NSAttributedStringDocumentAttributeKey, str)
        self.assertIsTypedEnum(AppKit.NSAttributedStringDocumentReadingOptionKey, str)
        self.assertIsTypedEnum(AppKit.NSAttributedStringDocumentType, str)
        self.assertIsTypedEnum(AppKit.NSTextEffectStyle, str)
        self.assertIsTypedEnum(AppKit.NSTextLayoutSectionKey, str)
        self.assertIsTypedEnum(AppKit.NSAttributedStringFormattingContextKey, str)

    def test_enum_types_appkit(self):
        self.assertIsEnumType(AppKit.NSSpellingState)
        self.assertIsEnumType(AppKit.NSTextScalingType)
        self.assertIsEnumType(AppKit.NSUnderlineStyle)
        self.assertIsEnumType(AppKit.NSWritingDirectionFormatType)

    def test_enum_types_fnd(self):
        self.assertIsEnumType(Foundation.NSAttributedStringEnumerationOptions)
        self.assertIsEnumType(Foundation.NSAttributedStringFormattingOptions)
        self.assertIsEnumType(Foundation.NSAttributedStringMarkdownInterpretedSyntax)
        self.assertIsEnumType(Foundation.NSAttributedStringMarkdownParsingFailurePolicy)
        self.assertIsEnumType(Foundation.NSInlinePresentationIntent)
        self.assertIsEnumType(Foundation.NSPresentationIntentKind)
        self.assertIsEnumType(Foundation.NSPresentationIntentTableColumnAlignment)

    def testMethodsFoundation(self):
        self.assertArgIsOut(
            AppKit.NSAttributedString.attributesAtIndex_effectiveRange_, 1
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.attributesAtIndex_longestEffectiveRange_inRange_,
            1,
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.attribute_atIndex_longestEffectiveRange_inRange_,
            2,
        )

        self.assertResultIsBOOL(AppKit.NSAttributedString.isEqualToAttributedString_)

    def testConstantsAppKit(self):
        self.assertIsInstance(AppKit.NSManagerDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSFontAttributeName, str)
        self.assertIsInstance(AppKit.NSParagraphStyleAttributeName, str)
        self.assertIsInstance(AppKit.NSForegroundColorAttributeName, str)
        self.assertIsInstance(AppKit.NSUnderlineStyleAttributeName, str)
        self.assertIsInstance(AppKit.NSSuperscriptAttributeName, str)
        self.assertIsInstance(AppKit.NSBackgroundColorAttributeName, str)
        self.assertIsInstance(AppKit.NSAttachmentAttributeName, str)
        self.assertIsInstance(AppKit.NSLigatureAttributeName, str)
        self.assertIsInstance(AppKit.NSBaselineOffsetAttributeName, str)
        self.assertIsInstance(AppKit.NSKernAttributeName, str)
        self.assertIsInstance(AppKit.NSLinkAttributeName, str)
        self.assertIsInstance(AppKit.NSStrokeWidthAttributeName, str)
        self.assertIsInstance(AppKit.NSStrokeColorAttributeName, str)
        self.assertIsInstance(AppKit.NSUnderlineColorAttributeName, str)
        self.assertIsInstance(AppKit.NSStrikethroughStyleAttributeName, str)
        self.assertIsInstance(AppKit.NSStrikethroughColorAttributeName, str)
        self.assertIsInstance(AppKit.NSShadowAttributeName, str)
        self.assertIsInstance(AppKit.NSObliquenessAttributeName, str)
        self.assertIsInstance(AppKit.NSExpansionAttributeName, str)
        self.assertIsInstance(AppKit.NSCursorAttributeName, str)
        self.assertIsInstance(AppKit.NSToolTipAttributeName, str)
        self.assertIsInstance(AppKit.NSCharacterShapeAttributeName, str)
        self.assertIsInstance(AppKit.NSGlyphInfoAttributeName, str)
        self.assertIsInstance(AppKit.NSMarkedClauseSegmentAttributeName, str)
        self.assertIsInstance(AppKit.NSSpellingStateAttributeName, str)

        self.assertEqual(AppKit.NSUnderlineStyleNone, 0x00)
        self.assertEqual(AppKit.NSUnderlineStyleSingle, 0x01)
        self.assertEqual(AppKit.NSUnderlineStyleThick, 0x02)
        self.assertEqual(AppKit.NSUnderlineStyleDouble, 0x09)
        self.assertEqual(AppKit.NSUnderlinePatternSolid, 0x0000)
        self.assertEqual(AppKit.NSUnderlinePatternDot, 0x0100)
        self.assertEqual(AppKit.NSUnderlinePatternDash, 0x0200)
        self.assertEqual(AppKit.NSUnderlinePatternDashDot, 0x0300)
        self.assertEqual(AppKit.NSUnderlinePatternDashDotDot, 0x0400)

        self.assertIsInstance(AppKit.NSUnderlineByWordMask, int)

        self.assertEqual(AppKit.NSSpellingStateSpellingFlag, 1)
        self.assertEqual(AppKit.NSSpellingStateGrammarFlag, 2)

        self.assertIsInstance(AppKit.NSPlainTextDocumentType, str)
        self.assertIsInstance(AppKit.NSRTFTextDocumentType, str)
        self.assertIsInstance(AppKit.NSRTFDTextDocumentType, str)
        self.assertIsInstance(AppKit.NSMacSimpleTextDocumentType, str)
        self.assertIsInstance(AppKit.NSHTMLTextDocumentType, str)
        self.assertIsInstance(AppKit.NSDocFormatTextDocumentType, str)
        self.assertIsInstance(AppKit.NSWordMLTextDocumentType, str)
        self.assertIsInstance(AppKit.NSWebArchiveTextDocumentType, str)
        self.assertIsInstance(AppKit.NSOfficeOpenXMLTextDocumentType, str)
        self.assertIsInstance(AppKit.NSOpenDocumentTextDocumentType, str)
        self.assertIsInstance(AppKit.NSPaperSizeDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSLeftMarginDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSRightMarginDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSTopMarginDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSBottomMarginDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSViewSizeDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSViewZoomDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSViewModeDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSDocumentTypeDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSReadOnlyDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSConvertedDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSCocoaVersionDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSBackgroundColorDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSHyphenationFactorDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSDefaultTabIntervalDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSCharacterEncodingDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSTitleDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSCompanyDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSCopyrightDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSSubjectDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSAuthorDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSKeywordsDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSCommentDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSEditorDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSCreationTimeDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSModificationTimeDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSExcludedElementsDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSTextEncodingNameDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSPrefixSpacesDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSDocumentTypeDocumentOption, str)
        self.assertIsInstance(AppKit.NSDefaultAttributesDocumentOption, str)
        self.assertIsInstance(AppKit.NSCharacterEncodingDocumentOption, str)
        self.assertIsInstance(AppKit.NSTextEncodingNameDocumentOption, str)
        self.assertIsInstance(AppKit.NSBaseURLDocumentOption, str)
        self.assertIsInstance(AppKit.NSTimeoutDocumentOption, str)
        self.assertIsInstance(AppKit.NSWebPreferencesDocumentOption, str)
        self.assertIsInstance(AppKit.NSWebResourceLoadDelegateDocumentOption, str)
        self.assertIsInstance(AppKit.NSTextSizeMultiplierDocumentOption, str)

        self.assertEqual(AppKit.NSNoUnderlineStyle, 0)
        self.assertEqual(AppKit.NSSingleUnderlineStyle, 1)
        self.assertIsInstance(AppKit.NSUnderlineStrikethroughMask, int)

    def testMethodsAppKit(self):
        self.assertResultIsBOOL(AppKit.NSAttributedString.containsAttachments)
        self.assertArgIsBOOL(AppKit.NSAttributedString.nextWordFromIndex_forward_, 1)
        self.assertArgIsOut(AppKit.NSAttributedString.URLAtIndex_effectiveRange_, 1)

        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithURL_options_documentAttributes_error_, 2
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithURL_options_documentAttributes_error_, 3
        )

        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithData_options_documentAttributes_error_, 2
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithData_options_documentAttributes_error_, 3
        )

        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithPath_documentAttributes_, 1
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithURL_documentAttributes_, 1
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithRTF_documentAttributes_, 1
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithRTFD_documentAttributes_, 1
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithHTML_documentAttributes_, 1
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithHTML_options_documentAttributes_, 2
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithHTML_baseURL_documentAttributes_, 2
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithRTFDFileWrapper_documentAttributes_, 1
        )

        self.assertArgIsOut(
            AppKit.NSAttributedString.dataFromRange_documentAttributes_error_, 2
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.fileWrapperFromRange_documentAttributes_error_, 2
        )

        self.assertResultIsBOOL(
            AppKit.NSMutableAttributedString.readFromURL_options_documentAttributes_error_
        )
        self.assertArgIsOut(
            AppKit.NSMutableAttributedString.readFromURL_options_documentAttributes_error_,
            2,
        )
        self.assertArgIsOut(
            AppKit.NSMutableAttributedString.readFromURL_options_documentAttributes_error_,
            3,
        )

        self.assertResultIsBOOL(
            AppKit.NSMutableAttributedString.readFromData_options_documentAttributes_error_
        )
        self.assertArgIsOut(
            AppKit.NSMutableAttributedString.readFromData_options_documentAttributes_error_,
            2,
        )
        self.assertArgIsOut(
            AppKit.NSMutableAttributedString.readFromData_options_documentAttributes_error_,
            3,
        )

        self.assertResultIsBOOL(
            AppKit.NSMutableAttributedString.readFromURL_options_documentAttributes_
        )
        self.assertArgIsOut(
            AppKit.NSMutableAttributedString.readFromURL_options_documentAttributes_, 2
        )

        self.assertResultIsBOOL(
            AppKit.NSMutableAttributedString.readFromData_options_documentAttributes_
        )
        self.assertArgIsOut(
            AppKit.NSMutableAttributedString.readFromData_options_documentAttributes_, 2
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSAttributedStringEnumerationReverse, 1 << 1)
        self.assertEqual(
            AppKit.NSAttributedStringEnumerationLongestEffectiveRangeNotRequired,
            1 << 20,
        )

        self.assertIsInstance(AppKit.NSWritingDirectionAttributeName, str)
        self.assertIsInstance(AppKit.NSFileTypeDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSCategoryDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSFileTypeDocumentOption, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AppKit.NSVerticalGlyphFormAttributeName, str)
        self.assertIsInstance(AppKit.NSTextLayoutSectionOrientation, str)
        self.assertIsInstance(AppKit.NSTextLayoutSectionRange, str)
        self.assertIsInstance(AppKit.NSTextLayoutSectionsAttribute, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(AppKit.NSTextAlternativesAttributeName, str)
        self.assertIsInstance(AppKit.NSUsesScreenFontsDocumentAttribute, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AppKit.NSTextEffectAttributeName, str)
        self.assertIsInstance(AppKit.NSTextEffectLetterpressStyle, str)

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertEqual(Foundation.NSInlinePresentationIntentEmphasized, 1 << 0)
        self.assertEqual(
            Foundation.NSInlinePresentationIntentStronglyEmphasized, 1 << 1
        )
        self.assertEqual(Foundation.NSInlinePresentationIntentCode, 1 << 2)
        self.assertEqual(Foundation.NSInlinePresentationIntentStrikethrough, 1 << 5)
        self.assertEqual(Foundation.NSInlinePresentationIntentSoftBreak, 1 << 6)
        self.assertEqual(Foundation.NSInlinePresentationIntentLineBreak, 1 << 7)
        self.assertEqual(Foundation.NSInlinePresentationIntentInlineHTML, 1 << 8)
        self.assertEqual(Foundation.NSInlinePresentationIntentBlockHTML, 1 << 9)

        self.assertIsInstance(Foundation.NSInlinePresentationIntentAttributeName, str)
        self.assertIsInstance(Foundation.NSAlternateDescriptionAttributeName, str)
        self.assertIsInstance(Foundation.NSImageURLAttributeName, str)
        self.assertIsInstance(Foundation.NSLanguageIdentifierAttributeName, str)

        self.assertEqual(
            Foundation.NSAttributedStringMarkdownParsingFailureReturnError, 0
        )
        self.assertEqual(
            Foundation.NSAttributedStringMarkdownParsingFailureReturnPartiallyParsedIfPossible,
            1,
        )

        self.assertEqual(Foundation.NSAttributedStringMarkdownInterpretedSyntaxFull, 0)
        self.assertEqual(
            Foundation.NSAttributedStringMarkdownInterpretedSyntaxInlineOnly, 1
        )

        self.assertEqual(
            Foundation.NSAttributedStringFormattingInsertArgumentAttributesWithoutMerging,
            1 << 0,
        )
        self.assertEqual(
            Foundation.NSAttributedStringFormattingApplyReplacementIndexAttribute,
            1 << 1,
        )

        self.assertIsInstance(Foundation.NSReplacementIndexAttributeName, str)
        self.assertIsInstance(Foundation.NSMorphologyAttributeName, str)
        self.assertIsInstance(Foundation.NSInflectionRuleAttributeName, str)
        self.assertIsInstance(Foundation.NSPresentationIntentAttributeName, str)
        self.assertIsInstance(Foundation.NSInflectionAlternativeAttributeName, str)

        self.assertEqual(Foundation.NSPresentationIntentKindParagraph, 0)
        self.assertEqual(Foundation.NSPresentationIntentKindHeader, 1)
        self.assertEqual(Foundation.NSPresentationIntentKindOrderedList, 2)
        self.assertEqual(Foundation.NSPresentationIntentKindUnorderedList, 3)
        self.assertEqual(Foundation.NSPresentationIntentKindListItem, 4)
        self.assertEqual(Foundation.NSPresentationIntentKindCodeBlock, 5)
        self.assertEqual(Foundation.NSPresentationIntentKindBlockQuote, 6)
        self.assertEqual(Foundation.NSPresentationIntentKindThematicBreak, 7)
        self.assertEqual(Foundation.NSPresentationIntentKindTable, 8)
        self.assertEqual(Foundation.NSPresentationIntentKindTableHeaderRow, 9)
        self.assertEqual(Foundation.NSPresentationIntentKindTableRow, 10)
        self.assertEqual(Foundation.NSPresentationIntentKindTableCell, 11)

        self.assertEqual(Foundation.NSPresentationIntentTableColumnAlignmentLeft, 0)
        self.assertEqual(Foundation.NSPresentationIntentTableColumnAlignmentCenter, 1)
        self.assertEqual(Foundation.NSPresentationIntentTableColumnAlignmentRight, 2)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(Foundation.NSMarkdownSourcePositionAttributeName, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(Foundation.NSInflectionConceptsKey, str)
        self.assertIsInstance(
            Foundation.NSInflectionAgreementArgumentAttributeName, str
        )
        self.assertIsInstance(Foundation.NSInflectionAgreementConceptAttributeName, str)
        self.assertIsInstance(Foundation.NSInflectionReferentConceptAttributeName, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgHasType(
            AppKit.NSAttributedString.enumerateAttributesInRange_options_usingBlock_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            AppKit.NSAttributedString.enumerateAttributesInRange_options_usingBlock_,
            2,
            b"v@" + AppKit.NSRange.__typestr__ + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgHasType(
            AppKit.NSAttributedString.enumerateAttribute_inRange_options_usingBlock_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            AppKit.NSAttributedString.enumerateAttribute_inRange_options_usingBlock_,
            3,
            b"v@" + AppKit.NSRange.__typestr__ + b"o^" + objc._C_NSBOOL,
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            Foundation.NSAttributedStringMarkdownParsingOptions.allowsExtendedAttributes
        )
        self.assertArgIsBOOL(
            Foundation.NSAttributedStringMarkdownParsingOptions.setAllowsExtendedAttributes_,
            0,
        )

        self.assertArgIsOut(
            Foundation.NSAttributedString.initWithContentsOfMarkdownFileAtURL_options_baseURL_error_,
            3,
        )
        self.assertArgIsOut(
            Foundation.NSAttributedString.initWithMarkdown_options_baseURL_error_, 3
        )
        self.assertArgIsOut(
            Foundation.NSAttributedString.initWithMarkdownString_options_baseURL_error_,
            3,
        )

        self.assertArgIsPrintf(
            Foundation.NSAttributedString.initWithFormat_options_locale_, 0
        )
        self.assertArgIsPrintf(
            Foundation.NSAttributedString.localizedAttributedStringWithFormat_, 0
        )
        self.assertArgIsPrintf(
            Foundation.NSAttributedString.localizedAttributedStringWithFormat_options_,
            0,
        )

        self.assertArgIsPrintf(
            Foundation.NSMutableAttributedString.appendLocalizedFormat_, 0
        )

        self.assertResultIsBOOL(
            Foundation.NSPresentationIntent.isEquivalentToPresentationIntent_
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            Foundation.NSAttributedStringMarkdownParsingOptions.appliesSourcePositionAttributes
        )
        self.assertArgIsBOOL(
            Foundation.NSAttributedStringMarkdownParsingOptions.setAppliesSourcePositionAttributes_,
            0,
        )
