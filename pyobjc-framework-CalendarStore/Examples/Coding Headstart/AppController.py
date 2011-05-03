from Cocoa import *
from CalendarStore import *

class AppController (NSObject):
    mainWindow = objc.IBOutlet()
    taskCreationDialog = objc.IBOutlet()
    priorityPopup = objc.IBOutlet()
    eventCreationDialog = objc.IBOutlet()
    calendarData = objc.IBOutlet()
    
    calItemTitle = objc.ivar()
    calItemStartDate = objc.ivar()
    calItemEndDate = objc.ivar()

    objc.synthesize('calItemTitle',     copy=True)
    objc.synthesize('calItemStartDate', copy=True)
    objc.synthesize('calItemEndDate',   copy=True)

    @objc.IBAction
    def showTaskCreationDialog_(self, sender):
        # Set default values for the title, start date and priority
        # Cocoa bindings will clear out the related fields in the sheet
        self._.calItemTitle = None
        self._.calItemStartDate = NSDate.date()
        NSApp.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_(
            self.taskCreationDialog, self.mainWindow,
            self, 'didEndSheet:returnCode:contextInfo:', None)


    @objc.IBAction
    def showEventCreationDialog_(self, sender): 
        # Set default values for the title and start/end date
        # Cocoa bindings will clear out the related fields in the sheet
        self._.calItemTitle = None
        self._.calItemStartDate = NSDate.date()
        self._.calItemEndDate = NSDate.dateWithTimeIntervalSinceNow_(3600)
        NSApp.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_(
                self.eventCreationDialog, self.mainWindow, self,
                'didEndSheet:returnCode:contextInfo:', None)

    # Called when the "Add" button is pressed on the event/task entry sheet
    # This starts the sheet dismissal process
    @objc.IBAction
    def dismissDialog_(self, sender):
        NSApp.endSheet_(sender.window())

    @objc.selectorFor(NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_)
    def didEndSheet_returnCode_contextInfo_(self, sheet, returnCode, contextInfo):

        # Find out which calendar was selected for the new event/task
        # We do this using the calendarData array controller which is bound to 
        # the calendar popups in the sheet
        selectedCalendar = None
        count = len(self.calendarData.selectedObjects())
        if count > 0:
            selectedCalendarUID = self.calendarData.selectedObjects()[0].uid()
            selectedCalendar = CalCalendarStore.defaultCalendarStore(
                    ).calendarWithUID_(selectedCalendarUID)

        # Create an event/task based on which sheet was used
        if sheet is self.taskCreationDialog:
            if self._.calItemTitle is None:
                self._.calItemTitle = "My Task"

            self.createNewTaskWithCalendar_title_priority_dueDate_(
                    selectedCalendar, self._.calItemTitle,
                    self.priorityPopup.selectedTag(),
                    self._.calItemStartDate)

        else:
            if self._.calItemTitle is None:
                self._.calItemTitle = "My Event"

            self.createNewEventWithCalendar_title_startDate_endDate_(
                    selectedCalendar, self._.calItemTitle,
                    self._.calItemStartDate, self._.calItemEndDate)
        
        # Dismiss the sheet
        sheet.orderOut_(self)


    def createNewEventWithCalendar_title_startDate_endDate_(
                self, calendar, title, startDate, endDate):

        # Create a new CalEvent object
        newEvent = CalEvent.event()
        
        # Set the calendar, title, start date and end date on the new event
        # using the parameters passed to this method
        newEvent._.calendar = calendar;
        newEvent._.title = title;
        newEvent._.startDate = startDate;
        newEvent._.endDate = endDate;

        # Save the new event to the calendar store (CalCalendarStore) and 
        # return it
        res, err = CalCalendarStore.defaultCalendarStore().saveEvent_span_error_(
                newEvent, 0, None)
        if res:
            return newEvent

        NSLog("error:%@", err.localizedDescription())
        return None

    def createNewTaskWithCalendar_title_priority_dueDate_(
            self, calendar, title, priority, dueDate):

        # Create a new CalTask object
        newTask = CalTask.task()

        # Set the calendar, title, priority and due date on the new task
        # using the parameters passed to this method
        newTask._.calendar = calendar
        newTask._.title = title
        newTask._.priority = priority
        newTask._.dueDate = dueDate
        
        # Save the new task to the calendar store (CalCalendarStore) and 
        # return it
        res, err = CalCalendarStore.defaultCalendarStore().saveTask_error_(newTask, None)
        if res:
            return newTask
    
        NSLog("error:%@", err.localizedDescription())
        return None
