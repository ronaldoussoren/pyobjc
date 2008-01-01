"""
Adds WWDC 2007 to the 'Work' calendar
"""
from CalendarStore import *
import textwrap

store = CalCalendarStore.defaultCalendarStore()
for cal in store.calendars():
    if cal._.title == u"Work":
        event = CalEvent.event()
        event._.calendar = cal
        event._.title = "WWDC 2007"
        event._.notes = textwrap.dedent('''\
                This June, the center of the Mac universe will be at Moscone 
                West in downtown San Francisco, as developers and IT 
                professionals from around the globe come together for the 
                Apple Worldwide Developers Conference. 
                
                Don't miss this opportunity to connect with Apple engineers, 
                get a firsthand look at the latest technology, and spend a 
                week getting the kind of inspiration you won't find anywhere 
                else.
                ''')
        event._.url = NSURL.URLWithString_('http://developer.apple.com/wwdc/')
        event._.location = "Moscone West, San Francisco, CA, USA"
        event._.isAllDay = True
        start = NSDate.dateWithString_("2007-06-11 00:00:00 +0600")
        stop = NSDate.dateWithString_("2007-06-15 23:59:59 +0600")
        event._.startDate = start
        event._.endDate = stop
        res, err = store.saveEvent_span_error_(event, 0, None)
        if not res:
            print "Adding WWDC failed", err.localizedDescription()
        break


else:
    print "Cannot find the right calendar"
