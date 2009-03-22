
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextViewHelper (NSObject):
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

class TestNSTextView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSSelectByCharacter, 0)
        self.failUnlessEqual(NSSelectByWord, 1)
        self.failUnlessEqual(NSSelectByParagraph, 2)
        self.failUnlessEqual(NSSelectionAffinityUpstream, 0)
        self.failUnlessEqual(NSSelectionAffinityDownstream, 1)
        self.failUnlessEqual(NSFindPanelActionShowFindPanel, 1)
        self.failUnlessEqual(NSFindPanelActionNext, 2)
        self.failUnlessEqual(NSFindPanelActionPrevious, 3)
        self.failUnlessEqual(NSFindPanelActionReplaceAll, 4)
        self.failUnlessEqual(NSFindPanelActionReplace, 5)
        self.failUnlessEqual(NSFindPanelActionReplaceAndFind, 6)
        self.failUnlessEqual(NSFindPanelActionSetFindString, 7)
        self.failUnlessEqual(NSFindPanelActionReplaceAllInSelection, 8)
        self.failUnlessEqual(NSFindPanelActionSelectAll, 9)
        self.failUnlessEqual(NSFindPanelActionSelectAllInSelection, 10)

        self.failUnlessIsInstance(NSFindPanelSearchOptionsPboardType, unicode)

        self.failUnlessIsInstance(NSFindPanelCaseInsensitiveSearch, unicode)
        self.failUnlessIsInstance(NSFindPanelSubstringMatch, unicode)

        self.failUnlessEqual(NSFindPanelSubstringMatchTypeContains, 0)
        self.failUnlessEqual(NSFindPanelSubstringMatchTypeStartsWith, 1)
        self.failUnlessEqual(NSFindPanelSubstringMatchTypeFullWord, 2)
        self.failUnlessEqual(NSFindPanelSubstringMatchTypeEndsWith, 3)

        self.failUnlessIsInstance(NSAllRomanInputSourcesLocaleIdentifier, unicode)

        self.failUnlessIsInstance(NSTextViewWillChangeNotifyingTextViewNotification, unicode)
        self.failUnlessIsInstance(NSTextViewDidChangeSelectionNotification, unicode)
        self.failUnlessIsInstance(NSTextViewDidChangeTypingAttributesNotification, unicode)
        

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTextView.rulerView_shouldMoveMarker_)
        self.failUnlessResultIsBOOL(NSTextView.rulerView_shouldAddMarker_)
        self.failUnlessResultIsBOOL(NSTextView.rulerView_shouldRemoveMarker_)
        self.failUnlessArgIsBOOL(NSTextView.setNeedsDisplayInRect_avoidAdditionalLayout_, 1)
        self.failUnlessArgIsBOOL(NSTextView.drawInsertionPointInRect_color_turnedOn_, 2)
        self.failUnlessArgIsOut(NSTextView.completionsForPartialWordRange_indexOfSelectedItem_, 1)
        self.failUnlessArgIsBOOL(NSTextView.insertCompletion_forPartialWordRange_movement_isFinal_, 3)
        self.failUnlessResultIsBOOL(NSTextView.writeSelectionToPasteboard_type_)
        self.failUnlessResultIsBOOL(NSTextView.writeSelectionToPasteboard_types_)
        self.failUnlessResultIsBOOL(NSTextView.readSelectionFromPasteboard_type_)
        self.failUnlessResultIsBOOL(NSTextView.readSelectionFromPasteboard_)
        self.failUnlessResultIsBOOL(NSTextView.dragSelectionWithEvent_offset_slideBack_)
        self.failUnlessArgIsBOOL(NSTextView.dragSelectionWithEvent_offset_slideBack_, 2)
        self.failUnlessArgIsBOOL(NSTextView.setSelectedRanges_affinity_stillSelecting_, 2)
        self.failUnlessArgIsBOOL(NSTextView.setSelectedRange_affinity_stillSelecting_, 2)
        self.failUnlessArgIsBOOL(NSTextView.updateInsertionPointStateAndRestartTimer_, 0)
        self.failUnlessResultIsBOOL(NSTextView.acceptsGlyphInfo)
        self.failUnlessArgIsBOOL(NSTextView.setAcceptsGlyphInfo_, 0)
        self.failUnlessArgIsBOOL(NSTextView.setRulerVisible_, 0)
        self.failUnlessResultIsBOOL(NSTextView.usesRuler)
        self.failUnlessArgIsBOOL(NSTextView.setUsesRuler_, 0)
        self.failUnlessResultIsBOOL(NSTextView.isContinuousSpellCheckingEnabled)
        self.failUnlessArgIsBOOL(NSTextView.setContinuousSpellCheckingEnabled_, 0)
        self.failUnlessResultIsBOOL(NSTextView.isGrammarCheckingEnabled)
        self.failUnlessArgIsBOOL(NSTextView.setGrammarCheckingEnabled_, 0)
        self.failUnlessResultIsBOOL(NSTextView.shouldChangeTextInRanges_replacementStrings_)
        self.failUnlessResultIsBOOL(NSTextView.shouldChangeTextInRange_replacementString_)
        self.failUnlessResultIsBOOL(NSTextView.usesFindPanel)
        self.failUnlessArgIsBOOL(NSTextView.setUsesFindPanel_, 0)
        self.failUnlessResultIsBOOL(NSTextView.allowsDocumentBackgroundColorChange)
        self.failUnlessArgIsBOOL(NSTextView.setAllowsDocumentBackgroundColorChange_, 0)
        self.failUnlessResultIsBOOL(NSTextView.allowsUndo)
        self.failUnlessArgIsBOOL(NSTextView.setAllowsUndo_, 0)
        self.failUnlessResultIsBOOL(NSTextView.allowsImageEditing)
        self.failUnlessArgIsBOOL(NSTextView.setAllowsImageEditing_, 0)
        self.failUnlessResultIsBOOL(NSTextView.isEditable)
        self.failUnlessArgIsBOOL(NSTextView.setEditable_, 0)
        self.failUnlessResultIsBOOL(NSTextView.isSelectable)
        self.failUnlessArgIsBOOL(NSTextView.setSelectable_, 0)
        self.failUnlessResultIsBOOL(NSTextView.isRichText)
        self.failUnlessArgIsBOOL(NSTextView.setRichText_, 0)
        self.failUnlessResultIsBOOL(NSTextView.importsGraphics)
        self.failUnlessArgIsBOOL(NSTextView.setImportsGraphics_, 0)
        self.failUnlessResultIsBOOL(NSTextView.drawsBackground)
        self.failUnlessArgIsBOOL(NSTextView.setDrawsBackground_, 0)
        self.failUnlessResultIsBOOL(NSTextView.isFieldEditor)
        self.failUnlessArgIsBOOL(NSTextView.setFieldEditor_, 0)
        self.failUnlessResultIsBOOL(NSTextView.usesFontPanel)
        self.failUnlessArgIsBOOL(NSTextView.setUsesFontPanel_, 0)
        self.failUnlessResultIsBOOL(NSTextView.isRulerVisible)
        self.failUnlessResultIsBOOL(NSTextView.smartInsertDeleteEnabled)
        self.failUnlessArgIsBOOL(NSTextView.setSmartInsertDeleteEnabled_, 0)

        self.failUnlessArgIsOut(NSTextView.dragImageForSelectionWithEvent_origin_, 1)
        self.failUnlessArgIsOut(NSTextView.smartInsertForString_replacingRange_beforeString_afterString_, 2)
        self.failUnlessArgIsOut(NSTextView.smartInsertForString_replacingRange_beforeString_afterString_, 3)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSTextView.displaysLinkToolTips)
        self.failUnlessArgIsBOOL(NSTextView.setDisplaysLinkToolTips_, 0)
        self.failUnlessResultIsBOOL(NSTextView.isAutomaticQuoteSubstitutionEnabled)
        self.failUnlessArgIsBOOL(NSTextView.setAutomaticQuoteSubstitutionEnabled_, 0)
        self.failUnlessResultIsBOOL(NSTextView.isAutomaticLinkDetectionEnabled)
        self.failUnlessArgIsBOOL(NSTextView.setAutomaticLinkDetectionEnabled_, 0)


    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSTextViewHelper.textView_clickedOnLink_atIndex_)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_clickedOnLink_atIndex_, 2, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_clickedOnCell_inRect_atIndex_, 2, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_clickedOnCell_inRect_atIndex_, 3, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_doubleClickedOnCell_inRect_atIndex_, 2, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_doubleClickedOnCell_inRect_atIndex_, 3, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_draggedCell_inRect_event_atIndex_, 2, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_draggedCell_inRect_event_atIndex_, 4, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_writablePasteboardTypesForCell_atIndex_, 2, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestNSTextViewHelper.textView_writeCell_atIndex_toPasteboard_type_)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_writeCell_atIndex_toPasteboard_type_, 2, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_willChangeSelectionFromCharacterRange_toCharacterRange_, 1, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_willChangeSelectionFromCharacterRange_toCharacterRange_, 2, NSRange.__typestr__)
        self.failUnlessResultIsBOOL(TestNSTextViewHelper.textView_shouldChangeTextInRanges_replacementStrings_)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_willDisplayToolTip_forCharacterAtIndex_, 2, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_completions_forPartialWordRange_indexOfSelectedItem_, 2, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_completions_forPartialWordRange_indexOfSelectedItem_, 3, 'N^'+objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSTextViewHelper.textView_shouldChangeTextInRange_replacementString_)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_shouldChangeTextInRange_replacementString_, 1, NSRange.__typestr__)
        self.failUnlessResultIsBOOL(TestNSTextViewHelper.textView_doCommandBySelector_)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_doCommandBySelector_, 1, objc._C_SEL)
        self.failUnlessResultIsBOOL(TestNSTextViewHelper.textView_clickedOnLink_)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_clickedOnCell_inRect_, 2, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_doubleClickedOnCell_inRect_, 2, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_draggedCell_inRect_event_, 2, NSRect.__typestr__)

    @min_os_level('10.5')
    def testProtocols10_5(self):
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_shouldSetSpellingState_range_, 1, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_shouldSetSpellingState_range_, 2, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSTextViewHelper.textView_menu_forEvent_atIndex_, 3, objc._C_NSUInteger)




if __name__ == "__main__":
    main()
