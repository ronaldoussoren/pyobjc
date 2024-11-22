import AppKit
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_level_key,
    os_release,
    skipUnless,
)


class TestNSCell(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSControlStateValue, int)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSBackgroundStyle)
        self.assertIsEnumType(AppKit.NSCellAttribute)
        self.assertIsEnumType(AppKit.NSCellHitResult)
        self.assertIsEnumType(AppKit.NSCellImagePosition)
        self.assertIsEnumType(AppKit.NSCellStyleMask)
        self.assertIsEnumType(AppKit.NSCellType)
        self.assertIsEnumType(AppKit.NSControlSize)
        self.assertIsEnumType(AppKit.NSControlTint)
        self.assertIsEnumType(AppKit.NSImageScaling)

    @skipUnless(
        not (os_level_key("10.13") <= os_level_key(os_release())),
        "doesn't work on 10.13, 10.14",
    )
    def testUnicode(self):
        u = "\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8"
        cell = AppKit.NSCell.alloc().initTextCell_(u)
        cell.setStringValue_(u)
        self.assertEqual(cell.stringValue(), u)

    @skipUnless(
        not (os_level_key("10.13") <= os_level_key(os_release())),
        "doesn't work on 10.13, 10.14",
    )
    def testInt(self):
        i = 17
        cell = AppKit.NSCell.alloc().initTextCell_("")
        cell.setIntValue_(i)
        self.assertEqual(cell.intValue(), i)

    @skipUnless(
        not (os_level_key("10.13") <= os_level_key(os_release())),
        "doesn't work on 10.13, 10.14",
    )
    def testFloat(self):
        f = 3.125
        cell = AppKit.NSCell.alloc().initTextCell_("")
        cell.setFloatValue_(f)
        self.assertEqual(cell.floatValue(), f)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSCell.prefersTrackingUntilMouseUp)
        self.assertResultIsBOOL(AppKit.NSCell.isOpaque)
        self.assertResultIsBOOL(AppKit.NSCell.isEnabled)
        self.assertArgIsBOOL(AppKit.NSCell.setEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.isContinuous)
        self.assertArgIsBOOL(AppKit.NSCell.setContinuous_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.isEditable)
        self.assertArgIsBOOL(AppKit.NSCell.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.isSelectable)
        self.assertArgIsBOOL(AppKit.NSCell.setSelectable_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.isBordered)
        self.assertArgIsBOOL(AppKit.NSCell.setBordered_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.isBezeled)
        self.assertArgIsBOOL(AppKit.NSCell.setBezeled_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.isScrollable)
        self.assertArgIsBOOL(AppKit.NSCell.setScrollable_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.isHighlighted)
        self.assertArgIsBOOL(AppKit.NSCell.setHighlighted_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.wraps)
        self.assertArgIsBOOL(AppKit.NSCell.setWraps_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.isEntryAcceptable_)
        self.assertArgIsBOOL(AppKit.NSCell.setFloatingPointFormat_left_right_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.hasValidObjectValue)
        self.assertArgIsBOOL(AppKit.NSCell.highlight_withFrame_inView_, 0)
        self.assertArgIsOut(AppKit.NSCell.getPeriodicDelay_interval_, 0)
        self.assertArgIsOut(AppKit.NSCell.getPeriodicDelay_interval_, 1)
        self.assertResultIsBOOL(AppKit.NSCell.startTrackingAt_inView_)
        self.assertResultIsBOOL(AppKit.NSCell.continueTracking_at_inView_)
        self.assertArgIsBOOL(AppKit.NSCell.stopTracking_at_inView_mouseIsUp_, 3)
        self.assertResultIsBOOL(AppKit.NSCell.trackMouse_inRect_ofView_untilMouseUp_)
        self.assertArgIsBOOL(AppKit.NSCell.trackMouse_inRect_ofView_untilMouseUp_, 3)
        self.assertResultIsBOOL(AppKit.NSCell.sendsActionOnEndEditing)
        self.assertArgIsBOOL(AppKit.NSCell.setSendsActionOnEndEditing_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.allowsUndo)
        self.assertArgIsBOOL(AppKit.NSCell.setAllowsUndo_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.truncatesLastVisibleLine)
        self.assertArgIsBOOL(AppKit.NSCell.setTruncatesLastVisibleLine_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.refusesFirstResponder)
        self.assertArgIsBOOL(AppKit.NSCell.setRefusesFirstResponder_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.acceptsFirstResponder)
        self.assertResultIsBOOL(AppKit.NSCell.showsFirstResponder)
        self.assertArgIsBOOL(AppKit.NSCell.setShowsFirstResponder_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.wantsNotificationForMarkedText)
        self.assertResultIsBOOL(AppKit.NSCell.allowsEditingTextAttributes)
        self.assertArgIsBOOL(AppKit.NSCell.setAllowsEditingTextAttributes_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.importsGraphics)
        self.assertArgIsBOOL(AppKit.NSCell.setImportsGraphics_, 0)
        self.assertResultIsBOOL(AppKit.NSCell.allowsMixedState)
        self.assertArgIsBOOL(AppKit.NSCell.setAllowsMixedState_, 0)

    def testFunctions(self):
        self.assertArgIsBOOL(AppKit.NSDrawThreePartImage, 4)
        self.assertArgIsBOOL(AppKit.NSDrawThreePartImage, 7)
        self.assertArgIsBOOL(AppKit.NSDrawNinePartImage, 12)

    def testConstants(self):
        self.assertIsInstance(AppKit.NSControlTintDidChangeNotification, str)

        self.assertEqual(AppKit.NSAnyType, 0)
        self.assertEqual(AppKit.NSIntType, 1)
        self.assertEqual(AppKit.NSPositiveIntType, 2)
        self.assertEqual(AppKit.NSFloatType, 3)
        self.assertEqual(AppKit.NSPositiveFloatType, 4)
        self.assertEqual(AppKit.NSDoubleType, 6)
        self.assertEqual(AppKit.NSPositiveDoubleType, 7)

        self.assertEqual(AppKit.NSNullCellType, 0)
        self.assertEqual(AppKit.NSTextCellType, 1)
        self.assertEqual(AppKit.NSImageCellType, 2)

        self.assertEqual(AppKit.NSCellDisabled, 0)
        self.assertEqual(AppKit.NSCellState, 1)
        self.assertEqual(AppKit.NSPushInCell, 2)
        self.assertEqual(AppKit.NSCellEditable, 3)
        self.assertEqual(AppKit.NSChangeGrayCell, 4)
        self.assertEqual(AppKit.NSCellHighlighted, 5)
        self.assertEqual(AppKit.NSCellLightsByContents, 6)
        self.assertEqual(AppKit.NSCellLightsByGray, 7)
        self.assertEqual(AppKit.NSChangeBackgroundCell, 8)
        self.assertEqual(AppKit.NSCellLightsByBackground, 9)
        self.assertEqual(AppKit.NSCellIsBordered, 10)
        self.assertEqual(AppKit.NSCellHasOverlappingImage, 11)
        self.assertEqual(AppKit.NSCellHasImageHorizontal, 12)
        self.assertEqual(AppKit.NSCellHasImageOnLeftOrBottom, 13)
        self.assertEqual(AppKit.NSCellChangesContents, 14)
        self.assertEqual(AppKit.NSCellIsInsetButton, 15)
        self.assertEqual(AppKit.NSCellAllowsMixedState, 16)

        self.assertEqual(AppKit.NSNoImage, 0)
        self.assertEqual(AppKit.NSImageOnly, 1)
        self.assertEqual(AppKit.NSImageLeft, 2)
        self.assertEqual(AppKit.NSImageRight, 3)
        self.assertEqual(AppKit.NSImageBelow, 4)
        self.assertEqual(AppKit.NSImageAbove, 5)
        self.assertEqual(AppKit.NSImageOverlaps, 6)
        self.assertEqual(AppKit.NSImageLeading, 7)
        self.assertEqual(AppKit.NSImageTrailing, 8)

        self.assertEqual(AppKit.NSScaleProportionally, 0)
        self.assertEqual(AppKit.NSScaleToFit, 1)
        self.assertEqual(AppKit.NSScaleNone, 2)

        self.assertEqual(AppKit.NSImageScaleProportionallyDown, 0)
        self.assertEqual(AppKit.NSImageScaleAxesIndependently, 1)
        self.assertEqual(AppKit.NSImageScaleNone, 2)
        self.assertEqual(AppKit.NSImageScaleProportionallyUpOrDown, 3)

        self.assertEqual(AppKit.NSMixedState, -1)
        self.assertEqual(AppKit.NSOffState, 0)
        self.assertEqual(AppKit.NSOnState, 1)

        self.assertEqual(AppKit.NSControlStateMixed, -1)
        self.assertEqual(AppKit.NSControlStateOff, 0)
        self.assertEqual(AppKit.NSControlStateOn, 1)

        self.assertEqual(AppKit.NSNoCellMask, 0)
        self.assertEqual(AppKit.NSContentsCellMask, 1)
        self.assertEqual(AppKit.NSPushInCellMask, 2)
        self.assertEqual(AppKit.NSChangeGrayCellMask, 4)
        self.assertEqual(AppKit.NSChangeBackgroundCellMask, 8)

        self.assertEqual(AppKit.NSDefaultControlTint, 0)
        self.assertEqual(AppKit.NSBlueControlTint, 1)
        self.assertEqual(AppKit.NSGraphiteControlTint, 6)
        self.assertEqual(AppKit.NSClearControlTint, 7)

        self.assertEqual(AppKit.NSRegularControlSize, 0)
        self.assertEqual(AppKit.NSSmallControlSize, 1)
        self.assertEqual(AppKit.NSMiniControlSize, 2)

        self.assertEqual(AppKit.NSControlSizeRegular, 0)
        self.assertEqual(AppKit.NSControlSizeSmall, 1)
        self.assertEqual(AppKit.NSControlSizeMini, 2)

        self.assertEqual(AppKit.NSCellHitNone, 0)
        self.assertEqual(AppKit.NSCellHitContentArea, 1 << 0)
        self.assertEqual(AppKit.NSCellHitEditableTextArea, 1 << 1)
        self.assertEqual(AppKit.NSCellHitTrackableArea, 1 << 2)

        self.assertEqual(AppKit.NSBackgroundStyleLight, 0)
        self.assertEqual(AppKit.NSBackgroundStyleDark, 1)
        self.assertEqual(AppKit.NSBackgroundStyleRaised, 2)
        self.assertEqual(AppKit.NSBackgroundStyleLowered, 3)

        self.assertEqual(AppKit.NSControlStateValueMixed, -1)
        self.assertEqual(AppKit.NSControlStateValueOff, 0)
        self.assertEqual(AppKit.NSControlStateValueOn, 1)

        self.assertEqual(AppKit.NSBackgroundStyleNormal, 0)
        self.assertEqual(AppKit.NSBackgroundStyleEmphasized, 1)
        self.assertEqual(AppKit.NSBackgroundStyleRaised, 2)
        self.assertEqual(AppKit.NSBackgroundStyleLowered, 3)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSCell.usesSingleLineMode)
        self.assertArgIsBOOL(AppKit.NSCell.setUsesSingleLineMode_, 0)
