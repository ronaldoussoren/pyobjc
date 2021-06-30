import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSAttributedString(TestCase):
    def testConstants(self):
        self.assertIsInstance(AppKit.NSFontAttributeName, str)
        self.assertIsInstance(AppKit.NSParagraphStyleAttributeName, str)
        self.assertIsInstance(AppKit.NSForegroundColorAttributeName, str)
        self.assertIsInstance(AppKit.NSSuperscriptAttributeName, str)
        self.assertIsInstance(AppKit.NSBackgroundColorAttributeName, str)
        self.assertIsInstance(AppKit.NSLigatureAttributeName, str)
        self.assertIsInstance(AppKit.NSBaselineOffsetAttributeName, str)
        self.assertIsInstance(AppKit.NSKernAttributeName, str)
        self.assertIsInstance(AppKit.NSLinkAttributeName, str)

        self.assertIsInstance(AppKit.NSStrokeWidthAttributeName, str)
        self.assertIsInstance(AppKit.NSStrokeColorAttributeName, str)
        self.assertIsInstance(AppKit.NSUnderlineColorAttributeName, str)
        self.assertIsInstance(AppKit.NSStrikethroughStyleAttributeName, str)
        self.assertIsInstance(AppKit.NSUnderlineStyleAttributeName, str)
        self.assertIsInstance(AppKit.NSObliquenessAttributeName, str)
        self.assertIsInstance(AppKit.NSStrikethroughColorAttributeName, str)
        self.assertIsInstance(AppKit.NSShadowAttributeName, str)
        self.assertIsInstance(AppKit.NSExpansionAttributeName, str)
        self.assertIsInstance(AppKit.NSToolTipAttributeName, str)

        self.assertIsInstance(AppKit.NSCharacterShapeAttributeName, str)
        self.assertIsInstance(AppKit.NSGlyphInfoAttributeName, str)
        self.assertIsInstance(AppKit.NSMarkedClauseSegmentAttributeName, str)

        self.assertEqual(AppKit.NSUnderlineStyleNone, 0x00)
        self.assertEqual(AppKit.NSUnderlineStyleSingle, 0x01)
        self.assertEqual(AppKit.NSUnderlineStyleThick, 0x02)
        self.assertEqual(AppKit.NSUnderlineStyleDouble, 0x09)

        self.assertEqual(AppKit.NSUnderlinePatternSolid, 0x0000)
        self.assertEqual(AppKit.NSUnderlinePatternDot, 0x0100)
        self.assertEqual(AppKit.NSUnderlinePatternDash, 0x0200)
        self.assertEqual(AppKit.NSUnderlinePatternDashDot, 0x0300)
        self.assertEqual(AppKit.NSUnderlinePatternDashDotDot, 0x0400)

        self.assertEqual(AppKit.NSUnderlineByWordMask, 0x8000)
        self.assertEqual(AppKit.NSWritingDirectionEmbedding, 0 << 1)
        self.assertEqual(AppKit.NSWritingDirectionOverride, 1 << 1)

        self.assertIsInstance(AppKit.NSSpellingStateAttributeName, str)

        self.assertEqual(AppKit.NSSpellingStateSpellingFlag, (1 << 0))
        self.assertEqual(AppKit.NSSpellingStateGrammarFlag, (1 << 1))

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

        self.assertIsInstance(AppKit.NSAttachmentAttributeName, str)
        self.assertIsInstance(AppKit.NSCursorAttributeName, str)

        self.assertEqual(AppKit.NSUnderlineStylePatternSolid, 0x0000)
        self.assertEqual(AppKit.NSUnderlineStylePatternDot, 0x0100)
        self.assertEqual(AppKit.NSUnderlineStylePatternDash, 0x0200)
        self.assertEqual(AppKit.NSUnderlineStylePatternDashDot, 0x0300)
        self.assertEqual(AppKit.NSUnderlineStylePatternDashDotDot, 0x0400)

        self.assertEqual(AppKit.NSUnderlineStyleByWord, 0x8000)

        self.assertEqual(AppKit.NSTextScalingStandard, 0)
        self.assertEqual(AppKit.NSTextScalingiOS, 1)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(AppKit.NSAppearanceDocumentAttribute, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(AppKit.NSTextScalingDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSSourceTextScalingDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSTargetTextScalingDocumentOption, str)
        self.assertIsInstance(AppKit.NSSourceTextScalingDocumentOption, str)

    def testMethods(self):
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
            AppKit.NSAttributedString.dataFromRange_documentAttributes_error_, 2
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.fileWrapperFromRange_documentAttributes_error_, 2
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
            AppKit.NSAttributedString.initWithHTML_baseURL_documentAttributes_, 2
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithDocFormat_documentAttributes_, 1
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithHTML_options_documentAttributes_, 2
        )
        self.assertArgIsOut(
            AppKit.NSAttributedString.initWithRTFDFileWrapper_documentAttributes_, 1
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

        self.assertArgHasType(
            AppKit.NSAttributedString.URLAtIndex_effectiveRange_,
            1,
            b"o^" + AppKit.NSRange.__typestr__,
        )

        self.assertArgIsBOOL(
            AppKit.NSMutableAttributedString.nextWordFromIndex_forward_, 1
        )
        self.assertResultIsBOOL(AppKit.NSAttributedString.containsAttachments)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(
            AppKit.NSMutableAttributedString.containsAttachmentsInRange_
        )

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(AppKit.NSManagerDocumentAttribute, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
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

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(AppKit.NSDefaultAttributesDocumentAttribute, str)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(AppKit.NSTrackingAttributeName, str)
