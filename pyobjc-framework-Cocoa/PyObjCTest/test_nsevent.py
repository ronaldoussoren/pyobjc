import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSEvent(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSLeftMouseDown, 1)
        self.assertEqual(AppKit.NSLeftMouseUp, 2)
        self.assertEqual(AppKit.NSRightMouseDown, 3)
        self.assertEqual(AppKit.NSRightMouseUp, 4)
        self.assertEqual(AppKit.NSMouseMoved, 5)
        self.assertEqual(AppKit.NSLeftMouseDragged, 6)
        self.assertEqual(AppKit.NSRightMouseDragged, 7)
        self.assertEqual(AppKit.NSMouseEntered, 8)
        self.assertEqual(AppKit.NSMouseExited, 9)
        self.assertEqual(AppKit.NSKeyDown, 10)
        self.assertEqual(AppKit.NSKeyUp, 11)
        self.assertEqual(AppKit.NSFlagsChanged, 12)
        self.assertEqual(AppKit.NSAppKitDefined, 13)
        self.assertEqual(AppKit.NSSystemDefined, 14)
        self.assertEqual(AppKit.NSApplicationDefined, 15)
        self.assertEqual(AppKit.NSPeriodic, 16)
        self.assertEqual(AppKit.NSCursorUpdate, 17)
        self.assertEqual(AppKit.NSScrollWheel, 22)
        self.assertEqual(AppKit.NSTabletPoint, 23)
        self.assertEqual(AppKit.NSTabletProximity, 24)
        self.assertEqual(AppKit.NSOtherMouseDown, 25)
        self.assertEqual(AppKit.NSOtherMouseUp, 26)
        self.assertEqual(AppKit.NSOtherMouseDragged, 27)

        self.assertEqual(AppKit.NSEventTypeLeftMouseDown, 1)
        self.assertEqual(AppKit.NSEventTypeLeftMouseUp, 2)
        self.assertEqual(AppKit.NSEventTypeRightMouseDown, 3)
        self.assertEqual(AppKit.NSEventTypeRightMouseUp, 4)
        self.assertEqual(AppKit.NSEventTypeMouseMoved, 5)
        self.assertEqual(AppKit.NSEventTypeLeftMouseDragged, 6)
        self.assertEqual(AppKit.NSEventTypeRightMouseDragged, 7)
        self.assertEqual(AppKit.NSEventTypeMouseEntered, 8)
        self.assertEqual(AppKit.NSEventTypeMouseExited, 9)
        self.assertEqual(AppKit.NSEventTypeKeyDown, 10)
        self.assertEqual(AppKit.NSEventTypeKeyUp, 11)
        self.assertEqual(AppKit.NSEventTypeFlagsChanged, 12)
        self.assertEqual(AppKit.NSEventTypeAppKitDefined, 13)
        self.assertEqual(AppKit.NSEventTypeSystemDefined, 14)
        self.assertEqual(AppKit.NSEventTypeApplicationDefined, 15)
        self.assertEqual(AppKit.NSEventTypePeriodic, 16)
        self.assertEqual(AppKit.NSEventTypeCursorUpdate, 17)
        self.assertEqual(AppKit.NSEventTypeScrollWheel, 22)
        self.assertEqual(AppKit.NSEventTypeTabletPoint, 23)
        self.assertEqual(AppKit.NSEventTypeTabletProximity, 24)
        self.assertEqual(AppKit.NSEventTypeOtherMouseDown, 25)
        self.assertEqual(AppKit.NSEventTypeOtherMouseUp, 26)
        self.assertEqual(AppKit.NSEventTypeOtherMouseDragged, 27)

        self.assertEqual(AppKit.NSLeftMouseDownMask, 1 << AppKit.NSLeftMouseDown)
        self.assertEqual(AppKit.NSLeftMouseUpMask, 1 << AppKit.NSLeftMouseUp)
        self.assertEqual(AppKit.NSRightMouseDownMask, 1 << AppKit.NSRightMouseDown)
        self.assertEqual(AppKit.NSRightMouseUpMask, 1 << AppKit.NSRightMouseUp)
        self.assertEqual(AppKit.NSMouseMovedMask, 1 << AppKit.NSMouseMoved)
        self.assertEqual(AppKit.NSLeftMouseDraggedMask, 1 << AppKit.NSLeftMouseDragged)
        self.assertEqual(
            AppKit.NSRightMouseDraggedMask, 1 << AppKit.NSRightMouseDragged
        )
        self.assertEqual(AppKit.NSMouseEnteredMask, 1 << AppKit.NSMouseEntered)
        self.assertEqual(AppKit.NSMouseExitedMask, 1 << AppKit.NSMouseExited)
        self.assertEqual(AppKit.NSKeyDownMask, 1 << AppKit.NSKeyDown)
        self.assertEqual(AppKit.NSKeyUpMask, 1 << AppKit.NSKeyUp)
        self.assertEqual(AppKit.NSFlagsChangedMask, 1 << AppKit.NSFlagsChanged)
        self.assertEqual(AppKit.NSAppKitDefinedMask, 1 << AppKit.NSAppKitDefined)
        self.assertEqual(AppKit.NSSystemDefinedMask, 1 << AppKit.NSSystemDefined)
        self.assertEqual(
            AppKit.NSApplicationDefinedMask, 1 << AppKit.NSApplicationDefined
        )
        self.assertEqual(AppKit.NSPeriodicMask, 1 << AppKit.NSPeriodic)
        self.assertEqual(AppKit.NSCursorUpdateMask, 1 << AppKit.NSCursorUpdate)
        self.assertEqual(AppKit.NSScrollWheelMask, 1 << AppKit.NSScrollWheel)
        self.assertEqual(AppKit.NSTabletPointMask, 1 << AppKit.NSTabletPoint)
        self.assertEqual(AppKit.NSTabletProximityMask, 1 << AppKit.NSTabletProximity)
        self.assertEqual(AppKit.NSOtherMouseDownMask, 1 << AppKit.NSOtherMouseDown)
        self.assertEqual(AppKit.NSOtherMouseUpMask, 1 << AppKit.NSOtherMouseUp)
        self.assertEqual(
            AppKit.NSOtherMouseDraggedMask, 1 << AppKit.NSOtherMouseDragged
        )
        self.assertEqual(AppKit.NSAnyEventMask, AppKit.NSUIntegerMax)

        self.assertEqual(
            AppKit.NSEventMaskLeftMouseDown, 1 << AppKit.NSEventTypeLeftMouseDown
        )
        self.assertEqual(
            AppKit.NSEventMaskLeftMouseUp, 1 << AppKit.NSEventTypeLeftMouseUp
        )
        self.assertEqual(
            AppKit.NSEventMaskRightMouseDown, 1 << AppKit.NSEventTypeRightMouseDown
        )
        self.assertEqual(
            AppKit.NSEventMaskRightMouseUp, 1 << AppKit.NSEventTypeRightMouseUp
        )
        self.assertEqual(
            AppKit.NSEventMaskMouseMoved, 1 << AppKit.NSEventTypeMouseMoved
        )
        self.assertEqual(
            AppKit.NSEventMaskLeftMouseDragged, 1 << AppKit.NSEventTypeLeftMouseDragged
        )
        self.assertEqual(
            AppKit.NSEventMaskRightMouseDragged,
            1 << AppKit.NSEventTypeRightMouseDragged,
        )
        self.assertEqual(
            AppKit.NSEventMaskMouseEntered, 1 << AppKit.NSEventTypeMouseEntered
        )
        self.assertEqual(
            AppKit.NSEventMaskMouseExited, 1 << AppKit.NSEventTypeMouseExited
        )
        self.assertEqual(AppKit.NSEventMaskKeyDown, 1 << AppKit.NSEventTypeKeyDown)
        self.assertEqual(AppKit.NSEventMaskKeyUp, 1 << AppKit.NSEventTypeKeyUp)
        self.assertEqual(
            AppKit.NSEventMaskFlagsChanged, 1 << AppKit.NSEventTypeFlagsChanged
        )
        self.assertEqual(
            AppKit.NSEventMaskAppKitDefined, 1 << AppKit.NSEventTypeAppKitDefined
        )
        self.assertEqual(
            AppKit.NSEventMaskSystemDefined, 1 << AppKit.NSEventTypeSystemDefined
        )
        self.assertEqual(
            AppKit.NSEventMaskApplicationDefined,
            1 << AppKit.NSEventTypeApplicationDefined,
        )
        self.assertEqual(AppKit.NSEventMaskPeriodic, 1 << AppKit.NSEventTypePeriodic)
        self.assertEqual(
            AppKit.NSEventMaskCursorUpdate, 1 << AppKit.NSEventTypeCursorUpdate
        )
        self.assertEqual(
            AppKit.NSEventMaskScrollWheel, 1 << AppKit.NSEventTypeScrollWheel
        )
        self.assertEqual(
            AppKit.NSEventMaskTabletPoint, 1 << AppKit.NSEventTypeTabletPoint
        )
        self.assertEqual(
            AppKit.NSEventMaskTabletProximity, 1 << AppKit.NSEventTypeTabletProximity
        )
        self.assertEqual(
            AppKit.NSEventMaskOtherMouseDown, 1 << AppKit.NSEventTypeOtherMouseDown
        )
        self.assertEqual(
            AppKit.NSEventMaskOtherMouseUp, 1 << AppKit.NSEventTypeOtherMouseUp
        )
        self.assertEqual(
            AppKit.NSEventMaskOtherMouseDragged,
            1 << AppKit.NSEventTypeOtherMouseDragged,
        )

        self.assertEqual(AppKit.NSAlphaShiftKeyMask, 1 << 16)
        self.assertEqual(AppKit.NSShiftKeyMask, 1 << 17)
        self.assertEqual(AppKit.NSControlKeyMask, 1 << 18)
        self.assertEqual(AppKit.NSAlternateKeyMask, 1 << 19)
        self.assertEqual(AppKit.NSCommandKeyMask, 1 << 20)
        self.assertEqual(AppKit.NSNumericPadKeyMask, 1 << 21)
        self.assertEqual(AppKit.NSHelpKeyMask, 1 << 22)
        self.assertEqual(AppKit.NSFunctionKeyMask, 1 << 23)
        self.assertEqual(AppKit.NSDeviceIndependentModifierFlagsMask, 0xFFFF0000)

        self.assertEqual(AppKit.NSEventModifierFlagCapsLock, 1 << 16)
        self.assertEqual(AppKit.NSEventModifierFlagShift, 1 << 17)
        self.assertEqual(AppKit.NSEventModifierFlagControl, 1 << 18)
        self.assertEqual(AppKit.NSEventModifierFlagOption, 1 << 19)
        self.assertEqual(AppKit.NSEventModifierFlagCommand, 1 << 20)
        self.assertEqual(AppKit.NSEventModifierFlagNumericPad, 1 << 21)
        self.assertEqual(AppKit.NSEventModifierFlagHelp, 1 << 22)
        self.assertEqual(AppKit.NSEventModifierFlagFunction, 1 << 23)
        self.assertEqual(
            AppKit.NSEventModifierFlagDeviceIndependentFlagsMask, 0xFFFF0000
        )

        self.assertEqual(AppKit.NSUnknownPointingDevice, 0)
        self.assertEqual(AppKit.NSPenPointingDevice, 1)
        self.assertEqual(AppKit.NSCursorPointingDevice, 2)
        self.assertEqual(AppKit.NSEraserPointingDevice, 3)

        self.assertEqual(AppKit.NSPointingDeviceTypeUnknown, 0)
        self.assertEqual(AppKit.NSPointingDeviceTypePen, 1)
        self.assertEqual(AppKit.NSPointingDeviceTypeCursor, 2)
        self.assertEqual(AppKit.NSPointingDeviceTypeEraser, 3)

        self.assertEqual(AppKit.NSPenTipMask, 1)
        self.assertEqual(AppKit.NSPenLowerSideMask, 2)
        self.assertEqual(AppKit.NSPenUpperSideMask, 4)

        self.assertEqual(AppKit.NSEventButtonMaskPenTip, 1)
        self.assertEqual(AppKit.NSEventButtonMaskPenLowerSide, 2)
        self.assertEqual(AppKit.NSEventButtonMaskPenUpperSide, 4)

        self.assertEqual(AppKit.NSWindowExposedEventType, 0)
        self.assertEqual(AppKit.NSApplicationActivatedEventType, 1)
        self.assertEqual(AppKit.NSApplicationDeactivatedEventType, 2)
        self.assertEqual(AppKit.NSWindowMovedEventType, 4)
        self.assertEqual(AppKit.NSScreenChangedEventType, 8)
        self.assertEqual(AppKit.NSAWTEventType, 16)
        self.assertEqual(AppKit.NSPowerOffEventType, 1)

        self.assertEqual(AppKit.NSMouseEventSubtype, 0)
        self.assertEqual(AppKit.NSTabletPointEventSubtype, 1)
        self.assertEqual(AppKit.NSTabletProximityEventSubtype, 2)
        self.assertEqual(AppKit.NSTouchEventSubtype, 3)

        self.assertEqual(AppKit.NSEventSubtypeMouseEvent, 0)
        self.assertEqual(AppKit.NSEventSubtypeTabletPoint, 1)
        self.assertEqual(AppKit.NSEventSubtypeTabletProximity, 2)
        self.assertEqual(AppKit.NSEventSubtypeTouch, 3)

        self.assertEqual(AppKit.NSEventSubtypeWindowExposed, 0)
        self.assertEqual(AppKit.NSEventSubtypeApplicationActivated, 1)
        self.assertEqual(AppKit.NSEventSubtypeApplicationDeactivated, 2)
        self.assertEqual(AppKit.NSEventSubtypeWindowMoved, 4)
        self.assertEqual(AppKit.NSEventSubtypeScreenChanged, 8)
        self.assertEqual(AppKit.NSEventSubtypePowerOff, 1)

        self.assertEqual(AppKit.NSUpArrowFunctionKey, chr(0xF700))
        self.assertEqual(AppKit.NSDownArrowFunctionKey, chr(0xF701))
        self.assertEqual(AppKit.NSLeftArrowFunctionKey, chr(0xF702))
        self.assertEqual(AppKit.NSRightArrowFunctionKey, chr(0xF703))
        self.assertEqual(AppKit.NSF1FunctionKey, chr(0xF704))
        self.assertEqual(AppKit.NSF2FunctionKey, chr(0xF705))
        self.assertEqual(AppKit.NSF3FunctionKey, chr(0xF706))
        self.assertEqual(AppKit.NSF4FunctionKey, chr(0xF707))
        self.assertEqual(AppKit.NSF5FunctionKey, chr(0xF708))
        self.assertEqual(AppKit.NSF6FunctionKey, chr(0xF709))
        self.assertEqual(AppKit.NSF7FunctionKey, chr(0xF70A))
        self.assertEqual(AppKit.NSF8FunctionKey, chr(0xF70B))
        self.assertEqual(AppKit.NSF9FunctionKey, chr(0xF70C))
        self.assertEqual(AppKit.NSF10FunctionKey, chr(0xF70D))
        self.assertEqual(AppKit.NSF11FunctionKey, chr(0xF70E))
        self.assertEqual(AppKit.NSF12FunctionKey, chr(0xF70F))
        self.assertEqual(AppKit.NSF13FunctionKey, chr(0xF710))
        self.assertEqual(AppKit.NSF14FunctionKey, chr(0xF711))
        self.assertEqual(AppKit.NSF15FunctionKey, chr(0xF712))
        self.assertEqual(AppKit.NSF16FunctionKey, chr(0xF713))
        self.assertEqual(AppKit.NSF17FunctionKey, chr(0xF714))
        self.assertEqual(AppKit.NSF18FunctionKey, chr(0xF715))
        self.assertEqual(AppKit.NSF19FunctionKey, chr(0xF716))
        self.assertEqual(AppKit.NSF20FunctionKey, chr(0xF717))
        self.assertEqual(AppKit.NSF21FunctionKey, chr(0xF718))
        self.assertEqual(AppKit.NSF22FunctionKey, chr(0xF719))
        self.assertEqual(AppKit.NSF23FunctionKey, chr(0xF71A))
        self.assertEqual(AppKit.NSF24FunctionKey, chr(0xF71B))
        self.assertEqual(AppKit.NSF25FunctionKey, chr(0xF71C))
        self.assertEqual(AppKit.NSF26FunctionKey, chr(0xF71D))
        self.assertEqual(AppKit.NSF27FunctionKey, chr(0xF71E))
        self.assertEqual(AppKit.NSF28FunctionKey, chr(0xF71F))
        self.assertEqual(AppKit.NSF29FunctionKey, chr(0xF720))
        self.assertEqual(AppKit.NSF30FunctionKey, chr(0xF721))
        self.assertEqual(AppKit.NSF31FunctionKey, chr(0xF722))
        self.assertEqual(AppKit.NSF32FunctionKey, chr(0xF723))
        self.assertEqual(AppKit.NSF33FunctionKey, chr(0xF724))
        self.assertEqual(AppKit.NSF34FunctionKey, chr(0xF725))
        self.assertEqual(AppKit.NSF35FunctionKey, chr(0xF726))
        self.assertEqual(AppKit.NSInsertFunctionKey, chr(0xF727))
        self.assertEqual(AppKit.NSDeleteFunctionKey, chr(0xF728))
        self.assertEqual(AppKit.NSHomeFunctionKey, chr(0xF729))
        self.assertEqual(AppKit.NSBeginFunctionKey, chr(0xF72A))
        self.assertEqual(AppKit.NSEndFunctionKey, chr(0xF72B))
        self.assertEqual(AppKit.NSPageUpFunctionKey, chr(0xF72C))
        self.assertEqual(AppKit.NSPageDownFunctionKey, chr(0xF72D))
        self.assertEqual(AppKit.NSPrintScreenFunctionKey, chr(0xF72E))
        self.assertEqual(AppKit.NSScrollLockFunctionKey, chr(0xF72F))
        self.assertEqual(AppKit.NSPauseFunctionKey, chr(0xF730))
        self.assertEqual(AppKit.NSSysReqFunctionKey, chr(0xF731))
        self.assertEqual(AppKit.NSBreakFunctionKey, chr(0xF732))
        self.assertEqual(AppKit.NSResetFunctionKey, chr(0xF733))
        self.assertEqual(AppKit.NSStopFunctionKey, chr(0xF734))
        self.assertEqual(AppKit.NSMenuFunctionKey, chr(0xF735))
        self.assertEqual(AppKit.NSUserFunctionKey, chr(0xF736))
        self.assertEqual(AppKit.NSSystemFunctionKey, chr(0xF737))
        self.assertEqual(AppKit.NSPrintFunctionKey, chr(0xF738))
        self.assertEqual(AppKit.NSClearLineFunctionKey, chr(0xF739))
        self.assertEqual(AppKit.NSClearDisplayFunctionKey, chr(0xF73A))
        self.assertEqual(AppKit.NSInsertLineFunctionKey, chr(0xF73B))
        self.assertEqual(AppKit.NSDeleteLineFunctionKey, chr(0xF73C))
        self.assertEqual(AppKit.NSInsertCharFunctionKey, chr(0xF73D))
        self.assertEqual(AppKit.NSDeleteCharFunctionKey, chr(0xF73E))
        self.assertEqual(AppKit.NSPrevFunctionKey, chr(0xF73F))
        self.assertEqual(AppKit.NSNextFunctionKey, chr(0xF740))
        self.assertEqual(AppKit.NSSelectFunctionKey, chr(0xF741))
        self.assertEqual(AppKit.NSExecuteFunctionKey, chr(0xF742))
        self.assertEqual(AppKit.NSUndoFunctionKey, chr(0xF743))
        self.assertEqual(AppKit.NSRedoFunctionKey, chr(0xF744))
        self.assertEqual(AppKit.NSFindFunctionKey, chr(0xF745))
        self.assertEqual(AppKit.NSHelpFunctionKey, chr(0xF746))
        self.assertEqual(AppKit.NSModeSwitchFunctionKey, chr(0xF747))

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(AppKit.NSEventTypeGesture, 29)
        self.assertEqual(AppKit.NSEventTypeMagnify, 30)
        self.assertEqual(AppKit.NSEventTypeSwipe, 31)
        self.assertEqual(AppKit.NSEventTypeRotate, 18)
        self.assertEqual(AppKit.NSEventTypeBeginGesture, 19)
        self.assertEqual(AppKit.NSEventTypeEndGesture, 20)

        self.assertEqual(AppKit.NSEventMaskGesture, 1 << 29)
        self.assertEqual(AppKit.NSEventMaskMagnify, 1 << 30)
        self.assertEqual(AppKit.NSEventMaskSwipe, 1 << 31)
        self.assertEqual(AppKit.NSEventMaskRotate, 1 << 18)
        self.assertEqual(AppKit.NSEventMaskBeginGesture, 1 << 19)
        self.assertEqual(AppKit.NSEventMaskEndGesture, 1 << 20)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSEventPhaseNone, 0)
        self.assertEqual(AppKit.NSEventPhaseBegan, 1)
        self.assertEqual(AppKit.NSEventPhaseStationary, 2)
        self.assertEqual(AppKit.NSEventPhaseChanged, 4)
        self.assertEqual(AppKit.NSEventPhaseEnded, 8)
        self.assertEqual(AppKit.NSEventPhaseCancelled, 16)
        self.assertEqual(AppKit.NSEventPhaseMayBegin, 32)

        self.assertEqual(AppKit.NSEventGestureAxisNone, 0)
        self.assertEqual(AppKit.NSEventGestureAxisHorizontal, 1)
        self.assertEqual(AppKit.NSEventGestureAxisVertical, 2)

        self.assertEqual(AppKit.NSEventSwipeTrackingLockDirection, 1)
        self.assertEqual(AppKit.NSEventSwipeTrackingClampGestureAmount, 2)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(AppKit.NSEventTypeSmartMagnify, 32)
        self.assertEqual(AppKit.NSEventTypeQuickLook, 33)
        self.assertEqual(AppKit.NSEventMaskSmartMagnify, 1 << 32)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(AppKit.NSEventTypePressure, 34)
        self.assertEqual(AppKit.NSEventTypeDirectTouch, 37)
        self.assertEqual(AppKit.NSEventMaskPressure, 1 << 34)
        self.assertEqual(AppKit.NSEventMaskDirectTouch, 1 << 37)

        self.assertEqual(AppKit.NSPressureBehaviorUnknown, -1)
        self.assertEqual(AppKit.NSPressureBehaviorPrimaryDefault, 0)
        self.assertEqual(AppKit.NSPressureBehaviorPrimaryClick, 1)
        self.assertEqual(AppKit.NSPressureBehaviorPrimaryGeneric, 2)
        self.assertEqual(AppKit.NSPressureBehaviorPrimaryAccelerator, 3)
        self.assertEqual(AppKit.NSPressureBehaviorPrimaryDeepClick, 5)
        self.assertEqual(AppKit.NSPressureBehaviorPrimaryDeepDrag, 6)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertEqual(AppKit.NSEventTypeChangeMode, 38)
        self.assertEqual(
            AppKit.NSEventMaskChangeMode, 1 << AppKit.NSEventTypeChangeMode
        )

    def testFunctions(self):
        v = AppKit.NSEventMaskFromType(AppKit.NSLeftMouseDown)
        self.assertEqual(v, AppKit.NSLeftMouseDownMask)

        v = AppKit.NSEventMaskFromType(AppKit.NSOtherMouseDown)
        self.assertEqual(v, AppKit.NSOtherMouseDownMask)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(AppKit.NSEvent.isMouseCoalescingEnabled)
        self.assertArgIsBOOL(AppKit.NSEvent.setMouseCoalescingEnabled_, 0)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSEvent.isARepeat)
        self.assertResultIsBOOL(AppKit.NSEvent.isEnteringProximity)

        self.assertArgIsBOOL(
            AppKit.NSEvent.keyEventWithType_location_modifierFlags_timestamp_windowNumber_context_characters_charactersIgnoringModifiers_isARepeat_keyCode_,  # noqa: B950
            8,
        )
        self.assertArgHasType(
            AppKit.NSEvent.enterExitEventWithType_location_modifierFlags_timestamp_windowNumber_context_eventNumber_trackingNumber_userData_,  # noqa: B950
            8,
            b"^v",
        )

        self.assertResultHasType(AppKit.NSEvent.userData, b"^v")

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBlock(
            AppKit.NSEvent.addGlobalMonitorForEventsMatchingMask_handler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            AppKit.NSEvent.addLocalMonitorForEventsMatchingMask_handler_, 1, b"@@"
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSEvent.hasPreciseScrollingDeltas)
        self.assertResultIsBOOL(AppKit.NSEvent.isDirectionInvertedFromDevice)
        self.assertResultIsBOOL(AppKit.NSEvent.isSwipeTrackingFromScrollEventsEnabled)

        self.assertArgIsBlock(
            AppKit.NSEvent.trackSwipeEventWithOptions_dampenAmountThresholdMin_max_usingHandler_,  # noqa: B950
            3,
            b"v"
            + objc._C_CGFloat
            + objc._C_NSUInteger
            + objc._C_NSBOOL
            + b"o^"
            + objc._C_NSBOOL,
        )
