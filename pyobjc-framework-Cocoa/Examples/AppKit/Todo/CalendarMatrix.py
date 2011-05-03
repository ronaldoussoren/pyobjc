from Cocoa import *

gNumDaysInMonth = ( 0, 31, 28, 31, 30, 21, 30, 31, 31, 30, 31, 30, 31 )

def isLeap(year):
    return (((year % 4) == 0 and ((year % 100) != 0)) or (year % 400) == 0)

class CalendarMatrix (NSMatrix):
    lastMonthButton = objc.IBOutlet()
    monthName = objc.IBOutlet()
    nextMonthButton = objc.IBOutlet()

    __slots__ = ('_selectedDay', '_startOffset')

    def initWithFrame_(self, frameRect):
        self._selectedDay = None
        self._startOffset = 0

        cell = NSButtonCell.alloc().initTextCell_("")
        now  = NSCalendarDate.date()

        cell.setShowsStateBy_(NSOnOffButton)
        self.initWithFrame_mode_prototype_numberOfRows_numberOfColumns_(
            frameRect, NSRadioModeMatrix, cell, 5, 7)

        count = 0
        for i in range(6):
            for j in range(7):
                val = self.cellAtRow_column_(i, j)
                if val:
                    val.setTag_(count)
                count += 1

        self._selectedDay = NSCalendarDate.dateWithYear_month_day_hour_minute_second_timeZone_(
                now.yearOfCommonEra(),
                now.monthOfYear(),
                now.dayOfMonth(),
                0,
                0,
                0,
                NSTimeZone.localTimeZone())
        return self


    @objc.IBAction
    def choseDay_(self, sender):
        prevSelDate = self.selectedDay()
        selDay = self.selectedCell().tag() - self._startOffset + 1

        selDate = NSCalendarDate.dateWithYear_month_day_hour_minute_second_timeZone_(
                prevSelDate.yearOfCommonEra(),
                prevSelDate.monthOfYear(),
                selDay,
                0,
                0,
                0,
                NSTimeZone.localTimeZone())
        self.setSelectedDay_(selDate)
        self.highlightTodayIfVisible()

        if self.delegate().respondsToSelector_('calendarMatrix:didChangeToDate:'):
            self.delegate().calendarMatrix_didChangeToDate_(
                self, selDate)


    @objc.IBAction
    def monthChanged_(self, sender):
        thisDate = self.selectedDay()
        currentYear = thisDate.yearOfCommonEra()
        currentMonth = thisDate.monthOfYear()

        if sender is self.nextMonthButton:
            if currentMonth == 12:
                currentMonth = 1
                currentYear += 1
            else:
                currentMonth += 1
        else:
            if currentMonth == 1:
                currentMonth = 12
                currentYear -= 1
            else:
                currentMonth -= 1

        self.setSelectedDay_(NSCalendarDate.dateWithYear_month_day_hour_minute_second_timeZone_(currentYear, currentMonth, 1, 0, 0, 0, NSTimeZone.localTimeZone()))
        self.refreshCalendar()
        self.choseDay_(self)

    def setSelectedDay_(self, newDay):
        self._selectedDay = newDay

    def selectedDay(self):
        return self._selectedDay

    def refreshCalendar(self):

        selDate = self.selectedDay()
        currentMonth = selDate.monthOfYear()
        currentYear = selDate.yearOfCommonEra()

        firstOfMonth = NSCalendarDate.dateWithYear_month_day_hour_minute_second_timeZone_(
                    currentYear,
                    currentMonth,
                    1,
                    0,
                    0,
                    0,
                    NSTimeZone.localTimeZone())
        self.monthName.setStringValue_(
            firstOfMonth.descriptionWithCalendarFormat_("%B %Y"))
        daysInMonth = gNumDaysInMonth[currentMonth]

        if (currentMonth == 2) and isLeap(currentYear):
            daysInMonth += 1

        self._startOffset = firstOfMonth.dayOfWeek()

        dayLabel = 1

        for i in range(42):
            cell = self.cellWithTag_(i)
            if cell is None:
                continue

            if i < self._startOffset or i >= (daysInMonth + self._startOffset):
                # blank out unused cells in the matrix
                cell.setBordered_(False)
                cell.setEnabled_(False)
                cell.setTitle_("")
                cell.setCellAttribute_to_(NSCellHighlighted, False)
            else:
                # Fill in valid days in the matrix
                cell.setBordered_(True)
                cell.setEnabled_(True)
                cell.setFont_(NSFont.systemFontOfSize_(12))
                cell.setTitle_(str(dayLabel))
                dayLabel += 1
                cell.setCellAttribute_to_(NSCellHighlighted, False)

        self.selectCellWithTag_(selDate.dayOfMonth() + self._startOffset - 1)
        self.highlightTodayIfVisible()


    def highlightTodayIfVisible(self):
        now = NSCalendarDate.date()
        selDate = self.selectedDay()

        if (selDate.yearOfCommonEra() == now.yearOfCommonEra()
                and selDate.monthOfYear() == now.monthOfYear()
                and selDate.dayOfMonth() == now.dayOfMonth()):
            aCell = self.cellWithTag_(
                now.dayOfMonth() + self._startOffset - 1)
            aCell.setHighlightsBy_(NSMomentaryChangeButton)
            aCell.setCellAttribute_to_(NSCellHighlighted, True)

    def awakeFromNib(self):
        self.setTarget_(self)
        self.setAction_('choseDay:')
        self.setAutosizesCells_(True)
        self.refreshCalendar()
        self.choseDay_(self)
