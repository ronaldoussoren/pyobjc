import HIServices
from PyObjCTools.TestSupport import TestCase


class TestAXWebConstants(TestCase):
    def testConstants(self):
        self.assertEqual(HIServices.kAXARIAAtomicAttribute, "AXARIAAtomic")
        self.assertEqual(HIServices.kAXARIAColumnCountAttribute, "AXARIAColumnCount")
        self.assertEqual(HIServices.kAXARIAColumnIndexAttribute, "AXARIAColumnIndex")
        self.assertEqual(HIServices.kAXARIACurrentAttribute, "AXARIACurrent")
        self.assertEqual(HIServices.kAXARIALiveAttribute, "AXARIALive")
        self.assertEqual(HIServices.kAXARIAPosInSetAttribute, "AXARIAPosInSet")
        self.assertEqual(HIServices.kAXARIARelevantAttribute, "AXARIARelevant")
        self.assertEqual(HIServices.kAXARIARowCountAttribute, "AXARIARowCount")
        self.assertEqual(HIServices.kAXARIARowIndexAttribute, "AXARIARowIndex")
        self.assertEqual(HIServices.kAXARIASetSizeAttribute, "AXARIASetSize")
        self.assertEqual(HIServices.kAXAccessKeyAttribute, "AXAccessKey")
        self.assertEqual(HIServices.kAXActiveElementAttribute, "AXActiveElement")
        self.assertEqual(HIServices.kAXBrailleLabelAttribute, "AXBrailleLabel")
        self.assertEqual(
            HIServices.kAXBrailleRoleDescriptionAttribute, "AXBrailleRoleDescription"
        )
        self.assertEqual(
            HIServices.kAXCaretBrowsingEnabledAttribute, "AXCaretBrowsingEnabled"
        )
        self.assertEqual(HIServices.kAXDOMClassListAttribute, "AXDOMClassList")
        self.assertEqual(HIServices.kAXDOMIdentifierAttribute, "AXDOMIdentifier")
        self.assertEqual(HIServices.kAXDatetimeValueAttribute, "AXDateTimeValue")
        self.assertEqual(HIServices.kAXDescribedByAttribute, "AXDescribedBy")
        self.assertEqual(HIServices.kAXDropEffectsAttribute, "AXDropEffects")
        self.assertEqual(HIServices.kAXEditableAncestorAttribute, "AXEditableAncestor")
        self.assertEqual(HIServices.kAXElementBusyAttribute, "AXElementBusy")
        self.assertEqual(HIServices.kAXEndTextMarkerAttribute, "AXEndTextMarker")
        self.assertEqual(
            HIServices.kAXErrorMessageElementsAttribute, "AXErrorMessageElements"
        )
        self.assertEqual(
            HIServices.kAXExpandedTextValueAttribute, "AXExpandedTextValue"
        )
        self.assertEqual(
            HIServices.kAXFocusableAncestorAttribute, "AXFocusableAncestor"
        )
        self.assertEqual(HIServices.kAXGrabbedAttribute, "AXGrabbed")
        self.assertEqual(
            HIServices.kAXHasDocumentRoleAncestorAttribute, "AXHasDocumentRoleAncestor"
        )
        self.assertEqual(HIServices.kAXHasPopupAttribute, "AXHasPopup")
        self.assertEqual(
            HIServices.kAXHasWebApplicationAncestorAttribute,
            "AXHasWebApplicationAncestor",
        )
        self.assertEqual(
            HIServices.kAXHighestEditableAncestorAttribute, "AXHighestEditableAncestor"
        )
        self.assertEqual(HIServices.kAXInlineTextAttribute, "AXInlineText")
        self.assertEqual(
            HIServices.kAXIntersectionWithSelectionRangeAttribute,
            "AXIntersectionWithSelectionRange",
        )
        self.assertEqual(HIServices.kAXInvalidAttribute, "AXInvalid")
        self.assertEqual(HIServices.kAXKeyShortcutsAttribute, "AXKeyShortcutsValue")
        self.assertEqual(HIServices.kAXLinkUIElementsAttribute, "AXLinkUIElements")
        self.assertEqual(HIServices.kAXLoadedAttribute, "AXLoaded")
        self.assertEqual(HIServices.kAXLoadingProgressAttribute, "AXLoadingProgress")
        self.assertEqual(HIServices.kAXMathBaseAttribute, "AXMathBase")
        self.assertEqual(HIServices.kAXMathFencedCloseAttribute, "AXMathFencedClose")
        self.assertEqual(HIServices.kAXMathFencedOpenAttribute, "AXMathFencedOpen")
        self.assertEqual(
            HIServices.kAXMathFractionDenominatorAttribute, "AXMathFractionDenominator"
        )
        self.assertEqual(
            HIServices.kAXMathFractionNumeratorAttribute, "AXMathFractionNumerator"
        )
        self.assertEqual(
            HIServices.kAXMathLineThicknessAttribute, "AXMathLineThickness"
        )
        self.assertEqual(HIServices.kAXMathOverAttribute, "AXMathOver")
        self.assertEqual(HIServices.kAXMathPostscriptsAttribute, "AXMathPostscripts")
        self.assertEqual(HIServices.kAXMathPrescriptsAttribute, "AXMathPrescripts")
        self.assertEqual(HIServices.kAXMathRootIndexAttribute, "AXMathRootIndex")
        self.assertEqual(HIServices.kAXMathRootRadicandAttribute, "AXMathRootRadicand")
        self.assertEqual(HIServices.kAXMathSubscriptAttribute, "AXMathSubscript")
        self.assertEqual(HIServices.kAXMathSuperscriptAttribute, "AXMathSuperscript")
        self.assertEqual(HIServices.kAXMathUnderAttribute, "AXMathUnder")
        self.assertEqual(HIServices.kAXOwnsAttribute, "AXOwns")
        self.assertEqual(HIServices.kAXPopupValueAttribute, "AXPopupValue")
        self.assertEqual(
            HIServices.kAXPreventKeyboardDOMEventDispatchAttribute,
            "AXPreventKeyboardDOMEventDispatch",
        )
        self.assertEqual(
            HIServices.kAXSelectedTextMarkerRangeAttribute, "AXSelectedTextMarkerRange"
        )
        self.assertEqual(HIServices.kAXStartTextMarkerAttribute, "AXStartTextMarker")
        self.assertEqual(
            HIServices.kAXTextInputMarkedTextMarkerRangeAttribute,
            "AXTextInputMarkedTextMarkerRange",
        )
        self.assertEqual(
            HIServices.kAXValueAutofillAvailableAttribute, "AXValueAutofillAvailable"
        )
        self.assertEqual(HIServices.kAXDidSpellCheckStringAttribute, "AXDidSpellCheck")
        self.assertEqual(HIServices.kAXHighlightStringAttribute, "AXHighlight")
        self.assertEqual(
            HIServices.kAXIsSuggestedDeletionStringAttribute, "AXIsSuggestedDeletion"
        )
        self.assertEqual(
            HIServices.kAXIsSuggestedInsertionStringAttribute, "AXIsSuggestedInsertion"
        )
        self.assertEqual(HIServices.kAXIsSuggestionStringAttribute, "AXIsSuggestion")
        self.assertEqual(
            HIServices.kAXActiveElementChangedNotification, "AXActiveElementChanged"
        )
        self.assertEqual(
            HIServices.kAXCurrentStateChangedNotification, "AXCurrentStateChanged"
        )
        self.assertEqual(HIServices.kAXExpandedChangedNotification, "AXExpandedChanged")
        self.assertEqual(
            HIServices.kAXInvalidStatusChangedNotification, "AXInvalidStatusChanged"
        )
        self.assertEqual(HIServices.kAXLayoutCompleteNotification, "AXLayoutComplete")
        self.assertEqual(
            HIServices.kAXLiveRegionChangedNotification, "AXLiveRegionChanged"
        )
        self.assertEqual(
            HIServices.kAXLiveRegionCreatedNotification, "AXLiveRegionCreated"
        )
        self.assertEqual(HIServices.kAXLoadCompleteNotification, "AXLoadComplete")
        self.assertEqual(
            HIServices.kAXAttributedStringForTextMarkerRangeParameterizedAttribute,
            "AXAttributedStringForTextMarkerRange",
        )
        self.assertEqual(
            HIServices.kAXBoundsForTextMarkerRangeParameterizedAttribute,
            "AXBoundsForTextMarkerRange",
        )
        self.assertEqual(
            HIServices.kAXConvertRelativeFrameParameterizedAttribute,
            "AXConvertRelativeFrame",
        )
        self.assertEqual(
            HIServices.kAXIndexForTextMarkerParameterizedAttribute,
            "AXIndexForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXLeftLineTextMarkerRangeForTextMarkerParameterizedAttribute,
            "AXLeftLineTextMarkerRangeForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXLeftWordTextMarkerRangeForTextMarkerParameterizedAttribute,
            "AXLeftWordTextMarkerRangeForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXLengthForTextMarkerRangeParameterizedAttribute,
            "AXLengthForTextMarkerRange",
        )
        self.assertEqual(
            HIServices.kAXLineForTextMarkerParameterizedAttribute, "AXLineForTextMarker"
        )
        self.assertEqual(
            HIServices.kAXLineTextMarkerRangeForTextMarkerParameterizedAttribute,
            "AXLineTextMarkerRangeForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXNextLineEndTextMarkerForTextMarkerParameterizedAttribute,
            "AXNextLineEndTextMarkerForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXNextParagraphEndTextMarkerForTextMarkerParameterizedAttribute,
            "AXNextParagraphEndTextMarkerForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXNextSentenceEndTextMarkerForTextMarkerParameterizedAttribute,
            "AXNextSentenceEndTextMarkerForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXNextTextMarkerForTextMarkerParameterizedAttribute,
            "AXNextTextMarkerForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXNextWordEndTextMarkerForTextMarkerParameterizedAttribute,
            "AXNextWordEndTextMarkerForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXParagraphTextMarkerRangeForTextMarkerParameterizedAttribute,
            "AXParagraphTextMarkerRangeForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXPreviousLineStartTextMarkerForTextMarkerParameterizedAttribute,
            "AXPreviousLineStartTextMarkerForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXPreviousParagraphStartTextMarkerForTextMarkerParameterizedAttribute,
            "AXPreviousParagraphStartTextMarkerForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXPreviousSentenceStartTextMarkerForTextMarkerParameterizedAttribute,
            "AXPreviousSentenceStartTextMarkerForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXPreviousTextMarkerForTextMarkerParameterizedAttribute,
            "AXPreviousTextMarkerForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXPreviousWordStartTextMarkerForTextMarkerParameterizedAttribute,
            "AXPreviousWordStartTextMarkerForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXRightLineTextMarkerRangeForTextMarkerParameterizedAttribute,
            "AXRightLineTextMarkerRangeForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXRightWordTextMarkerRangeForTextMarkerParameterizedAttribute,
            "AXRightWordTextMarkerRangeForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXSentenceTextMarkerRangeForTextMarkerParameterizedAttribute,
            "AXSentenceTextMarkerRangeForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXStringForTextMarkerRangeParameterizedAttribute,
            "AXStringForTextMarkerRange",
        )
        self.assertEqual(
            HIServices.kAXStyleTextMarkerRangeForTextMarkerParameterizedAttribute,
            "AXStyleTextMarkerRangeForTextMarker",
        )
        self.assertEqual(
            HIServices.kAXTextMarkerForIndexParameterizedAttribute,
            "AXTextMarkerForIndex",
        )
        self.assertEqual(
            HIServices.kAXTextMarkerForPositionParameterizedAttribute,
            "AXTextMarkerForPosition",
        )
        self.assertEqual(
            HIServices.kAXTextMarkerIsValidParameterizedAttribute, "AXTextMarkerIsValid"
        )
        self.assertEqual(
            HIServices.kAXTextMarkerRangeForLineParameterizedAttribute,
            "AXTextMarkerRangeForLine",
        )
        self.assertEqual(
            HIServices.kAXTextMarkerRangeForUIElementParameterizedAttribute,
            "AXTextMarkerRangeForUIElement",
        )
        self.assertEqual(
            HIServices.kAXTextMarkerRangeForUnorderedTextMarkersParameterizedAttribute,
            "AXTextMarkerRangeForUnorderedTextMarkers",
        )
        self.assertEqual(
            HIServices.kAXUIElementForTextMarkerParameterizedAttribute,
            "AXUIElementForTextMarker",
        )
        self.assertEqual(HIServices.kAXImageMapRole, "AXImageMap")
        self.assertEqual(
            HIServices.kAXApplicationAlertDialogSubrole, "AXApplicationAlertDialog"
        )
        self.assertEqual(HIServices.kAXApplicationAlertSubrole, "AXApplicationAlert")
        self.assertEqual(HIServices.kAXApplicationDialogSubrole, "AXApplicationDialog")
        self.assertEqual(HIServices.kAXApplicationGroupSubrole, "AXApplicationGroup")
        self.assertEqual(HIServices.kAXApplicationLogSubrole, "AXApplicationLog")
        self.assertEqual(
            HIServices.kAXApplicationMarqueeSubrole, "AXApplicationMarquee"
        )
        self.assertEqual(HIServices.kAXApplicationStatusSubrole, "AXApplicationStatus")
        self.assertEqual(HIServices.kAXApplicationTimerSubrole, "AXApplicationTimer")
        self.assertEqual(HIServices.kAXAudioSubrole, "AXAudio")
        self.assertEqual(HIServices.kAXCodeStyleGroupSubrole, "AXCodeStyleGroup")
        self.assertEqual(HIServices.kAXDefinitionSubrole, "AXDefinition")
        self.assertEqual(HIServices.kAXDeleteStyleGroupSubrole, "AXDeleteStyleGroup")
        self.assertEqual(HIServices.kAXDetailsSubrole, "AXDetails")
        self.assertEqual(HIServices.kAXDocumentArticleSubrole, "AXDocumentArticle")
        self.assertEqual(HIServices.kAXDocumentMathSubrole, "AXDocumentMath")
        self.assertEqual(HIServices.kAXDocumentNoteSubrole, "AXDocumentNote")
        self.assertEqual(HIServices.kAXEmptyGroupSubrole, "AXEmptyGroup")
        self.assertEqual(HIServices.kAXFieldsetSubrole, "AXFieldset")
        self.assertEqual(HIServices.kAXFileUploadButtonSubrole, "AXFileUploadButton")
        self.assertEqual(HIServices.kAXInsertStyleGroupSubrole, "AXInsertStyleGroup")
        self.assertEqual(HIServices.kAXLandmarkBannerSubrole, "AXLandmarkBanner")
        self.assertEqual(
            HIServices.kAXLandmarkComplementarySubrole, "AXLandmarkComplementary"
        )
        self.assertEqual(
            HIServices.kAXLandmarkContentInfoSubrole, "AXLandmarkContentInfo"
        )
        self.assertEqual(HIServices.kAXLandmarkMainSubrole, "AXLandmarkMain")
        self.assertEqual(
            HIServices.kAXLandmarkNavigationSubrole, "AXLandmarkNavigation"
        )
        self.assertEqual(HIServices.kAXLandmarkRegionSubrole, "AXLandmarkRegion")
        self.assertEqual(HIServices.kAXLandmarkSearchSubrole, "AXLandmarkSearch")
        self.assertEqual(HIServices.kAXMathFenceOperatorSubrole, "AXMathFenceOperator")
        self.assertEqual(HIServices.kAXMathFencedSubrole, "AXMathFenced")
        self.assertEqual(HIServices.kAXMathFractionSubrole, "AXMathFraction")
        self.assertEqual(HIServices.kAXMathIdentifierSubrole, "AXMathIdentifier")
        self.assertEqual(HIServices.kAXMathMultiscriptSubrole, "AXMathMultiscript")
        self.assertEqual(HIServices.kAXMathNumberSubrole, "AXMathNumber")
        self.assertEqual(HIServices.kAXMathOperatorSubrole, "AXMathOperator")
        self.assertEqual(HIServices.kAXMathRootSubrole, "AXMathRoot")
        self.assertEqual(HIServices.kAXMathRowSubrole, "AXMathRow")
        self.assertEqual(
            HIServices.kAXMathSeparatorOperatorSubrole, "AXMathSeparatorOperator"
        )
        self.assertEqual(HIServices.kAXMathSquareRootSubrole, "AXMathSquareRoot")
        self.assertEqual(
            HIServices.kAXMathSubscriptSuperscriptSubrole, "AXMathSubscriptSuperscript"
        )
        self.assertEqual(HIServices.kAXMathTableCellSubrole, "AXMathTableCell")
        self.assertEqual(HIServices.kAXMathTableRowSubrole, "AXMathTableRow")
        self.assertEqual(HIServices.kAXMathTableSubrole, "AXMathTable")
        self.assertEqual(HIServices.kAXMathTextSubrole, "AXMathText")
        self.assertEqual(HIServices.kAXMathUnderOverSubrole, "AXMathUnderOver")
        self.assertEqual(HIServices.kAXMeterSubrole, "AXMeter")
        self.assertEqual(HIServices.kAXRubyInlineSubrole, "AXRubyInline")
        self.assertEqual(HIServices.kAXRubyTextSubrole, "AXRubyText")
        self.assertEqual(
            HIServices.kAXSubscriptStyleGroupSubrole, "AXSubscriptStyleGroup"
        )
        self.assertEqual(HIServices.kAXSummarySubrole, "AXSummary")
        self.assertEqual(
            HIServices.kAXSuperscriptStyleGroupSubrole, "AXSuperscriptStyleGroup"
        )
        self.assertEqual(HIServices.kAXTabPanelSubrole, "AXTabPanel")
        self.assertEqual(HIServices.kAXTermSubrole, "AXTerm")
        self.assertEqual(HIServices.kAXTimeGroupSubrole, "AXTimeGroup")
        self.assertEqual(
            HIServices.kAXUserInterfaceTooltipSubrole, "AXUserInterfaceTooltip"
        )
        self.assertEqual(HIServices.kAXVideoSubrole, "AXVideo")
        self.assertEqual(HIServices.kAXWebApplicationSubrole, "AXWebApplication")
