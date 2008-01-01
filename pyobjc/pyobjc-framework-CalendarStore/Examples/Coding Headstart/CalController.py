"""
Bindings and notification support for Calendar data used
by this application.  Exposes read-only collections 
(calendars, events, tasks) as observable entities.
"""
from Cocoa import *
from CalendarStore import *

highPriority = "High"
normPriority = "Normal"
lowPriority = "Low"
nonePriority = "None"

# Transformer class for CalPriority->String conversion
class CalPriorityToStringTransformer (NSValueTransformer):
    '''
    The CalPriorityToStringTransformer class allows easy conversion between 
    CalPriority values (0-9) and human-readable priority strings (High, 
    Normal, Low, None). This allows us to populate the priority dropdown 
    using bindings
    '''

    @classmethod
    def transformedValueClass(cls):
        return type(NSString)

    @classmethod
    def allowsReverseTransformation(cls):
        return False

    def transformedValue_(self, value):
        priority = value.unsignedIntValue()
        if priority < CalPriorityHigh:
            return nonePriority

        elif priority < CalPriorityMedium:
            return highPriority

        elif priority == CalPriorityMedium:
            return normPriority

        return lowPriority

class CalController (NSObject):
    def awakeFromNib(self):
        # Register a transformer object for easy generation of 
        # human-readable priority strings
        #
        # See CalPriorityToStringTransformer implementation below

        prioTransformer = CalPriorityToStringTransformer.alloc().init()
        NSValueTransformer.setValueTransformer_forName_(
                prioTransformer, "CalPriorityToStringTransformer")
        
        # Register for notifications on calendars, events and tasks so we can 
        # update the GUI to reflect any changes beneath us
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                self, 'calendarsChanged:', 
                CalCalendarsChangedExternallyNotification, None)

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                self, 'calendarsChanged:', 
                CalCalendarsChangedNotification, None)
        
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                self, 'eventsChanged:', 
                CalEventsChangedExternallyNotification, None)

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                self, 'eventsChanged:', 
                CalEventsChangedNotification, None)
        
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                self, 'tasksChanged:',
                CalTasksChangedExternallyNotification, None)

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                self, 'tasksChanged:',
                CalTasksChangedNotification, None)


    # Set up the read-only calendars/events/tasks arrays from Calendar Store 
    # as observable keys for Cocoa Bindings
    # This in conjunction with the notifications will allow for immediate UI 
    # updates whenever calendar data changes outside of this app
    def calendars(self):
        return CalCalendarStore.defaultCalendarStore().calendars()

    def events(self):
        store = CalCalendarStore.defaultCalendarStore()
        # Pull all events starting now from all calendars in the CalendarStore
        allEventsPredicate = CalCalendarStore.eventPredicateWithStartDate_endDate_calendars_(
                NSDate.date(), NSDate.distantFuture(), store.calendars())
        return store.eventsWithPredicate_(allEventsPredicate)

    def tasks(self):
        store = CalCalendarStore.defaultCalendarStore()
        # Pull all uncompleted tasks from all calendars in the CalendarStore
        return store.tasksWithPredicate_(
                CalCalendarStore.taskPredicateWithUncompletedTasks_(
                    store.calendars()))


    # With the observable keys set up above and the appropriate bindings in IB,
    # we can trigger UI updates just by signaling changes to the keys
    def calendarsChanged_(self, notification):
        self.willChangeValueForKey_("calendars")
        self.didChangeValueForKey_("calendars")

    def eventsChanged_(self, notification): 
        self.willChangeValueForKey_("events")
        self.didChangeValueForKey_("events")

    def tasksChanged_(self, notification):
        self.willChangeValueForKey_("tasks")
        self.didChangeValueForKey_("tasks")
