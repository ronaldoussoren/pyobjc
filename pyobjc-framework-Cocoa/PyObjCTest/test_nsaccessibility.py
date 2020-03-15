import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSAccessibilityHelper(AppKit.NSObject):
    def accessibilityIsAttributeSettable_(self, arg):
        return 1

    def accessibilityIsIgnored(self):
        return 1

    def accessibilityHitTest_(self, pt):
        pass

    def accessibilitySetOverrideValue_forAttribute_(self, v, a):
        return 1

    def accessibilityNotifiesWhenDestroyed(self):
        pass

    def accessibilityIndexOfChild_(self, c):
        return 1

    def accessibilityArrayAttributeCount_(self, c):
        return 1

    def accessibilityArrayAttributeValues_index_maxCount_(self, v, i, c):
        return None


class TestNSAccessibility(TestCase):
    def testInformal(self):
        self.assertResultIsBOOL(
            TestNSAccessibilityHelper.accessibilityIsAttributeSettable_
        )
        self.assertResultIsBOOL(TestNSAccessibilityHelper.accessibilityIsIgnored)
        self.assertArgHasType(
            TestNSAccessibilityHelper.accessibilityHitTest_,
            0,
            AppKit.NSPoint.__typestr__,
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityHelper.accessibilitySetOverrideValue_forAttribute_
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityHelper.accessibilityNotifiesWhenDestroyed
        )
        self.assertResultHasType(
            TestNSAccessibilityHelper.accessibilityIndexOfChild_, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestNSAccessibilityHelper.accessibilityArrayAttributeCount_,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityHelper.accessibilityArrayAttributeCount_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityHelper.accessibilityArrayAttributeValues_index_maxCount_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityHelper.accessibilityArrayAttributeValues_index_maxCount_,
            2,
            objc._C_NSUInteger,
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.accessibilityDisplayShouldIncreaseContrast
        )
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.accessibilityDisplayShouldDifferentiateWithoutColor
        )
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.accessibilityDisplayShouldReduceTransparency
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.accessibilityDisplayShouldReduceMotion
        )
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.accessibilityDisplayShouldInvertColors
        )

    @min_os_level("10.10")
    def testFunctions10_10(self):
        AppKit.NSAccessibilityFrameInView  # Existence
        AppKit.NSAccessibilityPointInView  # Existence

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            AppKit.NSWorkspaceAccessibilityDisplayOptionsDidChangeNotification, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityActivationPointAttribute, str)

        self.assertIsInstance(AppKit.NSAccessibilitySharedFocusElementsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityAlternateUIVisibleAttribute, str)

        self.assertEqual(AppKit.NSAccessibilityOrientationUnknown, 0)
        self.assertEqual(AppKit.NSAccessibilityOrientationVertical, 1)
        self.assertEqual(AppKit.NSAccessibilityOrientationHorizontal, 2)

        self.assertEqual(AppKit.NSAccessibilitySortDirectionUnknown, 0)
        self.assertEqual(AppKit.NSAccessibilitySortDirectionAscending, 1)
        self.assertEqual(AppKit.NSAccessibilitySortDirectionDescending, 2)

        self.assertEqual(AppKit.NSAccessibilityRulerMarkerTypeUnknown, 0)
        self.assertEqual(AppKit.NSAccessibilityRulerMarkerTypeTabStopLeft, 1)
        self.assertEqual(AppKit.NSAccessibilityRulerMarkerTypeTabStopRight, 2)
        self.assertEqual(AppKit.NSAccessibilityRulerMarkerTypeTabStopCenter, 3)
        self.assertEqual(AppKit.NSAccessibilityRulerMarkerTypeTabStopDecimal, 4)
        self.assertEqual(AppKit.NSAccessibilityRulerMarkerTypeIndentHead, 5)
        self.assertEqual(AppKit.NSAccessibilityRulerMarkerTypeIndentTail, 6)
        self.assertEqual(AppKit.NSAccessibilityRulerMarkerTypeIndentFirstLine, 7)

        self.assertEqual(AppKit.NSAccessibilityUnitsUnknown, 0)
        self.assertEqual(AppKit.NSAccessibilityUnitsInches, 1)
        self.assertEqual(AppKit.NSAccessibilityUnitsCentimeters, 2)
        self.assertEqual(AppKit.NSAccessibilityUnitsPoints, 3)
        self.assertEqual(AppKit.NSAccessibilityUnitsPicas, 4)

    def testFunction(self):
        v = AppKit.NSAccessibilityRoleDescription(
            AppKit.NSAccessibilityButtonRole, None
        )
        self.assertIsInstance(v, str)

        b = AppKit.NSButton.alloc().init()
        v = AppKit.NSAccessibilityRoleDescriptionForUIElement(b)
        self.assertIsInstance(v, str)

        v = AppKit.NSAccessibilityActionDescription(
            AppKit.NSAccessibilityIncrementAction
        )
        self.assertIsInstance(v, str)

        self.assertRaises(
            objc.error,
            AppKit.NSAccessibilityRaiseBadArgumentException,
            b,
            "attribute",
            "value",
        )

        v = AppKit.NSAccessibilityUnignoredAncestor(b)
        self.assertIs(v, None)
        v = AppKit.NSAccessibilityUnignoredDescendant(b)
        self.assertIsInstance(b, AppKit.NSView)

        v = AppKit.NSAccessibilityUnignoredChildren([b])
        self.assertIsInstance(v, AppKit.NSArray)

        v = AppKit.NSAccessibilityUnignoredChildrenForOnlyChild(b)
        self.assertIsInstance(v, AppKit.NSArray)

        v = AppKit.NSAccessibilityPostNotification(b, "hello")
        self.assertIs(v, None)

    def testConstants(self):
        self.assertEqual(AppKit.NSAccessibilityAnnotationPositionFullRange, 0)
        self.assertEqual(AppKit.NSAccessibilityAnnotationPositionStart, 1)
        self.assertEqual(AppKit.NSAccessibilityAnnotationPositionEnd, 2)

        self.assertIsInstance(AppKit.NSAccessibilityErrorCodeExceptionInfo, str)
        self.assertIsInstance(AppKit.NSAccessibilityRoleAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityRoleDescriptionAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySubroleAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityHelpAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityValueAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMinValueAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMaxValueAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityEnabledAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityFocusedAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityParentAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityChildrenAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityWindowAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityTopLevelUIElementAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySelectedChildrenAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityVisibleChildrenAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityPositionAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySizeAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityContentsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityTitleAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityDescriptionAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityShownMenuAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityValueDescriptionAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityPreviousContentsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityNextContentsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityHeaderAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityEditedAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityTabsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityHorizontalScrollBarAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityVerticalScrollBarAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityOverflowButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityIncrementButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityDecrementButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityFilenameAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityExpandedAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySelectedAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySplittersAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityDocumentAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityURLAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityIndexAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityRowCountAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityColumnCountAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityOrderedByRowAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityTitleUIElementAttribute, str)
        self.assertIsInstance(
            AppKit.NSAccessibilityServesAsTitleForUIElementsAttribute, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityLinkedUIElementsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySelectedTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySelectedTextRangeAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityNumberOfCharactersAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityVisibleCharacterRangeAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySharedTextUIElementsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySharedCharacterRangeAttribute, str)
        self.assertIsInstance(
            AppKit.NSAccessibilityInsertionPointLineNumberAttribute, str
        )
        self.assertIsInstance(AppKit.NSAccessibilitySelectedTextRangesAttribute, str)
        self.assertIsInstance(
            AppKit.NSAccessibilityLineForIndexParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityRangeForLineParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityStringForRangeParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityRangeForPositionParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityRangeForIndexParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityBoundsForRangeParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityRTFForRangeParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityStyleRangeForIndexParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityAttributedStringForRangeParameterizedAttribute, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityFontTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityForegroundColorTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityBackgroundColorTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityUnderlineColorTextAttribute, str)
        self.assertIsInstance(
            AppKit.NSAccessibilityStrikethroughColorTextAttribute, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityUnderlineTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySuperscriptTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityStrikethroughTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityShadowTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityAttachmentTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityLinkTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMisspelledTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMarkedMisspelledTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityFontNameKey, str)
        self.assertIsInstance(AppKit.NSAccessibilityFontFamilyKey, str)
        self.assertIsInstance(AppKit.NSAccessibilityVisibleNameKey, str)
        self.assertIsInstance(AppKit.NSAccessibilityFontSizeKey, str)
        self.assertIsInstance(AppKit.NSAccessibilityMainAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMinimizedAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityCloseButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityZoomButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMinimizeButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityToolbarButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityProxyAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityGrowAreaAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityModalAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityDefaultButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityCancelButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMenuBarAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityWindowsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityFrontmostAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityHiddenAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMainWindowAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityFocusedWindowAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityFocusedUIElementAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityOrientationAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityVerticalOrientationValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityHorizontalOrientationValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityColumnTitlesAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySearchButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySearchMenuAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityClearButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityRowsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityVisibleRowsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySelectedRowsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityColumnsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityVisibleColumnsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySelectedColumnsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySortDirectionAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityAscendingSortDirectionValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityDescendingSortDirectionValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityUnknownSortDirectionValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityDisclosingAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityDisclosedRowsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityDisclosedByRowAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityDisclosureLevelAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityAllowedValuesAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityLabelUIElementsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityLabelValueAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMatteHoleAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMatteContentUIElementAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMarkerUIElementsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMarkerValuesAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMarkerGroupUIElementAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityUnitsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityUnitDescriptionAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMarkerTypeAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMarkerTypeDescriptionAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityLeftTabStopMarkerTypeValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityRightTabStopMarkerTypeValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityCenterTabStopMarkerTypeValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityDecimalTabStopMarkerTypeValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityHeadIndentMarkerTypeValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityTailIndentMarkerTypeValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityFirstLineIndentMarkerTypeValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityUnknownMarkerTypeValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityInchesUnitValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityCentimetersUnitValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityPointsUnitValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityPicasUnitValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityUnknownUnitValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityPressAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityIncrementAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityDecrementAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityConfirmAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityPickAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityCancelAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityRaiseAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityShowMenuAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityDeleteAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityMainWindowChangedNotification, str)
        self.assertIsInstance(
            AppKit.NSAccessibilityFocusedWindowChangedNotification, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityFocusedUIElementChangedNotification, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityApplicationActivatedNotification, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityApplicationDeactivatedNotification, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityApplicationHiddenNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityApplicationShownNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityWindowCreatedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityWindowMovedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityWindowResizedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityWindowMiniaturizedNotification, str)
        self.assertIsInstance(
            AppKit.NSAccessibilityWindowDeminiaturizedNotification, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityDrawerCreatedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilitySheetCreatedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityUIElementDestroyedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityValueChangedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityTitleChangedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityResizedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityMovedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityCreatedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityHelpTagCreatedNotification, str)
        self.assertIsInstance(
            AppKit.NSAccessibilitySelectedTextChangedNotification, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityRowCountChangedNotification, str)
        self.assertIsInstance(
            AppKit.NSAccessibilitySelectedChildrenChangedNotification, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilitySelectedRowsChangedNotification, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilitySelectedColumnsChangedNotification, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityUnknownRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityButtonRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityRadioButtonRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityCheckBoxRole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySliderRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityTabGroupRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityTextFieldRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityStaticTextRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityTextAreaRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityScrollAreaRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityPopUpButtonRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityMenuButtonRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityTableRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityApplicationRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityGroupRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityRadioGroupRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityListRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityScrollBarRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityValueIndicatorRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityImageRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityMenuBarRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityMenuRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityMenuItemRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityColumnRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityRowRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityToolbarRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityBusyIndicatorRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityProgressIndicatorRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityWindowRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityDrawerRole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySystemWideRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityOutlineRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityIncrementorRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityBrowserRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityComboBoxRole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySplitGroupRole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySplitterRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityColorWellRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityGrowAreaRole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySheetRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityHelpTagRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityMatteRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityRulerRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityRulerMarkerRole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySortButtonRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityLinkRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityDisclosureTriangleRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityGridRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityUnknownSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityCloseButtonSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityZoomButtonSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityMinimizeButtonSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityToolbarButtonSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityTableRowSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityOutlineRowSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySecureTextFieldSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityStandardWindowSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityDialogSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySystemDialogSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityFloatingWindowSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySystemFloatingWindowSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityIncrementArrowSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityDecrementArrowSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityIncrementPageSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityDecrementPageSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySearchFieldSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityTextAttachmentSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityTextLinkSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityTimelineSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityRelevanceIndicatorRole, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(AppKit.NSAccessibilityUnknownOrientationValue, str)
        self.assertIsInstance(AppKit.NSAccessibilityWarningValueAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityCriticalValueAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityPlaceholderValueAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilitySelectedCellsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityVisibleCellsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityRowHeaderUIElementsAttribute, str)
        self.assertIsInstance(
            AppKit.NSAccessibilityColumnHeaderUIElementsAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityCellForColumnAndRowParameterizedAttribute, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityRowIndexRangeAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityColumnIndexRangeAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityHorizontalUnitsAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityVerticalUnitsAttribute, str)
        self.assertIsInstance(
            AppKit.NSAccessibilityHorizontalUnitDescriptionAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityVerticalUnitDescriptionAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityLayoutPointForScreenPointParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityLayoutSizeForScreenSizeParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityScreenPointForLayoutPointParameterizedAttribute, str
        )
        self.assertIsInstance(
            AppKit.NSAccessibilityScreenSizeForLayoutSizeParameterizedAttribute, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityHandlesAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityRowExpandedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityRowCollapsedNotification, str)
        self.assertIsInstance(
            AppKit.NSAccessibilitySelectedCellsChangedNotification, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityUnitsChangedNotification, str)
        self.assertIsInstance(
            AppKit.NSAccessibilitySelectedChildrenMovedNotification, str
        )
        self.assertIsInstance(AppKit.NSAccessibilitySortButtonRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityLevelIndicatorRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityCellRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityLayoutAreaRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityLayoutItemRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityHandleRole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySortButtonSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityRatingIndicatorSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityContentListSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityDefinitionListSubrole, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AppKit.NSAccessibilityAutocorrectedTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityFullScreenButtonAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityPopoverRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityFullScreenButtonSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityIdentifierAttribute, str)
        self.assertIsInstance(
            AppKit.NSAccessibilityAnnouncementRequestedNotification, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityAnnouncementKey, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(AppKit.NSAccessibilityExtrasMenuBarAttribute, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(
            AppKit.NSAccessibilityContainsProtectedContentAttribute, str
        )
        self.assertIsInstance(AppKit.NSAccessibilityShowAlternateUIAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityShowDefaultUIAction, str)
        self.assertIsInstance(AppKit.NSAccessibilityLayoutChangedNotification, str)
        self.assertIsInstance(AppKit.NSAccessibilityToggleSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySwitchSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityDescriptionListSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityUIElementsKey, str)
        self.assertIsInstance(AppKit.NSAccessibilityPriorityKey, str)

        self.assertEqual(AppKit.NSAccessibilityPriorityLow, 10)
        self.assertEqual(AppKit.NSAccessibilityPriorityMedium, 50)
        self.assertEqual(AppKit.NSAccessibilityPriorityHigh, 90)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(AppKit.NSAccessibilityListItemPrefixTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityListItemIndexTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityListItemLevelTextAttribute, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AppKit.NSAccessibilityRequiredAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityMenuBarItemRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityTextAlignmentAttribute, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AppKit.NSAccessibilityAnnotationLabel, str)
        self.assertIsInstance(AppKit.NSAccessibilityAnnotationElement, str)
        self.assertIsInstance(AppKit.NSAccessibilityAnnotationLocation, str)

        self.assertIsInstance(AppKit.NSAccessibilityLanguageTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityCustomTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityAnnotationTextAttribute, str)
        self.assertIsInstance(AppKit.NSAccessibilityPageRole, str)
        self.assertIsInstance(AppKit.NSAccessibilityTabButtonSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilityCollectionListSubrole, str)
        self.assertIsInstance(AppKit.NSAccessibilitySectionListSubrole, str)

    @min_os_level("10.7")
    def testFunctions10_7(self):
        self.assertIsInstance(
            AppKit.NSAccessibilityPostNotificationWithUserInfo, objc.function
        )

    @min_os_level("10.9")
    def testFunctions10_9(self):
        self.assertArgIsBOOL(AppKit.NSAccessibilitySetMayContainProtectedContent, 0)
        self.assertResultIsBOOL(AppKit.NSAccessibilitySetMayContainProtectedContent)
