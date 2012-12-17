
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSTextViewHelper (NSObject):
    def textView_URLForContentsOfTextAttachment_atIndex_(self, a, b, c): pass
    def textView_clickedOnLink_atIndex_(self, tv, a, b): return 1
    def textView_clickedOnCell_inRect_atIndex_(self, tv, a, b, c): return 1
    def textView_doubleClickedOnCell_inRect_atIndex_(self, tv, a, b, c): return 1
    def textView_draggedCell_inRect_event_atIndex_(elf, tv, a, b, c, d): return 1
    def textView_writablePasteboardTypesForCell_atIndex_(self, tv, a, b): return 1
    def textView_writeCell_atIndex_toPasteboard_type_(self, tv, a, b, c, d): return 1
    def textView_willChangeSelectionFromCharacterRange_toCharacterRange_(self, tv, a, b): return 1
    def textView_shouldChangeTextInRanges_replacementStrings_(self, tv, a, b): return 1
    def textView_willDisplayToolTip_forCharacterAtIndex_(self, tv, a, b): return 1
    def textView_completions_forPartialWordRange_indexOfSelectedItem_(self, tv, a, b, c): return 1
    def textView_shouldChangeTextInRange_replacementString_(self, tv, a, b): return 1
    def textView_doCommandBySelector_(self, tv, a): return 1
    def textView_clickedOnLink_(self, tv, a): return 1
    def textView_clickedOnCell_inRect_(self, tv, a, b): return 1
    def textView_doubleClickedOnCell_inRect_(self, tv, a, b): return 1
    def textView_draggedCell_inRect_event_(self, tv, a, b, c): return 1
    def textView_shouldSetSpellingState_range_(self, tv, a, b): return 1
    def textView_menu_forEvent_atIndex_(self, tv, a, b, c): return 1
    def textView_willCheckTextInRange_options_types_(self, tv, a, b, c): return 1
    def textView_didCheckTextInRange_types_options_results_orthography_wordCount_(self, tv, r, t, o, rs, ort, wc): return 1

class TestNSTextView (TestCase):
    def testConstants(self):
        self.assertEqual(NSSelectByCharacter, 0)
        self.assertEqual(NSSelectByWord, 1)
        self.assertEqual(NSSelectByParagraph, 2)
        self.assertEqual(NSSelectionAffinityUpstream, 0)
        self.assertEqual(NSSelectionAffinityDownstream, 1)
        self.assertEqual(NSFindPanelActionShowFindPanel, 1)
        self.assertEqual(NSFindPanelActionNext, 2)
        self.assertEqual(NSFindPanelActionPrevious, 3)
        self.assertEqual(NSFindPanelActionReplaceAll, 4)
        self.assertEqual(NSFindPanelActionReplace, 5)
        self.assertEqual(NSFindPanelActionReplaceAndFind, 6)
        self.assertEqual(NSFindPanelActionSetFindString, 7)
        self.assertEqual(NSFindPanelActionReplaceAllInSelection, 8)
        self.assertEqual(NSFindPanelActionSelectAll, 9)
        self.assertEqual(NSFindPanelActionSelectAllInSelection, 10)

        self.assertIsInstance(NSFindPanelSearchOptionsPboardType, unicode)

        self.assertIsInstance(NSFindPanelCaseInsensitiveSearch, unicode)
        self.assertIsInstance(NSFindPanelSubstringMatch, unicode)

        self.assertEqual(NSFindPanelSubstringMatchTypeContains, 0)
        self.assertEqual(NSFindPanelSubstringMatchTypeStartsWith, 1)
        self.assertEqual(NSFindPanelSubstringMatchTypeFullWord, 2)
        self.assertEqual(NSFindPanelSubstringMatchTypeEndsWith, 3)

        self.assertIsInstance(NSAllRomanInputSourcesLocaleIdentifier, unicode)

        self.assertIsInstance(NSTextViewWillChangeNotifyingTextViewNotification, unicode)
        self.assertIsInstance(NSTextViewDidChangeSelectionNotification, unicode)
        self.assertIsInstance(NSTextViewDidChangeTypingAttributesNotification, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(NSTextView.rulerView_shouldMoveMarker_)
        self.assertResultIsBOOL(NSTextView.rulerView_shouldAddMarker_)
        self.assertResultIsBOOL(NSTextView.rulerView_shouldRemoveMarker_)
        self.assertArgIsBOOL(NSTextView.setNeedsDisplayInRect_avoidAdditionalLayout_, 1)
        self.assertArgIsBOOL(NSTextView.drawInsertionPointInRect_color_turnedOn_, 2)
        self.assertArgIsOut(NSTextView.completionsForPartialWordRange_indexOfSelectedItem_, 1)
        self.assertArgIsBOOL(NSTextView.insertCompletion_forPartialWordRange_movement_isFinal_, 3)
        self.assertResultIsBOOL(NSTextView.writeSelectionToPasteboard_type_)
        self.assertResultIsBOOL(NSTextView.writeSelectionToPasteboard_types_)
        self.assertResultIsBOOL(NSTextView.readSelectionFromPasteboard_type_)
        self.assertResultIsBOOL(NSTextView.readSelectionFromPasteboard_)
        self.assertResultIsBOOL(NSTextView.dragSelectionWithEvent_offset_slideBack_)
        self.assertArgIsBOOL(NSTextView.dragSelectionWithEvent_offset_slideBack_, 2)
        self.assertArgIsBOOL(NSTextView.setSelectedRanges_affinity_stillSelecting_, 2)
        self.assertArgIsBOOL(NSTextView.setSelectedRange_affinity_stillSelecting_, 2)
        self.assertArgIsBOOL(NSTextView.updateInsertionPointStateAndRestartTimer_, 0)
        self.assertResultIsBOOL(NSTextView.acceptsGlyphInfo)
        self.assertArgIsBOOL(NSTextView.setAcceptsGlyphInfo_, 0)
        self.assertArgIsBOOL(NSTextView.setRulerVisible_, 0)
        self.assertResultIsBOOL(NSTextView.usesRuler)
        self.assertArgIsBOOL(NSTextView.setUsesRuler_, 0)
        self.assertResultIsBOOL(NSTextView.isContinuousSpellCheckingEnabled)
        self.assertArgIsBOOL(NSTextView.setContinuousSpellCheckingEnabled_, 0)
        self.assertResultIsBOOL(NSTextView.isGrammarCheckingEnabled)
        self.assertArgIsBOOL(NSTextView.setGrammarCheckingEnabled_, 0)
        self.assertResultIsBOOL(NSTextView.shouldChangeTextInRanges_replacementStrings_)
        self.assertResultIsBOOL(NSTextView.shouldChangeTextInRange_replacementString_)
        self.assertResultIsBOOL(NSTextView.usesFindPanel)
        self.assertArgIsBOOL(NSTextView.setUsesFindPanel_, 0)
        self.assertResultIsBOOL(NSTextView.allowsDocumentBackgroundColorChange)
        self.assertArgIsBOOL(NSTextView.setAllowsDocumentBackgroundColorChange_, 0)
        self.assertResultIsBOOL(NSTextView.allowsUndo)
        self.assertArgIsBOOL(NSTextView.setAllowsUndo_, 0)
        self.assertResultIsBOOL(NSTextView.allowsImageEditing)
        self.assertArgIsBOOL(NSTextView.setAllowsImageEditing_, 0)
        self.assertResultIsBOOL(NSTextView.isEditable)
        self.assertArgIsBOOL(NSTextView.setEditable_, 0)
        self.assertResultIsBOOL(NSTextView.isSelectable)
        self.assertArgIsBOOL(NSTextView.setSelectable_, 0)
        self.assertResultIsBOOL(NSTextView.isRichText)
        self.assertArgIsBOOL(NSTextView.setRichText_, 0)
        self.assertResultIsBOOL(NSTextView.importsGraphics)
        self.assertArgIsBOOL(NSTextView.setImportsGraphics_, 0)
        self.assertResultIsBOOL(NSTextView.drawsBackground)
        self.assertArgIsBOOL(NSTextView.setDrawsBackground_, 0)
        self.assertResultIsBOOL(NSTextView.isFieldEditor)
        self.assertArgIsBOOL(NSTextView.setFieldEditor_, 0)
        self.assertResultIsBOOL(NSTextView.usesFontPanel)
        self.assertArgIsBOOL(NSTextView.setUsesFontPanel_, 0)
        self.assertResultIsBOOL(NSTextView.isRulerVisible)
        self.assertResultIsBOOL(NSTextView.smartInsertDeleteEnabled)
        self.assertArgIsBOOL(NSTextView.setSmartInsertDeleteEnabled_, 0)

        self.assertArgIsOut(NSTextView.dragImageForSelectionWithEvent_origin_, 1)
        self.assertArgIsOut(NSTextView.smartInsertForString_replacingRange_beforeString_afterString_, 2)
        self.assertArgIsOut(NSTextView.smartInsertForString_replacingRange_beforeString_afterString_, 3)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSTextView.usesInspectorBar)
        self.assertArgIsBOOL(NSTextView.setUsesInspectorBar_, 0)
        self.assertResultIsBOOL(NSTextView.usesFindBar)
        self.assertArgIsBOOL(NSTextView.setUsesFindBar_, 0)
        self.assertResultIsBOOL(NSTextView.isIncrementalSearchingEnabled)
        self.assertArgIsBOOL(NSTextView.setIncrementalSearchingEnabled_, 0)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSTextView.displaysLinkToolTips)
        self.assertArgIsBOOL(NSTextView.setDisplaysLinkToolTips_, 0)
        self.assertResultIsBOOL(NSTextView.isAutomaticQuoteSubstitutionEnabled)
        self.assertArgIsBOOL(NSTextView.setAutomaticQuoteSubstitutionEnabled_, 0)
        self.assertResultIsBOOL(NSTextView.isAutomaticLinkDetectionEnabled)
        self.assertArgIsBOOL(NSTextView.setAutomaticLinkDetectionEnabled_, 0)


    def testProtocols(self):
        self.assertResultIsBOOL(TestNSTextViewHelper.textView_clickedOnLink_atIndex_)
        self.assertArgHasType(TestNSTextViewHelper.textView_clickedOnLink_atIndex_, 2, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextViewHelper.textView_clickedOnCell_inRect_atIndex_, 2, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextViewHelper.textView_clickedOnCell_inRect_atIndex_, 3, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextViewHelper.textView_doubleClickedOnCell_inRect_atIndex_, 2, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextViewHelper.textView_doubleClickedOnCell_inRect_atIndex_, 3, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextViewHelper.textView_draggedCell_inRect_event_atIndex_, 2, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextViewHelper.textView_draggedCell_inRect_event_atIndex_, 4, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextViewHelper.textView_writablePasteboardTypesForCell_atIndex_, 2, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestNSTextViewHelper.textView_writeCell_atIndex_toPasteboard_type_)
        self.assertArgHasType(TestNSTextViewHelper.textView_writeCell_atIndex_toPasteboard_type_, 2, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextViewHelper.textView_willChangeSelectionFromCharacterRange_toCharacterRange_, 1, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextViewHelper.textView_willChangeSelectionFromCharacterRange_toCharacterRange_, 2, NSRange.__typestr__)
        self.assertResultIsBOOL(TestNSTextViewHelper.textView_shouldChangeTextInRanges_replacementStrings_)
        self.assertArgHasType(TestNSTextViewHelper.textView_willDisplayToolTip_forCharacterAtIndex_, 2, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextViewHelper.textView_completions_forPartialWordRange_indexOfSelectedItem_, 2, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextViewHelper.textView_completions_forPartialWordRange_indexOfSelectedItem_, 3, b'N^'+objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSTextViewHelper.textView_shouldChangeTextInRange_replacementString_)
        self.assertArgHasType(TestNSTextViewHelper.textView_shouldChangeTextInRange_replacementString_, 1, NSRange.__typestr__)
        self.assertResultIsBOOL(TestNSTextViewHelper.textView_doCommandBySelector_)
        self.assertArgHasType(TestNSTextViewHelper.textView_doCommandBySelector_, 1, objc._C_SEL)
        self.assertResultIsBOOL(TestNSTextViewHelper.textView_clickedOnLink_)
        self.assertArgHasType(TestNSTextViewHelper.textView_clickedOnCell_inRect_, 2, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextViewHelper.textView_doubleClickedOnCell_inRect_, 2, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextViewHelper.textView_draggedCell_inRect_event_, 2, NSRect.__typestr__)

    @min_os_level('10.5')
    def testProtocols10_5(self):
        self.assertArgHasType(TestNSTextViewHelper.textView_shouldSetSpellingState_range_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSTextViewHelper.textView_shouldSetSpellingState_range_, 2, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextViewHelper.textView_menu_forEvent_atIndex_, 3, objc._C_NSUInteger)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSTextView.isCoalescingUndo)

        self.assertArgIsBOOL(NSTextView.setAutomaticDataDetectionEnabled_, 0)
        self.assertResultIsBOOL(NSTextView.isAutomaticDataDetectionEnabled)
        self.assertArgIsBOOL(NSTextView.setAutomaticDashSubstitutionEnabled_, 0)
        self.assertResultIsBOOL(NSTextView.isAutomaticDashSubstitutionEnabled)
        self.assertArgIsBOOL(NSTextView.setAutomaticTextReplacementEnabled_, 0)
        self.assertResultIsBOOL(NSTextView.isAutomaticTextReplacementEnabled)
        self.assertArgIsBOOL(NSTextView.setAutomaticSpellingCorrectionEnabled_, 0)
        self.assertResultIsBOOL(NSTextView.isAutomaticSpellingCorrectionEnabled)

        self.assertArgHasType(NSTextView.checkTextInRange_types_options_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextView.handleTextCheckingResults_forRange_types_options_orthography_wordCount_, 1, NSRange.__typestr__)

    @min_os_level('10.6')
    def testProtocols10_6(self):
        self.assertArgHasType(TestNSTextViewHelper.textView_willCheckTextInRange_options_types_, 1, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextViewHelper.textView_willCheckTextInRange_options_types_, 3, b'N^' + objc._C_NSInteger)

        self.assertArgHasType(TestNSTextViewHelper.textView_didCheckTextInRange_types_options_results_orthography_wordCount_, 1, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextViewHelper.textView_didCheckTextInRange_types_options_results_orthography_wordCount_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSTextViewHelper.textView_didCheckTextInRange_types_options_results_orthography_wordCount_, 6, objc._C_NSInteger)

    @min_os_level('10.7')
    def testProtocols10_7(self):
        self.assertArgHasType(TestNSTextViewHelper.textView_URLForContentsOfTextAttachment_atIndex_, 2, objc._C_NSUInteger)



if __name__ == "__main__":
    main()
