
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDatePickerHelper (NSObject):
    def datePickerCell_validateProposedDateValue_timeInterval_(self, v1, v2, v3):
        pass


class TestNSDatePickerCell (TestCase):
    def testConstants(self):
        self.assertEqual(NSTextFieldAndStepperDatePickerStyle, 0)
        self.assertEqual(NSClockAndCalendarDatePickerStyle, 1)
        self.assertEqual(NSTextFieldDatePickerStyle, 2)
        self.assertEqual(NSSingleDateMode, 0)
        self.assertEqual(NSRangeDateMode, 1)
        self.assertEqual(NSHourMinuteDatePickerElementFlag, 0x000c)
        self.assertEqual(NSHourMinuteSecondDatePickerElementFlag, 0x000e)
        self.assertEqual(NSTimeZoneDatePickerElementFlag, 0x0010)
        self.assertEqual(NSYearMonthDatePickerElementFlag, 0x00c0)
        self.assertEqual(NSYearMonthDayDatePickerElementFlag, 0x00e0)
        self.assertEqual(NSEraDatePickerElementFlag, 0x0100)

    def testMethods(self):
        o = TestNSDatePickerHelper.alloc().init()
        m = o.datePickerCell_validateProposedDateValue_timeInterval_.__metadata__()
        self.assertEqual(m['arguments'][3]['type'], b'N^@')
        self.assertStartswith(m['arguments'][4]['type'], b'N^')

        self.assertResultIsBOOL(NSDatePickerCell.drawsBackground)
        self.assertArgIsBOOL(NSDatePickerCell.setDrawsBackground_, 0)

if __name__ == "__main__":
    main()
