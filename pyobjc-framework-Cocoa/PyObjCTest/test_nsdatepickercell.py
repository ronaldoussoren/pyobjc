import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSDatePickerHelper(AppKit.NSObject):
    def datePickerCell_validateProposedDateValue_timeInterval_(self, v1, v2, v3):
        pass


class TestNSDatePickerCell(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSTextFieldAndStepperDatePickerStyle, 0)
        self.assertEqual(AppKit.NSClockAndCalendarDatePickerStyle, 1)
        self.assertEqual(AppKit.NSTextFieldDatePickerStyle, 2)

        self.assertEqual(AppKit.NSSingleDateMode, 0)
        self.assertEqual(AppKit.NSRangeDateMode, 1)

        self.assertEqual(AppKit.NSHourMinuteDatePickerElementFlag, 0x000C)
        self.assertEqual(AppKit.NSHourMinuteSecondDatePickerElementFlag, 0x000E)
        self.assertEqual(AppKit.NSTimeZoneDatePickerElementFlag, 0x0010)
        self.assertEqual(AppKit.NSYearMonthDatePickerElementFlag, 0x00C0)
        self.assertEqual(AppKit.NSYearMonthDayDatePickerElementFlag, 0x00E0)
        self.assertEqual(AppKit.NSEraDatePickerElementFlag, 0x0100)

        self.assertEqual(AppKit.NSDatePickerStyleTextFieldAndStepper, 0)
        self.assertEqual(AppKit.NSDatePickerStyleClockAndCalendar, 1)
        self.assertEqual(AppKit.NSDatePickerStyleTextField, 2)

        self.assertEqual(AppKit.NSDatePickerModeSingle, 0)
        self.assertEqual(AppKit.NSDatePickerModeRange, 1)

        self.assertEqual(AppKit.NSDatePickerElementFlagHourMinute, 0x000C)
        self.assertEqual(AppKit.NSDatePickerElementFlagHourMinuteSecond, 0x000E)
        self.assertEqual(AppKit.NSDatePickerElementFlagTimeZone, 0x0010)

        self.assertEqual(AppKit.NSDatePickerElementFlagYearMonth, 0x00C0)
        self.assertEqual(AppKit.NSDatePickerElementFlagYearMonthDay, 0x00E0)
        self.assertEqual(AppKit.NSDatePickerElementFlagEra, 0x0100)

    def testMethods(self):
        o = TestNSDatePickerHelper.alloc().init()
        m = o.datePickerCell_validateProposedDateValue_timeInterval_.__metadata__()
        self.assertEqual(m["arguments"][3]["type"], b"N^@")
        self.assertStartswith(m["arguments"][4]["type"], b"N^")

        self.assertResultIsBOOL(AppKit.NSDatePickerCell.drawsBackground)
        self.assertArgIsBOOL(AppKit.NSDatePickerCell.setDrawsBackground_, 0)

    @min_sdk_level("10.10")
    def testProtocols(self):
        objc.protocolNamed("NSDatePickerCellDelegate")
