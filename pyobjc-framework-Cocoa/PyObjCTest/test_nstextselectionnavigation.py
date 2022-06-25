import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSTextSelectionNavigationHelper(AppKit.NSObject):
    def locationFromLocation_withOffset_(self, a, b):
        return 1

    def offsetFromLocation_toLocation_(self, a, b):
        return 1

    def baseWritingDirectionAtLocation_(self, a):
        return 1

    def enumerateCaretOffsetsInLineFragmentAtLocation_usingBlock_(self, a, b):
        pass

    def lineFragmentRangeForPoint_inContainerAtLocation_(self, a, b):
        return 1

    def enumerateContainerBoundariesFromLocation_reverse_usingBlock_(self, a, b, c):
        pass

    def enumerateSubstringsFromLocation_options_usingBlock_(self, a, b, c):
        pass

    def textLayoutOrientationAtLocation_(self, a):
        return 1


class TestNSTextSelectionNavigation(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTextSelectionNavigationDestination)
        self.assertIsEnumType(AppKit.NSTextSelectionNavigationDirection)
        self.assertIsEnumType(AppKit.NSTextSelectionNavigationLayoutOrientation)
        self.assertIsEnumType(AppKit.NSTextSelectionNavigationModifier)
        self.assertIsEnumType(AppKit.NSTextSelectionNavigationWritingDirection)

    def test_constants(self):
        self.assertEqual(AppKit.NSTextSelectionNavigationDirectionForward, 0)
        self.assertEqual(AppKit.NSTextSelectionNavigationDirectionBackward, 1)
        self.assertEqual(AppKit.NSTextSelectionNavigationDirectionRight, 2)
        self.assertEqual(AppKit.NSTextSelectionNavigationDirectionLeft, 3)
        self.assertEqual(AppKit.NSTextSelectionNavigationDirectionUp, 4)
        self.assertEqual(AppKit.NSTextSelectionNavigationDirectionDown, 5)

        self.assertEqual(AppKit.NSTextSelectionNavigationDestinationCharacter, 0)
        self.assertEqual(AppKit.NSTextSelectionNavigationDestinationWord, 1)
        self.assertEqual(AppKit.NSTextSelectionNavigationDestinationLine, 2)
        self.assertEqual(AppKit.NSTextSelectionNavigationDestinationSentence, 3)
        self.assertEqual(AppKit.NSTextSelectionNavigationDestinationParagraph, 4)
        self.assertEqual(AppKit.NSTextSelectionNavigationDestinationContainer, 5)
        self.assertEqual(AppKit.NSTextSelectionNavigationDestinationDocument, 6)

        self.assertEqual(AppKit.NSTextSelectionNavigationModifierExtend, 1 << 0)
        self.assertEqual(AppKit.NSTextSelectionNavigationModifierVisual, 1 << 1)
        self.assertEqual(AppKit.NSTextSelectionNavigationModifierMultiple, 1 << 2)

        self.assertEqual(AppKit.NSTextSelectionNavigationWritingDirectionLeftToRight, 0)
        self.assertEqual(AppKit.NSTextSelectionNavigationWritingDirectionRightToLeft, 1)

        self.assertEqual(AppKit.NSTextSelectionNavigationLayoutOrientationHorizontal, 0)
        self.assertEqual(AppKit.NSTextSelectionNavigationLayoutOrientationVertical, 1)

    @min_sdk_level("12.0")
    def test_protocols(self):
        self.assertProtocolExists("NSTextSelectionDataSource")

    def test_methods(self):
        self.assertArgHasType(
            TestNSTextSelectionNavigationHelper.locationFromLocation_withOffset_,
            1,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSTextSelectionNavigationHelper.offsetFromLocation_toLocation_,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSTextSelectionNavigationHelper.baseWritingDirectionAtLocation_,
            objc._C_NSInteger,
        )

        self.assertArgIsBlock(
            TestNSTextSelectionNavigationHelper.enumerateCaretOffsetsInLineFragmentAtLocation_usingBlock_,
            1,
            b"vd@Zo^Z",
        )

        self.assertArgHasType(
            TestNSTextSelectionNavigationHelper.lineFragmentRangeForPoint_inContainerAtLocation_,
            0,
            AppKit.NSPoint.__typestr__,
        )

        self.assertArgIsBOOL(
            TestNSTextSelectionNavigationHelper.enumerateContainerBoundariesFromLocation_reverse_usingBlock_,
            1,
        )
        self.assertArgIsBlock(
            TestNSTextSelectionNavigationHelper.enumerateContainerBoundariesFromLocation_reverse_usingBlock_,
            2,
            b"v@o^Z",
        )

        self.assertArgIsBlock(
            TestNSTextSelectionNavigationHelper.enumerateSubstringsFromLocation_options_usingBlock_,
            2,
            b"v@@@o^Z",
        )

        self.assertArgIsBOOL(
            TestNSTextSelectionNavigationHelper.enumerateContainerBoundariesFromLocation_reverse_usingBlock_,
            1,
        )
        self.assertArgIsBlock(
            TestNSTextSelectionNavigationHelper.enumerateContainerBoundariesFromLocation_reverse_usingBlock_,
            2,
            b"v@o^Z",
        )

        self.assertResultHasType(
            TestNSTextSelectionNavigationHelper.textLayoutOrientationAtLocation_,
            objc._C_NSInteger,
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            AppKit.NSTextSelectionNavigation.allowsNonContiguousRanges
        )
        self.assertArgIsBOOL(
            AppKit.NSTextSelectionNavigation.setAllowsNonContiguousRanges_, 0
        )

        self.assertResultIsBOOL(
            AppKit.NSTextSelectionNavigation.rotatesCoordinateSystemForLayoutOrientation
        )
        self.assertArgIsBOOL(
            AppKit.NSTextSelectionNavigation.setRotatesCoordinateSystemForLayoutOrientation_,
            0,
        )

        self.assertArgIsBOOL(
            AppKit.NSTextSelectionNavigation.destinationSelectionForTextSelection_direction_destination_extending_confined_,
            3,
        )
        self.assertArgIsBOOL(
            AppKit.NSTextSelectionNavigation.destinationSelectionForTextSelection_direction_destination_extending_confined_,
            4,
        )
        self.assertArgIsBOOL(
            AppKit.NSTextSelectionNavigation.textSelectionsInteractingAtPoint_inContainerAtLocation_anchors_modifiers_selecting_bounds_,  # noqa: B950
            4,
        )
        self.assertArgIsBOOL(
            AppKit.NSTextSelectionNavigation.deletionRangesForTextSelection_direction_destination_allowsDecomposition_,
            3,
        )
