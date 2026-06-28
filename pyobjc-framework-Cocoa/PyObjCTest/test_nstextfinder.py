import AppKit
import objc
from PyObjCTools.TestSupport import TestCase


class TestNSTextFinderHelper(AppKit.NSObject):
    def rectsForCharacterRange_(self, r):
        return 1

    def replaceCharactersInRange_withString_(self, r, s):
        pass

    def stringLength(self):
        return 0

    def isSelectable(self):
        pass

    def allowsMultipleSelection(self):
        pass

    def isEditable(self):
        pass

    def stringAtIndex_effectiveRange_endswithSearchBoundary_(self, a, b, c):
        pass

    def firstSelectedRange(self):
        pass

    def scrollRangeToVisible_(self, a):
        pass

    def shouldReplaceCharactersInRanges_withStrings_(self, a, b):
        pass

    def contentViewAtIndex_effectiveCharacterRange_(self, a, b):
        pass

    def drawCharactersInRange_forContentView_(self, a, b):
        pass

    def isFindBarVisible(self):
        return 1

    def setFindBarVisible_(self, a):
        pass


class TestNSTextFinder(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(AppKit.NSPasteboardTypeTextFinderOptionKey, str)

    def test_enums(self):
        self.assertIsEnumType(AppKit.NSTextFinderAction)
        self.assertEqual(AppKit.NSTextFinderActionShowFindInterface, 1)
        self.assertEqual(AppKit.NSTextFinderActionNextMatch, 2)
        self.assertEqual(AppKit.NSTextFinderActionPreviousMatch, 3)
        self.assertEqual(AppKit.NSTextFinderActionReplaceAll, 4)
        self.assertEqual(AppKit.NSTextFinderActionReplace, 5)
        self.assertEqual(AppKit.NSTextFinderActionReplaceAndFind, 6)
        self.assertEqual(AppKit.NSTextFinderActionSetSearchString, 7)
        self.assertEqual(AppKit.NSTextFinderActionReplaceAllInSelection, 8)
        self.assertEqual(AppKit.NSTextFinderActionSelectAll, 9)
        self.assertEqual(AppKit.NSTextFinderActionSelectAllInSelection, 10)
        self.assertEqual(AppKit.NSTextFinderActionHideFindInterface, 11)
        self.assertEqual(AppKit.NSTextFinderActionShowReplaceInterface, 12)
        self.assertEqual(AppKit.NSTextFinderActionHideReplaceInterface, 13)

        self.assertIsEnumType(AppKit.NSTextFinderMatchingType)
        self.assertEqual(AppKit.NSTextFinderMatchingTypeContains, 0)
        self.assertEqual(AppKit.NSTextFinderMatchingTypeStartsWith, 1)
        self.assertEqual(AppKit.NSTextFinderMatchingTypeFullWord, 2)
        self.assertEqual(AppKit.NSTextFinderMatchingTypeEndsWith, 3)

    def test_constants(self):
        self.assertIsInstance(AppKit.NSTextFinderCaseInsensitiveKey, str)
        self.assertIsInstance(AppKit.NSTextFinderMatchingTypeKey, str)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSTextFinder.validateAction_)
        self.assertResultIsBOOL(AppKit.NSTextFinder.findIndicatorNeedsUpdate)
        self.assertArgIsBOOL(AppKit.NSTextFinder.setFindIndicatorNeedsUpdate_, 0)
        self.assertResultIsBOOL(AppKit.NSTextFinder.isIncrementalSearchingEnabled)
        self.assertArgIsBOOL(AppKit.NSTextFinder.setIncrementalSearchingEnabled_, 0)
        self.assertResultIsBOOL(
            AppKit.NSTextFinder.incrementalSearchingShouldDimContentView
        )
        self.assertArgIsBOOL(
            AppKit.NSTextFinder.setIncrementalSearchingShouldDimContentView_, 0
        )

    def test_protocols(self):
        self.assertProtocolExists("NSTextFinderClient", AppKit)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestNSTextFinderHelper.isSelectable)
        self.assertResultIsBOOL(TestNSTextFinderHelper.allowsMultipleSelection)
        self.assertResultIsBOOL(TestNSTextFinderHelper.isEditable)

        self.assertArgHasType(
            TestNSTextFinderHelper.stringAtIndex_effectiveRange_endswithSearchBoundary_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextFinderHelper.stringAtIndex_effectiveRange_endswithSearchBoundary_,
            1,
            b"o^" + AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextFinderHelper.stringAtIndex_effectiveRange_endswithSearchBoundary_,
            2,
            b"o^" + objc._C_NSBOOL,
        )

        self.assertResultHasType(
            TestNSTextFinderHelper.stringLength, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestNSTextFinderHelper.firstSelectedRange, AppKit.NSRange.__typestr__
        )
        self.assertArgHasType(
            TestNSTextFinderHelper.scrollRangeToVisible_, 0, AppKit.NSRange.__typestr__
        )
        self.assertResultIsBOOL(
            TestNSTextFinderHelper.shouldReplaceCharactersInRanges_withStrings_
        )
        self.assertArgHasType(
            TestNSTextFinderHelper.replaceCharactersInRange_withString_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextFinderHelper.rectsForCharacterRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextFinderHelper.contentViewAtIndex_effectiveCharacterRange_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextFinderHelper.contentViewAtIndex_effectiveCharacterRange_,
            1,
            b"o^" + AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextFinderHelper.drawCharactersInRange_forContentView_,
            0,
            AppKit.NSRange.__typestr__,
        )

        self.assertProtocolExists("NSTextFinderBarContainer", AppKit)

        self.assertResultIsBOOL(TestNSTextFinderHelper.isFindBarVisible)
        self.assertArgIsBOOL(TestNSTextFinderHelper.setFindBarVisible_, 0)
