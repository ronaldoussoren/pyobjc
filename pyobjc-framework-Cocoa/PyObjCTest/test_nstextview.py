import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSTextViewHelper(AppKit.NSObject):
    def textView_URLForContentsOfTextAttachment_atIndex_(self, a, b, c):
        pass

    def textView_clickedOnLink_atIndex_(self, tv, a, b):
        return 1

    def textView_clickedOnCell_inRect_atIndex_(self, tv, a, b, c):
        return 1

    def textView_doubleClickedOnCell_inRect_atIndex_(self, tv, a, b, c):
        return 1

    def textView_draggedCell_inRect_event_atIndex_(elf, tv, a, b, c, d):
        return 1

    def textView_writablePasteboardTypesForCell_atIndex_(self, tv, a, b):
        return 1

    def textView_writeCell_atIndex_toPasteboard_type_(self, tv, a, b, c, d):
        return 1

    def textView_willChangeSelectionFromCharacterRange_toCharacterRange_(
        self, tv, a, b
    ):
        return 1

    def textView_shouldChangeTextInRanges_replacementStrings_(self, tv, a, b):
        return 1

    def textView_willDisplayToolTip_forCharacterAtIndex_(self, tv, a, b):
        return 1

    def textView_completions_forPartialWordRange_indexOfSelectedItem_(
        self, tv, a, b, c
    ):
        return 1

    def textView_shouldChangeTextInRange_replacementString_(self, tv, a, b):
        return 1

    def textView_doCommandBySelector_(self, tv, a):
        return 1

    def textView_clickedOnLink_(self, tv, a):
        return 1

    def textView_clickedOnCell_inRect_(self, tv, a, b):
        return 1

    def textView_doubleClickedOnCell_inRect_(self, tv, a, b):
        return 1

    def textView_draggedCell_inRect_event_(self, tv, a, b, c):
        return 1

    def textView_shouldSetSpellingState_range_(self, tv, a, b):
        return 1

    def textView_menu_forEvent_atIndex_(self, tv, a, b, c):
        return 1

    def textView_willCheckTextInRange_options_types_(self, tv, a, b, c):
        return 1

    def textView_didCheckTextInRange_types_options_results_orthography_wordCount_(
        self, tv, r, t, o, rs, ort, wc
    ):
        return 1

    def textView_candidatesForSelectedRange_(self, tv, r):
        return 1

    def textView_candidates_forSelectedRange_(self, tv, c, r):
        return 1

    def textView_shouldSelectCandidateAtIndex_(self, tv, i):
        return 1


class TestNSTextView(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSPasteboardTypeFindPanelSearchOptionKey, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSFindPanelAction)
        self.assertIsEnumType(AppKit.NSFindPanelSubstringMatchType)
        self.assertIsEnumType(AppKit.NSSelectionAffinity)
        self.assertIsEnumType(AppKit.NSSelectionGranularity)

    def testConstants(self):
        self.assertEqual(AppKit.NSSelectByCharacter, 0)
        self.assertEqual(AppKit.NSSelectByWord, 1)
        self.assertEqual(AppKit.NSSelectByParagraph, 2)

        self.assertEqual(AppKit.NSSelectionAffinityUpstream, 0)
        self.assertEqual(AppKit.NSSelectionAffinityDownstream, 1)

        self.assertEqual(AppKit.NSFindPanelActionShowFindPanel, 1)
        self.assertEqual(AppKit.NSFindPanelActionNext, 2)
        self.assertEqual(AppKit.NSFindPanelActionPrevious, 3)
        self.assertEqual(AppKit.NSFindPanelActionReplaceAll, 4)
        self.assertEqual(AppKit.NSFindPanelActionReplace, 5)
        self.assertEqual(AppKit.NSFindPanelActionReplaceAndFind, 6)
        self.assertEqual(AppKit.NSFindPanelActionSetFindString, 7)
        self.assertEqual(AppKit.NSFindPanelActionReplaceAllInSelection, 8)
        self.assertEqual(AppKit.NSFindPanelActionSelectAll, 9)
        self.assertEqual(AppKit.NSFindPanelActionSelectAllInSelection, 10)

        self.assertIsInstance(AppKit.NSFindPanelSearchOptionsPboardType, str)

        self.assertIsInstance(AppKit.NSFindPanelCaseInsensitiveSearch, str)
        self.assertIsInstance(AppKit.NSFindPanelSubstringMatch, str)

        self.assertEqual(AppKit.NSFindPanelSubstringMatchTypeContains, 0)
        self.assertEqual(AppKit.NSFindPanelSubstringMatchTypeStartsWith, 1)
        self.assertEqual(AppKit.NSFindPanelSubstringMatchTypeFullWord, 2)
        self.assertEqual(AppKit.NSFindPanelSubstringMatchTypeEndsWith, 3)

        self.assertIsInstance(AppKit.NSAllRomanInputSourcesLocaleIdentifier, str)

        self.assertIsInstance(
            AppKit.NSTextViewWillChangeNotifyingTextViewNotification, str
        )
        self.assertIsInstance(AppKit.NSTextViewDidChangeSelectionNotification, str)
        self.assertIsInstance(
            AppKit.NSTextViewDidChangeTypingAttributesNotification, str
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierCharacterPicker, str)
        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierTextColorPicker, str)
        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierTextStyle, str)
        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierTextAlignment, str)
        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierTextList, str)
        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierTextFormat, str)

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(
            AppKit.NSTextViewWillSwitchToNSLayoutManagerNotification, str
        )
        self.assertIsInstance(
            AppKit.NSTextViewDidSwitchToNSLayoutManagerNotification, str
        )

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTextView.shouldDrawInsertionPoint)
        # self.assertArgIsBOOL(AppKit.NSTextView.setShouldDrawInsertionPoint_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.rulerView_shouldMoveMarker_)
        self.assertResultIsBOOL(AppKit.NSTextView.rulerView_shouldAddMarker_)
        self.assertResultIsBOOL(AppKit.NSTextView.rulerView_shouldRemoveMarker_)
        self.assertArgIsBOOL(
            AppKit.NSTextView.setNeedsDisplayInRect_avoidAdditionalLayout_, 1
        )
        self.assertArgIsBOOL(
            AppKit.NSTextView.drawInsertionPointInRect_color_turnedOn_, 2
        )
        self.assertArgIsOut(
            AppKit.NSTextView.completionsForPartialWordRange_indexOfSelectedItem_, 1
        )
        self.assertArgIsBOOL(
            AppKit.NSTextView.insertCompletion_forPartialWordRange_movement_isFinal_, 3
        )
        self.assertResultIsBOOL(AppKit.NSTextView.writeSelectionToPasteboard_type_)
        self.assertResultIsBOOL(AppKit.NSTextView.writeSelectionToPasteboard_types_)
        self.assertResultIsBOOL(AppKit.NSTextView.readSelectionFromPasteboard_type_)
        self.assertResultIsBOOL(AppKit.NSTextView.readSelectionFromPasteboard_)
        self.assertResultIsBOOL(
            AppKit.NSTextView.dragSelectionWithEvent_offset_slideBack_
        )
        self.assertArgIsBOOL(
            AppKit.NSTextView.dragSelectionWithEvent_offset_slideBack_, 2
        )
        self.assertArgIsBOOL(
            AppKit.NSTextView.setSelectedRanges_affinity_stillSelecting_, 2
        )
        self.assertArgIsBOOL(
            AppKit.NSTextView.setSelectedRange_affinity_stillSelecting_, 2
        )
        self.assertArgIsBOOL(
            AppKit.NSTextView.updateInsertionPointStateAndRestartTimer_, 0
        )
        self.assertResultIsBOOL(AppKit.NSTextView.acceptsGlyphInfo)
        self.assertArgIsBOOL(AppKit.NSTextView.setAcceptsGlyphInfo_, 0)
        self.assertArgIsBOOL(AppKit.NSTextView.setRulerVisible_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.usesRuler)
        self.assertArgIsBOOL(AppKit.NSTextView.setUsesRuler_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isContinuousSpellCheckingEnabled)
        self.assertArgIsBOOL(AppKit.NSTextView.setContinuousSpellCheckingEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isGrammarCheckingEnabled)
        self.assertArgIsBOOL(AppKit.NSTextView.setGrammarCheckingEnabled_, 0)
        self.assertResultIsBOOL(
            AppKit.NSTextView.shouldChangeTextInRanges_replacementStrings_
        )
        self.assertResultIsBOOL(
            AppKit.NSTextView.shouldChangeTextInRange_replacementString_
        )
        self.assertResultIsBOOL(AppKit.NSTextView.usesFindPanel)
        self.assertArgIsBOOL(AppKit.NSTextView.setUsesFindPanel_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.allowsDocumentBackgroundColorChange)
        self.assertArgIsBOOL(
            AppKit.NSTextView.setAllowsDocumentBackgroundColorChange_, 0
        )
        self.assertResultIsBOOL(AppKit.NSTextView.allowsUndo)
        self.assertArgIsBOOL(AppKit.NSTextView.setAllowsUndo_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.allowsImageEditing)
        self.assertArgIsBOOL(AppKit.NSTextView.setAllowsImageEditing_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isEditable)
        self.assertArgIsBOOL(AppKit.NSTextView.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isSelectable)
        self.assertArgIsBOOL(AppKit.NSTextView.setSelectable_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isRichText)
        self.assertArgIsBOOL(AppKit.NSTextView.setRichText_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.importsGraphics)
        self.assertArgIsBOOL(AppKit.NSTextView.setImportsGraphics_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.drawsBackground)
        self.assertArgIsBOOL(AppKit.NSTextView.setDrawsBackground_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isFieldEditor)
        self.assertArgIsBOOL(AppKit.NSTextView.setFieldEditor_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.usesFontPanel)
        self.assertArgIsBOOL(AppKit.NSTextView.setUsesFontPanel_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isRulerVisible)
        self.assertArgIsBOOL(AppKit.NSTextView.setRulerVisible_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.smartInsertDeleteEnabled)
        self.assertArgIsBOOL(AppKit.NSTextView.setSmartInsertDeleteEnabled_, 0)

        self.assertArgIsOut(AppKit.NSTextView.dragImageForSelectionWithEvent_origin_, 1)
        self.assertArgIsOut(
            AppKit.NSTextView.smartInsertForString_replacingRange_beforeString_afterString_,
            2,
        )
        self.assertArgIsOut(
            AppKit.NSTextView.smartInsertForString_replacingRange_beforeString_afterString_,
            3,
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSTextView.usesRolloverButtonForSelection)
        self.assertArgIsBOOL(AppKit.NSTextView.setUsesRolloverButtonForSelection_, 0)

    @min_os_level("10.7")
    def testMethods10_7(self):

        self.assertResultIsBOOL(AppKit.NSTextView.usesInspectorBar)
        self.assertArgIsBOOL(AppKit.NSTextView.setUsesInspectorBar_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.usesFindBar)
        self.assertArgIsBOOL(AppKit.NSTextView.setUsesFindBar_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isIncrementalSearchingEnabled)
        self.assertArgIsBOOL(AppKit.NSTextView.setIncrementalSearchingEnabled_, 0)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(AppKit.NSTextView.displaysLinkToolTips)
        self.assertArgIsBOOL(AppKit.NSTextView.setDisplaysLinkToolTips_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isAutomaticQuoteSubstitutionEnabled)
        self.assertArgIsBOOL(AppKit.NSTextView.setAutomaticQuoteSubstitutionEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isAutomaticLinkDetectionEnabled)
        self.assertArgIsBOOL(AppKit.NSTextView.setAutomaticLinkDetectionEnabled_, 0)

    @min_sdk_level("10.6")
    def testProtocolObjects(self):
        objc.protocolNamed("NSTextViewDelegate")

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSTextViewHelper.textView_clickedOnLink_atIndex_)
        self.assertArgHasType(
            TestNSTextViewHelper.textView_clickedOnLink_atIndex_, 2, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_clickedOnCell_inRect_atIndex_,
            2,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_clickedOnCell_inRect_atIndex_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_doubleClickedOnCell_inRect_atIndex_,
            2,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_doubleClickedOnCell_inRect_atIndex_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_draggedCell_inRect_event_atIndex_,
            2,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_draggedCell_inRect_event_atIndex_,
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_writablePasteboardTypesForCell_atIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestNSTextViewHelper.textView_writeCell_atIndex_toPasteboard_type_
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_writeCell_atIndex_toPasteboard_type_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_willChangeSelectionFromCharacterRange_toCharacterRange_,  # noqa: B950
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_willChangeSelectionFromCharacterRange_toCharacterRange_,  # noqa: B950
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultIsBOOL(
            TestNSTextViewHelper.textView_shouldChangeTextInRanges_replacementStrings_
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_willDisplayToolTip_forCharacterAtIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_completions_forPartialWordRange_indexOfSelectedItem_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_completions_forPartialWordRange_indexOfSelectedItem_,
            3,
            b"N^" + objc._C_NSInteger,
        )
        self.assertResultIsBOOL(
            TestNSTextViewHelper.textView_shouldChangeTextInRange_replacementString_
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_shouldChangeTextInRange_replacementString_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultIsBOOL(TestNSTextViewHelper.textView_doCommandBySelector_)
        self.assertArgHasType(
            TestNSTextViewHelper.textView_doCommandBySelector_, 1, objc._C_SEL
        )
        self.assertResultIsBOOL(TestNSTextViewHelper.textView_clickedOnLink_)
        self.assertArgHasType(
            TestNSTextViewHelper.textView_clickedOnCell_inRect_,
            2,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_doubleClickedOnCell_inRect_,
            2,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_draggedCell_inRect_event_,
            2,
            AppKit.NSRect.__typestr__,
        )

    @min_os_level("10.5")
    def testProtocols10_5(self):
        self.assertArgHasType(
            TestNSTextViewHelper.textView_shouldSetSpellingState_range_,
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_shouldSetSpellingState_range_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_menu_forEvent_atIndex_, 3, objc._C_NSUInteger
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSTextView.isCoalescingUndo)

        self.assertArgIsBOOL(AppKit.NSTextView.setAutomaticDataDetectionEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isAutomaticDataDetectionEnabled)
        self.assertArgIsBOOL(AppKit.NSTextView.setAutomaticDashSubstitutionEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isAutomaticDashSubstitutionEnabled)
        self.assertArgIsBOOL(AppKit.NSTextView.setAutomaticTextReplacementEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSTextView.isAutomaticTextReplacementEnabled)
        self.assertArgIsBOOL(
            AppKit.NSTextView.setAutomaticSpellingCorrectionEnabled_, 0
        )
        self.assertResultIsBOOL(AppKit.NSTextView.isAutomaticSpellingCorrectionEnabled)

        self.assertArgHasType(
            AppKit.NSTextView.checkTextInRange_types_options_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            AppKit.NSTextView.handleTextCheckingResults_forRange_types_options_orthography_wordCount_,  # noqa: B950
            1,
            AppKit.NSRange.__typestr__,
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSTextView.stronglyReferencesTextStorage)

        self.assertResultIsBOOL(AppKit.NSTextView.allowsCharacterPickerTouchBarItem)
        self.assertArgIsBOOL(AppKit.NSTextView.setAllowsCharacterPickerTouchBarItem_, 0)

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertResultIsBOOL(
            AppKit.NSTextView.performValidatedReplacementInRange_withAttributedString_
        )
        self.assertResultIsBOOL(
            AppKit.NSTextView.usesAdaptiveColorMappingForDarkAppearance
        )
        self.assertArgIsBOOL(
            AppKit.NSTextView.setUsesAdaptiveColorMappingForDarkAppearance_, 0
        )

    @min_os_level("10.6")
    def testProtocols10_6(self):
        self.assertArgHasType(
            TestNSTextViewHelper.textView_willCheckTextInRange_options_types_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_willCheckTextInRange_options_types_,
            3,
            b"N^" + objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestNSTextViewHelper.textView_didCheckTextInRange_types_options_results_orthography_wordCount_,  # noqa: B950
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_didCheckTextInRange_types_options_results_orthography_wordCount_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_didCheckTextInRange_types_options_results_orthography_wordCount_,  # noqa: B950
            6,
            objc._C_NSInteger,
        )

    @min_os_level("10.7")
    def testProtocols10_7(self):
        self.assertArgHasType(
            TestNSTextViewHelper.textView_URLForContentsOfTextAttachment_atIndex_,
            2,
            objc._C_NSUInteger,
        )

    @min_os_level("10.12")
    def testProtocols10_12(self):
        self.assertArgHasType(
            TestNSTextViewHelper.textView_candidatesForSelectedRange_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_candidates_forSelectedRange_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextViewHelper.textView_shouldSelectCandidateAtIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestNSTextViewHelper.textView_shouldSelectCandidateAtIndex_
        )

    @min_os_level("10.14")
    def testProtocols10_14(self):
        objc.protocolNamed("NSUserActivityRestoring")
