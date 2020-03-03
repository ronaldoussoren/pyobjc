import HIServices
from PyObjCTools.TestSupport import TestCase


class TestAXAttributeConstants(TestCase):
    def testConstants(self):
        self.assertEqual(HIServices.kAXRoleAttribute, "AXRole")
        self.assertEqual(HIServices.kAXSubroleAttribute, "AXSubrole")
        self.assertEqual(HIServices.kAXRoleDescriptionAttribute, "AXRoleDescription")
        self.assertEqual(HIServices.kAXHelpAttribute, "AXHelp")
        self.assertEqual(HIServices.kAXTitleAttribute, "AXTitle")
        self.assertEqual(HIServices.kAXValueAttribute, "AXValue")
        self.assertEqual(HIServices.kAXValueDescriptionAttribute, "AXValueDescription")
        self.assertEqual(HIServices.kAXMinValueAttribute, "AXMinValue")
        self.assertEqual(HIServices.kAXMaxValueAttribute, "AXMaxValue")
        self.assertEqual(HIServices.kAXValueIncrementAttribute, "AXValueIncrement")
        self.assertEqual(HIServices.kAXAllowedValuesAttribute, "AXAllowedValues")
        self.assertEqual(HIServices.kAXPlaceholderValueAttribute, "AXPlaceholderValue")
        self.assertEqual(HIServices.kAXEnabledAttribute, "AXEnabled")
        self.assertEqual(HIServices.kAXElementBusyAttribute, "AXElementBusy")
        self.assertEqual(HIServices.kAXFocusedAttribute, "AXFocused")
        self.assertEqual(HIServices.kAXParentAttribute, "AXParent")
        self.assertEqual(HIServices.kAXChildrenAttribute, "AXChildren")
        self.assertEqual(HIServices.kAXSelectedChildrenAttribute, "AXSelectedChildren")
        self.assertEqual(HIServices.kAXVisibleChildrenAttribute, "AXVisibleChildren")
        self.assertEqual(HIServices.kAXWindowAttribute, "AXWindow")
        self.assertEqual(
            HIServices.kAXTopLevelUIElementAttribute, "AXTopLevelUIElement"
        )
        self.assertEqual(HIServices.kAXPositionAttribute, "AXPosition")
        self.assertEqual(HIServices.kAXSizeAttribute, "AXSize")
        self.assertEqual(HIServices.kAXOrientationAttribute, "AXOrientation")
        self.assertEqual(HIServices.kAXDescriptionAttribute, "AXDescription")
        self.assertEqual(HIServices.kAXDescription, "AXDescription")
        self.assertEqual(HIServices.kAXSelectedTextAttribute, "AXSelectedText")
        self.assertEqual(
            HIServices.kAXSelectedTextRangeAttribute, "AXSelectedTextRange"
        )
        self.assertEqual(
            HIServices.kAXSelectedTextRangesAttribute, "AXSelectedTextRanges"
        )
        self.assertEqual(
            HIServices.kAXVisibleCharacterRangeAttribute, "AXVisibleCharacterRange"
        )
        self.assertEqual(
            HIServices.kAXNumberOfCharactersAttribute, "AXNumberOfCharacters"
        )
        self.assertEqual(
            HIServices.kAXSharedTextUIElementsAttribute, "AXSharedTextUIElements"
        )
        self.assertEqual(
            HIServices.kAXSharedCharacterRangeAttribute, "AXSharedCharacterRange"
        )
        self.assertEqual(
            HIServices.kAXSharedFocusElementsAttribute, "AXSharedFocusElements"
        )
        self.assertEqual(
            HIServices.kAXInsertionPointLineNumberAttribute,
            "AXInsertionPointLineNumber",
        )
        self.assertEqual(HIServices.kAXMainAttribute, "AXMain")
        self.assertEqual(HIServices.kAXMinimizedAttribute, "AXMinimized")
        self.assertEqual(HIServices.kAXCloseButtonAttribute, "AXCloseButton")
        self.assertEqual(HIServices.kAXZoomButtonAttribute, "AXZoomButton")
        self.assertEqual(HIServices.kAXMinimizeButtonAttribute, "AXMinimizeButton")
        self.assertEqual(HIServices.kAXToolbarButtonAttribute, "AXToolbarButton")
        self.assertEqual(HIServices.kAXFullScreenButtonAttribute, "AXFullScreenButton")
        self.assertEqual(HIServices.kAXProxyAttribute, "AXProxy")
        self.assertEqual(HIServices.kAXGrowAreaAttribute, "AXGrowArea")
        self.assertEqual(HIServices.kAXModalAttribute, "AXModal")
        self.assertEqual(HIServices.kAXDefaultButtonAttribute, "AXDefaultButton")
        self.assertEqual(HIServices.kAXCancelButtonAttribute, "AXCancelButton")
        self.assertEqual(HIServices.kAXMenuItemCmdCharAttribute, "AXMenuItemCmdChar")
        self.assertEqual(
            HIServices.kAXMenuItemCmdVirtualKeyAttribute, "AXMenuItemCmdVirtualKey"
        )
        self.assertEqual(HIServices.kAXMenuItemCmdGlyphAttribute, "AXMenuItemCmdGlyph")
        self.assertEqual(
            HIServices.kAXMenuItemCmdModifiersAttribute, "AXMenuItemCmdModifiers"
        )
        self.assertEqual(HIServices.kAXMenuItemMarkCharAttribute, "AXMenuItemMarkChar")
        self.assertEqual(
            HIServices.kAXMenuItemPrimaryUIElementAttribute,
            "AXMenuItemPrimaryUIElement",
        )
        self.assertEqual(HIServices.kAXMenuBarAttribute, "AXMenuBar")
        self.assertEqual(HIServices.kAXWindowsAttribute, "AXWindows")
        self.assertEqual(HIServices.kAXFrontmostAttribute, "AXFrontmost")
        self.assertEqual(HIServices.kAXHiddenAttribute, "AXHidden")
        self.assertEqual(HIServices.kAXMainWindowAttribute, "AXMainWindow")
        self.assertEqual(HIServices.kAXFocusedWindowAttribute, "AXFocusedWindow")
        self.assertEqual(HIServices.kAXFocusedUIElementAttribute, "AXFocusedUIElement")
        self.assertEqual(HIServices.kAXExtrasMenuBarAttribute, "AXExtrasMenuBar")
        self.assertEqual(HIServices.kAXHeaderAttribute, "AXHeader")
        self.assertEqual(HIServices.kAXEditedAttribute, "AXEdited")
        self.assertEqual(HIServices.kAXValueWrapsAttribute, "AXValueWraps")
        self.assertEqual(HIServices.kAXTabsAttribute, "AXTabs")
        self.assertEqual(HIServices.kAXTitleUIElementAttribute, "AXTitleUIElement")
        self.assertEqual(
            HIServices.kAXHorizontalScrollBarAttribute, "AXHorizontalScrollBar"
        )
        self.assertEqual(
            HIServices.kAXVerticalScrollBarAttribute, "AXVerticalScrollBar"
        )
        self.assertEqual(HIServices.kAXOverflowButtonAttribute, "AXOverflowButton")
        self.assertEqual(HIServices.kAXFilenameAttribute, "AXFilename")
        self.assertEqual(HIServices.kAXExpandedAttribute, "AXExpanded")
        self.assertEqual(HIServices.kAXSelectedAttribute, "AXSelected")
        self.assertEqual(HIServices.kAXSplittersAttribute, "AXSplitters")
        self.assertEqual(HIServices.kAXNextContentsAttribute, "AXNextContents")
        self.assertEqual(HIServices.kAXDocumentAttribute, "AXDocument")
        self.assertEqual(HIServices.kAXDecrementButtonAttribute, "AXDecrementButton")
        self.assertEqual(HIServices.kAXIncrementButtonAttribute, "AXIncrementButton")
        self.assertEqual(HIServices.kAXPreviousContentsAttribute, "AXPreviousContents")
        self.assertEqual(HIServices.kAXContentsAttribute, "AXContents")
        self.assertEqual(HIServices.kAXIncrementorAttribute, "AXIncrementor")
        self.assertEqual(HIServices.kAXHourFieldAttribute, "AXHourField")
        self.assertEqual(HIServices.kAXMinuteFieldAttribute, "AXMinuteField")
        self.assertEqual(HIServices.kAXSecondFieldAttribute, "AXSecondField")
        self.assertEqual(HIServices.kAXAMPMFieldAttribute, "AXAMPMField")
        self.assertEqual(HIServices.kAXDayFieldAttribute, "AXDayField")
        self.assertEqual(HIServices.kAXMonthFieldAttribute, "AXMonthField")
        self.assertEqual(HIServices.kAXYearFieldAttribute, "AXYearField")
        self.assertEqual(HIServices.kAXColumnTitleAttribute, "AXColumnTitles")
        self.assertEqual(HIServices.kAXURLAttribute, "AXURL")
        self.assertEqual(HIServices.kAXLabelUIElementsAttribute, "AXLabelUIElements")
        self.assertEqual(HIServices.kAXLabelValueAttribute, "AXLabelValue")
        self.assertEqual(
            HIServices.kAXShownMenuUIElementAttribute, "AXShownMenuUIElement"
        )
        self.assertEqual(
            HIServices.kAXServesAsTitleForUIElementsAttribute,
            "AXServesAsTitleForUIElements",
        )
        self.assertEqual(HIServices.kAXLinkedUIElementsAttribute, "AXLinkedUIElements")
        self.assertEqual(HIServices.kAXRowsAttribute, "AXRows")
        self.assertEqual(HIServices.kAXVisibleRowsAttribute, "AXVisibleRows")
        self.assertEqual(HIServices.kAXSelectedRowsAttribute, "AXSelectedRows")
        self.assertEqual(HIServices.kAXColumnsAttribute, "AXColumns")
        self.assertEqual(HIServices.kAXVisibleColumnsAttribute, "AXVisibleColumns")
        self.assertEqual(HIServices.kAXSelectedColumnsAttribute, "AXSelectedColumns")
        self.assertEqual(HIServices.kAXSortDirectionAttribute, "AXSortDirection")
        self.assertEqual(HIServices.kAXIndexAttribute, "AXIndex")
        self.assertEqual(HIServices.kAXDisclosingAttribute, "AXDisclosing")
        self.assertEqual(HIServices.kAXDisclosedRowsAttribute, "AXDisclosedRows")
        self.assertEqual(HIServices.kAXDisclosedByRowAttribute, "AXDisclosedByRow")
        self.assertEqual(HIServices.kAXDisclosureLevelAttribute, "AXDisclosureLevel")
        self.assertEqual(HIServices.kAXMatteHoleAttribute, "AXMatteHole")
        self.assertEqual(
            HIServices.kAXMatteContentUIElementAttribute, "AXMatteContentUIElement"
        )
        self.assertEqual(HIServices.kAXMarkerUIElementsAttribute, "AXMarkerUIElements")
        self.assertEqual(HIServices.kAXUnitsAttribute, "AXUnits")
        self.assertEqual(HIServices.kAXUnitDescriptionAttribute, "AXUnitDescription")
        self.assertEqual(HIServices.kAXMarkerTypeAttribute, "AXMarkerType")
        self.assertEqual(
            HIServices.kAXMarkerTypeDescriptionAttribute, "AXMarkerTypeDescription"
        )
        self.assertEqual(
            HIServices.kAXIsApplicationRunningAttribute, "AXIsApplicationRunning"
        )
        self.assertEqual(HIServices.kAXSearchButtonAttribute, "AXSearchButton")
        self.assertEqual(HIServices.kAXClearButtonAttribute, "AXClearButton")
        self.assertEqual(
            HIServices.kAXFocusedApplicationAttribute, "AXFocusedApplication"
        )
        self.assertEqual(HIServices.kAXRowCountAttribute, "AXRowCount")
        self.assertEqual(HIServices.kAXColumnCountAttribute, "AXColumnCount")
        self.assertEqual(HIServices.kAXOrderedByRowAttribute, "AXOrderedByRow")
        self.assertEqual(HIServices.kAXWarningValueAttribute, "AXWarningValue")
        self.assertEqual(HIServices.kAXCriticalValueAttribute, "AXCriticalValue")
        self.assertEqual(HIServices.kAXSelectedCellsAttribute, "AXSelectedCells")
        self.assertEqual(HIServices.kAXVisibleCellsAttribute, "AXVisibleCells")
        self.assertEqual(
            HIServices.kAXRowHeaderUIElementsAttribute, "AXRowHeaderUIElements"
        )
        self.assertEqual(
            HIServices.kAXColumnHeaderUIElementsAttribute, "AXColumnHeaderUIElements"
        )
        self.assertEqual(HIServices.kAXRowIndexRangeAttribute, "AXRowIndexRange")
        self.assertEqual(HIServices.kAXColumnIndexRangeAttribute, "AXColumnIndexRange")
        self.assertEqual(HIServices.kAXHorizontalUnitsAttribute, "AXHorizontalUnits")
        self.assertEqual(HIServices.kAXVerticalUnitsAttribute, "AXVerticalUnits")
        self.assertEqual(
            HIServices.kAXHorizontalUnitDescriptionAttribute,
            "AXHorizontalUnitDescription",
        )
        self.assertEqual(
            HIServices.kAXVerticalUnitDescriptionAttribute, "AXVerticalUnitDescription"
        )
        self.assertEqual(HIServices.kAXHandlesAttribute, "AXHandles")
        self.assertEqual(HIServices.kAXTextAttribute, "AXText")
        self.assertEqual(HIServices.kAXVisibleTextAttribute, "AXVisibleText")
        self.assertEqual(HIServices.kAXIsEditableAttribute, "AXIsEditable")
        self.assertEqual(HIServices.kAXColumnTitlesAttribute, "AXColumnTitles")
        self.assertEqual(HIServices.kAXIdentifierAttribute, "AXIdentifier")
        self.assertEqual(
            HIServices.kAXAlternateUIVisibleAttribute, "AXAlternateUIVisible"
        )
        self.assertEqual(
            HIServices.kAXLineForIndexParameterizedAttribute, "AXLineForIndex"
        )
        self.assertEqual(
            HIServices.kAXRangeForLineParameterizedAttribute, "AXRangeForLine"
        )
        self.assertEqual(
            HIServices.kAXStringForRangeParameterizedAttribute, "AXStringForRange"
        )
        self.assertEqual(
            HIServices.kAXRangeForPositionParameterizedAttribute, "AXRangeForPosition"
        )
        self.assertEqual(
            HIServices.kAXRangeForIndexParameterizedAttribute, "AXRangeForIndex"
        )
        self.assertEqual(
            HIServices.kAXBoundsForRangeParameterizedAttribute, "AXBoundsForRange"
        )
        self.assertEqual(
            HIServices.kAXRTFForRangeParameterizedAttribute, "AXRTFForRange"
        )
        self.assertEqual(
            HIServices.kAXAttributedStringForRangeParameterizedAttribute,
            "AXAttributedStringForRange",
        )
        self.assertEqual(
            HIServices.kAXStyleRangeForIndexParameterizedAttribute,
            "AXStyleRangeForIndex",
        )
        self.assertEqual(
            HIServices.kAXCellForColumnAndRowParameterizedAttribute,
            "AXCellForColumnAndRow",
        )
        self.assertEqual(
            HIServices.kAXLayoutPointForScreenPointParameterizedAttribute,
            "AXLayoutPointForScreenPoint",
        )
        self.assertEqual(
            HIServices.kAXLayoutSizeForScreenSizeParameterizedAttribute,
            "AXLayoutSizeForScreenSize",
        )
        self.assertEqual(
            HIServices.kAXScreenPointForLayoutPointParameterizedAttribute,
            "AXScreenPointForLayoutPoint",
        )
        self.assertEqual(
            HIServices.kAXScreenSizeForLayoutSizeParameterizedAttribute,
            "AXScreenSizeForLayoutSize",
        )
