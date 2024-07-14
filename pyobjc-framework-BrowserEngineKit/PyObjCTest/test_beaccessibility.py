import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase
import objc


class TestBEAccessibilityHelper(BrowserEngineKit.NSObject):
    def browserAccessibilityIsRequired(self):
        return 1

    def setBrowserAccessibilityIsRequired_(self, a):
        pass

    def browserAccessibilityPressedState(self):
        return 1

    def setBrowserAccessibilityPressedState_(self, a):
        pass

    def browserAccessibilityHasDOMFocus(self):
        return 1

    def setBrowserAccessibilityHasDOMFocus_(self, a):
        pass

    def browserAccessibilityContainerType(self):
        return 1

    def setBrowserAccessibilityContainerType_(self, a):
        pass

    def browserAccessibilitySelectedTextRange(self):
        return

    def browserAccessibilitySetSelectedTextRange_(self, a):
        pass

    def browserAccessibilityValueInRange_(self, a):
        return 1

    def browserAccessibilityAttributedValueInRange_(self, a):
        return 1

    def browserAccessibilityInsertTextAtCursor_(self, a):
        pass

    def browserAccessibilityDeleteTextAtCursor_(self, a):
        pass


class TestBEAccessibility(TestCase):
    def test_constants(self):
        self.assertIsEnumType(BrowserEngineKit.BEAccessibilityPressedState)
        self.assertEqual(BrowserEngineKit.BEAccessibilityPressedStateUndefined, 0)
        self.assertEqual(BrowserEngineKit.BEAccessibilityPressedStateFalse, 1)
        self.assertEqual(BrowserEngineKit.BEAccessibilityPressedStateTrue, 2)
        self.assertEqual(BrowserEngineKit.BEAccessibilityPressedStateMixed, 3)

        self.assertIsEnumType(BrowserEngineKit.BEAccessibilityContainerType)
        self.assertEqual(BrowserEngineKit.BEAccessibilityContainerTypeNone, 0)
        self.assertEqual(BrowserEngineKit.BEAccessibilityContainerTypeLandmark, 1 << 0)
        self.assertEqual(BrowserEngineKit.BEAccessibilityContainerTypeTable, 1 << 1)
        self.assertEqual(BrowserEngineKit.BEAccessibilityContainerTypeList, 1 << 2)
        self.assertEqual(BrowserEngineKit.BEAccessibilityContainerTypeFieldset, 1 << 3)
        self.assertEqual(BrowserEngineKit.BEAccessibilityContainerTypeDialog, 1 << 4)
        self.assertEqual(BrowserEngineKit.BEAccessibilityContainerTypeTree, 1 << 5)
        self.assertEqual(BrowserEngineKit.BEAccessibilityContainerTypeFrame, 1 << 6)
        self.assertEqual(BrowserEngineKit.BEAccessibilityContainerTypeArticle, 1 << 7)
        self.assertEqual(
            BrowserEngineKit.BEAccessibilityContainerTypeSemanticGroup, 1 << 8
        )
        self.assertEqual(
            BrowserEngineKit.BEAccessibilityContainerTypeScrollArea, 1 << 9
        )
        self.assertEqual(BrowserEngineKit.BEAccessibilityContainerTypeAlert, 1 << 10)
        self.assertEqual(
            BrowserEngineKit.BEAccessibilityContainerTypeDescriptionList, 1 << 11
        )

    def test_methods(self):
        self.assertResultIsBOOL(
            TestBEAccessibilityHelper.browserAccessibilityIsRequired
        )
        self.assertArgIsBOOL(
            TestBEAccessibilityHelper.setBrowserAccessibilityIsRequired_, 0
        )
        self.assertResultHasType(
            TestBEAccessibilityHelper.browserAccessibilityPressedState,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestBEAccessibilityHelper.setBrowserAccessibilityPressedState_,
            0,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(
            TestBEAccessibilityHelper.browserAccessibilityHasDOMFocus
        )
        self.assertArgIsBOOL(
            TestBEAccessibilityHelper.setBrowserAccessibilityHasDOMFocus_, 0
        )
        self.assertResultHasType(
            TestBEAccessibilityHelper.browserAccessibilityContainerType,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestBEAccessibilityHelper.setBrowserAccessibilityContainerType_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestBEAccessibilityHelper.browserAccessibilitySelectedTextRange,
            BrowserEngineKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestBEAccessibilityHelper.browserAccessibilitySetSelectedTextRange_,
            0,
            BrowserEngineKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestBEAccessibilityHelper.browserAccessibilityValueInRange_,
            0,
            BrowserEngineKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestBEAccessibilityHelper.browserAccessibilityDeleteTextAtCursor_,
            0,
            objc._C_NSUInteger,
        )
