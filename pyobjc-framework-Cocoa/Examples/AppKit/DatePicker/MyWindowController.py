import Cocoa
import objc

# date/time element popup selections:
kNSHourMinuteDatePickerElementFlag = 0
kNSHourMinuteSecondDatePickerElementFlag = 1
kNSTimeZoneDatePickerElementFlag = 2

kNSYearMonthDatePickerElementFlag = 0
kNSYearMonthDayDatePickerElementFlag = 1
kNSEraDatePickerElementFlag = 2

kSingleDateMode = 0
kRangeDateMode = 1


class MyWindowController(Cocoa.NSWindowController):
    datePickerControl = objc.ivar()
    shrinkGrowFactor = objc.ivar.int()

    outerBox = objc.IBOutlet()
    datePickerPlaceHolder = objc.IBOutlet()

    dateResult1 = objc.IBOutlet()
    dateResult2 = objc.IBOutlet()
    dateResult3 = objc.IBOutlet()
    dateResult4 = objc.IBOutlet()
    dateResult5 = objc.IBOutlet()

    # appearance
    pickerStylePopup = objc.IBOutlet()
    drawsBackgroundCheck = objc.IBOutlet()
    bezeledCheck = objc.IBOutlet()
    borderedCheck = objc.IBOutlet()
    backColorWell = objc.IBOutlet()
    textColorWell = objc.IBOutlet()
    fontSizePopup = objc.IBOutlet()

    # date and time
    dateElementChecks = objc.IBOutlet()
    timeElementChecks = objc.IBOutlet()
    overrideDateCheck = objc.IBOutlet()
    overrideDate = objc.IBOutlet()

    # date range
    datePickerModeRadios = objc.IBOutlet()
    secondsRangeEdit = objc.IBOutlet()
    secondsRangeEditLabel = objc.IBOutlet()

    minDatePicker = objc.IBOutlet()
    maxDatePicker = objc.IBOutlet()
    setMinDateButton = objc.IBOutlet()
    setMaxDateButton = objc.IBOutlet()
    clearMinDateButton = objc.IBOutlet()
    clearMaxDateButton = objc.IBOutlet()

    def awakeFromNib(self):
        # based our date formatter on CFDateFormatter: allows more
        # configurability and better localization
        Cocoa.NSDateFormatter.setDefaultFormatterBehavior_(
            Cocoa.NSDateFormatterBehavior10_4
        )

        self.setupDatePickerControl_(Cocoa.NSClockAndCalendarDatePickerStyle)

        # setup the initial Cocoa.NSDatePickerElementFlags since we are using picker style:
        # Cocoa.NSClockAndCalendarDatePickerStyle
        flags = (
            Cocoa.NSYearMonthDatePickerElementFlag
            | Cocoa.NSYearMonthDayDatePickerElementFlag
            | Cocoa.NSEraDatePickerElementFlag
            | Cocoa.NSHourMinuteDatePickerElementFlag
            | Cocoa.NSHourMinuteSecondDatePickerElementFlag
            | Cocoa.NSTimeZoneDatePickerElementFlag
        )
        self.datePickerControl.setDatePickerElements_(flags)

        self.datePickerModeRadios.cellWithTag_(1).setEnabled_(
            False
        )  # not currently implemented in 10.4.x and earlier

        self.minDatePicker.setDateValue_(Cocoa.NSDate.date())
        self.maxDatePicker.setDateValue_(Cocoa.NSDate.distantFuture())

        self.updateControls()  # force update of all UI elements and the picker itself

    def applicationShouldTerminateAfterLastWindowClosed_(self, sender):
        return True

    def setupDatePickerControl_(self, pickerStyle):
        # we need to re-create the picker control (due to a resize bug when
        # switching between styles)
        if (
            self.datePickerControl is not None
        ):  # hide and release the previous date picker, if any
            self.datePickerControl.setHidden_(True)
            self.datePickerControl.setNeedsDisplay_(True)
            self.datePickerControl = None

        frame = self.datePickerPlaceHolder.frame()
        self.shrinkGrowFactor = frame.size.height - 30

        # create the date picker control if not created already
        if self.datePickerControl is None:
            self.datePickerControl = Cocoa.NSDatePicker.alloc().initWithFrame_(frame)

        self.datePickerControl.setFrameOrigin_(
            Cocoa.NSMakePoint(1, 0)
        )  # nudge the control placement a little

        self.datePickerControl.setDatePickerStyle_(
            pickerStyle
        )  # set our desired picker style

        self.datePickerPlaceHolder.addSubview_(
            self.datePickerControl
        )  # embed into our placeholder
        self.datePickerControl.setDrawsBackground_(True)
        self.datePickerControl.setBezeled_(True)
        self.datePickerControl.setBordered_(False)
        self.datePickerControl.setEnabled_(True)

        self.datePickerControl.setTextColor_(self.textColorWell.color())
        self.datePickerControl.setBackgroundColor_(self.backColorWell.color())

        # always set the date/time to TODAY
        # note that our delete override might block this...
        self.datePickerControl.setDateValue_(Cocoa.NSDate.date())

        self.datePickerControl.setNeedsDisplay_(True)
        self.updateControls()  # force update of all UI elements and the picker itself

        # synch the picker style popup with the new style change
        self.pickerStylePopup.selectItemWithTag_(pickerStyle)

        # we want to be the cell's delegate to catch date validation
        self.datePickerControl.setDelegate_(self)
        # or we can set us as the delegate to its cell like so:
        #                self.datePickerControl.cell().setDelegate_(self)

        # we want to respond to date/time changes
        self.datePickerControl.setAction_("datePickerAction:")

    def updateDateResult(self):
        theDate = self.datePickerControl.dateValue()
        if theDate is not None:
            formatter = Cocoa.NSDateFormatter.alloc().init()

            # some examples:
            # formatter.setDateStyle_(Cocoa.NSDateFormatterNoStyle)
            #     ->  <no date displayed>
            # formatter.setDateStyle_(Cocoa.NSDateFormatterMediumStyle)
            #     ->  Jan 24, 1984
            # formatter.setDateStyle_(Cocoa.NSDateFormatterShortStyle)
            #     ->  1/24/84
            # formatter.setDateStyle_(Cocoa.NSDateFormatterLongStyle)
            #     ->  January 24, 1984
            # formatter.setDateStyle_(Cocoa.NSDateFormatterFullStyle)
            #     ->  Tuesday, January 24, 1984
            #
            # formatter.setTimeStyle_(Cocoa.NSDateFormatterNoStyle)
            #     ->  <no time displayed>
            # formatter.setTimeStyle_(Cocoa.NSDateFormatterShortStyle)
            #     ->  2:44 PM
            # formatter.setTimeStyle_(Cocoa.NSDateFormatterMediumStyle)
            #     ->  2:44:55 PM
            # formatter.setTimeStyle_(Cocoa.NSDateFormatterLongStyle)
            #     ->  2:44:55 PM PDT
            # formatter.setTimeStyle_(Cocoa.NSDateFormatterFullStyle)
            #     ->  2:44:55 PM PDT
            #

            formatter.setDateStyle_(Cocoa.NSDateFormatterShortStyle)
            formatter.setTimeStyle_(Cocoa.NSDateFormatterNoStyle)
            formattedDateString = formatter.stringFromDate_(theDate)
            self.dateResult1.setStringValue_(formattedDateString)

            formatter.setDateStyle_(Cocoa.NSDateFormatterShortStyle)
            formatter.setTimeStyle_(Cocoa.NSDateFormatterShortStyle)
            formattedDateString = formatter.stringFromDate_(theDate)
            self.dateResult2.setStringValue_(formattedDateString)

            formatter.setDateStyle_(Cocoa.NSDateFormatterMediumStyle)
            formatter.setTimeStyle_(Cocoa.NSDateFormatterShortStyle)
            formattedDateString = formatter.stringFromDate_(theDate)
            self.dateResult3.setStringValue_(formattedDateString)

            formatter.setDateStyle_(Cocoa.NSDateFormatterLongStyle)
            formatter.setTimeStyle_(Cocoa.NSDateFormatterShortStyle)
            formattedDateString = formatter.stringFromDate_(theDate)
            self.dateResult4.setStringValue_(formattedDateString)

            formatter.setDateStyle_(Cocoa.NSDateFormatterFullStyle)
            formatter.setTimeStyle_(Cocoa.NSDateFormatterFullStyle)
            formattedDateString = formatter.stringFromDate_(theDate)
            self.dateResult5.setStringValue_(formattedDateString)

    def updateControls(self):
        self.datePickerControl.setNeedsDisplay_(True)  # force it to update

        self.updateDatePickerMode()
        self.updateDateTimeElementFlags()
        self.updateDateResult()

    @objc.IBAction
    def setPickerStyle_(self, sender):
        tag = sender.selectedCell().tag()

        windowFrame = self.window().frame()
        boxFrame = self.outerBox.frame()

        self.datePickerControl.setHidden_(True)

        if tag == Cocoa.NSClockAndCalendarDatePickerStyle:
            # for this picker style, we need to grow the window to make room

            windowFrame.size.height += self.shrinkGrowFactor
            windowFrame.origin.y -= self.shrinkGrowFactor

            boxFrame.size.height += self.shrinkGrowFactor
            self.outerBox.setFrame_(boxFrame)

            self.window().setFrame_display_animate_(windowFrame, True, True)

            # set our desired picker style
            self.datePickerControl.setDatePickerStyle_(
                Cocoa.NSClockAndCalendarDatePickerStyle
            )

            # shows these last
            self.dateResult1.setHidden_(False)
            self.dateResult2.setHidden_(False)
            self.dateResult3.setHidden_(False)
            self.dateResult4.setHidden_(False)

        else:
            currentPickerStyle = self.datePickerControl.datePickerStyle()

            # shrink the window only if the current style is "clock and calendar"
            if currentPickerStyle == Cocoa.NSClockAndCalendarDatePickerStyle:
                # hide these first
                self.dateResult1.setHidden_(True)
                self.dateResult2.setHidden_(True)
                self.dateResult3.setHidden_(True)
                self.dateResult4.setHidden_(True)

                windowFrame.size.height -= self.shrinkGrowFactor
                windowFrame.origin.y += self.shrinkGrowFactor

                boxFrame.size.height -= self.shrinkGrowFactor
                self.outerBox.setFrame_(boxFrame)

                self.window().setFrame_display_animate_(windowFrame, True, True)

            self.setupDatePickerControl_(tag)  # set our desired picker style

        self.datePickerControl.setHidden_(False)

        self.updateControls()  # force update of all UI elements and the picker itself

    @objc.IBAction
    def setFontSize_(self, sender):
        tag = sender.selectedCell().tag()
        if tag == Cocoa.NSMiniControlSize:
            self.datePickerControl.cell().setControlSize_(Cocoa.NSMiniControlSize)
            self.datePickerControl.cell().setFont_(Cocoa.NSFont.systemFontOfSize_(9.0))

        elif tag == Cocoa.NSSmallControlSize:
            self.datePickerControl.cell().setControlSize_(Cocoa.NSSmallControlSize)
            self.datePickerControl.cell().setFont_(Cocoa.NSFont.systemFontOfSize_(11.0))

        elif tag == Cocoa.NSRegularControlSize:
            self.datePickerControl.cell().setControlSize_(Cocoa.NSRegularControlSize)
            self.datePickerControl.cell().setFont_(Cocoa.NSFont.systemFontOfSize_(13.0))

    @objc.IBAction
    def datePickerAction_(self, sender):
        self.updateDateResult()

    @objc.IBAction
    def dateOverrideAction_(self, sender):
        checked = sender.selectedCell().state()
        if checked:
            self.datePickerControl.setDelegate_(self)

        else:
            self.datePickerControl.setDelegate_(None)

        self.datePickerControl.setDateValue_(
            Cocoa.NSDate.date()
        )  # force the delete "datePickerCell" to be called

    def datePickerCell_validateProposedDateValue_timeInterval_(
        self, aDatePickerCell, proposedDateValue, proposedTimeInterval
    ):
        controller = aDatePickerCell.delegate()

        if controller is self and aDatePickerCell is self.datePickerControl.cell():
            # override the date and time?
            if self.overrideDateCheck.cell().state():
                # override the date using the user specified date
                return (self.overrideDate.dateValue(), proposedTimeInterval)

        return (proposedDateValue, proposedTimeInterval)

    @objc.IBAction
    def setDrawsBackground_(self, sender):
        self.datePickerControl.setDrawsBackground_(sender.state())

    @objc.IBAction
    def setBackgroundColor_(self, sender):
        newColor = sender.color()
        self.datePickerControl.setBackgroundColor_(newColor)

    @objc.IBAction
    def setTextColor_(self, sender):
        newColor = sender.color()
        self.datePickerControl.setTextColor_(newColor)

    @objc.IBAction
    def setBezeled_(self, sender):
        self.datePickerControl.setBezeled_(sender.state())

    @objc.IBAction
    def setBordered_(self, sender):
        self.datePickerControl.setBordered_(sender.state())

    @objc.IBAction
    def setDateElementFlags_(self, sender):
        tag = sender.selectedCell().tag()
        flags = self.datePickerControl.datePickerElements()

        checked = sender.selectedCell().state()

        if tag == kNSYearMonthDatePickerElementFlag:
            if checked:
                flags |= Cocoa.NSYearMonthDatePickerElementFlag
            else:
                flags ^= Cocoa.NSYearMonthDatePickerElementFlag

        elif tag == kNSYearMonthDayDatePickerElementFlag:
            if checked:
                flags |= Cocoa.NSYearMonthDayDatePickerElementFlag
            else:
                flags ^= Cocoa.NSYearMonthDayDatePickerElementFlag

        elif tag == kNSEraDatePickerElementFlag:
            if checked:
                flags |= Cocoa.NSEraDatePickerElementFlag
            else:
                flags ^= Cocoa.NSEraDatePickerElementFlag

        self.datePickerControl.setDatePickerElements_(flags)

        self.updateControls()  # force update of all UI elements and the picker itself

    @objc.IBAction
    def setTimeElementFlags_(self, sender):
        tag = sender.selectedCell().tag()
        flags = self.datePickerControl.datePickerElements()

        checked = sender.selectedCell().state()

        if tag == kNSHourMinuteDatePickerElementFlag:
            if checked:
                flags |= Cocoa.NSHourMinuteDatePickerElementFlag
            else:
                flags ^= Cocoa.NSHourMinuteDatePickerElementFlag

        elif tag == kNSHourMinuteSecondDatePickerElementFlag:
            if checked:
                flags |= Cocoa.NSHourMinuteSecondDatePickerElementFlag
            else:
                flags ^= Cocoa.NSHourMinuteSecondDatePickerElementFlag

        elif tag == kNSTimeZoneDatePickerElementFlag:
            if checked:
                flags |= Cocoa.NSTimeZoneDatePickerElementFlag
            else:
                flags ^= Cocoa.NSTimeZoneDatePickerElementFlag

        self.datePickerControl.setDatePickerElements_(flags)

        self.updateControls()  # force update of all UI elements and the picker itself

    def updateDateTimeElementFlags(self):
        elementFlags = self.datePickerControl.datePickerElements()

        # time elements
        if (elementFlags & Cocoa.NSHourMinuteDatePickerElementFlag) != 0:
            self.timeElementChecks.selectCellWithTag_(0)
        if (elementFlags & Cocoa.NSHourMinuteSecondDatePickerElementFlag) != 0:
            self.timeElementChecks.selectCellWithTag_(1)
        if (elementFlags & Cocoa.NSTimeZoneDatePickerElementFlag) != 0:
            self.timeElementChecks.selectCellWithTag_(2)

        # date elements
        if (elementFlags & Cocoa.NSYearMonthDatePickerElementFlag) != 0:
            self.dateElementChecks.selectCellWithTag_(0)
        if (elementFlags & Cocoa.NSYearMonthDayDatePickerElementFlag) != 0:
            self.dateElementChecks.selectCellWithTag_(1)
        if (elementFlags & Cocoa.NSEraDatePickerElementFlag) != 0:
            self.dateElementChecks.selectCellWithTag_(2)

    @objc.IBAction
    def setMinDate_(self, sender):
        self.datePickerControl.setMinDate_(self.minDatePicker.dateValue())
        self.setMinDateButton.setEnabled_(False)
        self.clearMinDateButton.setEnabled_(True)

    @objc.IBAction
    def setMaxDate_(self, sender):
        self.datePickerControl.setMaxDate_(self.maxDatePicker.dateValue())
        self.setMaxDateButton.setEnabled_(False)
        self.clearMaxDateButton.setEnabled_(True)

    @objc.IBAction
    def clearMinDate_(self, sender):
        self.datePickerControl.setMinDate_(Cocoa.NSDate.distantPast())
        self.clearMinDateButton.setEnabled_(False)
        self.setMinDateButton.setEnabled_(True)

    @objc.IBAction
    def clearMaxDate_(self, sender):
        self.datePickerControl.setMaxDate_(Cocoa.NSDate.distantFuture())
        self.clearMaxDateButton.setEnabled_(False)
        self.setMaxDateButton.setEnabled_(True)

    @objc.IBAction
    def setDatePickerMode_(self, sender):
        tag = sender.selectedCell().tag()

        if tag == kSingleDateMode:
            self.datePickerControl.setDatePickerMode_(Cocoa.NSSingleDateMode)

        elif tag == kRangeDateMode:
            self.datePickerControl.setDatePickerMode_(Cocoa.NSRangeDateMode)

        self.updateControls()  # force update of all UI elements and the picker itself

    def updateDatePickerMode(self):
        mode = self.datePickerControl.datePickerMode()
        if mode == Cocoa.NSSingleDateMode:
            self.datePickerModeRadios.selectCellWithTag_(0)

            # interval value not applicable:
            self.secondsRangeEdit.setEnabled_(False)
            self.secondsRangeEditLabel.setTextColor_(Cocoa.NSColor.lightGrayColor())

            self.datePickerControl.setTimeInterval_(0)

        elif mode == Cocoa.NSRangeDateMode:
            self.datePickerModeRadios.selectCellWithTag_(1)

            # interval value applies:
            self.secondsRangeEdit.setEnabled_(True)
            self.secondsRangeEditLabel.setTextColor_(Cocoa.NSColor.blackColor())

            # set the date range by start date (here we use the current date in the date picker
            # control), and time interval (in seconds)
            secsStr = self.secondsRangeEdit.stringValue()
            numSeconds = int(secsStr)
            self.datePickerControl.setTimeInterval_(numSeconds)

    def controlTextDidEndEditing_(self, notification):
        self.updateDatePickerMode()  # force update of the date picker control
