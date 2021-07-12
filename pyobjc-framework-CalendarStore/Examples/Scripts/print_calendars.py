"""
Print some information about calendars
"""

from CalendarStore import CalCalendarStore

store = CalCalendarStore.defaultCalendarStore()

for calendar in store.calendars():
    print("")
    print("Name:", calendar._.title)
    print("UUID:", calendar._.uid)
    print("Type:", calendar._.type)
