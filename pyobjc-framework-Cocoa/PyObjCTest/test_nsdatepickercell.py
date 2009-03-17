
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDatePickerHelper (NSObject):
    def datePickerCell_validateProposedDateValue_timeInterval_(self, v1, v2, v3):
        pass


class TestNSDatePickerCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTextFieldAndStepperDatePickerStyle, 0)
        self.failUnlessEqual(NSClockAndCalendarDatePickerStyle, 1)
        self.failUnlessEqual(NSTextFieldDatePickerStyle, 2)
        self.failUnlessEqual(NSSingleDateMode, 0)
        self.failUnlessEqual(NSRangeDateMode, 1)
        self.failUnlessEqual(NSHourMinuteDatePickerElementFlag, 0x000c)
        self.failUnlessEqual(NSHourMinuteSecondDatePickerElementFlag, 0x000e)
        self.failUnlessEqual(NSTimeZoneDatePickerElementFlag, 0x0010)
        self.failUnlessEqual(NSYearMonthDatePickerElementFlag, 0x00c0)
        self.failUnlessEqual(NSYearMonthDayDatePickerElementFlag, 0x00e0)
        self.failUnlessEqual(NSEraDatePickerElementFlag, 0x0100)

    def testMethods(self):
        o = TestNSDatePickerHelper.alloc().init()
        m = o.datePickerCell_validateProposedDateValue_timeInterval_.__metadata__()
        self.failUnlessEqual(m['arguments'][3]['type'], 'N^@')
        self.failUnlessStartswith(m['arguments'][4]['type'], 'N^')

        self.failUnlessResultIsBOOL(NSDatePickerCell.drawsBackground)
        self.failUnlessArgIsBOOL(NSDatePickerCell.setDrawsBackground_, 0)

if __name__ == "__main__":
    main()
