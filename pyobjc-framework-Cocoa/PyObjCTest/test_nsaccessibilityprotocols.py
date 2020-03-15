import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSAccessibilityProtocolsHelper(AppKit.NSObject):
    def accessibilityOrientation(self):
        return 1

    def setAccessibilityOrientation_(self, v):
        pass

    def accessibilityActivationPoint(self):
        return 1

    def accessibilityAttributedStringForRange_(self, v):
        return 1

    def accessibilityCellForColumn_row_(self, c, r):
        return 1

    def accessibilityColumnCount(self):
        return 1

    def accessibilityColumnIndexRange(self):
        return 1

    def accessibilityDisclosureLevel(self):
        return 1

    def accessibilityFrame(self):
        return 1

    def accessibilityFrameForRange_(self, v):
        return 1

    def accessibilityHorizontalUnits(self):
        return 1

    def accessibilityIndex(self):
        return 1

    def accessibilityInsertionPointLineNumber(self):
        return 1

    def accessibilityLabelValue(self):
        return 1

    def accessibilityLayoutPointForScreenPoint_(self, v):
        return 1

    def accessibilityLayoutSizeForScreenSize_(self, v):
        return 1

    def accessibilityLineForIndex_(self, v):
        return 1

    def accessibilityNumberOfCharacters(self):
        return 1

    def accessibilityPerformCancel(self):
        return 1

    def accessibilityPerformConfirm(self):
        return 1

    def accessibilityPerformDecrement(self):
        return 1

    def accessibilityPerformDelete(self):
        return 1

    def accessibilityPerformIncrement(self):
        return 1

    def accessibilityPerformPick(self):
        return 1

    def accessibilityPerformPress(self):
        return 1

    def accessibilityPerformRaise(self):
        return 1

    def accessibilityPerformShowAlternateUI(self):
        return 1

    def accessibilityPerformShowDefaultUI(self):
        return 1

    def accessibilityPerformShowMenu(self):
        return 1

    def accessibilityRTFForRange_(self, v):
        return 1

    def accessibilityRangeForIndex_(self, v):
        return 1

    def accessibilityRangeForLine_(self, v):
        return 1

    def accessibilityRangeForPosition_(self, v):
        return 1

    def accessibilityRowCount(self):
        return 1

    def accessibilityRowIndexRange(self):
        return 1

    def accessibilityRulerMarkerType(self):
        return 1

    def accessibilityScreenPointForLayoutPoint_(self, v):
        return 1

    def accessibilityScreenSizeForLayoutSize_(self, v):
        return 1

    def accessibilitySelectedTextRange(self):
        return 1

    def accessibilitySharedCharacterRange(self):
        return 1

    def accessibilitySortDirection(self):
        return 1

    def accessibilityStringForRange_(self, v):
        return 1

    def accessibilityStyleRangeForIndex_(self, v):
        return 1

    def accessibilityUnits(self):
        return 1

    def accessibilityVerticalUnits(self):
        return 1

    def accessibilityVisibleCharacterRange(self):
        return 1

    def isAccessibilityAlternateUIVisible(self):
        return 1

    def isAccessibilityDisclosed(self):
        return 1

    def setAccessibilityDisclosed_(self, v):
        pass

    def isAccessibilityEdited(self):
        return 1

    def isAccessibilityElement(self):
        return 1

    def isAccessibilityEnabled(self):
        return 1

    def isAccessibilityExpanded(self):
        return 1

    def isAccessibilityFocused(self):
        return 1

    def isAccessibilityFrontmost(self):
        return 1

    def isAccessibilityHidden(self):
        return 1

    def isAccessibilityMain(self):
        return 1

    def isAccessibilityMinimized(self):
        return 1

    def isAccessibilityModal(self):
        return 1

    def isAccessibilityOrderedByRow(self):
        return 1

    def isAccessibilityProtectedContent(self):
        return 1

    def isAccessibilitySelected(self):
        return 1

    def isAccessibilitySelectorAllowed_(self, sel):
        return 1

    def setAccessibilityActivationPoint_(self, p):
        pass

    def setAccessibilityAlternateUIVisible_(self, v):
        pass

    def setAccessibilityColumnCount_(self, v):
        pass

    def setAccessibilityColumnIndexRange_(self, v):
        pass

    def setAccessibilityDisclosureLevel_(self, v):
        pass

    def setAccessibilityEdited_(self, v):
        pass

    def setAccessibilityElement_(self, v):
        pass

    def setAccessibilityEnabled_(self, v):
        pass

    def setAccessibilityExpanded_(self, v):
        pass

    def setAccessibilityFocused_(self, v):
        pass

    def setAccessibilityFrame_(self, f):
        pass

    def setAccessibilityFrontmost_(self, v):
        pass

    def setAccessibilityHidden_(self, v):
        pass

    def setAccessibilityHorizontalUnits_(self, v):
        pass

    def setAccessibilityIndex_(self, v):
        pass

    def setAccessibilityInsertionPointLineNumber_(self, v):
        pass

    def setAccessibilityLabelValue_(self, v):
        pass

    def setAccessibilityMain_(self, v):
        return 1

    def setAccessibilityMinimized_(self, v):
        return 1

    def setAccessibilityModal_(self, v):
        return 1

    def setAccessibilityNumberOfCharacters_(self, v):
        pass

    def setAccessibilityOrderedByRow_(self, v):
        pass

    def setAccessibilityProtectedContent_(self, v):
        pass

    def setAccessibilityRowCount_(self, v):
        pass

    def setAccessibilityRowIndexRange_(self, v):
        pass

    def setAccessibilityRulerMarkerType_(self, v):
        pass

    def setAccessibilitySelectedTextRange_(self, v):
        pass

    def setAccessibilitySelected_(self, v):
        pass

    def setAccessibilitySharedCharacterRange_(self, v):
        pass

    def setAccessibilitySortDirection_(self, v):
        pass

    def setAccessibilityUnits_(self, v):
        pass

    def setAccessibilityVerticalUnits_(self, v):
        pass

    def setAccessibilityVisibleCharacterRange_(self, v):
        pass

    def isAccessibilityRequired(self):
        return 1


class TestNSAccessibilityProtocols(TestCase):
    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityGroup"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityElement"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityButton"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilitySwitch"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityRadioButton"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityCheckBox"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityStaticText"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityNavigableStaticText"),
            objc.formal_protocol,
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityProgressIndicator"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityStepper"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilitySlider"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityImage"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityContainsTransientUI"),
            objc.formal_protocol,
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityTable"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityOutline"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityList"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityRow"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityLayoutArea"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityLayoutItem"), objc.formal_protocol
        )
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibility"), objc.formal_protocol
        )

    @min_sdk_level("10.13")
    def testProtocolObjects10_13(self):
        self.assertIsInstance(
            objc.protocolNamed("NSAccessibilityElementLoading"), objc.formal_protocol
        )

    def testProtocols(self):
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityFocused
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityFrame,
            AppKit.NSRect.__typestr__,
        )

        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformPress
        )

        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformIncrement
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformDecrement
        )

        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityVisibleCharacterRange,
            AppKit.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityFrameForRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityFrameForRange_,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityStringForRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityLineForIndex_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityLineForIndex_,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRangeForLine_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRangeForLine_,
            AppKit.NSRange.__typestr__,
        )

        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformIncrement
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformDecrement
        )

        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformIncrement
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformDecrement
        )

        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformIncrement
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformDecrement
        )

        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformShowAlternateUI
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformShowDefaultUI
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityAlternateUIVisible
        )

        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityIndex, objc._C_NSInteger
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityDisclosureLevel,
            objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityFrame_,
            0,
            AppKit.NSRect.__typestr__,
        )

        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityElement
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityElement_, 0
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityFrame,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityFrame_,
            0,
            AppKit.NSRect.__typestr__,
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityFocused
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityFocused_, 0
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityActivationPoint,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityActivationPoint_,
            0,
            AppKit.NSPoint.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityOrientation,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityOrientation_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilitySelected
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilitySelected_, 0
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityExpanded
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityExpanded_, 0
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityEdited
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityEdited_, 0
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityEnabled
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityEnabled_, 0
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityProtectedContent
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityProtectedContent_, 0
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityAlternateUIVisible
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityAlternateUIVisible_, 0
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityHidden
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityHidden_, 0
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityFrontmost
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityFrontmost_, 0
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityOrderedByRow
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityOrderedByRow_, 0
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityHorizontalUnits,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityHorizontalUnits_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityVerticalUnits,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityVerticalUnits_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityLayoutPointForScreenPoint_,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityLayoutPointForScreenPoint_,
            0,
            AppKit.NSPoint.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityLayoutSizeForScreenSize_,
            AppKit.NSSize.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityLayoutSizeForScreenSize_,
            0,
            AppKit.NSSize.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityScreenPointForLayoutPoint_,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityScreenPointForLayoutPoint_,
            0,
            AppKit.NSPoint.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityScreenSizeForLayoutSize_,
            AppKit.NSSize.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityScreenSizeForLayoutSize_,
            0,
            AppKit.NSSize.__typestr__,
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityDisclosed
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityDisclosed_, 0
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityDisclosureLevel,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityDisclosureLevel_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityUnits, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityUnits_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRulerMarkerType,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityRulerMarkerType_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityLabelValue, objc._C_FLT
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityLabelValue_,
            0,
            objc._C_FLT,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityColumnCount,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityColumnCount_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRowCount, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityRowCount_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityIndex, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityIndex_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilitySortDirection,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilitySortDirection_,
            0,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityCellForColumn_row_,
            0,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityCellForColumn_row_,
            1,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRowIndexRange,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityRowIndexRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityColumnIndexRange,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityColumnIndexRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityInsertionPointLineNumber,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityInsertionPointLineNumber_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilitySharedCharacterRange,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilitySharedCharacterRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityVisibleCharacterRange,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityVisibleCharacterRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityNumberOfCharacters,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilityNumberOfCharacters_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilitySelectedTextRange,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.setAccessibilitySelectedTextRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRangeForLine_,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRangeForLine_,
            0,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityAttributedStringForRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityStringForRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRangeForPosition_,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRangeForPosition_,
            0,
            AppKit.NSPoint.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRangeForIndex_,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRangeForIndex_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityFrameForRange_,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityFrameForRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityRTFForRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityStyleRangeForIndex_,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityStyleRangeForIndex_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityStyleRangeForIndex_,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityStyleRangeForIndex_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityLineForIndex_,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSAccessibilityProtocolsHelper.accessibilityLineForIndex_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(TestNSAccessibilityProtocolsHelper.isAccessibilityModal)
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityModal_, 0
        )
        self.assertResultIsBOOL(TestNSAccessibilityProtocolsHelper.isAccessibilityMain)
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityMain_, 0
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityMinimized
        )
        self.assertArgIsBOOL(
            TestNSAccessibilityProtocolsHelper.setAccessibilityMinimized_, 0
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformCancel
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformConfirm
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformDecrement
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformDelete
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformIncrement
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformPick
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformPress
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformRaise
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformShowAlternateUI
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformShowDefaultUI
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.accessibilityPerformShowMenu
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilitySelectorAllowed_
        )
        self.assertResultIsBOOL(
            TestNSAccessibilityProtocolsHelper.isAccessibilityRequired
        )
